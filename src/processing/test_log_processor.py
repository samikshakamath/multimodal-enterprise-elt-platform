from log_processor import process_log_file
from pathlib import Path

df = process_log_file(
    "data/logs/hadoop-hdfs-datanode-mesos-01.log"
)

Path("bronze/logs").mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    "bronze/logs/parsed_logs.csv",
    index=False
)

print(df.head())

print(f"\nRecords Parsed: {len(df)}")

print("\nSaved to bronze/logs/parsed_logs.csv")
print(df.shape)
print(df["log_level"].value_counts())