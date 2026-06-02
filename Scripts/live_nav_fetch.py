import requests
import pandas as pd
from pathlib import Path

# Create folder automatically if it does not exist
output_dir = Path("data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

scheme_code = 125497
url = f"https://api.mfapi.in/mf/{scheme_code}"

try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()

    nav_df = pd.DataFrame(data["data"])
    nav_df["scheme_code"] = data["meta"]["scheme_code"]
    nav_df["scheme_name"] = data["meta"]["scheme_name"]

    output_file = output_dir / "hdfc_top100_live_nav.csv"
    nav_df.to_csv(output_file, index=False)

    print("NAV data fetched successfully.")
    print(f"Saved file: {output_file}")
    print(nav_df.head())

except requests.exceptions.RequestException as e:
    print("Error while fetching NAV data:", e)

except Exception as e:
    print("Error while processing NAV data:", e)