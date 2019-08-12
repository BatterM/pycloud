#!/usr/bin/env python3
#
#date:2019-8-12
#author:BatterM
#usage:bibao


import functools

def out01(out02):
    '''
    我是装饰器本身out01
    :param out02:
    :return: 。。
    '''
    @functools.wraps(out02)
    def in01():
        '''
        我是装饰器内部函数in01
        :return: 。。
        '''
        print('装饰器执行前')
        out02()
        print('装饰器执行后')
    return in01

@out01
def other():
    '''
    表明身份是other
    :return:身份
    '''
    print('我是外人！！')
    return print('我是自己人')
other()
print(other.__name__)
print(help(other))