# MYM.fans
![Python-Version](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)

A program written in Python for downloading pictures/videos from creators on [mym.fans](https://mym.fans/).

Un programme écrit en Python pour télécharger des images/vidéos des créateurs sur [mym.fans](https://mym.fans/)

<img src="https://raw.githubusercontent.com/Amenly/MYM.fans/main/media/example.gif">

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

<img src="https://raw.githubusercontent.com/Amenly/MYM.fans/main/media/cookies.png">

Find the row titled `Cookie` and find the values that correspond to `login_session_men_token` and `login_session_men_id`. Copy those values and paste them into their respective locations in the `config.json` file (you can't miss them).

Once those are in there, scroll a little further in the `Request Headers` until you find the row that begins with `User-Agent`. Copy your user agent and paste that into the `config.json` file as well.

Great stuff, you're almost done now. The last bit you need is your `user_id`. In order to get this, go to your [account information page](https://mym.fans/parameters.php?affichage=informations) and scroll down until you see your ID below the green 'Save' button. Copy that and paste it into your `config.json` file.

<img src="https://raw.githubusercontent.com/Amenly/MYM.fans/main/media/user_id.png">

By the end of it, your `config.json` file should look similar to the following:

```json
{   
    "auth": {
        "login_session_men_token": "shT47Gah4bksy1idyyb2y8pwqu752hns6bisa7i",
        "login_session_men_id": "1234567",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
        "user_id": "12a3b76fe3b7d719d71aeff2"
    }
}
```

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

### Installation

Pour utiliser, il faut avoir Python (version 3.6 ou supérieure mais ce programme peut peut-être marcher avec des versions plus inférieures). Il faut aussi installer les dépendances dans le fichier `requirements.txt`. Pour ce faire, effectuer ceci dans votre terminal:

```sh
$ pip install -r requirements.txt
```

Pour ceux qui utilisent Linux ou macOS, effectuer ceci plutôt:

```sh
$ pip3 install -r requirements.txt
```

Si les deux ne marchent pas, vérifiez que vous êtes dans le même répertoire de travail actuel que le fichier `requirements.txt`.

### Exigences

Quand les dépendances sont installées, il faut maintenant trouver quelques informations sur votre compte MYM.fans.

Tout d'abord, allez à [mym.fans](https://mym.fans/) et connectez-vous à votre compte. Une fois que vous êtes connecté, ouvrez les outils de développement de votre navigateur. Pour ce faire, consultez cette table:

| Système d'exploitation | Touches (pour Google Chrome) |
| :----------------: | :----: |
| macOS | <kbd>alt</kbd> + <kbd>cmd</kbd> + <kbd>i</kbd> |
| Windows | <kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>i</kbd> |
| Linux | <kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>i</kbd> |

Avec vos outils, cliquer sur le tab `Network` and allez à votre [page d'abonnement](https://mym.fans/subscriptions.php). Vous devriez voir un `fichier` qui s'appelle `subscriptions.php` (plus ou moins). Cliquez là-dessus ça et puis faites défiler ver la bas jusqu'à ce que vous voyiez une section qui s'appelle `Request Headers` (ou quelque chose comme ça en français, je sais pas).

<img src="https://raw.githubusercontent.com/Amenly/MYM.fans/main/media/cookies.png">

Vous êtes en cherche d'une ligne que s'appelle `Cookie`. Quand vous la trouvez, mettez les valeurs qui correspondent à `login_session_men_token` et `login_session_men_id` dans le fichier `config.json` qui vient avec ce programme.

Quand vous les avez, faites défiler un peu plus ver le bas (mais toujours dans la section `Request Headers`) et trouvez la ligne qui s'appelle `User-Agent`. Mettez ça dans le `config.json` également.

D'accord, on a presque fini. La dernière information, c'est votre `user_id`. Pour l'avoir, il faut aller à votre [page d'information sur le compte](https://mym.fans/parameters.php?affichage=informations). Faites défiler jusqu'à ce que vous voyiez votre ID à côté d'une bouton verte. Mettez-la dans votre `config.json`.

<img src="https://raw.githubusercontent.com/Amenly/MYM.fans/main/media/user_id.png">

Dans le bout, votre `config.json` devrait ressembler à ceci:

```json
{   
    "auth": {
        "login_session_men_token": "shT47Gah4bksy1idyyb2y8pwqu752hns6bisa7i",
        "login_session_men_id": "1234567",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
        "user_id": "12a3b76fe3b7d719d71aeff2"
    }
}
```

C'est tout, vous pouvez maintenant l'utiliser.

### Usage

C'est simple. Pour utiliser, effectuer ceci dans votre terminal:

```sh
$ python mymfans.py
```

Les utilisateurs de Linux et macOS devraient effectuer:

```
$ python3 mymfans.py
```

Lisez les instructions et voilà!

Je dois vous dire que le programme va montrer les créateurs qui sont dans votre liste de favoris. Donc, si vous ne voyez pas quelqu'un sur liste, mettez-les un 'cœur' sur leur page.

Il y a aussi d'autres choses que vous pouvez faire. Si vous voulez télécharger tout le contenu d'une personne en particulier, vous pouvez faire ceci:

```
$ python mymfans.py --model purehumansoul
```

*ou*

```sh
$ python mymfans.py -m purehumansoul
```

En plus, ce programme peut télécharger le contenu des créateurs à qui vous n'êtes pas inscrit (mais, vous n'allez pas télécharger le contenu 'premium' ou 'privé' bien sûr).
