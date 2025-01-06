import logging
import logging.config
from pathlib import Path

# Create logs directory if it doesn't exist
LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(exist_ok=True)

# Define the log file path
LOG_FILE = LOGS_DIR / "backend.log"

# Logger configuration
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
        "detailed": {
            "format": "%(asctime)s - %(name)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": str(LOG_FILE),
            "formatter": "detailed",
        },
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["file", "console"],
    },
    "loggers": {
        "uvicorn": {
            "level": "INFO",
            "handlers": ["file", "console"],
            "propagate": False,
        },
        "fastapi": {
            "level": "DEBUG",
            "handlers": ["file", "console"],
            "propagate": False,
        },
    },
}

# Configure logging
logging.config.dictConfig(LOGGING_CONFIG)

# Get logger for use in the project
logger = logging.getLogger("backend")
