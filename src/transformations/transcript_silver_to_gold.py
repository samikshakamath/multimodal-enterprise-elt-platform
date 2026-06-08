import pandas as pd
from pathlib import Path

df = pd.read_csv(
    "silver/transcripts/transcript_silver.csv"
)

Path("gold/transcripts").mkdir(
    parents=True,
    exist_ok=True
)

# Customer vs Support Volume

speaker_summary = (
    df.groupby("speaker_type")
      .size()
      .reset_index(name="message_count")
)

speaker_summary.to_csv(
    "gold/transcripts/speaker_summary.csv",
    index=False
)

print("\nMessages By Speaker Type")
print(speaker_summary)

# Top Support Organizations

support_summary = (
    df[df["speaker_type"] == "Support"]
    .groupby("speaker")
    .size()
    .reset_index(name="message_count")
    .sort_values(
        by="message_count",
        ascending=False
    )
    .head(20)
)

support_summary.to_csv(
    "gold/transcripts/top_support_brands.csv",
    index=False
)

print("\nTop Support Brands")
print(support_summary.head(10))