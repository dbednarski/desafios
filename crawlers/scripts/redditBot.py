#!/usr/bin/env python
#

import sys
from telegram.ext import Updater, CommandHandler
import logging
from crawlers.RedditPrinter import RedditPrinter



def bot_start(bot, update):
    """
    Telegram bot action for the command `start`

    Return the instructions.
    """
    printings = "I'm a bot that return the trending topics from Reddit.\n\n"\
                "Usage:\n"\
                "   /NadaPraFazer *list*\n\n"\
                "   where *list* is a list of subreddits, separeted by semicolons (;)\n\n"\
                "The trending threads retorned for each subreddit are those which have more\n"\
                "than 5000 upvotes amongst the 25 hottest threads inside such subreddit."
    bot.send_message(chat_id=update.message.chat_id, text=printings)



def bot_NadaPraFazer(bot, update, args):
    """
    Telegram bot action for the command `NadaPraFazer`

    Receive subreddits list separated by semicolons (;) and print
    the trending threads for the telegram user by calling
    readReddit() function.
    """

    if len(args) != 1:
        bot.send_message(chat_id=update.message.chat_id, text="ERROR: \"NadaParaFazer\" uses only one argument.")
    else:
        # Uses RedditPrinter class from crawlers module
        printer = RedditPrinter(args[0].split(";"))
        printings = printer.getCrawlers()
        bot.send_message(chat_id=update.message.chat_id, text=printings)



def main():
    
    # Token for @DanBedBot (RedditBot)
    token = "670693073:AAH0knXq5unQHWMMizPXQ2FAW_dBryrfOwI"

    # Create updater object
    updater = Updater(token=token)
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Set *start* command for Telegram
    start_handler = CommandHandler('start', bot_start)
    dispatcher.add_handler(start_handler)

    # Set *NadaPraFazer* command for Telegram
    return_handler = CommandHandler('NadaPraFazer', bot_NadaPraFazer, pass_args=True)
    dispatcher.add_handler(return_handler)

    updater.start_polling()

    sys.exit(0)
  
    

if __name__ == "__main__":
    main()

