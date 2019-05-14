"""
    RedditPrinter Class
"""

from __future__ import print_function, unicode_literals
import requests
from crawlers.Reddit import Reddit

class RedditPrinter:
    """Class of Reddit Crawlers Printer.

        Attributes:
            subredds (:obj:`list`): An array of strings (subrreds). 
            limit (int, optional): Limit of threads to sweep inside each subreddit. 
            min_upvotes (int, optional): Min of upvotes to be considerated a trending thread. 
            filter_18 (bool, optional): Filter 18+ threads.
        """ 
        
    def __init__(self, subredds, limit = 25, min_upvotes = 5000, filter_18 = False):
        # Initializes an instance
        Reddit.verbose = False
        if Reddit.limit != limit:
            Reddit.limit = limit
        if Reddit.min_upvotes != min_upvotes:
            Reddit.min_upvotes = min_upvotes
        if Reddit.filter_18 != filter_18:
            Reddit.filter_18 = filter_18
        self.__subredds = subredds


    def getCrawlers(self):
        """
        Returns a printable string of the trending threads (crawlers) found for the *subredds* attribute.

        Returns:
            :obj:`str`: printable string of trending threads
        """
        
        printings = ""
        num_errors = 0

        # Loop on subreddits
        for subredd in self.__subredds:

            num = len(subredd)+8
            printings += "="*num + "\n==  " + subredd.upper() + "  ==\n" + "="*num + "\n"

            obj = Reddit(subredd)
            url = obj.getSubreddUrl()
            crawlers = obj.crawlers()
            
            # Case some error on access subreddit page
            if crawlers == None:
                num_errors += 1
                printings += "\nUnable to access the subreddit (probably it doesn't exist)\n\n"
            elif crawlers == []:
                printings += "\nNo trendings found\n\n"
            else:
                # Print every trending thread
                for i, thread in enumerate(crawlers):
                    printings += "\n# {}.  {}\n\n".format(i+1,thread["title"])
                    printings += " SCORE: {}\n".format(thread["score"])
                    printings += " UP VOTES: {}\n".format(thread["ups"])
                    printings += " URL (LINK): {}\n".format(thread["link_url"])
                    printings += " URL (COMMENTS): {}\n\n".format(thread["thread_url"])

            if subredd != self.__subredds[-1]:
                printings += "\n"
        
        # In case of error in all subreddits (if there are more than just one)
        if num_errors == len(self.__subredds) and len(self.__subredds) != 1:
            return "ERROR: unable to access all subreddits!"
        else:
            return printings



    def printCrawlers(self):
        """
        Prints the trending threads (crawlers) found for the *subredds* attribute
        """
        print(self.getCrawlers())
