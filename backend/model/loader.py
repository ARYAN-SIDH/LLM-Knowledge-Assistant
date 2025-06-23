from transformers import pipeline
from config import Config

def get_pipeline():
    return pipeline('question-answering', model=Config.MODEL_NAME)
