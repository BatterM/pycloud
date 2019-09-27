import psutil
def cpu():
    getcpu=psutil.cpu_times_percent(interval=1)
    return getcpu.user+getcpu.system