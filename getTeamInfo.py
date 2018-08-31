# -*- coding:utf-8 -*-

'''
获取所有球队信息的列表
'''


import time
import re
import json
import downloader


def getTeamInfo():
    timestamp = int(round(time.time() * 1000))
    html_cont = downloader.downloader(
        'http://matchweb.sports.qq.com/rank/team?competitionId=100000&from=NBA_PC&callback=getTeamInfo&_=%s' % timestamp)
    jsonFile = open('json/teamInfo.json', 'w')
    con = re.match(r'^getTeamInfo\((.*)\)\;$', html_cont)
    loadJson = json.loads(con.group(1))
    jsonCon = json.dumps(
        loadJson[1], sort_keys=False, indent=4, ensure_ascii=False)
    jsonFile.write(jsonCon)
    jsonFile.close()


if __name__ == "__main__":
    print('getTeamInfo')
    getTeamInfo()
