from loguru import logger

from src.config import LOG_FILE_PATH

logger.add(sink=LOG_FILE_PATH, level='INFO')
