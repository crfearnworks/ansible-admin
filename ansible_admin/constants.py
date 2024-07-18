import os
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

START_IP = os.getenv('START_IP')
END_IP = os.getenv('END_IP')
OUTPUT_FILE = os.getenv('OUTPUT_FILE')

env_vars = [
    'START_IP',
    'END_IP',
    'OUTPUT_FILE',]

# Iterate through the list and check if any are not set
unset_vars = [var for var in env_vars if os.getenv(var) is None]

# Log environment variables that are not set
if unset_vars:
    logger.warning(f"Missing environment variables: {', '.join(unset_vars)}")
else:
    logger.info("All environment variables are set.")