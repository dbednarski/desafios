# RedditCrawlers

This package provides some tools to explore the trending threads of [Reddit](#reddit). Its core is composed by the Python module ``crawlers``, which can be used in others implementations for many purposes. The package also includes two own scripts to figure out the trending threads of subreddits: the first one is a typical script that prints the results in the terminal; the second one is an implementation of a "[Telegram Bot](#telegram)".


### Reddit

The [Reddit](https://www.reddit.com) is a kind of forum with thousands of categories, the called *subreddits*. In each *subreddit* there are others thousands of *threads*. Each *thread* has a score, which is computed by the "up votes" minus the "down votes".

### Telegram

The [Telegram](http://telegram.org) is a OpenSource and cloud-based instant messaging service, whose cryptography makes it one of the most secure messaging app. Telegram provides two API for developers make use in their codes and programs.

Telegram supports a type of account called *Bot*, that can be used to run programs and scripts inside the Telegram clients (app, browsers, etc). For example, [YTranslateBot](https://telegram.me/YTranslateBot) is a *Bot* that translate text among many languages.


## File structure

* `docs` -- directory of documentation
* `crawlers` -- directory of module ``crawlers``
* `scripts` -- directory of scripts


## Installation

First, go to the root directory of the package. Now you must to choose if you will install RedditCrawlers only for your user or in entire system. In case of the fist option, run:

```
$ python setup.py install --user
```

otherwise, you must have admin privileges:

```
$ sudo python setup.py install
```

### Requirements

* Python >= 2.7
* [setuptools](https://pypi.org/project/setuptools)
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
* [requests](https://github.com/requests/requests)
* [numpy](https://www.numpy.org/)



# Using the features


## crawlers module

The entire documentation of ``crawlers`` module can be found in [https://desafios.readthedocs.io](https://desafios.readthedocs.io). After installed, you can import any of the two classes -- or the full module. The recommended way:

```
from crawlers.Reddit import Reddit
from crawlers.RedditPrinter import RedditPrinter
```


## The scripts

The following scripts can be called from any directory:

* `redditTerm.py`: Script to show the trending threads of subreddits of Reddit in a terminal. This script is called by the following code:
```
$ redditTerm.py [-h] [-18] subredds
```
    Parameters:
        * ``subredds``:              list of subreddits separated by semicolons (;) (as ';' is a special character, you have to put your list among quotations ("")
        * ``-h``, ``--help``:        show the help message
        * ``-18``, ``--filter_18``:  filter threads classified as 18+ (Default: False)
* `redditBot.py`: Script of the Telegram Bot. That Bot allows the people to run a similar code to the ``redditTerm.py``  from the Telegram. To allow it, this code must be running in some local computer, or local or remote server. To run in background:
```
$ redditBot.py &
```

### Output

The main output of both scripts is the information about all the *threads* of each subreddit passed as input that:

1. have more than 5000 up votes; and
2. be among the 25 *hottest* threads (classified by the Reddit).



### Accessing and using the RedditBot

The *bot* [RedditBot](https://telegram.me/DanBedBot) was created to response the requests sent to the Telegram API, and redirected to the `redditBot.py`. This script must be running for the communication working.

In link above, click in *Send Message* to invite the RedditBot for our Telegram. Only there exist two commands for RedditBot:

* `/start`
  Prints the help message.

* `/NadaPraFazer *subredds*`
  The behavior is the same those when `redditTerm.py` is runned in a terminal. But now the messages are printed in Telegram Bot chat. `*subbreds*` is the same one parameter from `redditTerm.py`: a list of subreddits separated by semicolons (;).


## Author

Daniel Bednarski Ramos

[http://www.astro.iag.usp.br/~bednarski](https://www.astro.iag.usp.br/~bednarski)

daniel.bednarski.ramos@gmail.com


## License

GNU GPLv3
