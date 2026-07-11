import pathlib

# ==========================
# Paths del proyecto
# ==========================

ROOT_DIR = pathlib.Path(__file__).parent.parent

DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "procesada"

# ==========================
# Configuración de mercado
# ==========================

SYMBOLS = [
    "SPY",
    "QQQ"
]

START_DATE = "2010-01-01"
INITIAL_BALANCE = 1000.0

# ==========================
# Configuración indicadores
# ==========================

DEFAULT_SMA_SHORT = 20
DEFAULT_SMA_MEDIUM = 50
DEFAULT_SMA_LONG = 200
DEFAULT_EMA_PERIOD = 20
DEFAULT_RSI_PERIOD = 14