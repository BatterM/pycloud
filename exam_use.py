#!/usr/bin/env python3
#
#date:2019-8-22
#author:BatterM
#usage:exam to use
#根据要求书写程序(数据存储格式自己拟定)


#1.把mysql中的Grade.FirstStage表中的数据读取到Excel表格中, 并保存为grade.xlsx文件
# import openpyxl
# import pymysql
# #第一步：将数据读取到变量result
# client=pymysql.connect(
#     host='192.168.132.10',
#     user='batterm',
#     password='Good..123',
#     db='pycharm01',
#     # cursorclass=pymysql.cursors.DictCursor
# )
# sql=client.cursor()
# sql.execute('select * from grade')
# result=sql.fetchall()
# client.commit()
# client.close()
# print(result)
#
# # 第二步：将数据写入excel表中
# book=openpyxl.load_workbook('grade.xlsx')
# sheet=book['studentgrade']
# tuple01=('id','name','firstgrade','secendgrade','pointsdifferent')
# # for i in range(65,70):  #方法一：可以用循环输入
# #     sheet['{}1'.format(str(chr(i)))] = tuple01[i-65]
# sheet.append(tuple01)     #方法二：可以用append输入
# for i in result:
#     sheet.append(i)
# book.save('grade.xlsx')


#2.获取本地主机(linux)的cpu(user/system/idle)/memory(used/free/rate[比率])/disk信息(磁盘利用率), 并记录到数据库中
# import pymysql
# import psutil
# import time
# #1、使用psutil调出cpu,memory,disl信息中
# #cpu
# cpuinfo=psutil.cpu_times_percent(interval=1)
# data=time.strftime('%Y%m%d%H%M%S',time.localtime())   #时间
# infocpu=(cpuinfo.user,cpuinfo.system,cpuinfo.idle)
# user,system,idle=infocpu
# # print('user,system,idle',infocpu)
# #memory
# meminfo=psutil.virtual_memory()
# infomem=(meminfo.used/meminfo.total,meminfo.free/meminfo.total)
# used,free=infomem
# # print('used,free',infomem)
# #disk
# diskinfo=psutil.disk_usage('/')
# usage=diskinfo.percent
# # print('/',datatime,diskinfo.percent)
# #2、使用pymysql连接数据库，记录其中
# client=pymysql.connect(
#     host='192.168.132.10',
#     user='batterm',
#     password='Good..123',
#     db='pycharm01'
# )
# cpu01='insert into cpuinfo values("{}",{},{},{})'.format(data,user,system,idle)
# client.cursor().execute(cpu01)
# mem01='insert into meminfo values("{}",{:.2f},{:.2f})'.format(data,used,free)
# client.cursor().execute(mem01)
# disk01='insert into diskinfo values("{}",{})'.format(data,usage)
# client.cursor().execute(disk01)
#
# client.commit()
# client.close()

# create table cpuinfo( data varchar(1000) not null , user float not null, system float not null, idle float not null);
# create table meminfo( data varchar(1000) not null , used float not null, free float not null);
# create table diskinfo(data varchar(1000) not null , gen float not null);


#3.每日进行: 记录网站的pv/uv量,访问网站前十名IP信息,出现的状态码分布情况 统统记录到数据库中
# import paramiko
# import pymysql

#1、使用远程连接获取日志文件
# transport=paramiko.Transport(('192.168.132.10',22))
# private=paramiko.RSAKey.from_private_key_file('c:\\Users\WL\.ssh\id_rsa')
# transport.connect(username='root',pkey=private)
# sftp=paramiko.SFTPClient.from_transport(transport)
# # sftp.get(remotepath='/opt/pycloud/02.day/access_log',localpath='E:\\pycloud\\ss_log')
# sftp.put(localpath='E:\\pycloud\\02.day\\access_log',remotepath='/pycloud')
# transport.close()

#2、对文件进行信息提取


#3、使用pymysql连接数据库，记录数据库中
# client=pymysql.connect(
#     host='192.168.132.10',
#     user='batterm',
#     password='Good..123',
#     db='pycharm01'
# )


# create table puinfo( data varchar(1000) not null , PV int(100) not null, UV int(100) not null);
# create table ipinfo( data varchar(1000) not null , ip varchar(1000),cout int(100));
# create table codeinfo( data varchar(1000) not null , 404 int(100), 200 int(100));













