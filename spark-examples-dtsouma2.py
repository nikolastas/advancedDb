from pyspark.sql.functions import *
from pyspark.sql.types import *

#parquet input data found in https://github.com/Teradata/kylo/tree/master/samples/sample-data/parquet
#and saved in a local lab2/ directory
parDF1=spark.read.parquet("lab2/")

parDF1.count()
parDF1.printSchema()
parDF1.show(10)


#filters
parDF1.select("first_name", "last_name").show(10)
parDF1.filter(parDF1['salary'] > 150000).show(10)
parDF1.filter((parDF1['salary'] > 150000) & (parDF1['country']=="China")).show()

#string functions
parDF1.filter(parDF1['birthdate'].startswith("12/12")).show()
parDF1.filter(parDF1.email.like("%powel%")).show()

#aggregates
parDF1.groupby("country").avg("salary").count()
parDF1.groupby("country", "gender").avg("salary").show()

#convert string to date object, date manipulation
parDF2 = parDF1.withColumn('BD', to_date(parDF1.birthdate,'M/D/y'))
parDF2.select("BD").dtypes
parDF3 = parDF2.where(parDF2.BD.isNotNull()).show(10)

parDF3.select("last_name", current_date(),col("BD"),datediff(current_date(),col("BD")).alias("Date Difference in Days")).show(10)
parDF3.select("last_name", current_date(),col("BD"),months_between(current_date(),col("BD")).alias("Date Difference in Months")).show(10)

#Running SQL Queries Programmatically
parDF2.createOrReplaceTempView("userdata")
sqlDF1 = spark.sql("select * from userdata where country like '%Greece%' and BD IS NOT NULL")
sqlDF1.show()
sqlDF2 = spark.sql("select country, gender, avg(salary) from userdata where salary IS NOT NULL GROUP BY country, gender ORDER BY country")
sqlDF2.show()
sqlDF3 = spark.sql("select country, max(salary) from userdata WHERE salary IS NOT NULL GROUP BY country")
sqlDF3.show()

#join between 2 tables
#world countries csv found in https://www.kaggle.com/datasets/fernandol/countries-of-the-world?resource=download
schema1 = "Country STRING, Region STRING, Population INT, Area INT , REST STRING"
DF1 = spark.read.csv(path = "countries_world.csv", schema = schema1)
DF1.printSchema()

#clean a column from whitespace
DF2 = DF1.select(trim(DF1['country']).alias('country'), "Region", "Population")

DF2.select("Population").filter(DF2.Population > 20000000).show(10)
DF2.createOrReplaceTempView("countrydata")
sqlDF4 = spark.sql("SELECT userdata.last_name, countrydata.population FROM userdata INNER JOIN countrydata ON userdata.country == countrydata.country")
sqlDF4.show()

sqlDF4 = spark.sql("SELECT userdata.last_name, countrydata.population FROM userdata INNER JOIN countrydata ON userdata.country == countrydata.country")

parDF3.join(DF2, parDF3.country ==  DF2.country,"inner").select("last_name", "population").show()