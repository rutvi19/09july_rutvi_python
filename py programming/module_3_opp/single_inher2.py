class father:
    bal:int
    car:int

    def getdata(self):
        self.bal=int(input("enter balance:"))
        self.car=int(input("enter car price:"))

class son(father):
    def printdata(self):
        print("balance:",self.bal)
        print("car price:",self.car)

sn=son()
sn.getdata()
sn.printdata()