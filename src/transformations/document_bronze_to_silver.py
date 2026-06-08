import pandas as pd
from pathlib import Path

df = pd.read_csv(
    "bronze/documents/document_bronze.csv"
)

print("Bronze Count:", len(df))

silver_df = (
    df
    .drop_duplicates()
)

silver_df["document_type"] = (
    silver_df["document_type"]
    .astype(str)
    .str.lower()
    .str.strip()
)

Path("silver/documents").mkdir(
    parents=True,
    exist_ok=True
)

silver_df.to_csv(
    "silver/documents/document_silver.csv",
    index=False
)

print("Silver Count:", len(silver_df))

print("Document Silver Layer Created")