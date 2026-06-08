import pandas as pd

df = pd.read_csv(
    "silver/logs/silver_logs.csv"
)

print("Rows:", len(df))

# Check 1
null_timestamps = df["timestamp"].isnull().sum()

# Check 2
null_components = df["component"].isnull().sum()

# Check 3
valid_levels = ["INFO", "WARN", "ERROR"]

invalid_levels = (
    ~df["log_level"].isin(valid_levels)
).sum()

# Check 4
empty_messages = (
    df["message"]
    .fillna("")
    .str.strip()
    .eq("")
    .sum()
)

print("\nDATA QUALITY REPORT")
print("--------------------")

print(f"Null Timestamps: {null_timestamps}")
print(f"Null Components: {null_components}")
print(f"Invalid Log Levels: {invalid_levels}")
print(f"Empty Messages: {empty_messages}")

if (
    null_timestamps == 0
    and null_components == 0
    and invalid_levels == 0
):
    print("\nQUALITY CHECK PASSED")
else:
    print("\nQUALITY CHECK FAILED")