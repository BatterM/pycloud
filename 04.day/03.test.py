#!/usr/bin/env python3
#
#date:2019-8-9
#author:BatterM
#usage:test

# 1
# import json
# dict01={}
# with open(file='../02.day/access_log',mode='r',encoding='utf8') as log:
#     for line in log.readlines():
#         if line.split()[0] not in dict01.keys():
#             dict01.setdefault(line.split()[0],1)
#         else:
#             dict01[line.split()[0]] += 1
#     dict01=sorted(dict01.items(),key=lambda x:x[1],reverse=True)
#     head01=dict(dict01[0:10])
# print(head01)
# with open(file='pv.json',mode='w',encoding='utf8') as log:
#     json.dump(head01,log,ensure_ascii=False)


#2
# import json
# dict02,dict002={},{}
# char=('200','404','502','503')
# with open(file='../02.day/access_log',mode='r',encoding='utf8') as log:
#     for line in log.readlines():
#         if line.split()[8] not in dict02.keys():
#             dict02.setdefault(line.split()[8],1)
#         else:
#             dict02[line.split()[8]] += 1
#     for c in dict02.keys():
#         if c in char:
#             dict002.setdefault(c,dict02.get(c))
# print(dict002)
# with open(file='scode.json',mode='w',encoding='utf8') as log:
#     json.dump(dict002,log,ensure_ascii=False)

#3
# import json
# dict03,dict003={},{}
# char=('200','404','502','503')
# with open(file='../02.day/access_log',mode='r',encoding='utf8') as log:
#     for line in log.readlines():
#         if line.split()[6] not in dict03.keys():
#             dict03.setdefault(line.split()[6],1)
#         else:
#             dict03[line.split()[6]] += 1
#     dict03=sorted(dict03.items(),key=lambda x:x[1],reverse=True)
#     head03=dict(dict03[0:10])
# print(head03)
# with open(file='ipaddr.json',mode='w',encoding='utf8') as log:
#     json.dump(head03,log,ensure_ascii=False)

#4
# ips = {'192.168.161.10': 13, '39.100.110.135': 8, '1.1.1.1': 11, '8.8.8.8': 5}
# ips = dict(sorted(ips.items(),key=lambda x:x[1],reverse=True))
# print(ips)

#5
# import json
# def ipip(path):
#     dict01={}
#     pv=nv=0
#     with open(file=path,mode='r',encoding='utf8') as log:
#         for line in log.readlines():
#             pv+=1
#             if line.split()[0] not in dict01.keys():
#                 dict01.setdefault(line.split()[0],1)
#                 nv+=1
#     return pv,nv
# pvn,nvn=ipip('../02.day/access_log')
# print('PV的数量：{} , NV的数量：{}'.format(pvn,nvn))

#6
import json
dict01={}
with open(file='../02.day/access_log', mode='r', encoding='utf8') as log:
    for line in log.readlines():
        if line.split()[0] not in dict01.keys():
            dict01.setdefault(line.split()[0], 1)
        else:
            dict01[line.split()[0]] += 1
    dict01 = dict(sorted(dict01.items(), key=lambda x: x[1], reverse=True))
def dayu(di):
    di={}
    for i in di.keys():
        if di.get(i)>=100:
            di.setdefault(i,di.get(i))
    return di
dict001={}
ip100=list(filter(dayu,dict01))
print(ip100)

#7

#8

