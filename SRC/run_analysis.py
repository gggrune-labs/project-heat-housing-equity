from src.ingest import load_csv
from src.clean import clean_311
from src.features import build_features
from src.stats import monthly_counts, regression, anova, ancova

df = load_csv("data/raw/nyc311.csv")
df = clean_311(df)
df = build_features(df)

monthly = monthly_counts(df)
reg = regression(monthly)
