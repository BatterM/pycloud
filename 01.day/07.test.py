#!/usr/bin/env python3
#
#date:2019-8-5
#author:BatterM
#usage:* 1~10

# j = 1
# for i in range(1, 11):
#     j = j*i
# print("sum is :", j)

def sum(number,i):
    if i<=10:
        number=number*i
    else:
        print(number)
        return number
    sum(number, i + 1)
print(sum(1,1))

