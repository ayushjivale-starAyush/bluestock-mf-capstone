import requests
import pandas as pd
from pathlib import Path

schemes = {
    119551: "sbi_bluechip",
    120503: "icici_bluechip",
    118632: "nippon_large_cap",
    119092: "axis_bluechip",
    120841: "kotak_bluechip"
}

output_dir = Path("data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

for code, name in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()
        df = pd.DataFrame(data["data"])

        file_name = output_dir / f"{name}.csv"
        df.to_csv(file_name, index=False)

        print(f"Saved: {file_name}")

    except Exception as e:
        print(f"Error for {code}: {e}")