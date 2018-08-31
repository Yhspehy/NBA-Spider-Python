# -*- coding:utf-8 -*-

'''
获取球员相关排行榜

year代表该年下的nba赛事信息

seasonType 0:季前赛  1:常规赛  2:季后赛

limit 每项返回的条数

传参的时候请先传年份，再传seasonType
'''


import time
import sys
import re
import json
import downloader


def getPlayerStatsRankSummary(year = 2017, seasonType = 2, limit = 5):
    timestamp = int(round(time.time() * 1000))

    html_cont = downloader.downloader(
        'http://ziliaoku.sports.qq.com/cube/index?callback=getPlayerStatsRankSummary&cubeId=10&dimId=53,54,55,56,57,58&params=t2:%d|t3:%d&limit=%d&from=sportsdatabase&_:%d' % (year, seasonType, limit, timestamp))
    con = re.match(r'^getPlayerStatsRankSummary\((.*)\)$', html_cont)
    loadJson = json.loads(con.group(1))
    jsonCon = json.dumps(loadJson['data'], sort_keys=False, indent=4, ensure_ascii=False)

    jsonFile = open('json/getPlayerStatsRankSummary.json', 'w')
    jsonFile.write(jsonCon)
    jsonFile.close()




if __name__ == "__main__":
    argv = sys.argv
    if (len(argv) == 1):
        getPlayerStatsRankSummary()
    else:
        year = 2017
        seasonType = 2
        limit = 5
        for i, v in enumerate(argv):
            if (i == 0):
                continue
            elif (i == 1):
                year = int(argv[1])
            elif (i == 2):
                seasonType = int(argv[2])
            elif (i == 3):
                limit = int(argv[3])
            else:
                break
            
        getPlayerStatsRankSummary(year, seasonType, limit)
