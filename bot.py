#!/usr/bin/env python

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
import logging
from config import TELEGRAM_TOKEN

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    keyboard = ReplyKeyboardMarkup([['Adresse erstellen']])
    update.message.reply_text('Hi!', reply_markup=keyboard)


def reply(bot, update):
    update.message.reply_text(update.message.text)


def main():
    updater = Updater(TELEGRAM_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, reply))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
