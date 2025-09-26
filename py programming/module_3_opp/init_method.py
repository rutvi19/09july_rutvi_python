#init=Initialization_method call automatically when object is created. backgound process

class studinfo:
    def __init__(self):#constructor
       print("this is init method")

    def getdata(self):
        print("this is getdata method")
st=studinfo()
st.getdata()