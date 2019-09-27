
#[ip访问情况(pv/uv/IP及次数)/状态码/资源访问情况]
class log:
    def __init__(self,path):
        self.path=path

    def getip(self):
        ips={}
        uv=pv=0
        with open(file=self.path,mode='r',encoding='utf8') as iplog:
            for lines in iplog.readlines():
                pv+=1
                if lines.split()[0] not in ips.keys():
                    ips.setdefault(lines.split()[0],0)
                    uv+=1
                else:
                    ips[lines.split()[0]]+=1
            ips=sorted(ips.items(),key=lambda x:x[1],reverse=True)
        return ips,pv,uv

    def getcode(self):
        char,ips={},{}
        code=('200','201','202','203','300','301','302','303',
              '304','400','401','402','403','404','500','501',
              '502','503','504')
        with open(file=self.path,mode='r',encoding='utf8') as iplog:
            for lines in iplog.readlines():
                ips.setdefault(lines.split()[8],0)
                ips[lines.split()[8]]+=1
            for c in ips.keys():
                if c in code:
                    char.setdefault(c,ips.get(c))
        return char

    def getsource(self):
        source = {}
        with open(file=self.path, mode='r', encoding='utf8') as iplog:
            for lines in iplog.readlines():
                source.setdefault(lines.split()[6], 0)
                source[lines.split()[6]]+=1
        return source

ip=log('e:\\pycloud\\02.day\\access_log')
ips,pv,uv=ip.getip()
char=ip.getcode()
source=ip.getsource()
print('IP.count:{}'.format(ips))
print('PV:{} , UV:{}'.format(pv,uv))
print(char)
print(source)