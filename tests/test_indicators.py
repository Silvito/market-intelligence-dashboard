import pandas as pd
# desde el archivo test_indicators.py, importamos las funciones que vamos a probar
from src.indicators import add_macd, add_rsi, add_sma

def test_sma_column_exists():
    # crea un dataframe de prueba
    df = pd.DataFrame({
        "Close": [100, 101, 102, 103, 104]
    })

    # aplica la función add_sma al dataframe de prueba
    df = add_sma(df, 3)

    # revisa si la columna SMA_3 existe en el dataframe resultante
    assert "SMA_3" in df.columns
    assert not df["SMA_3"].dropna().empty

def test_rsi_ranges():
    # crea un dataframe de prueba
    df = pd.DataFrame({
        "Close": [100, 101, 102, 103, 104]
    })

    # aplica la función add_rsi al dataframe de prueba
    df = add_rsi(df, 3)

    # revisa si los valores de RSI_3 están entre 0 y 100
    assert df["RSI_3"].dropna().between(0, 100).all()

def test_macd_columns_exist():
    # crea un dataframe de prueba
    df = pd.DataFrame({
        "Close": [100, 101, 102, 103, 104]
    })

    # aplica la función add_macd al dataframe de prueba
    df = add_macd(df)

    # revisa si las columnas MACD, MACD_SIGNAL y MACD_HIST existen en el dataframe resultante
    assert "MACD" in df.columns
    assert "MACD_SIGNAL" in df.columns
    assert "MACD_HIST" in df.columns