# -*- coding: utf-8 -*-
import subprocess
import re
from multiprocessing import Pool

def delay_check(domain):
    print('Run task domain:%s',domain)
    ping_result={}
    p = subprocess.Popen(
        "ping -c 10 {0} \n".format(domain),
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True)
    out = p.stdout.read().decode('gbk')
    #正则匹配结果字符
    regIP = r'\d+\.\d+\.\d+\.\d+'
    regLost = r', (\d.*?%) packet loss'
    regCost = r'= (.*?) ms'
    #获取时间、丢包率等
    ip = re.search(regIP, out)
    lost = re.findall(regLost, out)[0]
    recost = re.findall(regCost, out)
    if recost:
        cost = recost[0].split('/')[1]
        ping_result['cost'] = float(cost)
    if ip:
        ip = ip.group()
        ping_result['ip'] = ip
    if lost:
        lost = lost.split(',')[1].lstrip()
        lost = float(lost.replace('%', ''))
        ping_result['lost'] = lost
    print ping_result
    return ping_result


if __name__ == '__main__':
    p=Pool(5)
    domainlist=['127.0.0.1','127.0.0.2','127.0.0.3','127.0.0.4','127.0.0.5']
    for domain in domainlist:
        p.apply_async(delay_check,args=(domain,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')