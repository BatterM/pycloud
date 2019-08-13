#!/usr/bin/env python3
#
#date:2019-8-13
#author:BatterM
#usage:nginx log


class Nginxlog:
    def __init__(self,path):
        self.path=path
    #1统计pv和uv量
    def pnv(self):
        UV=PV=0
        ips={}
        with open(file=self.path,mode='r',encoding='utf8') as log:
            for lines in log.readlines():
                PV+=1
                if lines.split()[0] not in ips.keys():
                    ips.setdefault(lines.split()[0],1)
                    UV+=1
                else:
                    ips[lines.split()[0]] +=1
        return 'PV量是:{},UV量是:{}'.format(PV,UV)

    #2统计状态码
    def ztm(self):
        zhuangtaima,zhuangtai,char={},{},('200','302','304','404','502','503','504')
        with open(file=self.path,mode='r',encoding='utf8') as log:
            for lines in log.readlines():
                if lines.split()[8] not in zhuangtai.keys():
                    zhuangtai.setdefault(lines.split()[8],1)
                else:
                    zhuangtai[lines.split()[8]]+=1
            for c in char:
                if c in zhuangtai.keys():
                    zhuangtaima.setdefault(c,zhuangtai.get(c))
        return zhuangtaima

    #3统计最热资源
    def zy(self):
        ziyuan={}
        with open(file=self.path,mode='r',encoding='utf8') as log:
            for lines in log.readlines():
                ziyuan.setdefault(lines.split()[6],0)
                ziyuan[lines.split()[6]] +=1
            ziyuan=(sorted(ziyuan.items(),key=lambda x:x[1],reverse=True))
            ziyuan=dict(ziyuan[0:5])
        return ziyuan

log=Nginxlog('../02.day/access_log')
print(log.pnv())
print(log.ztm())
print(log.zy())
