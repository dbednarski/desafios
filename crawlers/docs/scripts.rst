scripts
=============

redditTerm.py
-------------------

Script to show the trending threads of subreddits of Reddit in a terminal. It implements the classes of `crawlers` module,
considering the trending threads those which have more than 5000 upvotes amongst the 25 hottest threads inside such subreddit.
                                                  
This script can be called by the following code (in terminal):

.. code:: bash

    $ redditTerm.py [-h] [--18+] subredds

Parameters:


  * ``subredds``:         list of subreddits separeted by semicolons (;)

  * ``-h``, ``--help``:   show the help message

  * ``--18+``:            shows results classified as 18+? (Default: true)
   
   



redditBot.py
-----------------

Script for the Telegram Bot. That Bot allows the people to run a similar code to the ``redditTerm.py``  from the Telegram.
To allow it, this code must be running in some local computer, or local or remote server. To run in background:

.. code:: bash

    $ redditBot.py &
