# -*- coding:utf-8 -*-

'''
获取球队统计数据

year代表该年下的nba赛事信息

seasonType 0:季前赛  1:常规赛  2:季后赛

传参的时候请先传年份，再传seasonType
'''

import time
import sys
import re
import json
import downloader


def getTeamStatsTotal(year = 2017, seasonType = 2):
    timestamp = int(round(time.time() * 1000))

    html_cont = downloader.downloader(
        'http://ziliaoku.sports.qq.com/cube/index?callback=getTeamStatsTotal&cubeId=12&dimId=43&params=t2:%d|t3:%d|t64:west,east&order=t60&from=sportsdatabase&_:%d' % (year, seasonType, timestamp))
    con = re.match(r'^getTeamStatsTotal\((.*)\)$', html_cont)
    loadJson = json.loads(con.group(1))
    jsonCon = json.dumps(loadJson['data']['nbTeamSeasonStatRank'], sort_keys=False, indent=4, ensure_ascii=False)

    jsonFile = open('json/getTeamStatsTotal.json', 'w')
    jsonFile.write(jsonCon)
    jsonFile.close()




if __name__ == "__main__":
    argv = sys.argv
    
    if (len(argv) == 1):
        getTeamStatsTotal()
    else:
        year = 2017
        seasonType = 1
        for i, v in enumerate(argv):
            if (i == 0):
                continue
            elif (i == 1):
                year = int(argv[1])
            elif (i == 2):
                seasonType = int(argv[2])
            else:
                break
        getTeamStatsTotal(year, seasonType)
