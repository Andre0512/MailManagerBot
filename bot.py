#!/usr/bin/env python

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler
from telegram import ReplyKeyboardMarkup, ForceReply
import logging
from config import TELEGRAM_TOKEN
import re

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


def create_qmail(update):
    mail = update.message.text.lower()
    if not re.match(r'^[a-z0-9.-]*$', mail):
        update.message.reply_text('Keine valide E-Mail Adresse.')
        return


def read_msg(bot, update):
    if update.message.reply_to_message:
        if update.message.reply_to_message.text in [MAIL_NAME]:
            create_qmail(update)
    else:
        if update.message.text in [CREATE]:
            reply(bot, update)
        else:
            create(bot, update)


def main():
    updater = Updater(TELEGRAM_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(RegexHandler('.*', read_msg))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
