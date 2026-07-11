import pandas as pd
from dash import Dash, html, dcc
import plotly.graph_objects as go

from src.strategies import sma_crossover
from src.backtest import run_backtest
from src.config import INITIAL_BALANCE

# ==========================================
# Carga y preparación de datos
# ==========================================

df = pd.read_csv("data/procesada/spy.csv")

df = sma_crossover(df)

df = run_backtest(df, "SMA_SIGNAL")


# ==========================================
# Métricas principales
# ==========================================

final_capital = df["Strategy_Equity"].iloc[-1]

strategy_return = (
    (final_capital / INITIAL_BALANCE) - 1
) * 100

buy_hold_return = (
    (df["Market_Equity"].iloc[-1] / INITIAL_BALANCE) - 1
) * 100


# ==========================================
# Gráfico Equity Curve
# ==========================================

equity_fig = go.Figure()

equity_fig.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["Strategy_Equity"],
        name="SMA Strategy"
    )
)

equity_fig.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["Market_Equity"],
        name="Buy & Hold"
    )
)

equity_fig.update_layout(
    title="Strategy Equity vs Buy & Hold",
    xaxis_title="Date",
    yaxis_title="Portfolio Value"
)


# ==========================================
# Aplicación Dash
# ==========================================

app = Dash(__name__)

app.layout = html.Div(

    children=[

        html.H1(
            "Market Intelligence Dashboard"
        ),

        html.H3(
            "SMA 20/50 Crossover Strategy"
        ),

        html.Div(
            children=[
                html.P(
                    f"Initial Balance: ${INITIAL_BALANCE:,.2f}"
                ),

                html.P(
                    f"Final Balance: ${final_capital:,.2f}"
                ),

                html.P(
                    f"Strategy Return: {strategy_return:.2f}%"
                ),

                html.P(
                    f"Buy & Hold Return: {buy_hold_return:.2f}%"
                )
            ]
        ),

        dcc.Graph(
            figure=equity_fig
        )

    ]

)


if __name__ == "__main__":
    app.run(debug=True)