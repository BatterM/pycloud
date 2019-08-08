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
lgunba=[6,7,8,-1,0]

def acc(number):
    if type(number) not in {str,int}:
        response="please check your input~!"
    def add(number):
        result=0
        for n in range(number+1):
            result+=n
        return result
    return add(number)
print(acc(4))
