__author__ = 'supermacy'

import urllib2
import  parser

def get_data():
    _url_="https://www.test.jugnoo.in:8300/fetch_data"
    _file_="/home/supermacy/Downloads/data.json"
    #data =urllib2.urlopen(_url_)

    _data=open(_file_,'r')
    data_json=[]
    for line in _data:
        data_json= parser.get_json(line)
    return data_json
