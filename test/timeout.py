import time

cishu=0
def setInerval(func):
    def test(secend):
        time.sleep(secend)
        global cishu
        cishu+=1
        func(secend)
        return print('sleep!! 第{}次刷新~'.format(cishu))
    return test

@setInerval
def out(say):
    print('每隔{}秒刷新一次'.format(say))

#a=setInerval(out)
secend=int(input('你想几秒刷新一次:'))
n=int(input('你想刷新几次:'))
while True:
    if cishu >= n:
        print('刷新结束~~~~~~~~~~~')
        break
    out(secend)
