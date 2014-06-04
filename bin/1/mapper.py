#encoding=utf8

import sys


def load_city():
    result = {}
    f1 = file('./city.txt', 'rb')
    for line in f1:
        city, code = line[:-1].split('\t')[:2]
        result[code] = city
    return result


#甘肃   0757    20140204    15  1   1
def main(input=sys.stdin, output=sys.stdout):
    city_map = load_city()
    for line in input:
        try:
            keyword, city, date, hour, uv, pv = line[:-1].split('\t')
            if city in city_map:
                city = city_map[city]
            else:
                continue
            keyword = keyword.lower()
            if keyword == '':
                continue
            filter1 = '~ ()`!@#$%^&*_+-={}|:"<>?[]\;\',./'
            keyword = ''.join([i for i in keyword if i not in filter1])
            print >> output, '%s,%s\t%s;%s;%s' % (keyword, city, date, hour, uv)
        except:
            continue


if __name__ == '__main__':
    main()



