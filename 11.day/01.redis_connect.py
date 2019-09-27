import redis

#string
# pool=redis.ConnectionPool(host='192.168.132.20',port=6379,db=0)
# client=redis.Redis(connection_pool=pool)
#
# client.set(name='pycloud',value=17)  #修改和添加
# result=str(client.get('pycloud'),'utf8')  #查值
# print(result)
#
# client.mset({'user':'batterm','passwd':'123456'})    #多值添加
# result=client.mget('user','pycloud')  #多值查询
# print(result)
#
# client.delete('pycloud')
# result=client.get('pycloud')
# # print(str(result,'utf8'))  #删除的name是没有类型了，所以不能再进行类型转换
# print(result)

#hash
pool=redis.ConnectionPool(host='192.168.132.20',port=6379,db=0)
client=redis.Redis(connection_pool=pool)
client.hset('pycloud','user','batterm')
result=str(client.hget(name='pycloud',key='user'),'utf8')
print(result)

client.hmset('pycloud',{'id':12,'ip':'192.168.132.20','date':'2019/8/23'})
result=client.hmget('pycloud','id','user','date','ip')
print(result)


client.hdel('pycloud','date')
result=client.hget('pycloud','date')
print(result)
result=client.hgetall('pycloud')
print(result)
keys=client.hkeys('pycloud')
print(keys)
values=client.hvals('pycloud')
print(values)

if client.hexists('pycloud','date'):
    print(True)
else:
    print(False)