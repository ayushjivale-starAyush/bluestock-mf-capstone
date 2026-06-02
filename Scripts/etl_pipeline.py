import pandas as pd
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data folders
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

# Create processed folder if it doesn't exist
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

print("DAY 1 ETL PIPELINE STARTED")
print("=" * 60)

# Find all CSV files
csv_files = list(RAW_DIR.glob("*.csv"))

if not csv_files:
    print(f"No CSV files found in: {RAW_DIR}")
else:
    print(f"Total CSV files found: {len(csv_files)}")

    for file in csv_files:

        print("\n" + "=" * 60)
        print(f"File Name: {file.name}")
        print("=" * 60)

        try:
            df = pd.read_csv(file)

            # Shape
            rows, cols = df.shape
            print(f"\nRows: {rows}")
            print(f"Columns: {cols}")

            # Data types
            print("\nData Types:")
            print(df.dtypes)

            # First 5 rows
            print("\nFirst 5 Rows:")
            print(df.head())

            # Missing values
            print("\nMissing Values:")
            print(df.isnull().sum())

            # Duplicate rows
            print("\nDuplicate Rows:")
            print(df.duplicated().sum())

            # Save copy to processed folder
            output_file = PROCESSED_DIR / file.name
            df.to_csv(output_file, index=False)

            print(f"\nSaved to: {output_file}")

        except Exception as e:
            print(f"Error processing {file.name}: {e}")

print("\n" + "=" * 60)
print("DAY 1 ETL PIPELINE COMPLETED")
print("=" * 60)