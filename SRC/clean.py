import pandas as pd
from .config import CREATED_DATE, COMPLAINT_TYPE, BOROUGH

def clean_311(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize and clean NYC 311 housing complaint data.
    """
    df = df.copy()
    df.columns = df.columns.str.lower()

    df = df.rename(columns={
        "created_date": CREATED_DATE,
        "complaint_type": COMPLAINT_TYPE,
        "borough": BOROUGH
    })

    df[CREATED_DATE] = pd.to_datetime(df[CREATED_DATE], errors="coerce")
    df = df.dropna(subset=[CREATED_DATE, COMPLAINT_TYPE, BOROUGH])

    df[BOROUGH] = df[BOROUGH].str.upper().str.strip()
    df[COMPLAINT_TYPE] = df[COMPLAINT_TYPE].str.strip()

    return df
