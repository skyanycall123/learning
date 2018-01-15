#! usr/bin/python
#coding=utf-8
#filename train stations

import re
import requests
from pprint import pprint

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9043'

response = requests.get(url,verify=False)
stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',response.text)
pprint(dict(stations),indent=4)
#pprint (stations,indent=4)
#stations=dict(station)
#每行只打印一个字典元素
#pprint(stations,indent=4)   
#print(stations)      
