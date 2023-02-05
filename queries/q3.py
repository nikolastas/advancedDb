from load import *
import time


number_of_exec = 10
total_time = 0
for i in range(number_of_exec) :
    start = time.time()
    avgTripDistanceAndCost = spark.sql(
    """
    SELECT AVG(Trip_distance) as avg_trip_distance, AVG(Total_amount) as avg_trip_cost,
    CASE 
        WHEN 
            EXTRACT(day FROM tpep_pickup_datetime) BETWEEN 1 AND 15 
            THEN DATE_TRUNC('month', tpep_pickup_datetime)
        ELSE DATE_ADD(DATE_TRUNC('month', tpep_pickup_datetime), 15)
    END AS period
    FROM taxis
    WHERE tpep_pickup_datetime >= '2022-01-01'
    AND tpep_pickup_datetime < '2022-12-31'
    AND PULocationID != DOLocationID
    GROUP BY period
    ORDER BY period DESC
    """
    )
    avgTripDistanceAndCostCount = ((avgTripDistanceAndCost).collect())
    end = time.time()
    # spark.catalog.uncacheTable("taxis")
    # dff_taxis.createOrReplaceTempView("taxis")
    # bestTipTripMarchResult.unpersist()

    total_time += end-start
avgTripDistanceAndCostResult = ((avgTripDistanceAndCost).collect())
averageTimeForQuery2 = total_time / number_of_exec

print(avgTripDistanceAndCostResult)
print('Average Time: ',averageTimeForQuery2)

with open('./results/query3.txt', 'w') as f:
    f.write("Queyry 3:\n")
    f.write("Number of executions: {} \nResults: {}\nAverage Time:{}".format(number_of_exec, avgTripDistanceAndCostResult, averageTimeForQuery2))
    f.close()
