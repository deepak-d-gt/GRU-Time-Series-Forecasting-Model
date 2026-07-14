# from src.data_ingestion import load_data

# def test_load_data():
#     data = load_data()
#     assert len(data) > 0

import sys
import os

sys.path.append(os.path.abspath("."))

from src.data_ingestion import load_data

def test_load_data():
    data = load_data()
    assert len(data) > 0