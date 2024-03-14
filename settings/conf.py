from environs import Env

env = Env()
env.read_env()


DB_HOST = env.str("DB_HOST")
DB_PORT = env.str("DB_PORT")
DB_USER = env.str("DB_USER")
DB_NAME = env.str("DB_NAME")
DB_PASS = env.str("DB_PASS")

API_ID = env.str("API_ID")
API_HASH = env.str("API_HASH")
PHONE_NUMBER = env.str("PHONE_NUMBER")


database_url = (
    f"postgresql+asyncpg://{DB_USER}:" f"{DB_PASS}@{DB_HOST}:" f"{DB_PORT}/{DB_NAME}"
)
