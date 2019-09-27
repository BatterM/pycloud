import pymysql
import json
import requests
import paramiko
#拉取日志文件
def getsysteminfo(ips, rsa, port, use):
    private = paramiko.RSAKey.from_private_key_file(rsa)
    transport = paramiko.Transport((ips, port))
    transport.connect(username=use, pkey=private)
    sftp = paramiko.SFTPClient.from_transport(transport)
    # sftp.get(remotepath='/var/log/monitor/access_log', localpath='/opt/monitor/access_log{}'.format(ips))
    sftp.get(remotepath='/var/log/monitor/access_log', localpath='e:\\pycloud\\info3\\access_log{}'.format(ips))
    transport.close()

#钉钉报警
def dingtalk(token,content):
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
#存储数据
def putmysql(test,sql):
    client=pymysql.connect(
        host='192.168.132.10',
        user='batterm',
        password='Good..123',
        db='webserverinfo'
    )
    cursors = client.cursor()
    if cursors.execute(test) ==False:
        cursors.execute(sql)
    client.commit()
    client.close()
#ip分析
def ipinfo(path):
    pv=uv=0
    ipdict,code,usecode={},{},{}
    charcode=('200','300','400','404','500','502')
    with open(file=path,mode='r',encoding='utf8') as log:
        for lines in log.readlines():
            pv+=1
            if lines.split()[0] not in ipdict.keys():
                ipdict.setdefault(lines.split()[0],0)
                uv+=1
            ipdict[lines.split()[0]]+=1

            code.setdefault(lines.split()[8],0)
            code[lines.split()[8]]+=1
        ipdict=sorted(ipdict.items(),key=lambda x:x[1],reverse=True)
        ipdict = dict(ipdict[0:10])
        for key in code.keys():
            if key in charcode:
                usecode.setdefault(key,code.get(key))
    return pv,uv,ipdict,usecode
#生成数据库能依次传入的列表值
def tabledate(iplist,charcode,ipdict,usecode):
    ipcode={}
    print(usecode)
    for ip in ipdict.items():
        iplist.append(ip)
    for incode in charcode:
        for code in usecode.items():
            if code[0] == incode:
                if code[1] in usecode.values() :
                    ipcode.setdefault(code[0],code[1])
            elif incode not in usecode.keys():
                ipcode.setdefault(incode,0)
    for code in ipcode.items():
        iplist.append(code[1])
    for b in range(4, 14):
        if type(iplist[b]) is not (str and int):
            c = iplist[b][0] + ':' + str(iplist[b][1])
            iplist[b] = c
    return iplist