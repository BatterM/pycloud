#!/usr/bin/env python3
#
#date:2019-8-8
#author:BatterM
#usage:def


def fun(a,b=8):
    '''
    sum
    :param a: int
    :param b: int
    :return: a+b
    '''
    s=a+b
    return s
fu=fun(2)
print(fun(50),fu)

def acc(number):
    if type(number) not in {int}:
        response="please check your input~!"
    def add(number):
        result=0
        for n in range(number+1):
            result+=n
        return result
    return add(number)
print(acc(99))

#将列表中的int数，自身从0开始叠加
list01 = [1, 2, 3, 4, "string",5,100]
def summ(line):
    line01 = []
    for i in line:
        if type(i) not in {int}:
            continue
        result=0
        for j in range(i+1):
            result +=j
        line01.append(result)
    return line01
print(summ(list01))



