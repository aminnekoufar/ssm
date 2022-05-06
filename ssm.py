# -*- coding: utf-8 -*-
from sys import path
path.append('..')
from client import Client
bot_token = '*'
bot = Client(bot_token)
send = bot.send_text
try:
   messages = bot.get_messages()
   for message in messages:
      to = format(message['from'])
      if str(format(message['body']))=="start":
         if str(format(message['body']))=="SignUp":
            [error, success] = send(to, 'لطفا نام و نام خانوادگی خود را وارد کنید')
            if success:
               print('Message sent successfully')
            else:
               print('Sending message failed: {}'.format(error))
      else:
         # print("New message from {} \nType: {}\nBody: {}" .format(message['from'], message['type'], message['body']))

         # 2 rows. each row is a list of button dictionaries, each button is a dictionary os {'text': 'your text', 'command: 'your command'}
         keyboard = bot.make_keyboard(
            [[{'text': 'ثبت نام', 'command': 'SignUp'}, {'text': 'Row1Button2', 'command': 'back'}],
               [{'text': 'Row2Button1', 'command': 'options'}]])

         [error, success] = send(to, 'خوش امدید برای ادامه گزینه مورد نظر خود را انتخاب کنید', keyboard=keyboard)

         if success:
            print('Message sent successfully')
         else:
            print('Sending message failed: {}'.format(error))
except Exception as e:
   print(e.args[0])


