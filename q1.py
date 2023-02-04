from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, desc, row_number, asc, max, month, dayofmonth, hour
import os
import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable


spark = SparkSession.builder.master("spark://192.168.0.1:7077").config("spark.dynamicAllocation.enabled", "false").config("spark.executor.instances", "2").config("spark.executor.cores", "4").getOrCreate()
print("spark session created")

# hdfs files sytem
HDFS_FILES_PATH = 'hdfs://192.168.0.1:9000/user/user/'


taxi_trips_df = spark.read.option("header", "true").option("inferSchema", "true").parquet(HDFS_FILES_PATH + f"taxis/taxis_01.parquet")


taxi_trips_rdd = taxi_trips_df.rdd
taxi_trips_df.createOrReplaceTempView("taxi_trips")