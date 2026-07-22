from loguru import logger
import sys
import os

os.makedirs("backend/logs", exist_ok=True)

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level}</level> | "
           "{message}"
)

logger.add(
    "backend/logs/application.log",
    rotation="10 MB",
    retention="30 days",
    level="INFO",
)

app_logger = logger