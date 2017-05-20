RUNNING ACTIVITY 3

1) Start hadoop

 start-hadoop.sh

2) Run chmod

chmod +x ./mapper3.py
chmod +x ./reducer3.py

2) Put the input files to the hadoop directory :-
	
hdfs dfs -put $HOME/Activity3/act3input act3input

3) Run hadoop mapreduce:

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.6.4.jar -mapper $HOME/Activity3/mapper3.py -reducer $HOME/Activity3/reducer3.py -input act3input -output act3out

4) Read output:

 hdfs dfs -cat act3out/*