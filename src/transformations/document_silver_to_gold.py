import pandas as pd
from pathlib import Path

df = pd.read_csv(
    "silver/documents/document_silver.csv"
)

Path("gold/documents").mkdir(
    parents=True,
    exist_ok=True
)

document_summary = (
    df.groupby("document_type")
      .size()
      .reset_index(name="document_count")
      .sort_values(
          by="document_count",
          ascending=False
      )
)

document_summary.to_csv(
    "gold/documents/document_type_summary.csv",
    index=False
)

print(document_summary)