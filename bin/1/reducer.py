#encoding=utf8

import sys


#上海南站,021,20140202  20,1,1
def out(key, values, output):
    try:
        keyword, city = key.split(',')
        values.sort()
        vs = [value.split(';') for value in values]
        if max([int(uv) for dt, hour, uv in vs]) < 10:
            return
        print '%s\t%s\t%s' % (keyword, city, ','.join(values))
    except:
        return


def main(input=sys.stdin, output=sys.stdout):
    flag = 0
    last_key = ''
    last_value = []
    for line in input:
        line = line[:-1]
        kv = line.split('\t')
        if len(kv) != 2:
            continue
        key, value = kv
        if flag:
            if key != last_key:
                out(last_key, last_value, output)
                last_key = key
                last_value = [value]
            else:
                last_value.append(value)
        else:
            last_key = key
            last_value = [value]
            flag = 1

    if last_key != '':
        out(last_key, last_value, output)

if __name__ == '__main__':
    main()




