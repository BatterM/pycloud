#!/usr/bin/env python3
#
#date:2019-8-14
#author:BatterM
#usage:feng zhuang


# class Box:
#     def __init__(self, length, width, high):
#         self.__length = length
#         self.__width = width
#         self.__high = high
#
#     @property
#     def getArea(self):
#         sideArea = self.__length * self.__width + self.__length * self.__high
#         lowArea = self.__width * self.__high
#         return (sideArea + lowArea) * 2
#
#     @getArea.setter
#     def getArea(self, lenValues):
#         self.__length,self.__width,self.__high = lenValues
#     @getArea.deleter
#     def getArea(self):
#         print('this object deleted.')
#
# class erBox(Box):
#     def __init__(self,length,width,high):
#         super(erBox,self).__init__(length,width,high)
#
#
# pBox = erBox(20, 15, 10)
# print(pBox.getArea)
# pBox.getArea = (1,2,3)   #解元组/列表
# print(pBox.getArea)
# del pBox.getArea
# print(isinstance(pBox,Box))

class Box:
    def __init__(self, length, width, high):
        self.__length = length
        self.__width = width
        self.__high = high

    @property
    def getVolume(self):
        volume = self.__length * self.__width * self.__high
        return volume

    @getVolume.setter
    def getVolume(self, valuse01):
        self.__length, self.__width, self.__high = valuse01

    @getVolume.deleter
    def getVolume(self):
        print('this object was deleted!')


pBox = Box(20, 15, 10)
v=pBox.getVolume
print(v)

pBox.getVolume = (10,20,30)
print(pBox.getVolume)
del pBox.getVolume
print(getattr(pBox,'getVolume'))
print(hasattr(pBox,'getVolume'))

#内省
r=isinstance('goodman',str)
string='hello world'
re=isinstance(string,str)
num=[1,2,3,4,6,7,8]
#表示（内容中只要有一个条件能满足就返回True）
res=isinstance(num,((tuple or dict) and list))
print(r,re,res)
