import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import pandas as pd
import pytest


from src.data_loader import validate_data


def test_validate_data_accepts_valid_dataframe():

    df = pd.DataFrame({
        "Date": pd.date_range("2010-01-01", periods=3001),
        "Close": [100] * 3001,
        "High": [101] * 3001,
        "Low": [99] * 3001,
        "Open": [100] * 3001,
        "Volume": [1000000] * 3001
    })

    validate_data(df)

def test_validate_data_detects_null_values():

    df = pd.DataFrame({
        "Date": pd.date_range("2010-01-01", periods=3001),
        "Close": [100] * 3001,
        "High": [101] * 3001,
        "Low": [99] * 3001,
        "Open": [100] * 3001,
        "Volume": [1000000] * 3001
    })

    df.loc[0, "Close"] = None

    with pytest.raises(AssertionError):
        validate_data(df)

def test_validate_data_detects_negative_volume():

    df = pd.DataFrame({
        "Date": pd.date_range("2010-01-01", periods=3001),
        "Close": [100] * 3001,
        "High": [101] * 3001,
        "Low": [99] * 3001,
        "Open": [100] * 3001,
        "Volume": [1000000] * 3001
    })

    df.loc[0, "Volume"] = -1

    with pytest.raises(AssertionError):
        validate_data(df)