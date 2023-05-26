from environs import Env

env = Env()
env.read_env('./env.env')

API_ID = env.str('API_ID')
API_HASH = env.str('API_HASH')
API_TOKEN = env.str('API_TOKEN')
PHONE_NUMBER = env.str('PHONE_NUMBER')
CHAT_ID = env.str('CHAT_ID')
