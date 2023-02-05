# TAXI TRIPS AND Cities
# create a folder 
mkdir taxis
mkdir cities
# for every file we want to download it and save it to the correct location!
wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet -O taxis/taxis_01.parquet
wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-02.parquet -O taxis/taxis_02.parquet
wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-03.parquet -O taxis/taxis_03.parquet
wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-04.parquet -O taxis/taxis_04.parquet
wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-05.parquet -O taxis/taxis_05.parquet
wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-06.parquet -O taxis/taxis_06.parquet

wget https://d37ci6vzurychx.cloudfront.net/misc/taxi+_zone_lookup.csv -O cities/cities.csv

# create a hdfs user folder
hdfs dfs -mkdir -p /user/user

# put all files to dfs
hdfs dfs -mkdir taxis
hdfs dfs -put taxis
hdfs dfs -mkdir cities
hdfs dfs -put cities
