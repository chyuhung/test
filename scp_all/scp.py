import os
from threading import Thread

class RemoteShell(Thread):
    def __init__(self, host, user, pwd,local_path,remote_path):
        Thread.__init__(self)
        self.host = host
        self.user  = user
        self.pwd  = pwd
        self.local_path=local_path
        self.remote_path=remote_path

    def run(self):
        scp_put ='''
        set timeout -1  
        spawn scp %s %s@%s:%s  
        expect "(yes/no)?" {  
        send "yes\r"  
        expect "password:"  
        send "%s\r"  
        } "password:" {send "%s\r"}  
        expect eof  
        exit
        '''
        os.system("echo '%s' > scp_put.cmd" % (scp_put % (os.path.expanduser(self.local_path), self.user, self.host, self.remote_path, self.pwd, self.pwd)))
        os.system('expect scp_put.cmd')
        os.system('rm scp_put.cmd')


if __name__ == '__main__':
    hosts_list=[]
    with open("hosts.txt","r") as file:
        for line in file.readlines():
            try:
                hosts=[]
                line.replace(chr(3),'').replace(chr(0x0c),'')
                curLine=line.strip().split(" ")
                hosts.append(curLine[0:1])
                hosts.append(curLine[1:2])
                hosts.append(curLine[2:3])
                hosts.append(curLine[3:4])
                hosts.append(curLine[4:5])
                #print(hosts)
                hosts_list.append(hosts)
            except Exception as e:
                print("Error")
                exit()

    thread_list=[]

    for lines in hosts_list:
        temp=[]
        for line in lines:
            temp.append(line[0])
        print(temp)
        thread_list.append(RemoteShell(temp[0],temp[1],temp[2],temp[3],temp[4]))
    
    text=input("ok? (yes/no):")
    if len(text)>=3:
        for i in range(len(thread_list)):
            thread_list[i].start()
            thread_list[i].join()
    else:
        print("exit.")
        exit(0)

    #remote01=RemoteShell("121.5.56.23","cloud","Lin&shi#31o","/home/cyh/test/scp_all/test","/home/cloud/")
    #remote01.start()
    #remote01.join()