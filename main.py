# -*- coding:utf-8 -*-
import json
import re
import html_downloader



class SpiderMain(object):

    def __init__(self):

        self.downloader = html_downloader.HtmlDownload()
        
    
    def main(self):

        self.getTeamList()


    def getTeamList(self):
        html_cont = self.downloader.downloader('http://matchweb.sports.qq.com/team/list?columnId=100000&competitionId=100000&callback=getTeamList')
        jsonFile = open('json/teamList.json','w')
        con = re.match(r'^getTeamList\((.*)\)$', html_cont)
        loadJson = json.loads(con.group(1))
        jsonCon = json.dumps(loadJson, sort_keys=False, indent=4, ensure_ascii=False)
        jsonFile.write(jsonCon)
        jsonFile.close()










if __name__ == "__main__" :
    spider = SpiderMain()
    spider.main()