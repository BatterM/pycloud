#date:2018-8-26

# lista=[i for i in range(10)]
# print(lista)
#
# listb=(i for i in range(10))
# print(listb)
#
# for element in listb:
#     print(element)

class IterCheck:
    def __init__(self,param):
        self.param=param

    def check(self):
        try:
            iter(self.param)
            return True
        except Exception as error:
            return False,error
        finally:
            print('OK!')

listc=1
check=IterCheck(listc)
result=check.check()
print(result)