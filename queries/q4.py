from load import *
import time


number_of_exec = 1
total_time = 0
for i in range(number_of_exec) :
    start = time.time()
    # Να βρεθούν οι τρεις μεγαλύτερες (top 3) ώρες αιχμής ανά ημέρα της εβδομάδος,
    # εννοώντας τις ώρες (π.χ., 7-8πμ, 3-4μμ, κλπ) της ημέρας  | + με τον μεγαλύτερο αριθμό
    # επιβατών σε μια κούρσα ταξί. 
    # |Ο υπολογισμός αφορά όλους τους μήνες.|
    threeHighestHoursPerWeek = spark.sql(
    """
    WITH hourly_clients AS (
    SELECT HOUR(tpep_pickup_datetime) AS hour_of_day, DAYOFWEEK(tpep_pickup_datetime) AS day_of_week,
    AVG(Passenger_count) AS num_clients
    FROM taxis
    WHERE tpep_pickup_datetime >= '2022-01-01'
    AND tpep_pickup_datetime < '2022-12-31'
    GROUP BY hour_of_day, day_of_week
    )
    SELECT day_of_week, hour_of_day, num_clients
    FROM ( SELECT *, ROW_NUMBER() OVER (PARTITION BY day_of_week ORDER BY num_clients DESC) AS row_num
            FROM hourly_clients ) subquery
    WHERE row_num <= 3
    ORDER BY day_of_week, num_clients DESC
    """
    )
    threeHighestHoursPerWeekCount = ((threeHighestHoursPerWeek).count())
    end = time.time()
    # spark.catalog.uncacheTable("taxis")
    # dff_taxis.createOrReplaceTempView("taxis")
    # bestTipTripMarchResult.unpersist()

    total_time += end-start
threeHighestHoursPerWeekResult = ((threeHighestHoursPerWeek).collect())
averageTimeForQuery4 = total_time / number_of_exec

print(threeHighestHoursPerWeekResult)
print('Average Time: ',averageTimeForQuery4)

with open('./results_for_1_worker/query4.txt', 'w') as f:
    f.write("Queyry 4:\n")
    f.write("Number of executions: {} \nResults: {}\nAverage Time:{}".format(number_of_exec, threeHighestHoursPerWeekResult, averageTimeForQuery4))
    f.close()
