import pandas as pd
from pathlib import Path

BASE_PATH = "data/images"

records = []

for category in Path(BASE_PATH).iterdir():

    if category.is_dir():

        for file in category.iterdir():

            if file.is_file():

                records.append({
                    "image_name": file.name,
                    "image_category": category.name,
                    "file_path": str(file)
                })

df = pd.DataFrame(records)

Path("bronze/images").mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    "bronze/images/image_bronze.csv",
    index=False
)

print(df.head())

print("\nImages Processed:", len(df))

print("\nImage Bronze Layer Created")