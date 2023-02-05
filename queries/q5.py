from load import *
import time


number_of_exec = 1
total_time = 0
for i in range(number_of_exec) :
    start = time.time()
    # Να βρεθούν οι κορυφαίες πέντε (top 5) ημέρες ανά μήνα στις οποίες οι κούρσες είχαν
    # το μεγαλύτερο ποσοστό σε tip. Για παράδειγμα, εάν η κούρσα κόστισε 10$
    # (fare_amount) και το tip ήταν 5$, το ποσοστό είναι 50%.
    top5DaysPerMonthInTipsPerc = spark.sql(
    """
    WITH daily_tips AS (
        SELECT DAY(tpep_pickup_datetime) AS trip_day, MONTH(tpep_pickup_datetime) AS trip_month, AVG(Tip_amount / Fare_amount  * 100) AS tip_percentage
        FROM taxis
        WHERE tpep_pickup_datetime >= '2022-01-01'
        AND tpep_pickup_datetime < '2022-12-31'
        GROUP BY trip_month, trip_day
    )
    SELECT trip_month, trip_day, tip_percentage
    FROM ( SELECT *, ROW_NUMBER() OVER (PARTITION BY trip_month ORDER BY tip_percentage DESC) AS row_num
            FROM daily_tips
    ) subquery
    WHERE row_num <= 5
    ORDER BY trip_month, tip_percentage DESC
    """
    )
    top5DaysPerMonthInTipsPercCount = ((top5DaysPerMonthInTipsPerc).count())
    end = time.time()
    # spark.catalog.uncacheTable("taxis")
    # dff_taxis.createOrReplaceTempView("taxis")
    # bestTipTripMarchResult.unpersist()

    total_time += end-start
top5DaysPerMonthInTipsPercResult = ((top5DaysPerMonthInTipsPerc).collect())
averageTimeForQuery5 = total_time / number_of_exec

print(top5DaysPerMonthInTipsPercResult)
print('Average Time: ',averageTimeForQuery5)

with open('./results_for_1_worker/query5.txt', 'w') as f:
    f.write("Queyry 5:\n")
    f.write("Number of executions: {} \nResults: {}\nAverage Time:{}".format(number_of_exec, top5DaysPerMonthInTipsPercResult, averageTimeForQuery5))
    f.close()
