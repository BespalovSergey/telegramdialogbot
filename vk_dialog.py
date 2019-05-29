import vk_api
from vk_api.longpoll import VkLongPoll , VkEventType
import os
from answer_dialogflow import get_dialog_answer
import random


def echo(event ,vk_ap):
  vk_ap.messages.send(user_id = event.user_id,
  message = get_dialog_answer(event.user_id,event.text),
  random_id = random.randint(1,1000) )

def vk_bot():
  vk_session = vk_api.VkApi(token = os.environ['vk_token'])
  vk_ap = vk_session.get_api()
  longpoll = VkLongPoll(vk_session)

  for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
      echo(event,vk_ap)
