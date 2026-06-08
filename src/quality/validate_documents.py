import pandas as pd

df = pd.read_csv(
    "silver/documents/document_silver.csv"
)

null_types = (
    df["document_type"]
    .isnull()
    .sum()
)

null_names = (
    df["file_name"]
    .isnull()
    .sum()
)

print("\nDOCUMENT QUALITY REPORT")
print("-----------------------")

print("Null Types:", null_types)
print("Null File Names:", null_names)

if (
    null_types == 0
    and null_names == 0
):
    print("\nQUALITY CHECK PASSED")
else:
    print("\nQUALITY CHECK FAILED")