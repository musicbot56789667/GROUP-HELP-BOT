import logging

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("teamlegend.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOGS = logging.getLogger(__name__
