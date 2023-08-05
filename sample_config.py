import os

API_ID = os.environ.get("API_ID", 123)
API_HASH = os.environ.get("API_HASH", None)
ALLOW_CHATS = os.environ.get("ALLOW_CHATS", True)
BL_CHATS = set(int(x) for x in os.environ.get("BL_CHATS", "").split())
DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS", "").split())
DB_URI = os.environ.get("DATABASE_URL")
DEL_CMDS = bool(os.environ.get("DEL_CMDS", False)
LOGGER_ID = os.environ.get("LOGGER_ID", None)
LOAD = os.environ.get("LOAD", "").split()
MONGO_URI = os.environ.get("MONGO_URI", None)
NO_LOAD = os.environ.get("NO_LOAD", "").split()
OWNER_ID = int(os.environ.get("OWNER_ID", None))
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "LegendBot_OP")
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
TOKEN = os.environ.get("TOKEN", None)
TIME_API_KEY = os.environ.get("TIME_API_KEY", None)
WORKERS = int(os.environ.get("WORKERS", 8))


