#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket,time
from threading import Thread

class Host(Thread):
    def __init__(self,ip,port):
        Thread.__init__(self)
        self.ip=ip
        self.port=port
        self.status=False

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
        s.settimeout(2)
        print(self.ip,self.port)
        try:    
            s.connect((self.ip,self.port))
            self.status=True
        except Exception,e:
            self.status=False
        s.close()

def get_ip_port_List():
    ip_port_List=[]
    with open("ip_port_list.txt","r") as file:
        for line in file: 
            line=line.replace('\n','')
            line=line.replace('\t',' ')
            ip_port_List.append(line)
    return ip_port_List



if __name__=='__main__':
    thread_list=[]
    with open("log.txt","w") as log_file:
        for line in get_ip_port_List():
            ip=line.split(' ')[0]
            port=line.split(' ')[-1]
            port=int(port)
            thread_list.append(Host(ip,port))
        for i in range(len(thread_list)):
            thread_list[i].start()

        for i in range(len(thread_list)):
            thread_list[i].join()
            if thread_list[i].status:
                log_file.write(thread_list[i].ip+" "+str(thread_list[i].port)+" on\n")
            else:
                log_file.write(thread_list[i].ip+" "+str(thread_list[i].port)+" off\n")

