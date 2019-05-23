from telegram.ext import Updater ,CommandHandler ,MessageHandler ,Filters
import os
from answer_dialogflow import get_dialog_answer
import logging
def start( bot , update):
    bot.send_message(chat_id = update.message.chat_id , text = 'Здравствуйте!')

def echo(bot, update):
  answer_message = get_dialog_answer(update.message.chat_id,update.message.text,True)
  update.message.reply_text(answer_message)
def telegram_bot():
  updater = Updater(token= os.environ['telegram_token'])
  dispatcher = updater.dispatcher
  echo_handler = MessageHandler(Filters.text ,echo)
  dispatcher.add_handler(echo_handler)
  start_handler = CommandHandler('start',start)
  dispatcher.add_handler(start_handler)
  updater.start_polling()
