#!/usr/bin/env python3
#
#author:BatterM
#date:2019-8-7
#usage:

set01 = {1,2,3,3,32,2,5,15,15,15,5,9}   #创建一个集合
set01.add("goodboy")                    #增加一个元素
print(set01)
set01.pop()                             #删除第一个元素（但不稳定），建议使用remove方法
print(set01)
set01.remove(5)
set01.remove(9)
set01.pop()
for i in set01:                         #使用in遍历出集合的元素
    print(i)
list01=['goodboy','goodgilr']           #集合使用update面向的是可迭代对象
set01.update(list01)                    #去重，添加list01中集合没有的元素
print(set01)



