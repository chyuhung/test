#!/bin/bash  
#author: yifangyou  
#create time:2011-05-17  
#用来通过scp批量上传文件或者目录到目标机器的指定目录  
#配置文件格式：  
#ssh_hosts=("1.1.1.1" "2.2.2.2")  
#ssh_ports=("22" "22") 这个可以缺省，缺省值为22,或者个数比ssh_hosts少时，使用缺省值  
#ssh_users=("root" "root") 这个可以缺省，缺省值为root，,或者个数比ssh_hosts少时，使用缺省值  
#ssh_passwords=("323" "222") 这个可以缺省，缺省的话需要从命令行输入,或者个数比ssh_hosts少时，使用命令行输入  
#执行：sh multi_scp.sh conf_file_path file target  
if [ -z "$3" ]  
then 
echo "sh multi_scp.sh conf_file_path file target";  
exit;  
fi  
default_ssh_user="root" 
default_ssh_port="22";  
#upload shell script file path  
scp_upload=scp_upload.sh  
#configure file path  
conf_file=$1  
#then upload file path  
scp_file=$2  
#remote host'target file or dir path  
scp_target=$3  
#判断conf_file配置文件是存在  
if [ ! -e "$conf_file" ]  
then 
echo "$conf_file is not exists";  
exit;  
fi  
#判断scp_file是文件或者目录  
if [ ! -e "$scp_file" ] && [ ! -d "$scp_file" ]  
then 
echo "$scp_file is not exists";  
exit;  
fi  
#read configure file  
source $conf_file  
#若是没有在配置文件里提供密码，则在命令行输入  
if [ "${#ssh_passwords[@]}" = "0" ] || [ "${#ssh_passwords[@]}" -lt "${#ssh_hosts[@]}" ]  
then 
read -p "please input password:" -s default_ssh_password  
fi  
success_hosts="";  
fail_hosts="";  
for((i=0;i<${#ssh_hosts[@]};i++))  
do  
#remote ssh host  
ssh_host=${ssh_hosts[$i]};  
#remote ssh port  
ssh_port=${ssh_ports[$i]};  
if [ "$ssh_port" = "" ]  
then 
ssh_port=$default_ssh_port;  
fi  
#remote ssh user 
ssh_user=${ssh_users[$i]};  
if [ "$ssh_user" = "" ]  
then 
ssh_user=$default_ssh_user;  
fi  
#remote ssh password 
ssh_password=${ssh_passwords[$i]};  
if [ "$ssh_password" = "" ]  
then 
ssh_password=$default_ssh_password;  
fi  
echo "["`date +"%F %T"`"] (scp -r $scp_file $ssh_user@$ssh_host:$ssh_port:$scp_target) start" 
#scp file or dir  
/usr/bin/expect scp_upload.sh "$ssh_host" "$ssh_port" "$ssh_user" "$ssh_password" "$scp_file" "$scp_target" 
if [ "$?" -eq "0" ]  
then 
success_hosts="$success_hosts,$ssh_host" 
else 
fail_hosts="$fail_hosts,$ssh_host" 
fi  
echo "["`date +"%F %T"`"] (scp -r $scp_file $ssh_user@$ssh_host:$ssh_port:$scp_target) end" 
echo "" 
done  
echo "success_hosts=[$success_hosts]" 
echo "fail_hosts=[$fail_hosts]" 
