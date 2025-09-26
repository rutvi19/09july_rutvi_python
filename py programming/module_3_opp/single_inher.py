class studinfo:

    def getdata(self):
        self.id=int(input("enter id:"))
        self.name=input("enter name:")

class result(studinfo):

    def printdata(self):
        print("id:",self.id)
        print("name:",self.name)

rs=result()
rs.getdata()
rs.printdata()