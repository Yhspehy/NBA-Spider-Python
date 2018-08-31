# -*- coding:utf-8 -*-

'''
获取NBA赛程

'''

import sys
import time
import re
import json
import downloader


def getTeamSchedule(id = 1):
    timestamp = int(round(time.time() * 1000))

    html_cont = downloader.downloader(
        'http://mat1.gtimg.com/apps/hpage2/nbateammatchlist_%d.json?callback=getCastData&_:%d' % (id, timestamp))

    con = re.match(r'^getCastData\((.*)\)$', html_cont)
    loadJson = json.loads(con.group(1))
    jsonCon = json.dumps(loadJson, sort_keys=False, indent=4, ensure_ascii=False)

    jsonFile = open('json/getTeamSchedule.json', 'w')
    jsonFile.write(jsonCon)
    jsonFile.close()




if __name__ == "__main__":
    argv = sys.argv
    id = 1

    if (len(argv) == 1):
        getTeamSchedule()
    else:
        for i, v in enumerate(argv):
            if (i == 0):
                continue
            elif (i == 1):
                id = argv[1]
            else:
                break

        getTeamSchedule(id)
