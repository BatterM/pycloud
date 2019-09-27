from infoproject.infocpumemdisk import getcpuinfo
from infoproject.infocpumemdisk import getdiskinfo
from infoproject.infocpumemdisk import getmeminfo
import pymysql
import time
import subprocess

client=pymysql.connect(host='192.168.132.10',user='monitor',password='Good..123',db='sysinfo')
with client.cursor() as cursors:
    insert="insert into cpu values ({},'{}',{})"
    hostname=subprocess.run('hostname',shell=True,stdout=subprocess.PIPE)
    cursors.execute(insert.format(
        time.strftime('%Y%m%d%H%M%S'),
        hostname.stdout.decode('utf-8'),
        getcpuinfo.cpu()
    ))
client.commit()
with client.cursor() as cursors:
    insert="insert into memory values ({},'{}',{})"
    hostname=subprocess.run('hostname',shell=True,stdout=subprocess.PIPE)
    cursors.execute(insert.format(
        time.strftime('%Y%m%d%H%M%S'),
        hostname.stdout.decode('utf-8'),
        getmeminfo.memory()
    ))
client.commit()
with client.cursor() as cursors:
    insert="insert into disk values ({},'{}',{})"
    hostname=subprocess.run('hostname',shell=True,stdout=subprocess.PIPE)
    cursors.execute(insert.format(
        time.strftime('%Y%m%d%H%M%S'),
        hostname.stdout.decode('utf-8'),
        getdiskinfo.disk()
    ))
client.commit()

client.close()

