#!/bin/bash

cd /usr/local/hadoop/hdfs/
sudo rm -rf data
sudo rm -rf data-datanode
sudo rm -rf data-name-node

cd ~

sudo mkdir -p /usr/local/hadoop/hdfs/data-namenode
sudo chown user:user -R /usr/local/hadoop/hdfs/data-namenode
chmod 700 /usr/local/hadoop/hdfs/data-namenode


sudo mkdir -p /usr/local/hadoop/hdfs/data-datanode
sudo chown user:user -R /usr/local/hadoop/hdfs/data-datanode
chmod 700 /usr/local/hadoop/hdfs/data-datanode