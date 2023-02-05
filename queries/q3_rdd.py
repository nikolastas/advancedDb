from load import *
import time
from datetime import datetime 
def get_period(dt):
    day = dt.day
    if day >= 1 and day <= 15:
        return datetime(dt.year, dt.month, 1)
    else:
        return datetime(dt.year, dt.month, 16)
def handleGroupValues(x,y):
    return (x[0]+y[0], x[1]+y[1], x[2]+y[2])


number_of_exec = 3
total_time = 0
for i in range(number_of_exec) :
    start = time.time()
    avgTripDistanceAndCostRdd_step1 = \
    rdd_taxis \
    .filter(lambda x: x.PULocationID != x.DOLocationID \
        and  x.tpep_dropoff_datetime.strftime("%Y-%m-%d") >= "2022-01-01" \
        and  x.tpep_dropoff_datetime.strftime("%Y-%m-%d") <= "2022-06-31" ) 
    print('step 1 finished')
    avgTripDistanceAndCostRdd_step2 = \
        avgTripDistanceAndCostRdd_step1 \
        .map(lambda x: (get_period(x.tpep_pickup_datetime), (x.trip_distance, x.total_amount, 1)))
    print('step 2 finished')
    avgTripDistanceAndCostRdd_step3 = avgTripDistanceAndCostRdd_step2 \
    .reduceByKey(handleGroupValues)
    print('step 3 finished')
    avgTripDistanceAndCostRdd4 = avgTripDistanceAndCostRdd_step3 \
    .mapValues(lambda x: (x[0]/x[2], x[1]/x[2])).cache()
    print('step 4 finished')
    avgTripDistanceAndCostRddCollect = avgTripDistanceAndCostRdd4 \
        .collect()
    
    end = time.time()

    total_time += end-start
avgTripDistanceAndCostResult = avgTripDistanceAndCostRddCollect
averageTimeForQuery3RDD = total_time / number_of_exec

print(avgTripDistanceAndCostResult)
print('Average Time: ',averageTimeForQuery3RDD)

with open('./results/query3_rdd.txt', 'w') as f:
    f.write("Queyry 3:\n")
    f.write("Number of executions: {} \nResults: {}\nAverage Time:{}".format(number_of_exec, avgTripDistanceAndCostResult, averageTimeForQuery3RDD))
    f.close()
