#1、函数嵌套
# def A(*args,*kwargs):
#     函数体A
#     def B(*args,*kwargs):
#         函数体B
#         return XXX
#     return B()

#2、闭包
# def A(*args,*kwargs):
#     函数体A
#     def B(*args,*kwargs):
#         函数体B
#         return XXX
#     return B

#3、匿名函数
# 语法: 变量名 = lambda 参数01, 参数02, ... : 表达式
A= lambda a,b: a*b
print(A(a=1,b=2))
#ip排序
#Ips02=(sorted(ips01.items(),key=lambda x: x[1] , reverse=True))

#4、递归函数
# 函数的返回值是自己本身, 在函数内部设置检查机制符合条件时跳出循环
def addr(number):               # 求10的阶乘,并打印结果.
    if number == 1:
        return number
    return number * addr(number-1)
print(addr(10))

#5、高级函数 map / filter / reduce
#map:每个元素都执行一次函数并返回结果
#返回结果：每次函数执行的结果
B=map(lambda a:a+1,range(10))
B=list(B)
print(B)
#filter:每个元素都执行一次函数并留下符合过滤条件的元素（可迭代对象的元素）
#返回结果：可迭代对象中符合过滤条件的元素
B=filter(lambda a:a+1,range(1,10))
B=list(B)
print(B)
#reduce:每个元素都执行一次函数，但将返回最终的相乘结果
# 每次执行将return 的结果留作下一次函数参数之一，然后在可迭代对象再取一个元素当作另一个元素，最后相乘
#当可迭代对象取完，就将返回最终的相乘结果
#返回结果：迭代对象元素相乘结果
from functools import reduce
def nick(x, y):
    return x * y
C=reduce(nick,B)
print(C)

#6、装饰器
# import functools
# def A(函数名C):
#     @functools.wraps(函数名C)
#     函数体A
#     def B(*args,*kwargs):
#         函数体B
#         C()
#         # return XXX     #2选1
#     return B
#
# @A
# def C():
#     函数体
#     # return          #2选1
# 调用
# XXX = 函数名01（函数名03）          #装饰器中传入函数,并赋值变量
# XXX = ()                           #使用变量调用函数
