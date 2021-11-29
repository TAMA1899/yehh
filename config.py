import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAASuhlbu-Ap6JcsgaQ5Ut4KuGPoQtBJwOh2BLBTsfj08b9K2bpO2PQu69upBG41wKjFe0d00tHwU2ikNVs-n0GVwmrJ-fvDfYH6MEPRhZ2epofSi4G-L5Slvz3SPX_aRdTjam8jN5IsqYQzvioHR8c5japIWcUwhhN4I94Et7aKJElkODDqypmpIb5Oi359hOQlvky-UcSYd6fG65EOKTzxEkrsO7rSwlIOfFtPoag6w8o9nf3UUUjTha23mNC9xL8cVNb_Z0ZsCldw9YXNj_bQ7FHLe68VjpACn7lmMxxKWu989iruHqS7VOlOrj29xQgjrwFW7C4mEvF0yDl5WvsfXle9wA")
BOT_TOKEN = getenv("BOT_TOKEN", "2072190749:AAFtGSwIiz1cHe304bKUGdi4rdJcN-2C6PY")
BOT_NAME = getenv("BOT_NAME", "Alexa")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "-1001319845035")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/41126266cb7db2240e798.png")
admins = {}
API_ID = int(getenv("API_ID", "19360811"))
API_HASH = getenv("API_HASH", "5fd804c32a0885666d53b4ca5614bbdd")
BOT_USERNAME = getenv("BOT_USERNAME", "alexagroup_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "alexaassisten")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "robotprojectx")
PROJECT_NAME = getenv("PROJECT_NAME", "Alexa")
OWNER = getenv("OWNER", "seekorwhale")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/teamdaisyx/daisyxmusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "994286253").split()))
