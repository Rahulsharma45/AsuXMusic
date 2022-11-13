from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "10571256")) 
API_HASH = getenv("API_HASH", "a33ded138ee2b56111ee7cd5d3355c38")
ASS_HANDLER = list(getenv("ASS_HANDLER", "/").split())
BOT_TOKEN = getenv("BOT_TOKEN")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
LOGGER_ID = int(getenv("LOGGER_ID"))
MONGO_DB_URI = getenv("MONGO_DB_URI")
OWNER_ID = list(map(int, getenv("OWNER_ID", "2102097596").split()))
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/18a2c95d927848fa5f192.jpg")
START_IMG = getenv("START_IMG","https://te.legra.ph/file/7fd1cecadabad0bf96733.jpg")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TheFriendGroup")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/KSKxBots")
STRING_SESSION = getenv("STRING_SESSION", None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2102097596").split()))
