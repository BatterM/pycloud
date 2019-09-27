import paramiko
import pymysql
import json
import requests
import logging.config
import time

#拉取webserver主机上的日志文件到监视器主机monitor(用pycharm进行练习)
def getsysteminfo(ips,rsa,port,use,i):
    private = paramiko.RSAKey.from_private_key_file(rsa)
    transport=paramiko.Transport((ips,port))
    transport.connect(username=use,pkey=private)
    sftp=paramiko.SFTPClient.from_transport(transport)
    sftp.get(remotepath='/var/log/monitor/systeminfo.log',localpath='/opt/monitor/systeminfo_log{}'.format(i))
    transport.close()
#1、提取日志文件
ips=('192.168.132.30','192.168.132.40')         #被监控主机
i=0
try:
    for ip in ips:
        i+=1
        getsysteminfo(ip,'/root/.ssh/id_rsa',22,'root',i)
except Exception as error:
    pass
finally:
    pass
#2、钉钉报警
token = 'a0a724543893c0ce6c9be7e3909a3f39fcf25e6293e971cdec5371c7543d7aee'
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
#3、连接数据库
client=pymysql.connect(
    host='192.168.132.10',
    user='batterm',
    password='Good..123',
    db='webserverinfo'
)
sql_cpu = 'insert into cpu values ({},{},{});'
sql_mem = 'insert into memory values ({},{},{});'
sql_disk = 'insert into disk values ({},{},{});'
sql_test='select date from {} where date={} and servername={};'
cursors=client.cursor()
#4、处理文件
def putmysql(cpu,memory,disk,path,logpath):
    logging.config.fileConfig(logpath)
    logger = logging.getLogger('rotateSize')
    with open(file=path,mode='r',encoding='utf8') as log:
        for lines in log.readlines():
            allinfo=(lines.split(' - ')[2])   #a是字符串(数据信息)
            date=(lines.split(' - ')[0])    #日期
            servername=(lines.split(' - ')[1])    #主机名
            allinfo=json.loads(allinfo)        #a是一个字典了
            for sysinfo in allinfo.items():
#报警，并把信息写入logging日志和mysql数据库
                if sysinfo[0]=='cpu':
                    for cpuinfo in sysinfo[1].items():
                        test = cursors.execute(sql_test.format(sysinfo[0], date,servername))
                        if test == False:                           # 数据库中没有该数据
                            if cpuinfo[0] == 'used':
                                cursors.execute(sql_cpu.format(date, servername, cpuinfo[1]))
                                client.commit()
                                if cpuinfo[1] >cpu:
                                    dingtalk('''
                                    Date:{}
                                    Servername:{}
                                    Cpu BOOM!!:{}%'''.format(date,servername,cpuinfo[1]))
                                    logger.warning('Server:{}, CPU BOOM!!:{}%'.format(servername,cpuinfo[1]))
                                time.sleep(1)
                if sysinfo[0]=='memory':
                    test = cursors.execute(sql_test.format(sysinfo[0],date,servername))
                    if test == False:                              # 数据库中没有该数据
                        for meminfo in sysinfo[1].items():
                            if meminfo[0] =='used':
                                memused = round(meminfo[1], 2)
                                cursors.execute(sql_mem.format(date, servername, memused))
                                client.commit()
                                if meminfo[1] >memory:
                                    dingtalk('''
                                    Date:{}
                                    Servername:{}
                                    Memory BOOM!!:{}%'''.format(date,servername,memused))
                                    logger.warning('Server:{}, Memory BOOM!!:{}%'.format(servername,memused))
                                time.sleep(1)
                if sysinfo[0]=='disk':
                    test = cursors.execute(sql_test.format(sysinfo[0], date,servername))
                    if test == False:                              # 数据库中没有该数据
                        for diskinfo in sysinfo[1].items():
                            if diskinfo[0] =='used':
                                diskused=int(diskinfo[1].split('%')[0])
                                cursors.execute(sql_disk.format(date, servername, diskused))
                                client.commit()
                                if diskused>disk:
                                    dingtalk('''
                                    Date:{}
                                    Servername:{}
                                    Disk BOOM!!:{}%'''.format(date,servername,diskused))
                                    logger.warning('Server:{}, Disk BOOM!!:{}%'.format(servername,diskinfo[1]))
                                time.sleep(1)

paths=('/opt/monitor/systeminfo_log1','/opt/monitor/systeminfo_log2')
for path in paths:
    try:
        putmysql(80,20,20,path,'/opt/monitor/logconfig.conf')
    except BaseException as error:
        pass
    except requests.exceptions as error:
        pass
    finally:
        pass
client.close()