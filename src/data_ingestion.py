import pandas as pd
from src.logger import logger
import os

def load_data():
    logger.info("Loading data by logger")
    print("Loading data...")

    # data = pd.read_csv("data/Sample.csv")
    

    file_path = os.path.join("data", "Sample.csv")
    data = pd.read_csv(file_path)


    return data