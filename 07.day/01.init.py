#!/usr/bin/env python3
#
#date:2019-8-14
#author:BatterM
#usage:init


class Ball:         #基类/父类
    pi=3.1415926
    def __init__(self,redius):
        self.redius=redius

    def getarea(self):
        area=4*self.pi*self.redius**2
        return area

    def getvolume(self):
        volume=(4*self.pi*self.redius**3)/3
        return volume

ironBall=Ball(0.05)
print(ironBall.getarea())

class rule(Ball):       #派生类/子类
    def __init__(self,redius,color):
        super(rule,self).__init__(redius)
        self.color=color

baskeBall=rule(0.10,'yellow')
print(baskeBall.getvolume())

