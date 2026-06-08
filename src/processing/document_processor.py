import pandas as pd
from pathlib import Path

BASE_PATH = "data/documents"

records = []

for category in Path(BASE_PATH).iterdir():

    if category.is_dir():

        for file in category.iterdir():

            if file.is_file():

                records.append({
                    "file_name": file.name,
                    "document_type": category.name,
                    "file_path": str(file),
                    "file_size_kb": round(
                        file.stat().st_size / 1024,
                        2
                    )
                })

df = pd.DataFrame(records)

Path("bronze/documents").mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    "bronze/documents/document_bronze.csv",
    index=False
)

print(df.head())

print("\nDocuments Processed:", len(df))

print("\nDocument Bronze Layer Created")