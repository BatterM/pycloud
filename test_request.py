# import requests
# import json
# #钉钉报警器
# token = '4a082e99139a3fb63447f8b0b9a2f0239cdcccab3c063a471158cee2739f35c5'
# api = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(token)
# header = {'Content-Type': 'application/json'}
#
# data = {
#     "msgtype": "text",
#     "text": {
#         "content": "我是你隔壁老王兄弟啊！！"
#     },
#     'at': {
#         'atMobiles': [
#             '15270266620'
#         ]
#     },
#     'isAtAll': 'false'
# }
# sendData = json.dumps(data).encode('utf-8')
# requests.post(url=api, data=sendData, headers=header)

import pymysql
client = pymysql.connect(host='192.168.132.10', user='monitor', password='Good..123', db='sysinfo')
try:
    with client.cursor() as cursors:
        select = "select {},{},{} from {};"
        database = (('date','servername','cpupercent', 'cpu'), ('date','servername','mempercent', 'memory'), ('date','servername','diskpercent', 'disk'))
        for day,name,field, table in database:
            cursors.execute(select.format(day,name,field, table))
            data = cursors.fetchall()
            client.commit()
            print(data)
            #((12.5,), (11.8,))
            # data=list(data)
            # for i in data:
            #     m=i[2]
            #     n='{},{},{}:{}'.format(day,name,field,m)
            #     dingtalk(n)
# except requests.exceptions as error:
#     pass
finally:
    client.close()