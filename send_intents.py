import os
import requests
import logging
from log_handler import MyLogsHandler

def raise_response( response , logger):
  
  if response.raise_for_status():
    
    logger.info('Произошла ошибка при передачи интента')


def post_intents():

  logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message) s ')
  logger = logging.getLogger('bot_logger')
  logger.setLevel(logging.INFO)
  logger.addHandler(MyLogsHandler(my_chat_id = os.environ['telegram_chat_id']))

  url = os.environ['train_phrases']

  response = requests.get(url = url)
  raise_response(response,logger)
  phrases = response.json()
  
  
  googl_url = 'https://api.dialogflow.com/v1/intents/'
  headers = {
    "Authorization":os.environ['dialog_dev_token_v1'],
    'Content-Type': 'application/json'
    }
    
  for phrase in phrases:
    user_says = []

    for user_phras in phrases[phrase]['questions']:
      says = {
        'count':0,
        'data':[
          {
            'text':user_phras
          }
        ]
      }
      user_says.append(says)
      
    data={
      'v':'20150910',
      'auto':True,
      'context':[],
      'name':phrase,
      'responses':[
        {
          'messages':[{
            'speech':phrases[phrase]['answer'],
            'type':0
          }
          ]
        }
      ],
      'userSays': user_says
      }
        
    google_response = requests.post(url = googl_url,  headers = headers,json= data  )
    raise_response(google_response,logger)
 

if __name__ == '__main__':
  post_intents()  
  
  
  
  





  

 
