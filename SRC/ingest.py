import pandas as pd

def load_csv(path: str) -> pd.DataFrame:
    """
    Load a cached CSV exported from the NYC 311 API.
    """
    return pd.read_csv(path)
