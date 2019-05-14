"""
    Reddit Class
"""

from __future__ import print_function
from __future__ import unicode_literals
import requests


class Reddit:
    """Class for subreddit crawlers.

    Attributes:
        subredd (str): The name of the subreddit.
    """ 
    
    limit = 25
    """
        Limit of threads to sweep inside each subreddit.
    """
    min_upvotes = 5000
    """
        Min of upvotes to be considerated a trending thread.
    """
    filter_18 = False
    """
        Filter 18+ threads.
    """
    verbose = True
    """
        Print error messages.
    """
    
    def __init__(self, subredd):
        # Initializes an instance
        self.__subredd = subredd


    def getSubredd(self):
        """
        Returns the *subredd* atribute value
        
        Returns:
            str: the value of *subredd* atribute.
        """
        return self.__subredd
        
        
    def getSubreddUrl(self):
        """
        Returns the subreddit url.
        
        Returns:
            str: Subreddit URL.
        """
        return "http://www.reddit.com/r/" + self.__subredd

    
    def crawlers(self):
        """
        Search informations about the subreddit *subredd*, retorning
        informations about the trending threads.

        Returns:
            :obj:`list` | :obj:`None`: In case of some error, returns a :obj:`None` object.
            In success, returns a :obj:`list of dictionaries`. The dictionaries are concerning to
            each trending thread found, sorted by score (descending order). Their keys values are:
            
                * *title* - title of the thread.
                * *ups* - number of up votes of the thread.
                * *downs* - number of down votes of the thread.
                * *num_comments* - number of comments of the thread.
                * *over_18* - boolean indicating if is a 18+ thread.
                * *thread_url* - url to the comments of the thread.
                * *link_url* - url of the subject of the thread.
        """

        params = {
                   "limit": self.limit,
                   "raw_json" : 1
                  }
        header = {"User-agent": "Super Bot 9000"}

        # Request json file from subreddit
        response = requests.get("https://www.reddit.com/r/{}.json".format(self.__subredd), params = params, headers = header, allow_redirects = False)
        
        if response.status_code == 404:
            if self.verbose:
                print("ERROR: unable to access the subreddit (maybe it doesn't exist).")
            return None
        elif response.status_code != 200:
            if self.verbose:
                print("ERROR: unknown.")
            return None
        
        # Get only the json part regarding threads
        rjson = response.json()

        threads_json = rjson["data"]["children"]
        threads = []

        # Loop on threads
        for thread in threads_json:

            # Get score of thread for testing
            upvotes = thread["data"]["ups"]
            over_18 = thread["data"]["over_18"]

            # Skip threads up to min score
            if int(upvotes) < self.min_upvotes or (over_18 and self.filter_18):
                continue

            # Get informations about the thread from json
            threads += [{
                        "title": thread["data"]["title"],
                        "score": thread["data"]["score"],
                        "ups": upvotes,
                        "downs": thread["data"]["downs"],
                        "num_comments": thread["data"]["num_comments"],
                        "over_18": over_18,
                        "thread_url": "http://www.reddit.com" + thread["data"]["permalink"],
                        "link_url": thread["data"]["url"]
                        }]

        return sorted(threads, key=lambda x: int(x['score']), reverse= True)
