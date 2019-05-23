Данный скрипт работает как чат бот в телеграм и в группе вконтакте , ответы на входящие сообщения получает с помощью сервиса Dialogflow. Чтобы запустить скрипт необходимо :

1 Установить необходимые зависимости командой

pip install -r requirements.txt
2 в корне создать файл ".env " с следующим содержанием

  bot_error_token = 'Телеграм токен бота на который приходят ошибки'
  telegram_token = 'Телеграм токен бота на который приходят результаты проверки'
  telegram_chat_id = ' Ваш id чата' (его можно узнать обратившись с командой /start к телеграм боту с именем userinfobot)
  dialog_token = 'Bearer <Клиентский токен Dialogflow>'
  dialog_dev_token_v1 = 'Bearer <Токен разработчика Dialogflow> ( не обязателено для работы скрипта)'
  vk_token = 'Токет Вконтакте'
  train_phrases = 'Ссылка на json файл с обучающими фразами ( не обязателено для работы скрипта)' 
  
  
3 Запустить файл main.py набрав в консоли команду

  python main.py