import paramiko
import time
import pymysql
import requests
import json

def execute(ips):
    transport=paramiko.Transport((ips,22))
    private=paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport.connect(username='root',pkey=private)
    client=paramiko.SSHClient()
    client._transport=transport
    client.exec_command('python3.7 /root/main_use.py')
    transport.close()
#1、执行命令
ips = ('192.168.132.30', '192.168.132.40')
for ip in ips:
    execute(ip)
#2、睡觉
time.sleep(2)
#3、拉取数据
#钉钉报警器
token = 'a0a724543893c0ce6c9be7e3909a3f39fcf25e6293e971cdec5371c7543d7aee'
# token = '725124e947078adbb3fdfdff1e077c747c19440379c8565c9b381e94391982ad'
api = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(token)
header = {'Content-Type': 'application/json'}
def dingtalk(content):
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
    with client.cursor() as cursors:
        select = "select {},{},{} from {};"
        database = (('date','servername','cpupercent', 'cpu'), ('date','servername','mempercent', 'memory'), ('date','servername','diskpercent', 'disk'))
        for day,name,field, table in database:
            cursors.execute(select.format(day,name,field, table))
            if table=='cpu':
                cpu = cursors.fetchall()
                client.commit()
                for i in cpu:
                    if i[2] > 0:
                        n = 'CPU要炸啦：（{}:{}, {}:{}, {}:{}%）'.format(day, i[0], name, i[1], field, i[2])
                        dingtalk(n)
                        time.sleep(1)
            if table=='memory':
                memory = cursors.fetchall()
                client.commit()
                for i in memory:
                    if i[2]>85:
                        n = '内存要炸啦：（{}:{}, {}:{}, {}:{}%）'.format(day, i[0], name, i[1], field, i[2])
                        dingtalk(n)
                        time.sleep(1)
            if table=='disk':
                disk = cursors.fetchall()
                client.commit()
                for i in disk:
                    if i[2] > 85:
                        n = '磁盘要炸啦：（{}:{}, {}:{}, {}:{}%）'.format(day, i[0], name, i[1], field, i[2])
                        dingtalk(n)
                        time.sleep(1)
except requests.exceptions as error:
    pass
except BaseException as error:
    pass
finally:
    client.close()
# XXX = cursors.fetchall()  接收的结果：
# ((20190828165810, 'job01\n', 1.0), (20190828165816, 'job02\n', 1.0))
# ((20190828165811, 'job01\n', 27.9), (20190828165817, 'job02\n', 27.6))
# ((20190828165811, 'job01\n', 12.5), (20190828165817, 'job02\n', 11.8))