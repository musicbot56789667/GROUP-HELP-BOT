from telegram import Update

from TeamLegend.plugins import ALL_MODULES

from .core.clients import application, pbot, tbot
from .core.logger import LOGS


def main():
    """Run bot."""
    LOGS.info("Successfully loaded modules: " + str(ALL_MODULES))
    # Telethon Starting
    tbot.start()
    # Pyrogram starting
    pbot.start()
    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
