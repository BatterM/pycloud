#!/usr/bin/env python3
#
#date:2019-8-8
#author:BatterM
#usage:访问最多的资源

import json
#7
source={}
with open(file='../02.day/access_log', mode='r', encoding='utf8') as log:
    for i in log.readlines():
        if i.split()[6] not in source.keys():
            source.setdefault(i.split()[6], 1)
        else:
            source[i.split()[6]] += 1
    source = sorted(source.items(), key=lambda x: x[1], reverse=True)
head10 = dict(source[0:10])
print(head10)
#1/2/3/4
character01,character02= ('曹操', '刘备', '卧龙', '孙权'),('青龙偃月刀','丈八蛇矛',"赤兔马","雌雄双股剑")
display01,display02={},{}
with open(file='../02.day/txtfile/kingdoms.txt', mode='r', encoding='utf8') as log:
    content=log.read()
    text = content.replace(" ","").replace("\n","")
    for char in character01:
        display01.setdefault(char,text.count(char))
    display01=dict(sorted(display01.items(),key=lambda x:x[1],reverse=True))
    print(display01)
    for char in character02:
        display02.setdefault(char,text.count(char))
    display02 =dict(sorted(display02.items(), key=lambda x: x[1], reverse=True))
    print(display02)

with open(file='peoplename.json', mode='w', encoding='utf8') as log:
    json.dump(display01,log,ensure_ascii=False)
    log.write('\n')
    json.dump(display02,log,ensure_ascii=False)


