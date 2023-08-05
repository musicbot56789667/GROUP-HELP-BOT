from telegram.ext import import Application
from TeamLegend.Config import TOKEN
import logging

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("teamlegend.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOGS = logging.getLogger(__name__)
  
application = Application.builder().token("TOKEN").build()
