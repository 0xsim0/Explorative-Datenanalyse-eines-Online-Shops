"""Utility script to summarize the e-commerce dataset."""

from pathlib import Path
import argparse
import pandas as pd

def load_data(csv_path: str | None = None) -> pd.DataFrame:
    """Load the e-commerce transactions dataset from ``csv_path``.

    Parameters
    ----------
    csv_path : str or None, optional
        Path to the CSV file. If ``None`` (default), the file ``data/data.csv``
        located relative to this script is used.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing the raw transaction data.
    """

    if csv_path is None:
        csv_path = Path(__file__).resolve().parents[1] / "data" / "data.csv"
    else:
        csv_path = Path(csv_path)

    return pd.read_csv(csv_path, encoding="latin1")


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned copy of ``df`` suitable for analysis.

    Parameters
    ----------
    df : pandas.DataFrame
        Raw data frame to clean.

    Returns
    -------
    pandas.DataFrame
        Cleaned data with additional ``TotalPrice`` column.
    """

    df = df.copy()
    df = df[df["Quantity"] > 0]
    df = df.dropna(subset=["CustomerID"])
    df["CustomerID"] = df["CustomerID"].astype(int)
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]
    return df


def main() -> None:
    """Parse command line arguments and print summary statistics."""

    parser = argparse.ArgumentParser(
        description="Compute basic statistics for the e-commerce dataset.")
    parser.add_argument(
        "--csv",
        default=None,
        help="Path to the CSV file (defaults to data/data.csv).",
    )
    args = parser.parse_args()

    df = clean_data(load_data(args.csv))
    total_revenue = df["TotalPrice"].sum()
    avg_basket = df.groupby("InvoiceNo")["TotalPrice"].sum().mean()
    print(f"Total revenue: {total_revenue:.2f}")
    print(f"Average basket value: {avg_basket:.2f}")


if __name__ == "__main__":
    main()
