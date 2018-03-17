#!/usr/bin/env python

import re
import subprocess
import random
import string
import logging

from telegram import ReplyKeyboardMarkup, ForceReply, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler

from config import TELEGRAM_TOKEN, WEBMAIL, SERVER, ADDRESSES, USERS 
from strings import MESSAGE, CREATE, MAIL_NAME, INVALID, FORBIDDEN, ERROR

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    keyboard = ReplyKeyboardMarkup([[CREATE]], resize_keyboard=True)
    update.message.reply_text('Hi!', reply_markup=keyboard)


def create(bot, update):
    update.message.reply_text(update.message.text)


def reply(bot, update):
    update.message.reply_text(MAIL_NAME, reply_markup=ForceReply())


def send_full_data(update, values):
    values['WEBMAIL'] = WEBMAIL
    values['SERVER'] = SERVER
    values['MAIL'] = ADDRESSES[0]
    values['ADDRESSES'] = '\n'.join(['[{0}@{1}]("mailto:{0}@{1}")'.format(*[values['NAME'], x]) for x in ADDRESSES])
    message = MESSAGE.format(**values)
    update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)


def create_qmail(update):
    mail = update.message.text.lower().replace(' ', '.')
    if not re.match(r'^[a-z0-9.-]*$', mail):
        update.message.reply_text(INVALID)
        return
    passw = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(12))
    try:
        p1 = subprocess.Popen('printf {}'.format(passw).split(), stdout=subprocess.PIPE)
        output = subprocess.check_output('vadduser {}'.format(mail).split(), stdin=p1.stdout)
        if output.decode() not in "vadduser: user '{}' successfully added\n".format(mail):
            raise subprocess.CalledProcessError
        send_full_data(update, {'PASSWORD': passw, 'NAME': mail})
    except subprocess.CalledProcessError:
        update.message.reply_text(ERROR.format(mail))


def read_msg(bot, update):
    if update.message.from_user.id not in USERS:
        update.message.reply_text(FORBIDDEN)
        return
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
