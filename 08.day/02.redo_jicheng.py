#!/usr/bin/env python3
#
#date:2019-8-15
#author:BatterM
#usage:继承

#链式继承
# class A:
#     def __init__(self,name,age):
#         print('A')
#         self.name=name
#         self.age=age
#
#     def getName(self):
#         return self.name
#
# class B(A):
#     def __init__(self,name,age,sex):
#         print('B')
#         super(B, self).__init__(name,age)
#         self.sex = sex
#
#     def getName(self):
#         return self.name
#
#
# class C(B):
#     def __init__(self, name,age,sex,length):
#         print('C')
#         super(C, self).__init__(name,age,sex)
#         self.length=length
#
#     def getName(self):
#         return self.name
#
# class D(C):
#     def __init__(self, name,age,sex,length,width):
#         print('D')
#         super(D, self).__init__(name,age,sex,length)
#         self.width=width
#
#     def getName(self):
#         return self.name
#
#
# E=D('mars','18','M',165,50)

#菱形继承
# class A:
#     def __init__(self,name,age):
#         print('A')
#         self.name=name
#         self.age=age
#
#     def getName(self):
#         return self.name
#
# class B(A):
#     def __init__(self,name,age,**kwargs):
#         print('B')
#         super(B, self).__init__(name,age)
#         self.kwargs = kwargs
#
#     def getName(self):
#         return self.name
#
#
# class C(A):
#     def __init__(self, name,age,**kwargs):
#         print('C')
#         super(C, self).__init__(name,age)
#         self.kwargs=kwargs
#
#     def getName(self):
#         return self.name
#
# class D(B,C):
#     def __init__(self, name,age,**kwargs):
#         print('D')
#         super(D,self).__init__(name,age,**kwargs)
#
#     def __call__(self, *args, **kwargs):
#         return self.kwargs
#
#     def getName(self):
#         return self.name
#
# E=D('mars','18',yi={'good',10})
# print(E())

#钻石继承
class A:
    def __init__(self,name,age,length):
        print('A')
        self.name=name
        self.age=age
        self.length=length

    def getName(self):
        return self.name

class B:
    def __init__(self,name,age,sex):
        print('B')
        self.name=name
        self.age=age
        self.sex = sex

class C(A,B):
    def __init__(self, name,age,length,sex):
        print('C')
        super(C, self).__init__(name,age,length)
        self.sex=sex

    def getName(self):
        return self.sex

E=C('mars','18',10,20)
print(E.getName())