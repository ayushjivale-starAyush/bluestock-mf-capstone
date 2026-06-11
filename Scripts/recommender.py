import pandas as pd

scheme_df = pd.read_csv("../data/processed/07_scheme_performance_cleaned.csv")

user_risk = input("Enter risk level (Low/Moderate/VeryHigh): ")

recommendations = (
    scheme_df[
        scheme_df["risk_grade"] == user_risk
    ]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    [["scheme_name", "sharpe_ratio"]]
    .head(3)
)

print("\nTop 3 Recommended Funds:\n")
print(recommendations)