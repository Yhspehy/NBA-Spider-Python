# -*- coding:utf-8 -*-
from urllib import request

    
def downloader(url):
    if url is None :
        return
        
    response = request.urlopen(url)
        
    if response.getcode() != 200 :
        return
    
    return response.read().decode('utf-8')


