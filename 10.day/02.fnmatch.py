#!/usr/bin/env python3
#
#date:2019-8-19
#author:BatterM
#usage:fnmatch and os.walk


import fnmatch
import os
#1
# for name in os.listdir('E:/pycloud/02.day'):
#     if fnmatch.fnmatch(name,'*.py'):
#         print(name)


#2
# files=('*.day','*.py')
# for name in os.listdir('E:/pycloud'):
#     for file in files:
#         if fnmatch.fnmatch(name,file):
#             print(name)


#3 walk函数可以遍历当前目录及其子目录下所有的文件
files=('*.day','*.py')
dirfile=[]
for dirpath,dirname,filename in os.walk('e:/pycloud/02.day'):
    print('''
    dirpathname: {}
    directory: {}
    filename: {}'''.format(dirpath,len(dirname),len(filename)))
    for name in files:
        for file in fnmatch.filter(filename,name):
            dirfile.append(os.path.join(dirpath,file))
print(dirfile)