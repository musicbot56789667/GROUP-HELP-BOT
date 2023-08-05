from telegram.ext import Application
from TeamLegend.Config import TOKEN
from .logger import LOGS
LOGS.info("Client Starting")  
application = Application.builder().token("TOKEN").build()
