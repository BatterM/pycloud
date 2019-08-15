class Detail:
    def show(self,scale):
        print('D')
        print("There are {}s employes working in {}s.".format(scale,self.count_person))

class Scale:
    def check(self):
        print('S')
        if self.count_person > 500:                          # 判断公司人数是否大于500人
            return "%s is a super company.\n" %self.name
        else:
            return "%s is a small company.\n" %self.name

class Company(Scale,Detail):
    def __init__(self,name,count):                         # 构造函数给数据赋值
        print('C')
        self.name = name
        self.count_person = count

if __name__=="__main__":
    MY_company = Company("Google",75000)
    company_scale = MY_company.check()
    MY_company.show(company_scale)
