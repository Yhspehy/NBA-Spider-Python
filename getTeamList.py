'''
获取所有球队的列表

其中包括west，east，all三个字段
'''


import json
import re
import downloader


# 获取所有球队列表
def getTeamList():
    html_cont = downloader.downloader(
        'http://matchweb.sports.qq.com/team/list?columnId=100000&competitionId=100000&callback=getTeamList')
    jsonFile = open('json/teamList.json', 'w')
    con = re.match(r'^getTeamList\((.*)\)$', html_cont)
    loadJson = json.loads(con.group(1))
    jsonCon = json.dumps(
        loadJson['data'], sort_keys=False, indent=4, ensure_ascii=False)
    jsonFile.write(jsonCon)
    jsonFile.close()
    return loadJson['data']['all']


if __name__ == "__main__":
    print('getTeamList')
    getTeamList()
