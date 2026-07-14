import pandas as pd
from src.logger import logger

def load_data():
    logger.info("Loading data by logger")
    print("Loading data...")

    data = pd.read_csv("data\Sample.csv")


    return data