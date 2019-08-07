#!/usr/bin/env python3
#
#date:2019-8-5
#author:BatterM
#usage:einstein ladder

for i in range(201):
    if i%2==1 and i%3==2 and i%5==4 and i%6==5 and i%7==0:
        print(i)
