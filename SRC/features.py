import pandas as pd
from .config import CREATED_DATE

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create time-based features for analysis and modeling.
    """
    d = df.copy()

    d["year"] = d[CREATED_DATE].dt.year
    d["month"] = d[CREATED_DATE].dt.month
    d["year_month"] = d[CREATED_DATE].dt.to_period("M").astype(str)

    return d
