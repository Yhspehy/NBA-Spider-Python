# -*- coding:utf-8 -*-

'''
获取球队战绩统计

'''

import time
import re
import json
import downloader


def teamRank():
    timestamp = int(round(time.time() * 1000))

    html_cont = downloader.downloader(
        'http://matchweb.sports.qq.com/rank/team?callback=teamRank&competitionId=100000&from=NBA_PC&_:%d' % timestamp)
    con = re.match(r'^teamRank\((.*)\)\;$', html_cont)
    loadJson = json.loads(con.group(1))
    jsonCon = json.dumps(loadJson[1], sort_keys=False, indent=4, ensure_ascii=False)

    jsonFile = open('json/teamRank.json', 'w')
    jsonFile.write(jsonCon)
    jsonFile.close()




if __name__ == "__main__":
    teamRank()

