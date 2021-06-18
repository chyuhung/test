# encoding: utf-8

from threading import Thread
import os


class SCP_ALL(Thread):
    def __init__(self,ip,file_list):
        Thread.__init__(self)
        self.ip=ip
        self.file_list=file_list
    def run(self):
        file_all=""
        for file in self.file_list:
            file_all+=(" "+file)
            print(file_all)
        temp=os.popen('echo '+ip+file_all).read()
        print(temp)
        return

""" 文件内容格式：
ip file1 file2 file3 ...
执行命令：scp ip files dir """
""" def read_files(files_dir="/home/cloud/scps.txt"):
    files_list=[[""]]
    with open(files_dir) as files:
        i=0,j=0
        for line in files:
            for word in line:
                files_list[i][j]=word
                j++
            i++
        print(files_list) """
    

if __name__=="__main__":
    ip="127.0.0.0"
    file_list=["1.txt","2.txt"]

    host1=SCP_ALL(ip,file_list)
    host1.start()
    