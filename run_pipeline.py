import subprocess

print("Starting Mutual Fund Analytics Pipeline...")

# Step 1: Fetch scheme data
subprocess.run(["python", "Scripts/fetch_5_schemes.py"])

# Step 2: Fetch live NAV data
subprocess.run(["python", "Scripts/live_nav_fetch.py"])

# Step 3: Clean data and load into SQLite
subprocess.run(["python", "Scripts/day2_clean_load_sqlite.py"])

# Step 4: Load processed data into database
subprocess.run(["python", "Scripts/load_to_sqlite.py"])

print("Pipeline executed successfully!")
print("Database updated and ready for analysis.")