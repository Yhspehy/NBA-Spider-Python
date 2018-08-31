# -*- coding:utf-8 -*-
import sys
import time
import re
import json
import downloader


def getSinglePlayerInfo(id):
    timestamp = int(round(time.time() * 1000))

    html_cont = downloader.downloader(
        'http://ziliaoku.sports.qq.com/cube/index?callback=getSinglePlayerInfo&cubeId=8&dimId=5&params=t1:%s&from=sportsdatabase&_:%d' % (id, timestamp))
    con = re.match(r'^getSinglePlayerInfo\((.*)\)$', html_cont)
    loadJson = json.loads(con.group(1))
    return loadJson['data']['playerBaseInfo']




if __name__ == "__main__":
    argv = sys.argv
    list = []
    if (len(argv) == 1):
        print('please input playerId')
    else:
        for i, v in enumerate(argv):
            if (i == 0):
                continue
            else:
                d = getSinglePlayerInfo(v)
                list.append(d)

    jsonFile = open('json/singlePlayerInfo.json', 'w')
    jsonCon = json.dumps(list, sort_keys=False, indent=4, ensure_ascii=False)
    jsonFile.write(jsonCon)
    jsonFile.close()
