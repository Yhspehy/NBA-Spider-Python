# -*- coding:utf-8 -*-

'''
获取NBA赛程

'''

import sys
import time
import re
import json
import downloader


def getMatchSchedule(start = '2018-10-01', end = '2018-10-05'):
    timestamp = int(round(time.time() * 1000))

    html_cont = downloader.downloader(
        'http://matchweb.sports.qq.com/kbs/list?from=NBA_PC&columnId=100000&startTime=%s&endTime=%s&callback=schedule&_:%d' % (start, end, timestamp))
    con = re.match(r'^schedule\((.*)\)$', html_cont)
    loadJson = json.loads(con.group(1))
    jsonCon = json.dumps(loadJson['data'], sort_keys=False, indent=4, ensure_ascii=False)

    jsonFile = open('json/getMatchSchedule.json', 'w')
    jsonFile.write(jsonCon)
    jsonFile.close()




if __name__ == "__main__":
    argv = sys.argv
    start = '2018-10-01'
    end = '2018-10-05'

    if (len(argv) == 1):
        getMatchSchedule()
    else:
        for i, v in enumerate(argv):
            if (i == 0):
                continue
            elif (i == 1):
                start = argv[1]
            elif (i == 2):
                end = argv[2]
            else:
                break

        getMatchSchedule(start, end)
