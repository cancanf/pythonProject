import csv
import sys
import json

def getpy(file_name):
    rows = []
    path = sys.path[0]

    # s = f.read()
    # r = s.strip().split(':')
    # print(r)
    # readers = csv.reader(f, delimiter=',', quotechar=':')
    # next(readers, None)
    # for row in readers:
    #     temprows = []
    #     for i in row:
    #         temprows.append(i)
    #         print(i)
    #     rows.append(temprows)
    return rows


if __name__ == '__main__':
    getpy("test_baidu_data.json")
