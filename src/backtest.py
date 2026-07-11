from src.config import INITIAL_BALANCE
import numpy as np

def run_backtest(df, signal_column, initial_balance=INITIAL_BALANCE):
    """
    Ejecuta un backtest vectorizado basado en señales de trading.

    Parámetros:
        df (pd.DataFrame): DataFrame con precios y señales.
        signal_column (str): Nombre de la columna de señales.
                             Ejemplo: "SMA_SIGNAL"
        initial_balance (float): Capital inicial del backtest.

    Retorna:
        pd.DataFrame: DataFrame con métricas y equity curve agregadas.
    """

    df = df.copy()

    # ==========================================================
    # 1) Retorno diario del mercado
    # ==========================================================

    df["Market_Return"] = df["Close"].pct_change()

    # ==========================================================
    # 2) Construcción de posiciones
    #
    # Señal:
    #  1  -> entrar comprado
    # -1  -> salir de la posición
    #  0  -> mantener estado anterior
    # ==========================================================

    df["Position"] = np.nan

    df.loc[df[signal_column] == 1, "Position"] = 1
    df.loc[df[signal_column] == -1, "Position"] = 0

    # Mantener la última posición conocida
    df["Position"] = df["Position"].ffill()

    # Si al comienzo nunca hubo compra, estamos fuera del mercado
    df["Position"] = df["Position"].fillna(0)

    # ==========================================================
    # 3) Retorno de la estrategia
    #
    # shift(1) evita lookahead bias:
    # la señal aparece al cierre y operamos al día siguiente.
    # ==========================================================

    df["Strategy_Return"] = (
        df["Position"].shift(1).fillna(0)
        * df["Market_Return"]
    )

    # ==========================================================
    # 4) Curvas de capital
    # ==========================================================

    df["Market_Equity"] = (
        (1 + df["Market_Return"])
        .cumprod()
        * initial_balance
    )

    df["Strategy_Equity"] = (
        (1 + df["Strategy_Return"])
        .cumprod()
        * initial_balance
    )

    return df

if __name__ == "__main__":
    import pandas as pd
    from src.strategies import sma_crossover
    df = pd.read_csv("data/procesada/spy.csv")
    df = sma_crossover(df)
    df = run_backtest(df, "SMA_SIGNAL")

    total_return = (df["Strategy_Equity"].iloc[-1] / INITIAL_BALANCE - 1)
    market_return = (df["Market_Equity"].iloc[-1] / INITIAL_BALANCE - 1)
    sharpe_ratio = (df["Strategy_Return"].mean() / df["Strategy_Return"].std()) * (252 ** 0.5)
    drawdown = (df["Strategy_Equity"] / df["Strategy_Equity"].cummax()) - 1
    max_drawdown = drawdown.min()
    trades = (df["SMA_SIGNAL"] != 0).sum() / 2

    print("SMA CROSSOVER BACKTEST")
    print("Initial Capital: ", INITIAL_BALANCE)
    print("Final Capital: ", df["Strategy_Equity"].iloc[-1])
    print("Strategy return: ", (total_return * 100), "%")
    print("buy and hold return: ", (market_return * 100), "%")
    print("Sharpe ratio: ", sharpe_ratio)
    print("Max drawdown: ", (max_drawdown * 100), "%")
    print("Number of trades: ", trades)
    

