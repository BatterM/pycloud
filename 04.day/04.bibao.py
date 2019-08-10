#!/usr/bin/env python3
#
#date:2019-8-10
#author:BatterM
#usage:bibao

#闭包结构
def x(b):
    print(b)
    def f(c):
        print(c)
        return c*b
    return f
a=x(2)         #这里a=x()里面的变量是外部函数变量b
print(a(4))    #这里a()里面的变量是内部函数变量c


#访问日志，查看uv量及访问次数
dict01={1:2,3:4}
def a(path):
    def b(c):
        if type(c) not in {dict} or len(c) !=0:
            p='Type not dict or not null !!'
            return p
        with open(file=path,mode='r',encoding='utf8') as log:
            for line in log.readlines():
                if line.split()[0] not in c:
                    c.setdefault(line.split()[0],1)
                else:
                    c[line.split()[0]] +=1
            return c
    return b
dict03=[]
dict02={}
log01=a('../02.day/access_log')
print(log01(dict02))
print(log01(dict03))
dict02=dict(sorted(dict02.items(),key=lambda x:x[1],reverse=True))
print(dict02)

import os
aa=os.path.splitext('E:/pycloud/04.day/03.test.py')
print(aa)
