#!/usr/bin/env python3
#
#date:2019-8-5
#author:BatterM
#usage:反转.....
a = ["this","is","my","house","fuck",]
print(a.__sizeof__())
print("size: {}".format(a.__sizeof__()))
print(a)
for index in range(len(a)):
    if a[index] == "fuck" :
        a[index] = "*"
print(a)
print(len(a))
b=("string","world",1,2,3,4,5,9,10,4.153)
c=[]
for i in range(len(b)):
    if type(b[i])==int or type(b[i])==float:
        c.append(b[i])
print(c)

e="this is my house"
e_split=e.split()
e_split.reverse()
print(e_split)
result=""
# for i in range(len(e_split)):
#     result += e_split[i] + " "
# print(result.rstrip())
n=0
while n<len(e_split):
    result += e_split[n] + " "
    n+=1
print(result.rstrip())

d=["string","tuple","list",(1,2,3,4,5),[6,7,"good"]]
dd=list(d)
d_list=dd[-1]
d_slist=list(dd[3])
dd.pop(-1)
dd.pop(3)
dd.extend(d_slist)
dd.extend(d_list)
print(dd)

#对[23, 12, 15, 11, 29, 24, 57, 21, 80, 99, 45]
# 进行排序, 要求使用for循环（冒泡排序）
f=[23,12,15,11,29,24,57,21,80,99,45]
for i in range(len(f)):
    for j in range(len(f)):
        if f[j]>f[i]:
            f[i],f[j]=f[j],f[i]
print(f)
print(len(f))
