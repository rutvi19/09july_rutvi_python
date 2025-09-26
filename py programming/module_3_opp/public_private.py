# class studinfo:
#     #public
#     stid=101
#     stname="John"

#     def getdata(self):#public
#         print("this is getdata")

# st=studinfo()
# print("id:",st.stid)
# print("name:",st.stname)
# st.getdata()

class studinfo:
    #private
    __stid=101
    __stname="John"

    def __getdata(self): #private
        print("this is getdata")
        print("id:",st.__stid)
        print("name:",st.__stname)

    def getdata(self):
        self.__getdata()    

st=studinfo()
st.getdata()
