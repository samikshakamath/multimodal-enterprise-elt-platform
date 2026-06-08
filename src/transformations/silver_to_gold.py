import pandas as pd
from pathlib import Path

df = pd.read_csv(
    "silver/logs/silver_logs.csv"
)

Path("gold/logs").mkdir(
    parents=True,
    exist_ok=True
)

log_summary = (
    df.groupby("log_level")
      .size()
      .reset_index(name="event_count")
)

log_summary.to_csv(
    "gold/logs/log_level_summary.csv",
    index=False
)

print(log_summary)
component_summary = (
    df.groupby("component")
      .size()
      .reset_index(name="event_count")
      .sort_values(
          by="event_count",
          ascending=False
      )
)

component_summary.to_csv(
    "gold/logs/component_summary.csv",
    index=False
)

error_summary = (
    df[df["log_level"] == "ERROR"]
      .groupby("component")
      .size()
      .reset_index(name="error_count")
      .sort_values(
          by="error_count",
          ascending=False
      )
)

error_summary.to_csv(
    "gold/logs/error_summary.csv",
    index=False
)