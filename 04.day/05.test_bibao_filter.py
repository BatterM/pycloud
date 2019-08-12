#!/usr/bin/env python3
#
#date:2019-8-10
#author:BatterM
#usage:bibao and filter

#过滤出ip次数大于100的ip地址
dict01={}
with open(file='../02.day/access_log',mode='r',encoding='utf8') as log:
    for line in log.readlines():
        if line.split()[0] not in dict01.keys():
            dict01.setdefault(line.split()[0],1)
        else:
            dict01[line.split()[0]] += 1
    dict01=sorted(dict01.items(),key=lambda x:x[1],reverse=True)
    head01=dict(dict01[0:10])
print(head01)

def bijiao(one):
    if one[1]>100:
        return True

jieguo=list(filter(bijiao,dict01))
print(jieguo)

#闭包计步器
def stepCount(n):
    def Count():
        nonlocal n
        if n>0:
            n+=1
        return n
    return Count
step=stepCount(10)
print(step())
print(step())
print(step())
