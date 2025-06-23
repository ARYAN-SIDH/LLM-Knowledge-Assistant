import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MODEL_NAME = os.getenv('MODEL_NAME', 'distilbert-base-uncased-distilled-squad')
    CACHE_TIMEOUT = int(os.getenv('CACHE_TIMEOUT', '600'))
