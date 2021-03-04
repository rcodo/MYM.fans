import os
import sys
import re
import json
import time
import argparse
import concurrent.futures
import platform
import logging
from threading import Thread, Event

import requests
from bs4 import BeautifulSoup
from win32_setctime import setctime

from utils.constants import (
    MODEL_URL,
    POSTS_URL,
    SUBSCRIPTION_URL,
    FAVORITES_URL,
    SPINNERS
)


class Logger:
    FORMAT = '%(levelname)s: %(message)s'

    def __init__(self, level=logging.INFO):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level)
        if not self.logger.handlers:
            sh = logging.StreamHandler()
            formatter = logging.Formatter(self.FORMAT)
            sh.setFormatter(formatter)
            self.logger.addHandler(sh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)


class MYMfans(Logger):
    PREFIX = 'https://mym.fans'

    def __init__(self,
                 args,
                 cwd=os.getcwd(),
                 system=platform.system(),
                 model_id=None,
                 media_total=None,
                 actual_total=0,
                 current_total=0):
        super().__init__()
        with open(os.path.join(sys.path[0], 'config.json')) as f:
            auth = json.load(f)['auth']
        user_agent = auth['user_agent']
        self.token = auth['login_session_men_token']
        self.id_ = auth['login_session_men_id']
        self.connecte = auth['user_id']
        self.headers = {
            'accept': 'text/html, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'connection': 'keep-alive',
            'user-agent': user_agent,
            'cookie': f'login_session_men_token={self.token};login_session_men_id={self.id_}'}
        self.cwd = cwd
        self.system = system
        self.model = args.model
        self.model_id = model_id
        self.media_total = media_total
        self.actual_total = actual_total
        self.current_total = current_total

    def get_favorites(self):
        with requests.Session() as s:
            r = s.get(FAVORITES_URL, headers=self.headers)
        if r.ok:
            soup = BeautifulSoup(r.content, 'lxml')
            pseudos = soup.find_all('a', {'class': 'subscriptions-pseudo'})
            names = [pseudo.text.strip() for pseudo in pseudos]
            slugs = [pseudo['href'].rsplit('/', 1)[-1] for pseudo in pseudos]
            table_contents = list(enumerate(zip(names, slugs), 1))
            fmt = '{:<8}{:<25}{:<25}'
            header = fmt.format('NUM', 'NAME', 'SLUG')
            print(header)
            for c, v in table_contents:
                print(fmt.format(c, *v))
            self.logger.info(
                'Enter the number next to the user whose page you would like to download')
            while True:
                try:
                    input_ = int(input('>>> '))
                    for c, v in table_contents:
                        if input_ == int(c):
                            self.model = v[1]
                            return
                        else:
                            pass
                except ValueError:
                    self.logger.error('Not a number')
        else:
            self.warning(
                'Your token, id, and user agent are either empty or have expired. Please recheck or refill the fields in the config.json file.')
            sys.exit(0)

    def get_model_id(self):
        with requests.Session() as s:
            r = s.get(MODEL_URL.format(self.model), headers=self.headers)
        if r.ok:
            soup = BeautifulSoup(r.content, 'lxml')
            fa_square = soup.find(
                'a', {'class': 'portfolio-switch-full no-bottom'})
            model_id_string = fa_square['href']
            pattern = re.compile(r'idg=(\S+)')
            match = re.search(pattern, model_id_string)
            self.model_id = match.group(1)
            self.logger.debug(
                'Found model_id' if self.model_id else 'Could not find model_id')
        else:
            r.raise_for_status()

    def get_model_posts(self, array=[], msg_id=None, msg_date=None, count=0):
        if array:
            with requests.Session() as s:
                r = s.post(POSTS_URL.format(
                    self.connecte, self.id_, self.model_id, msg_id, msg_date), headers=self.headers)
        else:
            with requests.Session() as s:
                r = s.get(MODEL_URL.format(
                    self.model), headers=self.headers)
        if r.ok:
            self.logger.debug('Loop')
            soup = BeautifulSoup(r.content, 'lxml')
            posts = soup.find_all('div', {
                                  'class': 'portfolio-item no-margin infinite-profile-{}-box'.format(self.model_id)})
            if not array:
                media_total = soup.find('div', {'class': 'profile_nb_medias'})
                pattern = re.compile(r'(\d+)')
                match = re.match(pattern, media_total.text)
                self.media_total = int(match[0])
            media_urls = [
                (self.PREFIX + post.find('a')['href'], int(post['data'])) for post in posts if post.find('a')['href'].startswith('/feed')]
            media_urls += array
            count += len(posts)
            if count < 12 or count == self.media_total:
                if array:
                    return media_urls
            else:
                msg_id, msg_date = posts[-1]['id'], posts[-1]['data']
                media_urls = self.get_model_posts(
                    media_urls, msg_id, msg_date, count)
                if array:
                    return media_urls
            return media_urls

    def prepare_download(self, posts):
        if posts:
            self.logger.debug(POSTS_URL.format(
                self.connecte, self.id_, self.model_id, 0, 0))
            self.actual_total = len(posts)
            self.logger.info(f'Found {self.actual_total} post of {self.media_total}' if self.actual_total ==
                             1 else f'Found {self.actual_total} posts of {self.media_total}')
            os.makedirs(os.path.join(self.cwd, self.model), exist_ok=True)
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = {
                    executor.submit(self.download(post)): post for post in posts}
                for future in concurrent.futures.as_completed(futures):
                    future.result
        else:
            self.logger.info('No posts found')

    def download(self, post):
        url, timestamp = post[0], post[1]
        with requests.Session() as s:
            r = s.get(url, headers=self.headers)
            if r.ok:
                soup = BeautifulSoup(r.content, 'lxml')
                try:
                    source = soup.find('source')['src']
                except TypeError:
                    source = soup.find(
                        'img', {'class': 'responsive-image margin-bottom-5'})['src']
                r = s.get(source, headers=self.headers)
                if r.ok:
                    filename = os.path.join(self.model, source.split('-')[-1])
                    with open(filename, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=1024):
                            f.write(chunk)
                    if self.system == 'Windows':
                        setctime(filename, timestamp)
                    os.utime(filename, (timestamp, timestamp))
                else:
                    self.logger.error(f'Unable to download: {source}')
            else:
                self.logger.error(f'Unable to download: {url}')
        self.current_total += 1

    def spinner(self, event):
        while True:
            for spinner in SPINNERS:
                if event.is_set():
                    self.logger.info('Complete')
                    return
                print(
                    f'{spinner} ({self.current_total} / {self.actual_total})', end='\r', flush=True)
                time.sleep(0.1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-m', '--model', help='username whose page you would like to scrape', type=str, required=False, metavar='USERNAME')
    args = parser.parse_args()
    mym = MYMfans(args)
    e1 = Event()
    t1 = Thread(group=None, target=mym.spinner, args=(e1,))
    if args.model:
        mym.get_model_id()
    else:
        mym.get_favorites()
        mym.get_model_id()
    t1.start()
    mym.prepare_download(mym.get_model_posts())
    e1.set()


if __name__ == '__main__':
    main()
