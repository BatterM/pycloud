#!/usr/bin/env python3
#
#date:2019-8-12
#author:BatterM
#usage:bibao

import functools

def renzheng(out01):
    @functools.wraps(out01)
    def yonghu(users,password):
        if users in u and p[users]== password:
            print('认证成功！！ yes!')
            out01(users,password)
        else:
            print('认证失败！！ no ~，请输入正确的用户名和密码')
    return yonghu

u=['tom','jack','mary','mars']
p={'tom': 123456, 'jack': 654321, 'mary': 321654, 'mars': 123456}

choose=input('输入你要进入的页面：')
user=input('请输入用户名：')
passwd=int(input('请输入密码：'))

@renzheng
def login(user,passwd):
    print('这里就是login页面内部!!!')

@renzheng
def cheak(user,passwd):
    print('这里就是cheak页面内部!!!')

if choose == 'login':
    login(user,passwd)
elif choose == 'cheak':
    cheak(user,passwd)
else:
    print('没有这个页面')
