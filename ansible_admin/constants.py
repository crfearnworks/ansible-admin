import os
from dotenv import load_dotenv, find_dotenv
from loguru import logger

# Load environment variables
load_dotenv(find_dotenv())

# Define constants
START_IP = os.getenv('START_IP')
END_IP = os.getenv('END_IP')
