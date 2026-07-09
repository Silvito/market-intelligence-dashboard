# Market Intelligence Dashboard — SPY & QQQ Technical Analysis

## Overview

Market Intelligence Dashboard is a Python-based financial data analysis project designed to evaluate the historical performance of technical trading strategies on major market ETFs.

The project focuses on answering questions such as:

* Which technical signals historically generated the best returns?
* How did each strategy behave during bull, bear, and sideways markets?
* How does each strategy compare against a Buy & Hold benchmark?

The initial implementation uses:

* SPY (S&P 500 ETF)
* QQQ (Nasdaq-100 ETF)

The architecture was designed to be easily extensible to additional assets such as:

* XLE (Energy Sector ETF)
* USO (United States Oil Fund)
* GLD (Gold ETF)
* TLT (20+ Year Treasury Bond ETF)

---

## Project Structure

```text
Market Intelligence Dashboard/
│
├── data/
│   ├── raw/              
│   └── procesada/
│
├── notebooks/
│   └── exploracion.ipynb 
│
├── src/
│   ├── data_loader.py  
│   ├── indicators.py   
│   ├── strategies.py   
│   ├── backtest.py     
│   └── config.py         
│
├── dashboard/
│   └── app.py            
│
├── tests/                
│   └── test_loader.py    
│
├── .gitignore            
├── requirements.txt  
└── README.md         

---

## Data Source

Historical market data is downloaded from Yahoo Finance using the `yfinance` library.

The project retrieves:

* Open price
* High price
* Low price
* Close price
* Trading volume

for both SPY and QQQ from 2010 to the present day.

Prices are automatically adjusted for:

* Stock splits
* Dividend distributions

using:

```python
auto_adjust=True
```

This guarantees accurate historical return calculations and fair comparisons with Buy & Hold strategies.

---

## Data Pipeline

The project currently implements a complete ETL pipeline:

### Extract

* Download historical OHLCV data from Yahoo Finance.

### Transform

* Flatten MultiIndex columns returned by `yfinance`.
* Remove duplicate rows.
* Remove missing values.
* Sort data chronologically.
* Reset DataFrame indices.

### Validate

The pipeline performs several quality checks:

* No missing values.
* Minimum dataset size validation.
* Chronological consistency validation.
* Non-negative volume validation.

Example:

```python
assert len(df) > 3000, "Dataset contains fewer than 3000 records"
assert df["Date"].is_monotonic_increasing, "Dates are not ordered"
assert (df["Volume"] >= 0).all(), "Negative volume detected"
```

### Load

Processed datasets are stored locally as CSV files for:

* Reproducibility
* Faster experimentation
* Decoupling data ingestion from analysis

Generated files:

```text
data/procesada/spy.csv
data/procesada/qqq.csv
```

---

## Current Features

* Historical market data download.
* Automatic corporate action adjustments.
* Data cleaning pipeline.
* Data quality validation.
* CSV persistence.
* Git version control.

---

## Planned Features

### Technical Indicators

* SMA 20
* SMA 50
* SMA 200
* RSI 14
* MACD
* ATR
* Bollinger Bands

### Trading Strategies

* Moving Average Crossover
* RSI Mean Reversion
* MACD Momentum
* Volatility Breakout

### Backtesting Engine

* Entry and exit simulation
* Transaction costs
* Performance metrics
* Benchmark comparison

### Interactive Dashboard

* Strategy comparison
* Equity curves
* Drawdown analysis
* Market regime analysis
* Signal visualization

---

## Installation

Clone the repository:

```bash
git clone <repository_url>
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Data Pipeline

Execute:

```bash
python src/data_loader.py
```

The script will:

1. Download SPY historical data.
2. Download QQQ historical data.
3. Clean and validate datasets.
4. Save processed CSV files.

---

## Technologies Used

* Python
* Pandas
* yfinance
* NumPy
* Git

---

## Project Status

Current version:

**Phase 1 — Data ingestion and validation pipeline completed.**

Next milestone:

**Implementation of technical indicators module (`indicators.py`).**# Market Intelligence Dashboard — SPY & QQQ Technical Analysis

## Overview

Market Intelligence Dashboard is a Python-based financial data analysis project designed to evaluate the historical performance of technical trading strategies on major market ETFs.

The project focuses on answering questions such as:

* Which technical signals historically generated the best returns?
* How did each strategy behave during bull, bear, and sideways markets?
* How does each strategy compare against a Buy & Hold benchmark?

The initial implementation uses:

* SPY (S&P 500 ETF)
* QQQ (Nasdaq-100 ETF)

The architecture was designed to be easily extensible to additional assets such as:

* XLE (Energy Sector ETF)
* USO (United States Oil Fund)
* GLD (Gold ETF)
* TLT (20+ Year Treasury Bond ETF)

---

## Project Structure

```text
Market Intelligence Dashboard/
│
├── data/
│   └── procesada/
│       ├── spy.csv
│       └── qqq.csv
│
├── src/
│   └── data_loader.py
│
├── venv/
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Data Source

Historical market data is downloaded from Yahoo Finance using the `yfinance` library.

The project retrieves:

* Open price
* High price
* Low price
* Close price
* Trading volume

for both SPY and QQQ from 2010 to the present day.

Prices are automatically adjusted for:

* Stock splits
* Dividend distributions

using:

```python
auto_adjust=True
```

This guarantees accurate historical return calculations and fair comparisons with Buy & Hold strategies.

---

## Data Pipeline

The project currently implements a complete ETL pipeline:

### Extract

* Download historical OHLCV data from Yahoo Finance.

### Transform

* Flatten MultiIndex columns returned by `yfinance`.
* Remove duplicate rows.
* Remove missing values.
* Sort data chronologically.
* Reset DataFrame indices.

### Validate

The pipeline performs several quality checks:

* No missing values.
* Minimum dataset size validation.
* Chronological consistency validation.
* Non-negative volume validation.

Example:

```python
assert len(df) > 3000, "Dataset contains fewer than 3000 records"
assert df["Date"].is_monotonic_increasing, "Dates are not ordered"
assert (df["Volume"] >= 0).all(), "Negative volume detected"
```

### Load

Processed datasets are stored locally as CSV files for:

* Reproducibility
* Faster experimentation
* Decoupling data ingestion from analysis

Generated files:

```text
data/procesada/spy.csv
data/procesada/qqq.csv
```

---

## Current Features

* Historical market data download.
* Automatic corporate action adjustments.
* Data cleaning pipeline.
* Data quality validation.
* CSV persistence.
* Git version control.

---

## Planned Features

### Technical Indicators

* SMA 20
* SMA 50
* SMA 200
* RSI 14
* MACD
* ATR
* Bollinger Bands

### Trading Strategies

* Moving Average Crossover
* RSI Mean Reversion
* MACD Momentum
* Volatility Breakout

### Backtesting Engine

* Entry and exit simulation
* Transaction costs
* Performance metrics
* Benchmark comparison

### Interactive Dashboard

* Strategy comparison
* Equity curves
* Drawdown analysis
* Market regime analysis
* Signal visualization

---

## Installation

Clone the repository:

```bash
git clone <repository_url>
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Data Pipeline

Execute:

```bash
python src/data_loader.py
```

The script will:

1. Download SPY historical data.
2. Download QQQ historical data.
3. Clean and validate datasets.
4. Save processed CSV files.

---

## Technologies Used

* Python
* Pandas
* yfinance
* NumPy
* Git

---

## Project Status

Current version:

**Phase 1 — Data ingestion and validation pipeline completed.**

Next milestone:

**Implementation of technical indicators module (`indicators.py`).**

