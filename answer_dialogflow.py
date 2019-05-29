import requests
import logging
import os

def get_dialog_answer(session_id,text,default_message = None):

  logger = logging.getLogger('bot_logger')
  answer_message = ''
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
  
  response  = requests.get(url = url, params = params,headers=headers)
  response.raise_for_status()
  server_answer = response.json()
    
  if server_answer['result']['metadata']['isFallbackIntent'] == 'true' and default_message:
    answer_message = default_message
  else:
    answer_message = server_answer['result']['fulfillment']['speech']
  
  return answer_message
