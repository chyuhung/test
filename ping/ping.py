from threading import Thread
import os
import re

class PING(Thread):
    def __init__(self,ip):
        Thread.__init__(self)
        self.ip=ip
        self.state=0
    def run(self):
        ping="ping -c 1 -w 1 "+self.ip
        temp=os.popen(ping).read()
        if re.search(", 0% packet loss,",temp):
            print("%s is UP"%self.ip)
            self.state=1
            return
        elif re.search(", 100% packet loss,",temp):
            print("%s is DOWN"%self.ip)
            self.state=-1
            return
        elif re.search("known",temp):
            print("%s is ERROR"%self.ip)
            self.state=0

thread_list=[]
if __name__=="__main__":
    file_ip="host.txt"
    file_result="result.txt"

    with open(file_ip,'r') as file_ip:
        for ip in file_ip.readlines():
            host=PING(ip.replace('\n',''))
            thread_list.append(host)

    with open(file_result,'w') as file_result:
        for i in range(len(thread_list)):
            thread_list[i].start()

        file_result.write("======= UP =======\n")
        for i in range(len(thread_list)):
            thread_list[i].join()
            if 1==thread_list[i].state:
                file_result.write(thread_list[i].ip+"\n")

        file_result.write("======= DOWN =======\n")
        for i in range(len(thread_list)):
            if -1==thread_list[i].state:
                file_result.write(thread_list[i].ip+"\n")

        file_result.write("======= ERROR =======\n")
        for i in range(len(thread_list)):
            if 0==thread_list[i].state:
                file_result.write(thread_list[i].ip+"\n")