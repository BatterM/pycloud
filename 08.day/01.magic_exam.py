#!/usr/bin/env python3
#
#date:2019-8-15
#author:BatterM
#usage:magic


#在类中使用以下方法：
#__init__ 创建实例时自动运行定义属性  __del__ 删除方法时自动运行
# __str__  print()返回操作时自动运行 __new__ 实例化时将实例自动分配到同一地址空间
#__call__ 使得实例可直接像函数直接调用  XXX()

#面向对象交互：两个对象调用类的方法可以改变对方的属性值
import random
class Renwu:
    Buff=random.randint(20,100)
    # def __new__(cls, *args, **kwargs):
    #     print('new')
    #     if not hasattr(cls,'instence'):
    #         cls.instence=super().__new__(cls)
    #     return cls.instence

    def __init__(self,blood,attack,energy,cost):
        self.blood=blood
        self.attack=attack
        self.energy=energy
        self.cost=cost

    def attackOprea(self,instence):
        instence.blood -= self.attack + self.Buff
        self.energy -=self.cost

    def zt(self):
        return {
            'blood:' : self.blood,
            'energy:' : self.energy
        }

rz=Renwu(750,100,320,60)
print(id(rz))
gl=Renwu(1000,60,0,0)
print(id(gl))
for i in range(100):
    if i % 2==0:
        if rz.blood<=0:
            print('rz的血量不足，gl赢了！！')
            break
        elif rz.energy<=0:
            print('rz的能量不足，gl赢了！！')
            break
        rz.attackOprea(gl)
        print('rz attack gl :')
    else:
        if gl.blood<=0:
            print('gl的血量不足，rz赢了！！')
            break
        gl.attackOprea(rz)
        print('gl zttack rz :')
    print('rz info: {}'.format(rz.zt()))
    print('gl info: {}'.format(gl.zt()))