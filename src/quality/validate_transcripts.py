import pandas as pd

df = pd.read_csv(
    "silver/transcripts/transcript_silver.csv"
)

null_messages = df["message"].isnull().sum()

empty_messages = (
    df["message"]
    .fillna("")
    .str.strip()
    .eq("")
    .sum()
)

null_speakers = (
    df["speaker"]
    .isnull()
    .sum()
)

print("\nTRANSCRIPT QUALITY REPORT")
print("-------------------------")

print("Null Messages:", null_messages)
print("Empty Messages:", empty_messages)
print("Null Speakers:", null_speakers)

if (
    null_messages == 0
    and empty_messages == 0
):
    print("\nQUALITY CHECK PASSED")
else:
    print("\nQUALITY CHECK FAILED")