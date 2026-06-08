import pandas as pd
from pathlib import Path

df = pd.read_csv(
    "silver/images/image_silver.csv"
)

Path("gold/images").mkdir(
    parents=True,
    exist_ok=True
)

# Category Distribution

category_summary = (
    df.groupby("image_category")
      .size()
      .reset_index(name="image_count")
      .sort_values(
          by="image_count",
          ascending=False
      )
)

category_summary.to_csv(
    "gold/images/category_summary.csv",
    index=False
)

# Resolution Statistics

resolution_summary = pd.DataFrame({
    "avg_width": [round(df["width"].mean(), 2)],
    "avg_height": [round(df["height"].mean(), 2)],
    "min_width": [df["width"].min()],
    "max_width": [df["width"].max()],
    "min_height": [df["height"].min()],
    "max_height": [df["height"].max()]
})

resolution_summary.to_csv(
    "gold/images/resolution_summary.csv",
    index=False
)

print("\nImage Categories")
print(category_summary)

print("\nResolution Statistics")
print(resolution_summary)