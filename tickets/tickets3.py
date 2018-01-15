#!usr/bin/python3
# coding=gbk
# file name pachong

"""�����в鿴��
Usage:
    tickets2 <from> <to> <date>

Options:
    -h    �����˵�
    -d    ����
    -g    ����
    -t    �ؿ�
    -k    ����
    -z    ֱ��
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

# ������������url
def setStation(from_station,to_station,queryDate,purpose_codes):
    url='https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=%s'  %(queryDate,from_station,to_station,purpose_codes)
    print(url)
    return url

# ����ҳ���Ϸ��ص����ݣ���json���ݽ�ȡ����
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
    new_stations = { v:k for k,v in stations.items()}    #��ת�ֵ�
    init()
    # ������
    from_station = stations.get(arguments['<from>'])   #��ͨ
    f_station = arguments['<from>']
    # Ŀ�ĵ�
    to_station = stations.get(arguments['<to>'])    # �γ�
    t_station = arguments['<to>']
    # ��������
    queryDate= arguments['<date>']
    purpose_codes = 'ADULT'
    yw_Count= 0
    yz_Count= 0

    url= setStation(from_station,to_station,queryDate,purpose_codes)
    #biaoti ='����  ����ʱ�� ����ʱ��  ��ʱ ����  ����  Ӳ��  Ӳ��'.split()
    #table = PrettyTable(["����" ,"ʼ��վ","����ʱ��","�յ�վ" "����ʱ��","��ʱ","����","����","Ӳ��","Ӳ��"])
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
        print ('û�в�ѯ��������Ϣ')
        bHaveTicket = False

    if bHaveTicket :
        table = PrettyTable([Fore.BLUE+"�˳�����","����" ,"ʼ����վ","����ʱ��","�յ㳵վ", "����ʱ��","��ʱ","����","����","Ӳ��","Ӳ��"+Fore.RESET])
        info ='' 
        for index in range (0,len(Data)):
            sResult =Data[index]
         #����
            station= Data[index].split('|')[3]
         #ʼ����վ
            station1 = Data[index].split('|')[4]
            f_station = new_stations.get(station1)
         #�յ�վ
            station2 = Data[index].split('|')[5]
            t_station = new_stations.get(station2)
         # ����ʱ��
            departTime= Data[index].split('|')[8]
         # ����ʱ��
            arriveTime =Data[index].split('|')[9]
         #��ʱ
            userTime =Data[index].split('|')[10]
         # ����
            way_22 = Data[index].split('|')[22]
         
            if (way_22 == ''):
                way_22 ='��'
            # ����
            
            way_25 = Data[index].split('|')[25]
            if (way_25 ==''):
                way_25 = '��'
            # Ӳ��
            way_27 = Data[index].split('|')[27]
            if (way_27 == ''):
                way_27 = '��'
            # Ӳ��
            way_28 = Data[index].split('|')[28]
            if (way_28 == ''):
                way_28 = '��'
            
           # texttmp = '����:  %s,  ����ʱ��:%s,  ����ʱ��: %s,��ʱ:%s,����:%s,����:%s,Ӳ��:%s,Ӳ��:%s \n '% (station,departTime,arriveTime,userTime,way_22,way_25,way_27,way_28)
            texttmp=[queryDate,station,Fore.GREEN+f_station,departTime+Fore.RESET,Fore.RED+t_station,arriveTime+Fore.RESET,userTime,way_22,way_25,way_27,way_28]
            #print(texttmp)
            table.add_row(texttmp)
        print (table)
            #print(info)



