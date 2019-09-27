#!/usr/bin/env python3
#
#date:2019-8-22
#author:BatterM
#usage:use pymysql


import pymysql

client=pymysql.connect(
    host='192.168.132.10',
    user='batterm',
    password='Good..123',
    db='pycharm01',
    cursorclass=pymysql.cursors.DictCursor  #将SQL结果以字典的形式显示
)

#接收语句结果显示到控制台
sql=client.cursor()
sql.execute('select * from grade;')
result=sql.fetchall()
print(result)
#将文件grade.txt中内容写入远程数据库中
# with open (file='grade.txt',mode='r',encoding='utf8') as log:
#     n=0
#     for lines in log.readlines():
#         name,firstgrafe,secendgrade,pointsdifferent=lines.split()
#         n+=1
#         sql = 'insert into grade values ({},"{}",{},{},{});'.format(n, name, int(firstgrafe), int(secendgrade), int(pointsdifferent))
#         client.cursor().execute(sql)
client.commit()
client.close()



