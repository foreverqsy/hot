#encoding=utf8

import os

cmd = '/home/devuse/bin/hadoop/bin/hadoop \
dfs -rm -r yuan/hot/output1'
print cmd
os.system(cmd)

cmd = '/home/devuse/bin/hadoop/bin/hadoop \
jar ~/bin/hadoop/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.2.1.jar \
-input ./yuan/hot/0.out \
-output ./yuan/hot/output1 \
-mapper "pypy mapper.py" \
-reducer "pypy reducer.py" \
-file *.py \
-file city.txt \
-jobconf mapred.map.tasks=20 \
-jobconf mapred.reduce.tasks=10 \
-jobconf mapred.job.name=”yuan.hot.1”;'
print cmd
os.system(cmd)


cmd = '/home/devuse/bin/hadoop/bin/hadoop \
dfs -cat yuan/hot/output1/part-* > ../../data/1.out'
print cmd
os.system(cmd)
