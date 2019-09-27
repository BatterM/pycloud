import paramiko
import time
import pymysql
import requests
import json


def tar(ips):
    transport = paramiko.Transport((ips, 22))
    private = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport.connect(username='root', pkey=private)
    client = paramiko.SSHClient()
    client._transport = transport
    client.exec_command('tar xf /root/monitor.tar -C /root/')
    transport.close()

def execute(ips):
    transport=paramiko.Transport((ips,22))
    private=paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport.connect(username='root',pkey=private)
    client=paramiko.SSHClient()
    client._transport=transport
    client.exec_command('python3.7 /root/main_use.py')
    transport.close()
def transfer(ips):
    private = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport((ips, 22))
    transport.connect(username='root',pkey=private)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(localpath='./monitor.tar', remotepath='/root/monitor.tar')     #打包文件
    transport.close()
#1、执行命令
ips = ('192.168.132.30', '192.168.132.40')
for ip in ips:
    transfer(ip)
for ip in ips:
    tar(ip)
for ip in ips:
    execute(ip)
#2、睡觉
time.sleep(5)
#3、拉取数据

#钉钉报警器
def dingtalk(content):
    token = '725124e947078adbb3fdfdff1e077c747c19440379c8565c9b381e94391982ad'
    api = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(token)
    header = {'Content-Type': 'application/json'}
    data = {
        "msgtype": "text",
        "text": {
            "content": "{}".format(content)
        },
        'at': {
            'atMobiles': [
                '15270266620',
            ]
        },
        'isAtAll': 'false'
    }
    sendData = json.dumps(data).encode('utf-8')
    requests.post(url=api, data=sendData, headers=header)

#数据处理
client = pymysql.connect(host='192.168.132.10', user='monitor', password='Good..123', db='sysinfo')
try:
    # client = pymysql.connect(host='192.168.132.10', user='monitor', password='Good..123', db='sysinfo')
    with client.cursor() as cursors:
        select = "select {} from {};"
        database = (('cpupercent', 'cpu'), ('mempercent', 'memory'), ('diskpercent', 'disk'))
        for field, table in database:
            cursors.execute(select.format(field, table))
            data = cursors.fetchall()
            client.commit()
            dingtalk(data)
            # for i in range(len(data)):
            #     if field == 'cpupercent':
            #         if float(data[i]) > 85:
            #             print('cpu报警啦!')
            #     elif field == 'mempercent':
            #         if float(data[i]) > 95:
            #             print('memory报警啦!')
            #     elif field == 'diskpercent':
            #         if float(data[i]) > 90:
            #             print('disk报警啦!')
except requests.exceptions as error:
    pass
finally:
    client.close()

