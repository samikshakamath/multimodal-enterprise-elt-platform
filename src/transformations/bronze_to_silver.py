from pyspark.sql import SparkSession
from pyspark.sql.functions import upper, col

spark = (
    SparkSession.builder
    .appName("BronzeToSilverLogs")
    .getOrCreate()
)

df = spark.read.csv(
    "bronze/logs/parsed_logs.csv",
    header=True,
    inferSchema=True
)

print("Bronze Count:", df.count())

silver_df = (
    df
    .dropDuplicates()
    .withColumn(
        "log_level",
        upper(col("log_level"))
    )
    .limit(100000)
)

print("Silver Count:", silver_df.count())

import pandas as pd
from pathlib import Path

Path("silver/logs").mkdir(
    parents=True,
    exist_ok=True
)

silver_pd = silver_df.toPandas()

silver_pd.to_csv(
    "silver/logs/silver_logs.csv",
    index=False
)

print("Silver layer created.")