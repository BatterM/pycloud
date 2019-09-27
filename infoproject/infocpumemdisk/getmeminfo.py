import psutil
def memory():
    getmem=psutil.virtual_memory()
    return getmem.percent