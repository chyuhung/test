#!/usr/bin/env python
# -*- coding:utf-8 -*-
#cloud密码生成
import re

def isValidIP(ip):
    if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",ip):
        return True

def ConversionRule(num):
    result=""
    if num == 0:
        result = "Z"
    elif num == 1:
        result = "Y"
    elif num == 2:
        result = "E"
    elif num == 3:
        result = "S"
    elif num == 4:
        result = "F"
    elif num == 5:
        result = "W"
    elif num == 6:
        result = "L"
    elif num == 7:
        result = "Q"
    elif num == 8:
        result = "B"
    elif num == 9:
        result = "J"
    return result

def numToStr(num):
    result=""
    for ch in num:
        result+=ConversionRule(ch)
    return result

def passwd_cloud(ip):
    if not isValidIP(ip):
        return

    ip_1 = str(ip).split('.')[0]
    ip_2 = str(ip).split('.')[1]
    ip_3 = str(ip).split('.')[2]
    ip_4 = str(ip).split('.')[-1]
    temp_3=int(ip_3)*3+128
    temp_4=int(ip_4)*3+128
    passwd_3=numToStr(temp_3)
    passwd_4=numToStr(temp_4)
    temp=passwd_3+passwd_4

    return "Ug#pvc"+temp

if __name__=="__main__":
    ip="100.11.110.9"
    cloud_passwd=passwd_cloud(ip)
    print(cloud_passwd)
