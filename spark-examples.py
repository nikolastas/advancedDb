#Example script demonstrated in live lab session 21/11/2022
#Advanced Data Bases, 9th Semester, ECE
#code by George Anastasakis

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, desc, row_number, asc, max, month, dayofmonth, hour
import os
import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

#details for setting up a spark standalone cluster and using the DataFrames API
# https://spark.apache.org/docs/latest/spark-standalone.html
# https://spark.apache.org/docs/2.2.0/sql-programming-guide.html

spark = SparkSession.builder.master("spark://192.168.0.2:7077").getOrCreate()
print("spark session created")

#read a sample input file in CSV format from local disk
df = spark.read.option("header", "true").option("inferSchema", "true").format("csv").csv("employees.csv")

#DataFrame transformations and actions
df.printSchema()
df.show()


df.select("FIRST_NAME").show()

df.groupBy("DEPARTMENT").max("SALARY").show()

df.groupBy("DEPARTMENT").agg(max("SALARY").alias("max_salary")).orderBy(asc("max_salary")).show()

df.filter(col("SALARY") > 8000).show()

# add columns
df.withColumn("month", month("HIRE_DATE"))\
  .withColumn("day", dayofmonth("HIRE_DATE"))\
  .show()

print("======================================================================")

#DataFrame transformations and actions using the sql interface

df.createOrReplaceTempView("employees")
sql = spark.sql("SELECT * FROM employees WHERE ID = 200")
sql.show()

#Sample transformations using the RDD API 
rdd = df.rdd
first_names_list = rdd.map(lambda x: "First name: "+x.FIRST_NAME).collect()

for x in first_names_list:
  print(x)


print("============================================================")
salaries_per_department = rdd.map(lambda x: (str(x.DEPARTMENT), int(x.SALARY)))

for x in salaries_per_department.collect():
  print(x)


print("============================================================")
max_salary_per_department = salaries_per_department.reduceByKey(lambda a,b: a if a>b else b)

for x in max_salary_per_department.collect():
  print(x)
