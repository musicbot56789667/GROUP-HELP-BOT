import os

from dotenv import load_dotenv
from core.logger import LOGS

if os.path.exists(".env"):
    load_dotenv(".env")

ENV = bool(os.environ.get("ENV", False))

if ENV or os.path.exists(".env"):
    from sample_config import *
    LOGS.info("Using Sample Config File")
elif os.path.exists("config.py"):
    from config import *
    LOGS.info("Using config file")
else:
    LOGS.info("Config file isn't exist make file config.py and add all required variable")
