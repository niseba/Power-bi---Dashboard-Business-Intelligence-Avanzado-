import pandas as pd
import glob
import os

def extract_orders(raw_path: str) -> pd.DataFrame:
    csv_files = glob.glob(os.path.join(raw_path, "orders_*.csv"))
    
    if not csv_files:
        raise FileNotFoundError(f"No se encontraron archivos CSV en {raw_path}")
    
    dataframes = []
    for file in csv_files:
     df = pd.read_csv(file, encoding="utf-8-sig", on_bad_lines="skip")
     print(f"{os.path.basename(file)}: {df.columns.tolist()}")
     dataframes.append(df)
    
    combined = pd.concat(dataframes, ignore_index=True)
    return combined