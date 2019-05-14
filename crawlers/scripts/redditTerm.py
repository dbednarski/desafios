#!/usr/bin/env python
#
import argparse, sys
from crawlers.RedditPrinter import RedditPrinter

   
    
def parseArguments():
    """
    This funcion sets the allowed command line input parameters
    and its formats, returning these arguments.
    
    Some errors can be returned by the builtin functions from
    argparse module.
    """
    

    # Desciption for the help parameter (-h | --help)
    parser = argparse.ArgumentParser(description="Script to show the trending threads of subreddits of Reddit.\n\
                                                  The trending threads are those which have more than 5000 upvotes\n\
                                                  amongst the 25 hottest threads inside such subreddit.")

    # Required argument
    parser.add_argument("subredds", help="List of subreddits separeted by semicolons (;)", type=str)

    # Optional arguments
    parser.add_argument("-18", "--filter_18", help="Filter threads classified as 18+", default=False, action="store_true")

    args = parser.parse_args()

    return args



if __name__ == "__main__":

    args = parseArguments()

    # Uses RedditPrinter class from crawlers module
    printer = RedditPrinter(args.__dict__["subredds"].split(";"), filter_18=args.__dict__["filter_18"])
    printer.printCrawlers()
    

