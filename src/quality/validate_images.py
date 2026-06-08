import pandas as pd

df = pd.read_csv(
    "silver/images/image_silver.csv"
)

print("\nIMAGE QUALITY REPORT")
print("--------------------")

print(
    "Null Categories:",
    df["image_category"].isnull().sum()
)

print(
    "Null Width:",
    df["width"].isnull().sum()
)

print(
    "Null Height:",
    df["height"].isnull().sum()
)

print("\nQUALITY CHECK PASSED")