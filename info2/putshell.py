#!/usr/bin/env python3.7
#
#author:batterm
#usage:get systeminfo.log and put sysinfo.sh

import paramiko
#上传shell脚本
#前提：解决windows传送shell脚本空行问题
#yum -y install dos2unix
#dos2unix sysinfo.sh

#创建远程webserver主机自动获取相关信息并记录日志（计划任务）
def putsysinfo(ips):
    private = paramiko.RSAKey.from_private_key_file('c:\\Users\WL\.ssh\id_rsa')
    transport=paramiko.Transport((ips,22))
    transport.connect(username='root',pkey=private)
    sftp=paramiko.SFTPClient.from_transport(transport)
    client = paramiko.SSHClient()
    client._transport = transport
    sftp.put(localpath='e:\\pycloud\\info2\\auto.sh', remotepath='/root/auto.sh')
    client.exec_command('dos2unix /root/auto.sh')
    client.exec_command('bash /root/auto.sh')
    sftp.put(localpath='e:\\pycloud\\info2\\sysinfo.sh', remotepath='/task/sysinfo.sh')
    client.exec_command('dos2unix /task/sysinfo.sh')
    client.exec_command('bash /task/sysinfo.sh')
    transport.close()

ips01=('192.168.132.30','192.168.132.40')
for ip in ips01:
    putsysinfo(ip)



