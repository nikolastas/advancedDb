from load import *
import time


number_of_exec = 10
total_time = 0
for i in range(number_of_exec) :
    start = time.time()
    highestTollFees = spark.sql(
    """
    SELECT MAX(Tolls_amount) as max_toll_fees_per_month, MONTH(tpep_pickup_datetime) as month, 
    MAX(tpep_pickup_datetime) as max_date
    FROM taxis
    where Tolls_amount > 0
    AND YEAR(tpep_pickup_datetime) = '2022'
    GROUP BY MONTH(tpep_pickup_datetime)
    """
    )
    bestTipTripMarchResult = ((highestTollFees).collect())
    end = time.time()
    # spark.catalog.uncacheTable("taxis")
    # dff_taxis.createOrReplaceTempView("taxis")
    # bestTipTripMarchResult.unpersist()

    total_time += end-start
bestTipTripMarchResult = ((highestTollFees).collect())
averageTimeForQuery2 = total_time / number_of_exec

print(bestTipTripMarchResult)
print('Average Time: ',averageTimeForQuery2)

with open('./results_for_1_worker/query2.txt', 'w') as f:
    f.write("Queyry 2:\n")
    f.write("Number of executions: {} \nResults: {}\nAverage Time:{}".format(number_of_exec, bestTipTripMarchResult, averageTimeForQuery2))
    f.close()
