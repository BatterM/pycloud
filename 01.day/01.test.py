#!/usr/bin/env python3
#
#date:2019-8-5
#author:BatterM
#usage:find sushu


for i in range(1,101):
    if i < 3:
        print(i)
    else:
        for j in range(2,i+1):
            if i % j == 0 and j < i:
                break
            elif i % j != 0:
                continue
            print(i)
