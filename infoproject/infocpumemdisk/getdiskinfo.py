import psutil
def disk():
    getdisk=psutil.disk_usage('/')
    return getdisk.percent