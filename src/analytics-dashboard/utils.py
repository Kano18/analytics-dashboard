"""
Utility helpers for Analytics Dashboard.
"""
from pathlib import Path
import pandas as pd

def load_data(filename: str = "[5/7] dataset_main (Master Travel Data.csv): TravelData.csv") -> pd.DataFrame:
    """Load CSV from data/ folder."""
    path = Path("data") / filename
    return pd.read_csv(path)
