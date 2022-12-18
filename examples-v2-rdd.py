from pyspark.sql import SparkSession
import os, sys, time

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable


spark = SparkSession.builder.master("spark://192.168.0.2:7077").appName("labX").getOrCreate()
print("spark session created")


df = spark.read.parquet('userdata1.parquet')

print(f'Rows: {df.count()}')
#df.printSchema()
#df.show()

start = time.time()


rdd = df.rdd

# 1. sum of salaries per country
rddx = rdd.filter(lambda x: x.salary is not None)\
          .map(lambda x: (str(x.country), float(x.salary)))\
          .reduceByKey(lambda x,y: x+y)

print(f'Countries: {rddx.count()}')

for y in rddx.collect():
    print(y)

# 2. pososto gunaikwn ana xwra
def convert(row):
    country_str = str(row.country)
    gender_str = str(row.gender)
    
    if gender_str == 'Female':
        t = 1
    else:
        t = 0    
    
    return (country_str, (t, 1))


rdd1 = rdd.map(convert)

for x in rdd1.collect():
    print(x)
    
final_rdd = rdd1.reduceByKey(lambda a,b: (a[0]+b[0], a[1]+b[1]))\
                .mapValues(lambda x: (x[0]/x[1]*100))

print()
print()
print()
for x in final_rdd.collect():
    print(x)    

end = time.time()

print()
print()
print(f'Time taken: {end-start} seconds.')