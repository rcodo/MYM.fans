# MYM.fans
A program written in Python for downloading pictures/videos from creators on [mym.fans](https://mym.fans/).

Un programme écrit en Python pour télécharger des images/vidéos des créateurs sur [mym.fans](https://mym.fans/)

## English

### Installation
In order to use this script, you'll need Python 3.6 or higher (though, this script could possibly work with older versions as well; no walrus operators around these parts.). You'll also need to install the dependencies in the `requirements.txt` file. To do so, run the following in your terminal:

```sh
$ pip install -r requirements.txt
```

Linux and macOS users should use the following:

```sh
$ pip3 install -r requirements.txt
```

If this isn't working, it's likely because you aren't in the same directory as the `requirements.txt` file or because your installation of Python is borked. Or both.

### Requirements
Once you get the dependencies installed, you'll need to get a few pieces of data through your account on mym.fans. Don't worry, it's not that difficult at all.

Go to [mym.fans](https://mym.fans/) and log in. Once your logged in, bring up your browser's developer tools. In order to find out how to do that, consult the following table:

| Operating System | Keys (for Google Chrome) |
| :----------------: | :----: |
| macOS | <kbd>alt</kbd> + <kbd>cmd</kbd> + <kbd>i</kbd> |
| Windows | <kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>i</kbd> |
| Linux | <kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>i</kbd> |

Once your developer tools are up, click on the `Network` tab and go to your [subscriptions page](https://mym.fans/subscriptions.php). You should see a `file` called subscriptions.php (or close to that effect). Click on that and then scroll down until you see a section called `Request Headers`.

Find the row titled `Cookie` and find the values that correspond to `login_session_men_token` and `login_session_men_id`. Copy those values and paste them into their respective locations in the `config.json` file (you can't miss them).

Once those are in there, scroll a little further in the `Request Headers` until you find the row that begins with `User-Agent`. Copy your user agent and paste that into the `config.json` file as well.

Great stuff, you're almost done now. The last bit you need is your `user_id`. In order to get this, go to your [account information page](https://mym.fans/parameters.php?affichage=informations) and scroll down until you see your ID below the green 'Save' button. Copy that and paste it into your `config.json` file. 

That's it. Now to use the script.

### Usage
Using it is simple. Just run the following in your terminal:

```sh
$ python mymfans.py
```

Linux and macOS users should run this instead:

```sh
$ python3 mymfans.py
```

Once you run it, just follow the on-screen directions and let it do its thing.

One thing I should note is that the script will only display a list of users that you have in your `My favourites` section. So if a user whom you're subscribed to isn't showing up, try clicking that little heart icon on their page to add them to your 'favourites' list.

*However*, I should also note that the script uses `argparse` which means you have the option of skipping the menu portion of the script and giving the name of the user whose content you want to scrape. For example, if you have a specific user in mind:

```sh
$ python mymfans.py --model purehumansoul
```

*or*

```sh
$ python mymfans.py -m purehumansoul
```

Running that will immediately scrape that user's content. Additionally, if you only wanted their **public-facing** media, you could get it using this script and the above method without entering any cookie information. Though I do recommend at least including a user agent, even if it's not yours.

## French
Coming soon