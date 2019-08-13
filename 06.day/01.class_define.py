#!/usr/bin/env python3
#
#date:2019-8-13
#author:BatterM
#usage:class
#创建一个类Box，并设定相应的属性和方法，然后实例化赋值并调用方法


class Box:        #定义类
    def __init__(self,length,width,height):     #定义属性
        self.length=length
        self.width=width
        self.height=height

    def volume(self):      #定义方法
        vo=self.length*self.width*self.height
        return vo

paperBox=Box(20,30,10)   #实例化

v=paperBox.volume()     #调用类的方法
print(v)
paperBox.length=10
v=paperBox.volume()
print(v)
