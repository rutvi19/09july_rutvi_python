# class stdinfo:                      
#     def userinput(self):
#        self.a=int(input("enter id:"))
#        self.b=input("enter name:")

#     def myinfo(self):
#         print("id:",self.a)
#         print("name:",self.b)
# """self refer to current object of class"""    
# st=stdinfo()
# st.userinput()    
# st.myinfo()

class info:
    def input(self):
        self.a=int(input("enter id:"))
        self.b=input("enter name:")

    def output(self):
        print("id:",self.a)
        print("name:",self.b)

i=info()
i.input()
i.output()
        