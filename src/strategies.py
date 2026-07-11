
from src.indicators import add_sma
from src.config import (DEFAULT_SMA_SHORT, DEFAULT_SMA_MEDIUM)
def sma_crossover(df):
     """
    Cruce medias moviles:
    Genera una señal de compra (1) cuando la SMA corta cruza por encima
    de la SMA media, y una señal de venta (-1) cuando la SMA corta cruza
    por debajo de la SMA media.
    Parámetros:
        df (pd.DataFrame): DataFrame con datos de mercado.
    Retorna:
        pd.DataFrame: DataFrame con una nueva columna 'SMA_SIGNAL'.
            1  -> cruce alcista
           -1  -> cruce bajista
            0  -> sin señal
    """
     # Calculamos las medias necesarias
     df = add_sma(df, DEFAULT_SMA_SHORT)
     df = add_sma(df, DEFAULT_SMA_MEDIUM)
     sma_short = df[f"SMA_{DEFAULT_SMA_SHORT}"]
     sma_medium = df[f"SMA_{DEFAULT_SMA_MEDIUM}"]

    # Inicializamos la columna de señales
     df["SMA_SIGNAL"] = 0

    # Cruce alcista
     bullish_cross = ((sma_short > sma_medium) & (sma_short.shift(1) <= sma_medium.shift(1)))

    # Cruce bajista
     bearish_cross = ((sma_short < sma_medium) & (sma_short.shift(1) >= sma_medium.shift(1)))

    # Asignamos señales
     df.loc[bullish_cross, "SMA_SIGNAL"] = 1
     df.loc[bearish_cross, "SMA_SIGNAL"] = -1
     return df


#bloque de prueba
if __name__ == "__main__":
     import pandas as pd
     df = pd.read_csv("data/procesada/spy.csv")
     df = sma_crossover(df)
     signals = df[df["SMA_SIGNAL"] != 0]
     print(signals[[
        "Date",
        f"SMA_{DEFAULT_SMA_SHORT}",
        f"SMA_{DEFAULT_SMA_MEDIUM}",
        "SMA_SIGNAL"]])
     print("\nCantidad total de señales:")
     print(len(signals))