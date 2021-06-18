#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Script function: 1.Cloud password automatic generation and automatic configuration
Author：chyuhung
Version：20210125
"""
import re,socket,os,random

#正则判断IP是否合规
def isValidIP(ip):
    if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",ip):
        return True

#实现数字对应字母的转换
def conversionRule(num):
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

#实现字符串数字的字母转换
def numToStr(num):
    result=""
    for char in str(num):
        result+=conversionRule(int(char))
    return result

#参数IP地址，生成cloud密码，如:IP 10.191.22.38,生成cloud密码:XXXX
def passwd_cloud(ip):
    if not isValidIP(ip):
        return
    else:
        ip_1 = str(ip).split('.')[0]
        ip_2 = str(ip).split('.')[1]
        ip_3 = str(ip).split('.')[2]
        ip_4 = str(ip).split('.')[-1]
        temp_3=int(ip_3)*3+128
        temp_4=int(ip_4)*3+128
        passwd_3=numToStr(temp_3)
        passwd_4=numToStr(temp_4)
        passwd_str=passwd_3+passwd_4
        passwd_num=str(temp_3)+str(temp_4)
        passwd_key=""
        for i in range(len(passwd_num)):
            if i%2==0:
                passwd_key+=passwd_num[i]
            else:
                passwd_key+=passwd_str[i]
        return "Ug#pvc"+passwd_key

#获取本机在用IP地址
def getHostIp():
    try:
        csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        csock.connect(('8.8.8.8', 80))
        (addr, port) = csock.getsockname()
        csock.close()
        return addr
    except socket.error:
        print("ERROR:IP address acquisition exception!")
        return

#根据IP生成伪随机root密码
def passwd_root(ip):
    seedNum=int(ip.replace(".",""))
    random.seed(seedNum)
    
#获取主机名
def hostname():
    hostname=os.popen("hostname").read()
    return hostname

#获取主机操作系统版本
def osVersion():
    with open("/proc/version") as file:
        osVersion=file.read()
        return osVersion

#修改cloud密码，需要root权限
def updateCloudPasswd(passwd):
    whoami=os.popen("whoami").read()
    #if whoami != "root":
    #    print("ERROR:Please use root to run the script!")
    #    return
    #strSetPasswd="echo -e \""+passwd+"\\n"+passwd+"\\n\""+"|passwd cloud"
    strSetPasswd="echo \""+passwd+"\""+"|passwd --stdin cloud"
    print("执行命令："+strSetPasswd)
    #result=os.popen(strSetPasswd).read()
    #print(result)

if __name__=="__main__":
    ip=getHostIp()
    cloud_passwd=passwd_cloud(ip)
    updateCloudPasswd(cloud_passwd)
    print(hostname())
    print(osVersion())
