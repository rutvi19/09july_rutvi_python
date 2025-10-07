class studinfo:

    def getdata(self,id):
        print("ID:",id)

    def getdata(self,name):
        print("Name:",name)

st=studinfo()
st.getdata(101)
st.getdata("John")

# it will print only the last method because python does not support method overloading

# class info:
    
#     def getdata(self,id):
#         print("ID:",id)
#     def getdata(self,name):
#         print("Name:",name)

# st=info()
# st.getdata(101)
# st.getdata("john")

# same method also class same but different arguments.
