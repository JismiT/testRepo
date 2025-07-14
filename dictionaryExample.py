myEmp = {"name":"jismi","age":23,"place":"irity","country":"india"}
print(myEmp)

class students:
    def __init__(self, sname, sgrade, smark):
        self.sname  = sname
        self.sgrade= sgrade
        self.smark = smark

    def demoFun(self):
        print("I am ", self.sname)
        print("from grade",self.sgrade)
        print("i have got ", self.smark," mark")

std1 = students("Jismi",12,680)
std2 = students("Neena",12,675)
std3 = students("kiara",12,685)

stsDict = dict({"student1":std1,"student2":std2, "student3":std3})
#print(stsDict.get("student1").demoFun())
print(len(stsDict))
for k in stsDict.keys():
    print(stsDict.get(k).demoFun())

#print(stsDict.keys())