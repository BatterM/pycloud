#encoding:utf-8
from info3.info3 import info
import time
date=time.strftime('%Y/%m/%d')          #记录时间
info.getsysteminfo('192.168.132.30','c:\\Users\WL\.ssh\id_rsa', 22, 'root')         #1、提取日志文件
path=('./info3/access_log192.168.132.30')
pv,uv,ipdict,usecode=info.ipinfo(path)          #2、分析日志
token = 'a0a724543893c0ce6c9be7e3909a3f39fcf25e6293e971cdec5371c7543d7aee'
content='''Date: {}   ServerIP: 192.168.132.30
PV : {}    UV : {}
ipTOP NO.1 - NO.10 :
{}
code :
{}
'''.format(date,pv,uv,ipdict,usecode)
info.dingtalk(token,content)        #3、钉钉报警
charcode=('200','300','400','404','500','502')
iplist=[date,'192.168.132.30',pv,uv]
datalist=info.tabledate(iplist,charcode,ipdict,usecode)       #3、产生数据列表
sql_webaccess = 'insert into webaccess values("{}","{}",{},{},"{}","{}","{}","{}","{}","{}","{}","{}","{}","{}",{},{},{},{},{},{});'.format(*datalist)
sql_test='select date from webaccess where date="{}" and serverip="{}";'.format(date,'192.168.132.30')
info.putmysql(sql_test,sql_webaccess)         #5、存数据







#表结构
# create table webaccess (date varchar(100) not null,serverip varchar(100) not null,
# pv int(100) not null,uv int(100) not null,iptop01 varchar(100),iptop02 varchar(100),
# iptop03 varchar(100),iptop04 varchar(100),iptop05 varchar(100),iptop06 varchar(100),
# iptop07 varchar(100),iptop08 varchar(100),iptop09 varchar(100),iptop10 varchar(100),
# c200 int(100),c300 int(100),c400 int(100),c404 int(100),c500 int(100),c502 int(100))