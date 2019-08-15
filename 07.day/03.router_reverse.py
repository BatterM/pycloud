#!/usr/bin/env python3
#
#date:2019-8-14
#author:BatterM
#usage:router reverse


class webopera:
    vesion='1.0'
    def __init__(self,url,token):
        self.url=url
        self.token=token

    def login(self):
        print('{} / {} login page'.format(self.url,self.token))

    def logout(self):
        print('{} / {} logout page'.format(self.url,self.token))

    @staticmethod
    def welcome(content):
        print('welcome to webopera {}'.format(content))

#反射01
# web = webopera('www.baidu.com','login')
# r=hasattr(web,'login')
# print(r)
#
# re=getattr(web,'login')
# re()
# getattr(web,'welcome')('good')
# web.welcome('no')
#
# setattr(web,'content','successfully')
# print(web.content)
#
# delattr(web,'content')
# print(web.content)

#反射02   hasattr 常常与 getattr 联合使用，找到正确的token
def opera(url01,token01):
    web=webopera(url=url01,token=token01)
    if hasattr(web,token01):
        method=getattr(web,token01)
        if token01=='welcome':
            method('''vesion:@ {}
        please input a right token:
            token:
                1: login
                2: logout
                3: welcome'''.format(webopera.vesion))
        else:
            method()
    else:
        print('error !!   not found {} in webopera '.format(token01))

url02=input('url: ')
token02=input('token: ')
opera(url02,token02)
