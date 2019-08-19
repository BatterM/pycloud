#log analysis
#data:2019-8-19

def ipsAnalysis(path):
    ips={}
    with open(file=path,mode='r',encoding='utf8') as log:
        for lines in log.readlines():
            ips.setdefault(lines.split()[0],0)
            ips[lines.split()[0]] +=1
    return ips
def codeAnalysis(path):
    code={}
    with open(file=path,mode='r',encoding='utf8') as log:
        for lines in log.readlines():
            if lines.split()[8] in ('200','404','502','499','400','301','302','304','503','504'):
                code.setdefault(lines.split()[8],0)
                code[lines.split()[8]] +=1
    return code

def sourceAnalysis(path):
    source={}
    with open(file=path,mode='r',encoding='utf8') as log:
        for lines in log.readlines():
            source.setdefault(lines.split()[6],0)
            source[lines.split()[6]] +=1
    return source