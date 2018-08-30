# -*- coding:utf-8 -*-

'''
通过给脚本传参可控制爬取哪些数据

python main.py  -  不带参数默认执行main函数
python main.py getTeamInfo - 带 getTeamInfo 则只执行getTeamInfo()
别的同理...
可一次性带多个参数

'''
import sys
import json
import re
import time
import getTeamList
import getTeamInfo
import getTeamPlayer


class SpiderMain(object):

    def main(self):
        self.getTeamInfo()
        self.getAllTeamPlayer()



    def getTeamInfo(self):
        getTeamInfo.getTeamInfo()



    def getAllTeamPlayer(self):
        teamList = getTeamList.getTeamList()

        teamDict = {}
        for v in teamList:
            print(v['name'])
            playerList = getTeamPlayer.getTeamPlayerIdStr(v['teamId'])
            teamDict[v['name']] = playerList['data']['playerBaseInfo']
            time.sleep(1)

        jsonFile = open('json/teamPlayerList.json', 'w')
        jsonFile.write(json.dumps(teamDict, sort_keys=False,
                                  indent=4, ensure_ascii=False))
        jsonFile.close()


if __name__ == "__main__":
    spider = SpiderMain()

    argv = sys.argv
    
    isRun = 0
    if (len(argv) == 1):
        spider.main()

    else:
        for i, v in enumerate(argv):
            if (v == 'main'):
                print('please run without params')
                isRun = 1
                break

        if isRun == 0:
            for i, v in enumerate(argv):
                if (i == 0):
                    continue
                else:
                    fun = getattr(spider, v, 404)
                    if fun != 404 :
                        fun()
            
                


    


