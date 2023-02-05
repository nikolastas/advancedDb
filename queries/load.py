from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, desc, row_number, asc, max, month, dayofmonth, hour
import os
import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable


spark = SparkSession.builder.master("spark://192.168.0.1:7077").config("spark.dynamicAllocation.enabled", "false") \
        .config("spark.executor.instances", "2").config("spark.executor.cores", "2").getOrCreate()
spark.catalog.clearCache()

print("spark session created")

# hdfs files sytem
HDFS_FILES_PATH = 'hdfs://192.168.0.1:9000/'


dff_taxis = spark.read.option("header", "true").option("inferSchema", "true").parquet(HDFS_FILES_PATH + f"taxis/")


rdd_taxis = dff_taxis.rdd
dff_taxis.createOrReplaceTempView("taxis")
# print('Printing trips...')
# taxi_trips_df.show(1)

dff_locactions = spark.read.csv(HDFS_FILES_PATH+'cities/cities.csv', header=True, inferSchema=True)
# dff_locactions.show()

rdd_locations = dff_locactions.rdd
dff_locactions.createOrReplaceTempView("locations")
print('loading done')


