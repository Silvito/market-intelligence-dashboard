#traemos las constantes desde config.py
from src.config import (DEFAULT_RSI_PERIOD,DEFAULT_SMA_SHORT,DEFAULT_SMA_MEDIUM,DEFAULT_SMA_LONG,DEFAULT_EMA_PERIOD)

#Indicadores para el analisis tecnico de los datos de mercado

#SMA o media movil simple, recibe un dataframe y un periodo, devuelve el dataframe con una nueva columna con la SMA
def add_sma(df, period):
    df[f"SMA_{period}"] = (
        df["Close"]
        .rolling(window=period)
        .mean()
    )

    return df

#EMA o media movil exponencial, recibe un dataframe y un periodo, devuelve el dataframe con una nueva columna con la EMA
def add_ema(df, period):
    df[f"EMA_{period}"] = (
        df["Close"]
        .ewm(
            span=period,
            adjust=False
        )
        .mean()
    )

    return df

#RSI o indice de fuerza relativa, recibe un dataframe y un periodo, devuelve el dataframe con una nueva columna con el RSI
def add_rsi(df, period=14):

    delta = df["Close"].diff()

    gain = delta.clip(lower=0)

    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(period).mean()

    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss

    df[f"RSI_{period}"] = 100 - (
        100 / (1 + rs)
    )

    return df

#MACD o convergencia/divergencia de medias moviles, recibe un dataframe y devuelve el dataframe con tres nuevas columnas: MACD, MACD_SIGNAL y MACD_HIST
def add_macd(df):

    ema12 = df["Close"].ewm(
        span=12,
        adjust=False
    ).mean()

    ema26 = df["Close"].ewm(
        span=26,
        adjust=False
    ).mean()

    df["MACD"] = ema12 - ema26

    df["MACD_SIGNAL"] = (
        df["MACD"]
        .ewm(
            span=9,
            adjust=False
        )
        .mean()
    )

    df["MACD_HIST"] = (
        df["MACD"]
        - df["MACD_SIGNAL"]
    )

    return df

#Bollinger Bands, recibe un dataframe, un periodo y un numero de desviaciones estandar, devuelve el dataframe con tres nuevas columnas: BB_UPPER, BB_LOWER y BB_MIDDLE
def add_bollinger_bands(df, period=20, num_std_dev=2):
    sma20 = df["Close"].rolling(period).mean()
    std20 = df["Close"].rolling(period).std()

    df[f"BB_UPPER_{period}_{num_std_dev}"] = sma20 + (std20 * num_std_dev)
    df[f"BB_LOWER_{period}_{num_std_dev}"] = sma20 - (std20 * num_std_dev)
    df[f"BB_MIDDLE_{period}"] = sma20

    return df

#Average Volume, recibe un dataframe y un periodo, devuelve el dataframe con una nueva columna con el promedio de volumen
def add_average_volume(df,period=20):
    df[f"AVG_VOLUME_{period}"] = (
        df["Volume"]
        .rolling(period)
        .mean()
    )

    return df

#Agrega todos los indicadores al dataframe, recibe un dataframe y devuelve el dataframe con todas las columnas de indicadores
def add_all_indicators(df):
    df = add_sma(df, DEFAULT_SMA_SHORT)
    df = add_sma(df, DEFAULT_SMA_MEDIUM)
    df = add_sma(df, DEFAULT_SMA_LONG)
    df = add_ema(df, DEFAULT_EMA_PERIOD)
    df = add_rsi(df, DEFAULT_RSI_PERIOD)
    df = add_macd(df)
    df = add_bollinger_bands(df, 20, 2)
    df = add_average_volume(df, 20)
    return df


    