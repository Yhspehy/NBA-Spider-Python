# -*- coding:utf-8 -*-

'''
获取所有球队队员
'''


import re
import json
import downloader


def getTeamPlayerIdStr(id):
    html_cont = downloader.downloader(
        'http://ziliaoku.sports.qq.com/cube/index?cubeId=10&dimId=31&params=t2:2017|t3:1|t4:%s&from=sportsdatabase&callback=getTeamPlayerIdList' % id)
    con = re.match(r'^getTeamPlayerIdList\((.*)\)$', html_cont)
    loadJson = json.loads(con.group(1))

    str = ''
    for v in loadJson['data']['nbaTeamPlayerSeasonStat']:
        str = str + v['playerId'] + ','
    str = str[:-1]
    return getTeamPlayerList(str)


# 获取某球队的球员列表
def getTeamPlayerList(idStr):
    html_cont = downloader.downloader(
        'http://ziliaoku.sports.qq.com/cube/index?cubeId=8&dimId=5&params=t1:%s&from=sportsdatabase&callback=getTeamPlayerList' % idStr)
    con = re.match(r'^getTeamPlayerList\((.*)\)$', html_cont)
    loadJson = json.loads(con.group(1))
    return loadJson


if __name__ == "__main__":
    print('getTeamPlayer')
    getTeamPlayerIdStr(1)
