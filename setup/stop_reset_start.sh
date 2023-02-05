stop-dfs.sh
echo "STOP ended"
hdfs namenode -format
echo "FORMAT Ended"
start-dfs.sh
echo "start endede"