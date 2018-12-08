from sys import path
path.append('..')
from client import Client
bot_token = 'ssDTYjqst0Lpo3VQARbP1zO-rMlWQikUyCwjCEOXapqL9YznSHzek36SvITb2tTv2qdRXRt_0o8XZcZ-_BDZ86xgdNLMkC--gU5uzX5ow4jtXEJf6ehLvhmFcNtJPQcWKqFhiGBHZ0YV2Lw4'
bot = Client(bot_token)
try:
   messages = bot.get_messages()
   for message in messages:
   print "test"
except Exception as e:
   print(e.args[0])