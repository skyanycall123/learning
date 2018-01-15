#!/usr/bin/python
# coding=gbk  
# filename tickets1


""" 命令行火车票查看器

Usage:
    tickets1 [-dfktz] <from>  <to>  <date>

Options:
    -h,  --hlep 查看帮助
    -d          动车
    -g          高铁
    -k          快速
    -t          特快
    -z          直达

Examples:
    
    tickets1 上海  北京  2016-10-10
    tickets1 -dg  成都  南京   2017-10-08

"""

import re
import requests
from docopt import docopt
from prettytable  import PrettyTable
from colorama import init, Fore






#init()

class TrainsColleciton:
    #'列车的相关属性和方法封装'

    header = '车次  车站  时间  历时  一等  二等  软卧  硬卧  无座'.split()

    def __init__(self,available_trains,options):

        self.available_trains = available_trains
        self.options = options
    
    def _get_duration(self,raw_train):

        duration = raw_train.get('lishi').replace(':','小时') + '分'
        if duration.startswith('00'):
            return duration[4:]
        
        if duration.startswith('0'):
            return duration[1:]
        return duration

    @property
    def trains(self):
        for raw_train in self.available_trains:
            train_no =raw_train['station_train_code']
            initial = train_no[0].lower()
            if not self.options or initial in self.options:
                train = [
                    train_no,
                    '/n'.join([fore.GREEN + raw_train['from_station_name'] + Fore.RESET,
                    Fore.RED + raw_train['to_station_name'] +Fore.RESET]),
                    '/n'.join([Fore.GREEN +raw_train['start_time'] + Fore.RESET,
                    Fore.RED + raw_train['arrive_time'] + Fore.RESET]),
                    self._get_duration(raw_train),
                    raw_train['zy_num'],
                    raw_train['ze_num'],
                    raw_train['rw_num'],
                    raw_train['yw_num'],
                    raw_train['yz_num'],
                    raw_train['wz_num'],
                ]
                yield train

    def pretty_print(self):
        pt =PrettyTable()
        pt._set_field_names(self.header)
        for train in self.trains:
            pt.add_row(train)
        print(pt)


def sta():
    url='https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9043'
    response = requests.get(url, verify=False)
    station= re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',response.text)
    return (dict(station))




def cli():
    stations=sta()
    print(stations)
    arguments= docopt(__doc__)
    print(arguments)

"""
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments['<date>']
    
    url=('https://kyfw.12306.cn/otn/lcxxcx/qurey?'
         'purpose_codes=ADULT&queryDate={}&'
         'from_station={}&to_station={}').format(
            date,from_station,to_station
         )
    options = ''.join([
        key for key, value in arguments.items() if value is True
        ])

    r= requests.get(url,verify=False)
    available_trains = r.json()['data']['datas']
    TrainsCollection(available_trains,options).pretty_print()
"""

if __name__ == '__main__':
    cli()
