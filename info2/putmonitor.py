#usage:get systeminfo.log and put sysinfo.sh

import paramiko
#上传shell脚本
#前提：解决windows传送shell脚本空行问题
#yum -y install dos2unix
#dos2unix sysinfo.sh
#创建远程webserver主机自动获取相关信息并记录日志（计划任务）
def putsysinfo():
    private = paramiko.RSAKey.from_private_key_file('c:\\Users\WL\.ssh\id_rsa')
    transport=paramiko.Transport(('192.168.132.20',22))
    transport.connect(username='root',pkey=private)
    sftp=paramiko.SFTPClient.from_transport(transport)
    sftp.put(localpath='e:\\pycloud\\info2\\getwebinfo.py', remotepath='/opt/monitor/getwebinfo.py')
    # sftp.put(localpath='e:\\pycloud\\info2\\logconfig.conf', remotepath='/opt/monitor/logconfig.conf')
    transport.close()

# ips01=('192.168.132.20')
# # ips01=('192.168.132.30','192.168.132.40')
# for ip in ips01:
putsysinfo()