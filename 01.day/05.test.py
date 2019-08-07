#!/usr/bin/env python3
#
#date:2019-8-5
#author:BatterM
#usage:比较出最小公倍数

var01 = int(input("first:"))
var02 = int(input("second:"))
if var01 > var02:
    var03 = var01
else:
    var03 = var02
var04 = var01*var02
for i in range(1,(var01*var02)+1):
    if i % var01 == 0 and i % var02 == 0:
        var04 = i
        break
print("最小公倍数是",var04)