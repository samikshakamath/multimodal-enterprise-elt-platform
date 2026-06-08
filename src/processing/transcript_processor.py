import pandas as pd
from pathlib import Path


INPUT_FILE = "data/transcripts/twcs.csv"

OUTPUT_FILE = "bronze/transcripts/transcript_bronze.csv"


df = pd.read_csv(INPUT_FILE)


bronze_df = pd.DataFrame({
    "interaction_id": df["tweet_id"],
    "timestamp": df["created_at"],
    "speaker": df["author_id"],
    "speaker_type": df["inbound"].apply(
        lambda x: "Customer" if x else "Support"
    ),
    "message": df["text"]
})


Path("bronze/transcripts").mkdir(
    parents=True,
    exist_ok=True
)


bronze_df.to_csv(
    OUTPUT_FILE,
    index=False
)


print(bronze_df.head())

print("\nRows:", len(bronze_df))

print("\nBronze transcript layer created.")