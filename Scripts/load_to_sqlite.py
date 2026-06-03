import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

PROCESSED_DIR = Path("data/processed")

files = [
    "02_nav_history_cleaned.csv",
    "08_investor_transactions_cleaned.csv",
    "07_scheme_performance_cleaned.csv"
]

for file in files:
    df = pd.read_csv(PROCESSED_DIR / file)

    table_name = file.replace(".csv", "")

    df.to_sql(
        table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"{table_name} loaded successfully")

print("\nSQLite database created successfully!")