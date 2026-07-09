## Data Ingestion Pipeline 08/07/2026

Historical OHLCV data is downloaded from Yahoo Finance using yfinance.

The ingestion pipeline performs:

- Download of SPY and QQQ data since 2010
- Automatic adjustment for dividends and stock splits
- MultiIndex normalization
- Missing value removal
- Duplicate removal
- Chronological ordering
- Data quality validation:
  - No missing values
  - Minimum number of observations
  - Chronological consistency
  - Non-negative volume

Processed datasets are stored locally as CSV files for reproducibility and faster experimentation.