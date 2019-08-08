#!/usr/bin/env python3
#
#date:2019-8-8
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


def ips(path):
    source, guodu, zhuangtaima ={}, {}, {}
    char=['404', '200', '502', '503']
    with open(file=path, mode='r', encoding='utf8') as log:
        for i in log.readlines():
            if i.split()[6] not in source.keys():
                source.setdefault(i.split()[6], 1)
            else:
                source[i.split()[6]] += 1
        source = sorted(source.items(), key=lambda x: x[1], reverse=True)
    head = dict(source[0:10])
    with open(file=path, mode='r', encoding='utf8') as log:
        for j in log.readlines():
            if j.split()[8] not in guodu.keys():
                guodu.setdefault(j.split()[8], 1)
            else:
                guodu[j.split()[8]] += 1
        # guodu = dict(sorted(guodu.items(), key=lambda x: x[1], reverse=True))
        for c in guodu.keys():
            if c in char:
                zhuangtaima.setdefault(c,guodu.get(c))
    return head,zhuangtaima
print(ips('../02.day/access_log'))