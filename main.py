from log_handler import MyLogsHandler
from dotenv import load_dotenv
from telegram_dialog import telegram_bot
import logging
import os
import requests
from vk_dialog import vk_bot

def main():

  logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message) s ')
  logger = logging.getLogger('bot_logger')
  logger.setLevel(logging.INFO)
  logger.addHandler(MyLogsHandler(my_chat_id = os.environ['telegram_chat_id']))
  logger.info('Бот проверки ошибок запущен')

  load_dotenv()

  try:
    telegram_bot()
    vk_bot()
  except (ConnectionError  ,requests.exceptions.HTTPError) as err:
    logger.info(err)
    
  
  
if __name__ == '__main__':
  main()
  
