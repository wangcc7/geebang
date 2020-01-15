# -*- coding: utf-8 -*-
# by wangcc
# mail:wangcc_sd@163.com


import pymysql
import  os,sys
import configparser

#解析配置文件
def analysis():
    conf = configparser.ConfigParser()
    file_path = './conf.ini'   #读取配置文件
    conf.read(file_path)

    items = conf.items('idss')
    print('获取指定section下所有的键值对', items)


    value = conf.get('mysql', 'host')
    print('获取指定的section下的option', type(value), value)

#获取ga_massage表数据


#处理成短信格式


#读取根据组选择对应的手机号


#发送短信给对应的联系人

def main():
    analysis()


if __name__ == '__main__':
    main()