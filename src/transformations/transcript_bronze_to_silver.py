import pandas as pd
from pathlib import Path

df = pd.read_csv(
    "bronze/transcripts/transcript_bronze.csv"
)

print("Bronze Count:", len(df))

silver_df = (
    df
    .drop_duplicates()
)

silver_df["message"] = (
    silver_df["message"]
    .astype(str)
    .str.strip()
)

silver_df = (
    silver_df[
        silver_df["message"] != ""
    ]
)

Path("silver/transcripts").mkdir(
    parents=True,
    exist_ok=True
)

silver_df.to_csv(
    "silver/transcripts/transcript_silver.csv",
    index=False
)

print("Silver Count:", len(silver_df))

print("Transcript Silver Layer Created")