import pandas as pd
from pathlib import Path

def load_data():
    data_path = Path(__file__).resolve().parents[1] / "data" / "data.csv"
    return pd.read_csv(data_path, encoding="latin1")


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df[df["Quantity"] > 0]
    df = df.dropna(subset=["CustomerID"])
    df["CustomerID"] = df["CustomerID"].astype(int)
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]
    return df


def main():
    df = clean_data(load_data())
    total_revenue = df["TotalPrice"].sum()
    avg_basket = df.groupby("InvoiceNo")["TotalPrice"].sum().mean()
    print(f"Total revenue: {total_revenue:.2f}")
    print(f"Average basket value: {avg_basket:.2f}")


if __name__ == "__main__":
    main()
