#!/usr/bin/env python3
#
#date:2019-8-19
#author:BatterM
#usage:re   split_findall_


import re
#1   split通过自定义的分隔符，将文件内容分割
date='Last login: Thu Mar  2 10:04:52 2019 from 39.100.110.135'
opare01=re.split('[:.]',date)
print(opare01)

#2   findall（正则表达规则，文件内容）   输出的是列表套元组
revar='(([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]).([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]).' \
      '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]).([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-4])$)'
opare02=re.findall(revar,date)
opare02.append(opare02[0][0])
opare02.pop(0)
print(opare02)

#3   compile定义查询规则，findall通过前者规则查询指定内容
reopare03=re.compile(revar)
opare03=reopare03.findall(date)
opare03.append(opare03[0][0])
opare03.pop(0)
print(opare03)

