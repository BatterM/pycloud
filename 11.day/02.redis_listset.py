import redis

pool=redis.ConnectionPool(host='192.168.132.20',port=6379,db=0)
client=redis.Redis(connection_pool=pool)

#增加\删除
client.delete('number01')
client.delete('number02')
client.lpush('number01',1,2,3,4,5)
result=client.lrange('number01',start=0,end=client.llen('number01'))
print(result)
client.rpush('number02',1,2,3,4,5)
result=client.lrange('number02',start=0,end=-1)
print(result)

client.lpushx('number01','lpushx')
result=client.lrange('number01',start=0,end=client.llen('number01'))
print(result)
client.rpushx('number01','rpushx')
result=client.lrange('number01',start=0,end=client.llen('number01'))
print(result)
client.linsert('number01',where='after',refvalue=3,value=1)

#修改
client.lset('number01',index=2,value=3)
result=client.lrange('number01',start=0,end=client.llen('number01'))
print(result)

#查找(遍历)
result=client.lrange('number01',start=0,end=client.llen('number01'))
print(result)
result=client.lrange('number01',start=0,end=-1)
print(result)
#查找(指定索引)
result=client.lindex('number01',-1)
print(result)

#删除count个同值
client.lrem('number01',count=2,value=3)
result=client.lrange('number01',start=0,end=-1)
print(result)
#删除指定范围外的值
client.ltrim('number01',start=2,end=4)
result=client.lrange('number01',start=0,end=-1)
print(result)
client.delete('number01')
client.delete('number02')


client.sadd('number',1,2,3,4,5,3)  # 集合去重
client.spop('number',count=3)     # 随机删除元素
result=client.smembers('number')
print(result)