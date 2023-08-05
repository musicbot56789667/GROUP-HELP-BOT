from telegram.ext import Application
from .client import 
from pyrogram import Client
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

from .logger import LOGS
loop = None

LOGS.info("Client Starting")
application = Application.builder().token("TOKEN").build()
tbot = TelegramClient(
    session="LegendTBot",
    api_id=APP_ID,
    api_hash=API_HASH,
    loop=loop,
    app_version=__version__,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=TOKEN)

pbot = Client("LegendPBot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)

