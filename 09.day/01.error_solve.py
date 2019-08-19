#!/usr/bin/env python3
#
#date:2019-8-16
#author:BatterM
#usage:error


try:    #开始测试代码
    print(1/0)
    print('the show must go on!!')
except Exception as error:       #提取错误
    print('ERROR: {}'.format(error))
finally:              #停止
    pass

print('the show must go on!!!')
