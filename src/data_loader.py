import yfinance as yf #api de yahoo finance para datos de mercado
import pandas as pd #pandas para trabajar con dataframes

#METODOS

#metodo de descarga de datos de yahoo finance, recibe un simbolo y una fecha de inicio, devuelve un dataframe con los datos descargados
def download_data(symbol, start_date="2010-01-01"):
    try: #capturamos errores en caso de que la descarga falle
        df = yf.download(
            symbol,
            start=start_date,
            auto_adjust=True,
            progress=False
        )

        #si las columnas son un MultiIndex, se toma el primer nivel de las columnas
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
        #si las columnas tienen un nombre, se elimina para evitar problemas al guardar en csv
        if df.columns.name is not None:
            df.columns.name = None
        print(f"\nColumnas descargadas para {symbol}:") #temporal para verificar que se descargaron las columnas correctas
        print(df.columns)

        if df.empty:
            raise ValueError(f"No se descargaron datos para {symbol}")

        df.reset_index(inplace=True)

        return df

    except Exception as e:
        print(f"Error descargando {symbol}: {e}")
        return None

#metodo de limpieza de datos, recibe un dataframe y devuelve un dataframe limpio
def clean_data(df):
    if df is None: #manejamos errores de none
        return None
    
    df = df.drop_duplicates()
    df = df.dropna()
    df = df.sort_values(by="Date")
    df = df.reset_index(drop=True) #evita que queden indices raros despues de borrar filas duplicadas o nulas
    return df

#metodo de validacion de datos, recibe un dataframe y valida que cumpla con ciertas condiciones
def validate_data(df):
    if df is None: #manejamos errores de none
        raise ValueError("El dataframe es None, no se puede validar")
    assert not df.isnull().values.any(), "Existen valores nulos en el dataset"
    assert len(df) > 3000, "El dataset tiene menos de 3000 registros"
    assert df["Date"].is_monotonic_increasing, "Las fechas no están ordenadas cronológicamente"
    assert (df["Volume"] >= 0).all(), "Existen volúmenes negativos"

#guarda el df en archivo csv
def save_data(df, filename):
    df.to_csv(filename, index=False)

#se descargan y validan los datos de SPY y QQQ, y se imprimen las primeras filas de cada dataframe
if __name__ == "__main__":
    #descargar, limpiar y despues validar datos de SPY y QQQ
    spy = clean_data(download_data("SPY"))
    validate_data(spy)
    qqq = clean_data(download_data("QQQ"))
    validate_data(qqq)

    #guardamos los datos en archivos csv
    save_data(spy, "data/procesada/spy.csv")
    save_data(qqq, "data/procesada/qqq.csv")

    #imprimimos las primeras filas de cada dataframe para verificar que se descargaron correctamente

    print(spy.head())
    print(qqq.head())