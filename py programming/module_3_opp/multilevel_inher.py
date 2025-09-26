class rutvi:
    rid:int
    rnm:str

    def r_getdata(self):
        self.rid=int(input("enter rutvi's id:"))
        self.rnm=input("enter rutvi's tech:")   

class priyanshi(rutvi):
    pid:int
    pnm:str

    def p_getdata(self):
        self.pid=int(input("enter priyanshi's id:"))
        self.pnm=input("enter priyanshi's tech:")   
       
class hiral(priyanshi):
    hid:int
    hnm:str

    def h_getdata(self):
        self.hid=int(input("enter hiral's id:"))
        self.hnm=input("enter hiral's tech:")    

class allinfo(hiral):
    def printdata(self):
        print("-----rutvi info-----")
        print("rutvi's id:",self.rid)
        print("rutvi's tech:",self.rnm)

        print("-----priyanshi info-----")
        print("priyanshi's id:",self.pid)
        print("priyanshi's tech:",self.pnm)

        print("-----hiral info-----")
        print("hiral's id:",self.hid)
        print("hiral's tech:",self.hnm)

                
a=allinfo()
a.r_getdata()
a.p_getdata()
a.h_getdata()
a.printdata()