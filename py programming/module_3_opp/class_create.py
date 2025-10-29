class studinfo:
    stid=12
    stnm="rutvi"

    def myfunc(self):
        print("this is my function")

#object of class
st=studinfo()                 
"""<-attribute reference"""

print(st.stid)
print(st.stnm)         
"""<-instatiatiion"""

st.myfunc()