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

#bloque de prueba

if __name__ == "__main__":
    import pandas as pd

    df = pd.read_csv("data/procesada/spy.csv")

    df = add_sma(df, 20)
    df = add_ema(df, 20)
    df = add_rsi(df, 14)
    df = add_macd(df)
    df = add_bollinger_bands(df, 20, 2)
    df = add_average_volume(df, 20)

    columns_to_show = [
        "Date",
        "Close",
        "SMA_20",
        "EMA_20",
        "RSI_14",
        "MACD",
        "MACD_SIGNAL",
        "MACD_HIST",
        "BB_UPPER_20_2",
        "BB_MIDDLE_20",
        "BB_LOWER_20_2",
        "AVG_VOLUME_20"
    ]

    print(df[columns_to_show].tail(10))
    print("\nColumnas generadas:")
    print(df.columns)
    print("\nValores nulos:")
    print(df[columns_to_show].isnull().sum())


    