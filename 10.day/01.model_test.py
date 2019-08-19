#!/usr/bin/env python3
#
#date:2019-8-19
#author:BatterM
#usage:model test

#1、库-包-模块
# from sharedir.logAnalysis import logAnalysis
#
# ip=logAnalysis.ipsAnalysis('../02.day/access_log')
# print(ip)
#
# code=logAnalysis.codeAnalysis('../02.day/access_log')
# print(code)
#
# source=logAnalysis.sourceAnalysis('../02.day/access_log')
# print(source)

#2、模块
# import sharedir.logAnalysis.logAnalysis
#
# ip=sharedir.logAnalysis.logAnalysis.ipsAnalysis('../02.day/access_log')
# print(ip)
#
# code=sharedir.logAnalysis.logAnalysis.codeAnalysis('../02.day/access_log')
# print(code)
#
# source=sharedir.logAnalysis.logAnalysis.sourceAnalysis('../02.day/access_log')
# print(source)

#3、反射路由模块(动态)
fd=__import__('sharedir.logAnalysis.logAnalysis', fromlist=True)  #等价于fromlist=['logAnalysis']
router=input('come to:')
if hasattr(fd,router):
    get01=getattr(fd,router)
    get01=get01('../02.day/access_log')
    get01 = sorted(get01.items(), key=lambda x: x[1], reverse=True)
    get01=dict(get01[0:10])
    print(get01)
else:
    print('error')
