#!/usr/bin/env python3
#
#date:2019-8-9
#author:BatterM
#usage:def

# var01=int(input("word01:"))
# var02=int(input("word02:"))
# var03=int(input("word03:"))
# list01=[var01,var02,var03]
#
# def maxNum(a,b,c):
#     number=[a,b,c]
#     m=number[0]
#     for n in number:
#         if m < n:
#             m,n=n,m
#     return m
# print(maxNum(var01,var02,var03))

import json

#1\2\3
def ips(path):
    source, guodu, zhuangtaima ={}, {}, {}
    char=['404', '200', '502', '503']
#最火热的资源
    with open(file=path, mode='r', encoding='utf8') as log:
        for i in log.readlines():
            if i.split()[6] not in source.keys():
                source.setdefault(i.split()[6], 1)
            else:
                source[i.split()[6]] += 1
        source = sorted(source.items(), key=lambda x: x[1], reverse=True)
    head = dict(source[0:10])
#符合的状态码
    with open(file=path, mode='r', encoding='utf8') as log:
        for j in log.readlines():
            if j.split()[8] not in guodu.keys():
                guodu.setdefault(j.split()[8], 1)
            else:
                guodu[j.split()[8]] += 1
        for c in guodu:
            if c in char:
                zhuangtaima.setdefault(c,guodu.get(c))
#访问量前10的ip及次数
        iplist, ipdict = [], {}
    with open('../02.day/access_log', 'r', encoding='utf8') as log:
        for i in log.readlines():
            iplist.append(i.split()[0])
        for i in range(len(iplist)):
            ipdict.setdefault(iplist[i], iplist.count(iplist[i]))
        ipdict = (sorted(ipdict.items(), key=lambda x: x[1], reverse=True))
        head01 = ipdict[0:10]
    return head,zhuangtaima,head01
print(ips('../02.day/access_log'))
with open('ziyuan.json','w',encoding='utf8') as ziyuan:
    json.dump(ips('../02.day/access_log'),ziyuan,ensure_ascii=False)

#4
ipip = {'192.168.161.10':13,'39.100.110.135':8,'1.1.1.1':11,'8.8.8.8':5}
# def paixu(ips01):
#     iplist03=list(ips01.items())
#     for i in range(len(iplist03)):
#         for j in range(len(iplist03)-i-1):
#             if iplist03[j][1]<iplist03[j+1][1]:
#                 iplist03[j],iplist03[j+1]=iplist03[j+1],iplist03[j]
#     return iplist03
# print(paixu(ipip))
ipip=dict(sorted(ipip.items(),key=lambda x:x[1],reverse=True))     #以一敌八，牛
print(ipip)

#5
pv=nuv=0
uv={}
with open('../02.day/access_log', 'r', encoding='utf8') as log:
    for line in log.readlines():
        pv +=1
        if line.split()[0] not in uv.keys():
            uv.setdefault(line.split()[0])
            nuv+=1
print(nuv,pv)