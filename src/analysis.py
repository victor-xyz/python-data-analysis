import json
from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "sample_sales.json"


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load and validate the sample sales dataset."""
    with path.open("r", encoding="utf-8") as file:
        records = json.load(file)

    df = pd.DataFrame(records)
    required = {"date", "region", "product", "units", "unit_price"}

    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    df["date"] = pd.to_datetime(df["date"], errors="raise")
    df["revenue"] = df["units"] * df["unit_price"]

    return df


def summarise(df: pd.DataFrame) -> None:
    print("Revenue by product:")
    print(df.groupby("product")["revenue"].sum().sort_values(ascending=False))

    print("\nRevenue by region:")
    print(df.groupby("region")["revenue"].sum().sort_values(ascending=False))

    print("\nTotal revenue:")
    print(f"{df['revenue'].sum():,.0f}")


if __name__ == "__main__":
    data = load_data()
    summarise(data)
