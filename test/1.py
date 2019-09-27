#将查询结果格式化输出到json文件中
import json
ips={}

with open(file='../02.day/access_log',mode='r',encoding='utf8') as log:
    for lines in log.readlines():
        ips.setdefault(lines.split()[0],0)
        ips[lines.split()[0]] +=1
    ips=sorted(ips.items(),key=lambda x:x[1],reverse=True)
    ips=dict(ips[0:10])
print(ips)

with open(file='./ips.json',mode='w',encoding='utf8') as log:
    log.write(json.dumps(ips))

ips={'192.168.161.10':13,'39.100.110.135':8,'1.1.1.1':11,'8.8.8.8':5}
ips=sorted(ips.items(),key=lambda x:x[1],reverse=True)
print(ips)

#计步器
print('start!!!!')
def bibao(x):
    def neibao():
        nonlocal x
        x+=1
        return x
    return neibao
a=bibao(10)
print(a())
print(a())
print(a())

#过滤IP次数大于100
ips={}
with open(file='../02.day/access_log',mode='r',encoding='utf8') as log:
    for lines in log.readlines():
        ips.setdefault(lines.split()[0],0)
        ips[lines.split()[0]] +=1
    ips=dict(sorted(ips.items(),key=lambda x:x[1],reverse=True))

def gt(a):
    if a[1]>=100:
        return a
n=filter(gt,ips.items())
print(list(n))