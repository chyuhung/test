#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket,time,thread

def get_ip_port_List():
    ip_port_List=[]
    with open("ip_port_list.txt","r") as file:
        for line in file: 
            ip_port_List.append(line)
    return ip_port_List

def scan(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
    s.settimeout(2)
    print(ip,port)
    try:    
        s.connect((ip,port))
        return True
    except Exception,e:
        return False
    s.close()

if __name__=='__main__':
    with open("log.txt","w") as log_file:
        for line in get_ip_port_List():
            line=line.replace('\n','')
            line=line.replace('\t',' ')
            ip=line.split(' ')[0]
            port=line.split(' ')[-1]
            port=int(port)
            if scan(ip,port):
                log_file.write(ip+" "+str(port)+" on\n")
            else:
                log_file.write(ip+" "+str(port)+" off\n")

