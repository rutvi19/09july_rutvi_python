studentdata={}
a=int(input("how many student you want to enter: "))

for i in range(a):
     key=input("enter key:")
     value=input("enter value:")
     studentdata[key]=value
print(studentdata)