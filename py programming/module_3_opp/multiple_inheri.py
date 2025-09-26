class rutvi:
    rid:int
    rnm:str

    def r_getdata(self):
        self.rid=int(input("enter id:"))
        self.rnm=input("enter name:")   

class priyanshi:
    pid:int
    pnm:str 

    def p_getdata(self):
        self.pid=int(input("enter id:"))
        self.pnm=input("enter name:")   
       
class hiral:
    hid:int
    hnm:str

    def h_getdata(self):
        self.hid=int(input("enter id:"))
        self.hnm=input("enter name:")    

class allinfo(priyanshi,hiral,rutvi):
    def printdata(self):
        print("-----priyanshi info-----")
        print("priyanshi's id:",self.sid)
        print("priyanshi's name:",self.snm)

        print("-----hiral info-----")
        print("hiral's id:",self.hid)
        print("hiral's name:",self.hnm)

        print("-----rutvi info-----")
        print("rutvi's id:",self.rid)
        print("rutvi's name:",self.rnm)        
a=allinfo()
a.s_getdata()
a.h_getdata()
a.r_getdata()
a.printdata()