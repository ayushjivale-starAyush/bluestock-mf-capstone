import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

###################################
# 1. Clean NAV History
###################################

nav_df = pd.read_csv(RAW_DIR / "02_nav_history.csv")

# Convert date column
nav_df["date"] = pd.to_datetime(nav_df["date"], errors="coerce")
nav_df = nav_df.dropna(subset=["date"])

# Sort by scheme and date
nav_df = nav_df.sort_values(["amfi_code", "date"])

# Remove duplicates
nav_df = nav_df.drop_duplicates()

# Keep only NAV > 0
nav_df = nav_df[nav_df["nav"] > 0]

# Forward fill missing values
nav_df["nav"] = nav_df.groupby("amfi_code")["nav"].ffill()

nav_df.to_csv(
    PROCESSED_DIR / "02_nav_history_cleaned.csv",
    index=False
)

print("NAV History cleaned.")

###################################
# 2. Clean Investor Transactions
###################################

trans_df = pd.read_csv(RAW_DIR / "08_investor_transactions.csv")

trans_df["transaction_date"] = pd.to_datetime(
    trans_df["transaction_date"],
    errors="coerce"
)

trans_df = trans_df.dropna(subset=["transaction_date"])

trans_df = trans_df[trans_df["amount_inr"] > 0]

trans_df["transaction_type"] = (
    trans_df["transaction_type"]
    .str.strip()
    .str.title()
)

trans_df.to_csv(
    PROCESSED_DIR / "08_investor_transactions_cleaned.csv",
    index=False
)

print("Investor transactions cleaned.")

###################################
# 3. Clean Scheme Performance
###################################

perf_df = pd.read_csv(RAW_DIR / "07_scheme_performance.csv")

print(perf_df.columns)

# Ensure returns are numeric
# Convert expense ratio to numeric
perf_df["expense_ratio_pct"] = pd.to_numeric(
    perf_df["expense_ratio_pct"],
    errors="coerce"
)

# Keep valid expense ratios
perf_df = perf_df[
    (perf_df["expense_ratio_pct"] >= 0.1)
    &
    (perf_df["expense_ratio_pct"] <= 2.5)
]

perf_df.to_csv(
    PROCESSED_DIR /
    "07_scheme_performance_cleaned.csv",
    index=False
)

print("Scheme performance cleaned.")

print("\nDAY 2 CLEANING COMPLETED")