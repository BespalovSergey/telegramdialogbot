import requests
import logging
import os

def get_dialog_answer(session_id,text,default):
  logger = logging.getLogger('bot_logger')
  answer_message = ''
  default_message = 'Извините я вас не понял'
  headers = {
  "Authorization":os.environ['dialog_token']
  }
  url = 'https://api.dialogflow.com/v1/query/'

  params = {
    'v':20150910,
    'name':'welcome',
    'lang':'ru',
    'sessionId':session_id,
    'query':text

  }
  try:

    response  = requests.get(url = url, params = params,headers= headers)
    response.raise_for_status()
    server_answer = response.json()
    
    if server_answer['result']['metadata']['isFallbackIntent'] == 'true' and default:
      answer_message = default_message
      
    else:
      answer_message = server_answer['result']['fulfillment']['speech']
  except (ConnectionError  ,requests.exceptions.HTTPError) as err:
    logger.info(err)
    answer_message = default_message
  return answer_message
