#usr/bin/python3
# coding=utf-8
# file name dict translate
""" 命令行界面提示
Usage:
    youdao <content>

Options:
    -h      帮助
"""

from docopt import docopt
from bs4 import BeautifulSoup
import requests
import json
from lxml import etree


def postList(url,data):
    senddata={'i':data,'from':'AUTO','to':'AUTO','smartresult':'dict','client':'fanyideskweb','doctype':'json','version':'2.1','keyfrom':'fanyi.web','action':'FY_BY_ENTER','typoResult':'false'} 
    web_data=requests.post(url,data=senddata)
    #print (web_data)
    #print (web_data.text)
    html=web_data.content
    #print(html)
    soup=BeautifulSoup(html,'lxml')
    local_data=soup.findAll('p')
    for letter in local_data:
        t = letter.text
    #print(t)
    return t

def digui(n):
    m=n[0]
    g=m[0]
    return g

if __name__=='__main__':
    """command line"""
    arguments = docopt(__doc__)
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'      #translate后_o要去掉，否则无法获取传回的值
    print(arguments)
    sdata=arguments['<content>']
    #sdata="开心"


    text=''
    try:
        aa=postList(url,sdata)      #字典
        #print (aa)
        text= json.loads(aa)         #json转换后还是字典，双引号变单引号
        #print(text)
        p = text['translateResult']
        #print (p)                     #字典中key translateResult的值，是个数组
        #Data = p['translateResult']
        dic = digui(p)                       #取出字典
        #print(dic)
        bSucess = True

    except Exception as e:
        print('抱歉，无法翻译')
        bSucess= False

    if bSucess:
        
        sResult = dic.get('tgt')
        print('翻译的内容为: ' + sResult)


