from pyrogram import Client
from environs import Env

from get_video_id import register_handlers

env = Env()
env.read_env()

api_id = env.str('API_ID')
api_hash = env.str('API_HASH')
app = Client("my_account", api_id=api_id, api_hash=api_hash)

register_handlers(app)

if __name__ == "__main__":
    app.run()
