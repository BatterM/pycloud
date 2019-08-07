#!/usr/bin/env python3
#
#date:2019-8-5
#author:BatterM
#usage:比较出最大公约数
var01 = int(input("first:"))
var02 = int(input("second:"))
if var01 > var02:
    var03 = var02
else:
    var03 = var01
var05 = 1
for i in range(1, var03+1):
    var04 = 1
    if var01 % i == 0 and var02 % i == 0:
        var04 = i
        if var04 > var05:
            var05 = var04
print("最大公约数是", var05 )

#方法二：递减，两者最小的数和相减的结果的数相减
# var01 = int(input("first:"))
# var02 = int(input("second:"))
# def
# if var01 > var02:
#     var03 = var01-var03
# else
#     var03 = var02 -var03



