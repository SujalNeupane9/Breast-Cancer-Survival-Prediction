import pandas as pd
from src.logger import get_console_logger
from src.paths import DATA_DIR
from typing import Optional


logger = get_console_logger('Data-ingestion')

## The data import from API is also imported here if there is any..
def ingest_data()-> pd.DataFrame:
    data = pd.read_csv(DATA_DIR)
    return data
