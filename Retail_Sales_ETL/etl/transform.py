import pandas as pd


def transform(orders: pd.DataFrame) -> pd.DataFrame:

    # ── 1. ELIMINAR DUPLICADOS ──────────────────────────────────────────
    before = len(orders)
    orders = orders.drop_duplicates(subset=["Order ID", "Product ID", "Customer ID"])
    duplicates_removed = before - len(orders)
    print(f"   ✔ Duplicados eliminados:           {duplicates_removed}")

    # ── 2. ESTANDARIZAR FECHAS ──────────────────────────────────────────
    for col in ["Order Date", "Ship Date"]:
        if col in orders.columns:
            orders[col] = pd.to_datetime(orders[col], format="mixed", dayfirst=False, errors="coerce")

    invalid_dates = orders["Order Date"].isna().sum()

    for col in ["Order Date", "Ship Date"]:
        if col in orders.columns:
            orders[col] = orders[col].dt.strftime("%Y-%m-%d")

    print(f"   ✔ Fechas estandarizadas            (fechas inválidas encontradas: {invalid_dates})")

    # ── 3. LIMPIAR COLUMNA SEGMENT ──────────────────────────────────────
    if "Segment" in orders.columns:
        orders["Segment"] = orders["Segment"].str.strip().str.title()
        print(f"   ✔ Segment normalizado              (strip + title case)")

    return orders