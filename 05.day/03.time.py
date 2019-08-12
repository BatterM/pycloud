#!/usr/bin/env python3
#
#date:2019-8-12
#author:BatterM
#usage:time

import datetime,time
actime=datetime.datetime.now()
print(actime)
print(actime.date())

first=time.perf_counter()

lista=[x for x in range(10)]
print(lista)
listb=[(lambda x: x**3)(x) for x in range(11)]
print(listb)

end=time.perf_counter()
print('时差是: {:f}'.format(end - first))

#函数时延
import functools
def logtime(def01):
    @functools.wraps(def01)
    def logdiaoyong(*args,**kwargs):
        first01=time.perf_counter()
        def01()
        end01=time.perf_counter()
        print('函数执行时间是：{:f}'.format(end01 - first01))
    return logdiaoyong

@logtime
def time01():
    listc=[(lambda x: x**4)(x) for x in range(15)]
    print('执行完毕！')

time01()
