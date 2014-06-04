#encoding=utf8

import os
import sys

def run(start_date, end_date):
    #从Hive获取日志到本地
    cmd = '/home/devuse/bin/hadoop/bin/hive -e \'select req["keywords"], city, dt, hour, count(DISTINCT req["user_info"]), count(*) from logamap_lse2.log_rc where dt>="%s" and city is not null and  dt<="%s" and req["keywords"] is not null and  req["keywords"]!=""  and hour >= "00" and hour <="23" group by req["keywords"], city, dt, hour \' > ../../data/0.out;' % (start_date, end_date)
    print cmd
    os.system(cmd)
    #清除hdfs中的目录
    cmd = '/home/devuse/bin/hadoop/bin/hadoop \
    dfs -rm -r yuan/hot/0.out'
    print cmd
    os.system(cmd)
    #推送本地日志到hdfs
    cmd = '/home/devuse/bin/hadoop/bin/hadoop \
    dfs -put ../../data/0.out yuan/hot/0.out'
    print cmd
    os.system(cmd)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'python start.py 20140101 20140102'
    else:
        start_date = sys.argv[1]
        end_date = sys.argv[2]
        run(start_date, end_date)



