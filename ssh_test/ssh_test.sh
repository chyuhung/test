#!/usr/bin/expect -f
#文件路径
set file ip_pwd_list.txt
set result result.txt
#打开文件
set fid [open $file r]
set rid [open $result w]

#登录测试主机名
set username ubuntu
set timeout 5


while { [gets $fid line] >=0 } {
    #第一个词读取为主机IP，第二个词读取为PASSWD
    set host [lindex $line 0]
    set passwd [lindex $line 1]
    #ssh连接测试
    spawn ssh ${username}@${host}
    sleep 2
    expect {
            #出现“yes/no”则键入yes
            "yes/no" { send "yes\r"; exp_continue }
            #sleep 2
            #出现“passwd”则键入密码
            "password:" { send "${passwd}\r";exp_continue }
            #sleep 2
            #出现登入的用户名则说明登录成功，执行命令查看IP地址
            "${username}@" { send "ip a|grep ${host}\r";exp_continue }
            #查询IP地址与连接测试IP是否相同，相同则该主机登录成功,写入文件
            "inet ${host}" { send_user "\n${host} is OK!\n";puts $rid "${host} PASSWD ${passwd} is CORRECT!";}
            }
    #登出主机
    send "exit\r"
    expect eof
}
#关闭文件
close $fid
close $rid
#提示结束
send_user "ALL ssh_test is OK!\n"
#interact