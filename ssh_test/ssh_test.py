import sys
import paramiko
import threading

def remote_comm(host,port,user,pwd,command):
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=host,port=port,username=user,password=pwd)
        try:
            stdin,stdout,stderr=ssh.exec_commond(command)
            out=stdout.read()
            error=stderr.read()
            if out:
                print(out)
            if error:
                print(error)
            ssh.close()
        except:
            pass
    except:
        pass
    return

if __name__=="__main__":
    text=["127.0.0.1 Linshi#312"]
    #passwdlist=["Linshi#312"]
    port=22
    user="cloud"
    command=""

    for line in text:
        host,pwd=line.split(" ")
        print(host,pwd)
        remote_comm(host,port,user,pwd,command)
        #t = threading.Thread(target=remote_comm, args=(host,port,user,pwd,command))
        #t.start()
