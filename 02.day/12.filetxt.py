#!/usr/bin/env python3
#
#author:BatterM
#date:2019-8-7
#usage: file.txt

#1/2
import json
with open(file='./txtfile/kingdoms.txt', mode='r+', encoding='utf8') as filetxt:
    content = filetxt.readlines()
a = b = c = d = e = f = g = h = 0
m = 0
for i in range(len(content)):
    m = content[i]
    a = a + m.count("曹操")
    b = b + m.count("刘备")
    c = c + m.count("卧龙")
    d = d + m.count("孙权")
    e = e + m.count("青龙偃月刀")
    f = f + m.count("丈八蛇矛")
    g = g + m.count("赤兔马")
    h = h + m.count("雌雄双股剑")
print("曹操:",a,"刘备:",b,"卧龙:",c,"孙权:",d)
dict01={'曹操:':a,'刘备:':b,"卧龙:":c,"孙权:":d}
dict02={'青龙偃月刀:':e,'丈八蛇矛:':f,"赤兔马:":g,"雌雄双股剑:":h}
print(dict01)
print(dict02)


list01=[]
list02=[]
#人名
for item in dict01.items():
    list01.append(item)
for i in range(len(list01)):
    for j in range(len(list01)-i-1):
        if list01[j][1]<list01[j+1][1]:
            list01[j],list01[j+1]=list01[j+1],list01[j]
dict03=dict(list01)
print(dict03)
#兵器
for item in dict02.items():
    list02.append(item)
for i in range(len(list02)):
    for j in range(len(list02)-i-1):
        if list02[j][1]<list02[j+1][1]:
            list02[j],list02[j+1]=list02[j+1],list02[j]
dict04=dict(list02)
print(dict04)

#将找到的内容写入文件
with open('dict03-04.json', mode='w',encoding='utf8') as json01:
    dict03_s=json.dump(dict03,json01,ensure_ascii=False)
    dict04_s=json.dump(dict04, json01,ensure_ascii=False)
    print(dict03)

#统计access_log访问量前十的ip
with open('./access_log',mode='r',encoding='utf8') as access_ip:
    ips=access_ip.readlines()
ip01,ip02,ip03,ipd01,ipd03=[],[],[],{},{}
for i in range(len(ips)):               #添加所有行中的第一个以空格隔开的元素（ip地址）
    ip01 = ips[i].split(" ")
    ip02.insert(i,ip01[0])
print(ip01)
print(ip02)
ipd02={}.fromkeys(ip02)                 #生成一个只有键的字典
print(ipd02)
for i in range(len(ip02)):              #计算每个ip出现的次数
    n = 0
    for j in range(len(ip02)):
        if i>=j and ip02[i]==ip02[j]:
            n=n+1
    ipd02[ip02[i]]=n                    #将次数加入字典ipd02中
print(ipd02)
for item in ipd02.items():      #将字典ipd02变表ip03
    ip03.append(item)
for i in range(len(ip03)):      #对列表ip03按大小排序
    for j in range(len(ip03)-i-1):
        if ip03[j][1]<ip03[j+1][1]:
            ip03[j],ip03[j+1]=ip03[j+1],ip03[j]
for i in range(11):             #将表ip03前10ip加入字典中
    ipd03[ip03[i][0]]=ip03[i][1]
print("访问量前十的ip及次数:",ipd03)
with open(file='ipd03.json', mode='w',encoding='utf8') as json02:   #将结果存到ipd03.json中
    ipd03_s=json.dump(ipd03,json02,ensure_ascii=False)