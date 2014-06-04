#encoding=utf8

import random
import math

for i in range(0, 100):
    s = ''
    for j in range(0, 60):
        s += '%f ' % (random.randint(-100,100)/100.0)
    print s + '-1'

#for i in range(0, 100):
#    s = ''
#    for j in range(0, 60):
#        s += '%f ' % (math.cos(j/(float(random.randint(90,110)/10.0))))
#    print s + '1'

#for i in range(0, 100):
#    s = ''
#    for j in range(0, 60):
#        s += '%f ' % (math.sin(j/(float(random.randint(90,120)/10.0))))
#    print s + '-1'

for i in range(0, 100):
    start = random.randint(-100, -90)
    step = 4
    s = ''
    for j in range(0, 60):
        start += random.randint(1, step)
        s += '%f ' % (start/100.0)
    print s + '1'



#for i in range(0, 100):
#    start = random.randint(1, 50)
#    step = 5
#    s = ''
#    for j in range(0, 60):
#        s += '%f ' % ((start + random.randint(0, step))/30.0)
#    print s + '-1'






