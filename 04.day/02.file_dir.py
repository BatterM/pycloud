#!/usr/bin/env python3
#
#date:2019-8-8
#author:BatterM
#usage:sum file and dir 统计某路径下有多少各文件和目录
import os
dirC,fileC=0,0
def content(path):
    if os.path.isdir(path):
        for file in os.listdir(path):
            fileA=os.path.join(path,file)
            if os.path.isdir(fileA):
                global dirC
                dirC +=1
                content(fileA)
            else:
                global fileC
                fileC +=1
    else:
        print('please use a true dir')
    return dirC,fileC
dirB,fileB=content('E:/pycloud/04.day/03.test.py')
print("dirctory {},file {}".format(dirB,fileB))
