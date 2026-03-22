from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("ETL Pipeline").getOrCreate()

df = spark.read.csv("/mnt/data/raw/data.csv", header=True, inferSchema=True)

df_clean = df.dropna()
df_clean = df_clean.withColumn("sales", col("sales").cast("double"))

df_clean.write.mode("overwrite").partitionBy("region").parquet("/mnt/data/processed/")
