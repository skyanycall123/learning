#!usr/bin/python3
# coding=gbk
# file name pachong

"""命令行查看器
Usage:
    tickets2 <from> <to> <date>

Options:
    -h    帮助菜单
    -d    动车
    -g    高铁
    -t    特快
    -k    快速
    -z    直达
"""
from docopt import docopt
import re
from bs4 import BeautifulSoup
import requests
import json
import time
from lxml import etree
from prettytable import PrettyTable
from colorama import init, Fore

# 处理访问请求的url
def setStation(from_station,to_station,queryDate,purpose_codes):
    url='https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=%s'  %(queryDate,from_station,to_station,purpose_codes)
    print(url)
    return url

# 处理页面上返回的数据，把json数据截取出来
def getList(url):
    wb_data = requests.get(url)
    #print(wb_data.text)
    html=wb_data.content
    #print (html)
    soup=BeautifulSoup(html,'lxml')
    data=soup.findAll('p')
    for letter in data:
        t = letter.text
   # print(t)
    return t

def sendToPhone(text):
    pass

def sta():
    url='https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9043'
    response = requests.get(url, verify=False)
    station= re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',response.text)
    return (dict(station))


if __name__ == '__main__' :
    """Command line interface"""
    arguments = docopt(__doc__)
    stations = sta()
    new_stations = { v:k for k,v in stations.items()}    #反转字典
    init()
    # 出发地
    from_station = stations.get(arguments['<from>'])   #南通
    f_station = arguments['<from>']
    # 目的地
    to_station = stations.get(arguments['<to>'])    # 盐城
    t_station = arguments['<to>']
    # 出发日期
    queryDate= arguments['<date>']
    purpose_codes = 'ADULT'
    yw_Count= 0
    yz_Count= 0

    url= setStation(from_station,to_station,queryDate,purpose_codes)
    #biaoti ='车次  出发时间 到达时间  用时 软卧  无座  硬卧  硬座'.split()
    #table = PrettyTable(["车次" ,"始发站","出发时间","终点站" "到达时间","用时","软卧","无座","硬卧","硬座"])
    #print (table)
    text = ''
    try:
        aa = getList(url)
       # print(aa)
        text = json.loads(aa)
        p = text['data']
        Data= p['result']
       # print(Data)
        bHaveTicket= True

    except Exception as e:
        print ('没有查询到车辆信息')
        bHaveTicket = False

    if bHaveTicket :
        table = PrettyTable([Fore.BLUE+"乘车日期","车次" ,"始发车站","出发时间","终点车站", "到达时间","用时","软卧","无座","硬卧","硬座"+Fore.RESET])
        info ='' 
        for index in range (0,len(Data)):
            sResult =Data[index]
         #车次
            station= Data[index].split('|')[3]
         #始发车站
            station1 = Data[index].split('|')[4]
            f_station = new_stations.get(station1)
         #终点站
            station2 = Data[index].split('|')[5]
            t_station = new_stations.get(station2)
         # 出发时间
            departTime= Data[index].split('|')[8]
         # 到达时间
            arriveTime =Data[index].split('|')[9]
         #用时
            userTime =Data[index].split('|')[10]
         # 软卧
            way_22 = Data[index].split('|')[22]
         
            if (way_22 == ''):
                way_22 ='无'
            # 无座
            
            way_25 = Data[index].split('|')[25]
            if (way_25 ==''):
                way_25 = '无'
            # 硬卧
            way_27 = Data[index].split('|')[27]
            if (way_27 == ''):
                way_27 = '无'
            # 硬座
            way_28 = Data[index].split('|')[28]
            if (way_28 == ''):
                way_28 = '无'
            
           # texttmp = '车次:  %s,  出发时间:%s,  到达时间: %s,历时:%s,软座:%s,无座:%s,硬卧:%s,硬座:%s \n '% (station,departTime,arriveTime,userTime,way_22,way_25,way_27,way_28)
            texttmp=[queryDate,station,Fore.GREEN+f_station,departTime+Fore.RESET,Fore.RED+t_station,arriveTime+Fore.RESET,userTime,way_22,way_25,way_27,way_28]
            #print(texttmp)
            table.add_row(texttmp)
        print (table)
            #print(info)



