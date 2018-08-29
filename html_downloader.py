# -*- coding:utf-8 -*-
from urllib import request


class HtmlDownload(object):
    
    
    def downloader(self,url):
        if url is None :
            return
        
        response = request.urlopen(url)
        
        if response.getcode() != 200 :
            return
    
        return response.read().decode('utf-8')


