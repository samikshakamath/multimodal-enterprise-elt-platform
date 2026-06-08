import pandas as pd
from pathlib import Path
from PIL import Image

bronze_df = pd.read_csv(
    "bronze/images/image_bronze.csv"
)

records = []

for _, row in bronze_df.iterrows():

    try:

        with Image.open(row["file_path"]) as img:

            records.append({
                "image_name": row["image_name"],
                "image_category": row["image_category"],
                "format": img.format,
                "width": img.width,
                "height": img.height
            })

    except Exception:
        pass

silver_df = pd.DataFrame(records)

Path("silver/images").mkdir(
    parents=True,
    exist_ok=True
)

silver_df.to_csv(
    "silver/images/image_silver.csv",
    index=False
)

print(silver_df.head())

print("\nImages Processed:", len(silver_df))

print("\nImage Silver Layer Created")