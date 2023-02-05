from load import *
import time

marchTrips = spark.sql(
  """
  SELECT *
  FROM taxis 
  INNER JOIN locations ON taxis.DOLocationID = locations.LocationID
  WHERE tpep_pickup_datetime >= '2022-03-01' 
  AND tpep_pickup_datetime < '2022-04-01' and tpep_dropoff_datetime >= '2022-03-01' 
  AND tpep_dropoff_datetime < '2022-04-01'
  AND locations.Zone = "Battery Park"
  ORDER BY Tip_amount DESC
  limit 1
  """
  )
number_of_exec = 1
total_time = 0
for i in range(number_of_exec) :
    start = time.time()
    bestTipTripMarch = ((marchTrips).collect())
    end = time.time()
    total_time += end-start

averageTimeForQuery1 = total_time / number_of_exec

print(bestTipTripMarch)
print('Average Time: ',averageTimeForQuery1)

with open('./results/query1.txt', 'w') as f:
    f.write("Queyry 1:\n")
    f.write("Number of executions: {} \nResults: {}\nAverage Time:{}".format(number_of_exec, bestTipTripMarch, averageTimeForQuery1))
    f.close()