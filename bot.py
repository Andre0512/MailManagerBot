#!/usr/bin/env python

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler
from telegram import ReplyKeyboardMarkup, ForceReply
import logging
from config import TELEGRAM_TOKEN
import re
import subprocess
import random
import string

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
    mail = update.message.text.lower().replace('.', ':')
    if not re.match(r'^[a-z0-9:-]*$', mail):
        update.message.reply_text('Keine valide E-Mail Adresse.')
        return
    passw = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(12))
    try:
        p1 = subprocess.Popen('printf {}'.format(passw).split(), stdout=subprocess.PIPE)
        output = subprocess.check_output('vadduser {}'.format(mail).split(), stdin=p1.stdout)
        if output.decode() not in "vadduser: user '{}' successfully added\n".format(mail):
            raise subprocess.CalledProcessError
        update.message.reply_text('Benutzer {} erfolgreich erstellt.'.format(mail))
    except subprocess.CalledProcessError:
        update.message.reply_text('Benutzer {} konnte nicht erstellt werden'.format(mail))


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
