# Instructions to set up Spark - Hadoop - And more!
Please read the Spark_Install_instructions.pdf as most of the instructions are there.

1. Setup your VM at https://cyclades.okeanos-knossos.grnet.gr/ui/#ips/ and attach the
public IP to it
----------------------------------------------------------------------------------------------
2. Connect: ssh user@snf-33040.ok-kno.grnetcloud.net (replace with your host name
here and use your password)
----------------------------------------------------------------------------------------------
3. Install python3.8
- `sudo apt update`
- `sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev`
- `wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz`
- `tar -xf Python-3.8.0.tgz`
- `cd Python-3.8.0`
- `./configure --enable-optimizations`
- `make -j 8`
- `sudo make altinstall`
- `python3.8 --version` (you should expect: Python 3.8.0)
- Delete old links
`sudo rm -rf /usr/bin/python3.5`
`sudo rm -rf /usr/bin/python3.5m`
`sudo rm -rf /usr/lib/python3.5`
`sudo rm -rf /etc/python3.5`
`sudo rm -rf /usr/local/lib/python3.5`
----------------------------------------------------------------------------------------------
4. Install pip
- `cd ../`
- `wget https://bootstrap.pypa.io/get-pip.py`
- `python3.8 get-pip.py`
----------------------------------------------------------------------------------------------
5. Install PySpark
- `pip3.8 install pyspark==3.1.3`
----------------------------------------------------------------------------------------------
6. Install Apache Spark
- `wget https://downloads.apache.org/spark/spark-3.1.3/spark-3.1.3-bin-hadoop2.7.tgz`
- `tar -xzf spark-3.1.3-bin-hadoop2.7.tgz`
c. `nano ~/.bashrc`
```
export SPARK_HOME=/home/user/spark-3.1.3-bin-hadoop2.7
export PATH=$PATH:$SPARK_HOME/sbin
export PYSPARK_PYTHON=python3.8
export PYSPARK_DRIVER_PYTHON=python3.8
```
- `source ~/.bashrc`
----------------------------------------------------------------------------------------------
7. Install Java
- `sudo apt-get install openjdk-8-jdk`
- `java -version` (you should expect: openjdk version "1.8.0_292")
----------------------------------------------------------------------------------------------
8. Setup a Cluster (1 master and 1 worker)
 Create a network at Okeanos and assign IPs to each VM
- `cd spark-3.1.3-bin-hadoop2.7/conf`
- `touch spark-env.sh`
- `nano spark-env.sh`
- `SPARK_MASTER_HOST='192.168.0.1'` or your master IP
- `start-master.sh`
----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
9. Start 1 worker on master 
- `spark-daemon.sh start org.apache.spark.deploy.worker.Worker 1 --webui-port 8080 --port 65509 --cores 2 --memory 3g spark://192.168.0.1:7077`
----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
10. set up a ssh between master and slave
- `sudo hostname master (on master VM)`
- `sudo vim /etc/hosts`
- 
```
<private_ip_master> master
<private_ip_slave> slave
```
- `ssh slave `
- `sudo hostname slave`
- `sudo vim /etc/hosts`
- 
```
<private_ip_master> master
<private_ip_slave> slave
```
---------------------------------------------------------------
11. install python on slave
- `sudo apt update`
- `sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev`
- `wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz`
- `tar -xf Python-3.8.0.tgz`
- `cd Python-3.8.0`
- `./configure --enable-optimizations`
- `make -j 8`
- `sudo make altinstall`
- `python3.8 --version` (you should expect: Python 3.8.0)
- Delete old links
`sudo rm -rf /usr/bin/python3.5`
`sudo rm -rf /usr/bin/python3.5m`
`sudo rm -rf /usr/lib/python3.5`
`sudo rm -rf /etc/python3.5`
`sudo rm -rf /usr/local/lib/python3.5`
- `cd ../`
------------------------------------------------------------------------------------------------
12. Install Apache Spark on slave
- `wget https://downloads.apache.org/spark/spark-3.1.3/spark-3.1.3-bin-hadoop2.7.tgz`
- `tar -xzf spark-3.1.3-bin-hadoop2.7.tgz`
- `vim ~/.bashrc`
```
export SPARK_HOME=/home/user/spark-3.1.3-bin-hadoop2.7
export PATH=$PATH:$SPARK_HOME/sbin
export PYSPARK_PYTHON=python3.8
export PYSPARK_DRIVER_PYTHON=python3.8
```
- `source ~/.bashrc`
------------------------------------------------------------------------------------------
13. Install Java on slave
- `sudo apt-get install openjdk-8-jdk`
- `java -version (you should expect: openjdk version "1.8.0_292")`
------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------
14 . Start worker on slave
- `spark-daemon.sh start org.apache.spark.deploy.worker.Worker 3 --webui-port 8080 \
--port 65511 --cores 2 --memory 3g spark://192.168.0.1:7077`
------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------
15. password less ssh master <--> slave
- `ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa`
- `cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys`
- `scp -r ~/.ssh/ user@slave:~/`
--------------------------------------------------------------
16. install hadoop
follow instructions https://sparkbyexamples.com/hadoop/apache-hadoop-installation/ 
- for hadoop 3.3.4 BINARY not source

`wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz` 

---------------------------------
17. start hdfs cluster
- `start-dfs.sh`
---------------
18 add, compare or remove to bashrc
- You should at least have these at your bashrc at this point
```
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
```
--------------
19. add to <spark-dir>/conf/spark-env.sh

If you are having problems with pyspark and hadoop version you maybe help if you add that to spark-env.sh
- `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HADOOP_HOME/lib/native`
------------
20. do steps 16 till 18 to slave
-----
21. hdfs namenode -format on master

## IN CASE OF ERROR 
use our file on reset_data_name_nodes.sh and then stop_reset_start.sh at your own risk.

-------
22. check the http://<yourIP>:9870/
on the datanodes tab you should have 2 or 1.

23. try running a pyspark shell it should load with native hadoop. 