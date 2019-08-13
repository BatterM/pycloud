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

    def volume(self):      #定义成员方法
        vo=self.length*self.width*self.height
        return vo

    @classmethod            #类方法
    def creatBox(cls,length,width,height):
        return cls(length=length,width=width,height=height)

    @staticmethod           #静态方法
    def erwuzai(*args,**kwargs):
        return ('''
        thanks you man!
        you're right!!''')

paperBox=Box(20,30,10)   #实例化

v=paperBox.volume()     #调用类的方法
print(v)
paperBox.__length=10
v=paperBox.volume()
print(v)

tiao=Box.creatBox(20,10,10)
v=tiao.volume()
print(v)

print(paperBox.erwuzai())
print(tiao.erwuzai())