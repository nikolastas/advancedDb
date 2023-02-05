# Instructions to set up Spark - Hadoop - And more!
Please read the Spark_Install_instructions.pdf as most of the instructions are there.

1. Setup your VM at https://cyclades.okeanos-knossos.grnet.gr/ui/#ips/ and attach the
public IP to it
----------------------------------------------------------------------------------------------
2. Connect: ssh user@snf-33040.ok-kno.grnetcloud.net (replace with your host name
here and use your password)
----------------------------------------------------------------------------------------------
3. Install python3.8
a. `sudo apt update`
b. sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
c. wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
d. tar -xf Python-3.8.0.tgz
e. cd Python-3.8.0
f. ./configure --enable-optimizations
g. make -j 8
h. sudo make altinstall
i. python3.8 --version (you should expect: Python 3.8.0)
j. Delete old links
sudo rm -rf /usr/bin/python3.5
sudo rm -rf /usr/bin/python3.5m
sudo rm -rf /usr/lib/python3.5
sudo rm -rf /etc/python3.5
sudo rm -rf /usr/local/lib/python3.5
----------------------------------------------------------------------------------------------
4. Install pip
a. cd ../
b. wget https://bootstrap.pypa.io/get-pip.py
c. python3.8 get-pip.py
----------------------------------------------------------------------------------------------
5. Install PySpark
a. pip3.8 install pyspark==3.1.3
----------------------------------------------------------------------------------------------
6. Install Apache Spark
a. wget https://downloads.apache.org/spark/spark-3.1.3/spark-3.1.3-bin-hadoop2.7.tgz
b. tar -xzf spark-3.1.3-bin-hadoop2.7.tgz
c. nano ~/.bashrc
export SPARK_HOME=/home/user/spark-3.1.3-bin-hadoop2.7
export PATH=$PATH:$SPARK_HOME/sbin
export PYSPARK_PYTHON=python3.8
export PYSPARK_DRIVER_PYTHON=python3.8
d. source ~/.bashrc
----------------------------------------------------------------------------------------------
7. Install Java
a. sudo apt-get install openjdk-8-jdk
b. java -version (you should expect: openjdk version "1.8.0_292")
----------------------------------------------------------------------------------------------
8. Setup a Cluster (1 master and 1 worker)
a. Create a network at Okeanos and assign IPs to each VM
b. cd spark-3.1.3-bin-hadoop2.7/conf
c. touch spark-env.sh
d. nano spark-env.sh
e. SPARK_MASTER_HOST='192.168.0.2'
f. start-master.sh
----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
9. Start 1 worker on master 
a. spark-daemon.sh start org.apache.spark.deploy.worker.Worker 1 --webui-port 8080 --port 65509 --cores 2 --memory 3g spark://192.168.0.1:7077
----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
10. set up a ssh between master and slave
a. sudo hostname master (on master VM)
b. sudo vim /etc/hosts
c. 
<private_ip_master> master
<private_ip_slave> slave
d. ssh slave 
e. sudo hostname slave
f. sudo vim /etc/hosts
h. 
<private_ip_master> master
<private_ip_slave> slave
---------------------------------------------------------------
11. install python on slave
a. sudo apt update
b. sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
c. wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
d. tar -xf Python-3.8.0.tgz
e. cd Python-3.8.0
f. ./configure --enable-optimizations
g. make -j 8
h. sudo make altinstall
i. python3.8 --version (you should expect: Python 3.8.0)
j. Delete old links
sudo rm -rf /usr/bin/python3.5
sudo rm -rf /usr/bin/python3.5m
sudo rm -rf /usr/lib/python3.5
sudo rm -rf /etc/python3.5
sudo rm -rf /usr/local/lib/python3.5
k. cd ../
------------------------------------------------------------------------------------------------
12. Install Apache Spark on slave
a. wget https://downloads.apache.org/spark/spark-3.1.3/spark-3.1.3-bin-hadoop2.7.tgz
b. tar -xzf spark-3.1.3-bin-hadoop2.7.tgz
c. vim ~/.bashrc
export SPARK_HOME=/home/user/spark-3.1.3-bin-hadoop2.7
export PATH=$PATH:$SPARK_HOME/sbin
export PYSPARK_PYTHON=python3.8
export PYSPARK_DRIVER_PYTHON=python3.8
d. source ~/.bashrc
------------------------------------------------------------------------------------------
13. Install Java on slave
a. sudo apt-get install openjdk-8-jdk
b. java -version (you should expect: openjdk version "1.8.0_292")
------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------
14 . Start worker on slave
a. spark-daemon.sh start org.apache.spark.deploy.worker.Worker 3 --webui-port 8080 \
--port 65511 --cores 2 --memory 3g spark://192.168.0.1:7077
------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------
15. password less ssh master <--> slave
a. ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
b. cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
c. scp -r ~/.ssh/ user@slave:~/
--------------------------------------------------------------
16. install hadoop
follow instructions https://sparkbyexamples.com/hadoop/apache-hadoop-installation/ for hadoop 3.3.4 BINARY not source
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz
---------------------------------
17. start hdfs cluster
a. start-dfs.sh
---------------
18 add these to bashrc
a.
# our code here
export SPARK_HOME=/home/user/spark-3.1.3-bin-hadoop2.7
export PATH=$PATH:$SPARK_HOME/bin
export PATH=$PATH:$SPARK_HOME/sbin
export PYSPARK_PYTHON=python3.8
export PYSPARK_DRIVER_PYTHON=python3.8
#end of our code
# java 
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
# hadoop
export HADOOP_HOME=/home/user/hadoop
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin
export PATH=$PATH:$HADOOP_HOME/lib/native
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
# spark env
export PYSPARK_PYTHON=python3.8
export PYSPARK_DRIVER_PYTHON=python3.8
export PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH

--------------
19. add to <spark-dir>/conf/spark-env.sh
a. export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HADOOP_HOME/lib/native
------------
20. do steps 16 till 18 to slave
-----
21. hdfs namenode -format on master
##### IN CASE OF ERROR #####
stop-dfs.sh 
AND
USE THE 21 COMMAND ON MASTER
#############################
-------
22. check the http://<yourIP>:9870/
on the datanodes tab you should have 2!


23. 