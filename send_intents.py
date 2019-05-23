import os
import dialogflow_v2  as dialogflow
import requests





def post_intents(logger):

  url = os.enviro['train_phrases']
  try:
    response = requests.get(url = url)
    response.raise_for_status()
    phrases = response.json()
    
    googl_url = 'https://api.dialogflow.com/v1/intents?v=20150910'

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
      google_response = requests.post(url = googl_url,  headers = headers,json= data)
      
  except (ConnectionError ,requests.exceptions.HTTPError) as err:
    logger.info(err)
  
  
  
  





  

 
