import pandas as pd
import os
from datetime import datetime


def load(df: pd.DataFrame, processed_path: str) -> None:
    os.makedirs(processed_path, exist_ok=True)

    # Archivo fijo para Power BI
    output_path = os.path.join(processed_path, "superstore_clean.csv")
    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    # Log con timestamp para auditoría
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = os.path.join(processed_path, "etl_log.txt")
    with open(log_path, "w") as f:
        f.write(f"ETL ejecutado: {timestamp}\n")
        f.write(f"Total filas exportadas: {len(df):,}\n")
        f.write(f"Columnas: {list(df.columns)}\n")

    print(f"   ✔ Archivo exportado:               {output_path}")
    print(f"   ✔ Log de auditoría:                {log_path}")
    print(f"   ✔ Total filas finales:             {len(df):,}")