#!/usr/bin/env python

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, ForceReply
import logging
from config import TELEGRAM_TOKEN

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

CREATE='Adresse erstellen'
MAIL_NAME = 'Welche Adresse soll angelegt werden?'

def start(bot, update):
    keyboard = ReplyKeyboardMarkup([[CREATE]])
    update.message.reply_text('Hi!', reply_markup=keyboard)


def create(bot, update):
    update.message.reply_text(update.message.text)


def reply(bot, update):
    update.message.reply_text(MAIL_NAME, reply_markup=ForceReply())


def main():
    updater = Updater(TELEGRAM_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, reply))
    dp.add_handler(MessageHandler(CREATE, create))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
