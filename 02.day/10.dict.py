#!/usr/bin/env python3
#
#author:BatterM
#date:2019-8-7
#usage: dict

dict01 = {'name': 'bavduer', 'age': 18, 'gender': 'male'}
dict02 = dict({'name': 'bavduer', 'age': 18, 'gender': 'male'})
dict03 = dict([('name', 'bavduer'), ('age', 18), ('gender', 'male')])
dict04 = dict(name='bavduer', age=18, gender='male')
print(dict01)
if dict01 == dict02 == dict03 == dict04:
  print("True")
else:
  print("False")
import json
test_dict = {'symbol': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}
print(test_dict)
print(type(test_dict))
json_str = json.dumps(test_dict)
print(json_str)
print(type(json_str))

ips = {'a192.168.132.10': 815, 'b36.100.110.50': 345, 'c1.1.1.1': 476, 'd8.8.8.8': 79}
iplist=[]
for i in ips.items():
    iplist.append(i)
iplist.sort(key=lambda x:x[1])
iplist.reverse()
iplist.sort(key=lambda x:x[0])
print(iplist)
iplist01=dict(iplist)
print(iplist01)
# for i in range(len(iplist)):
#     for j in range(len(iplist)-i-1):
#         if iplist[j][1] > iplist[j+1][1]:
#             iplist[j],iplist[j+1]=iplist[j+1],iplist[j]
# iplist02=dict(iplist)
# print(iplist)
# print(iplist02)

