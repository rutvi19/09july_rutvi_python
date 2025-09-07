#store multiple students infromation:
#timestamp(current date and time)
#id(must be random in 4 digit)
#name
#subject
#city


import datetime
import random
ts=datetime.datetime.now()
f=open("stud.txt","a")
n=int(input("enter number of students:"))
for i in range(n):
    x=random.randint(1000,9999)
    print(x)
    name=input("enter name:")
    subject=input("enter subject:")
    city=input("enter city:")
    f.write(f"{id}\n,{name}\n,{subject}\n,{city}\n,{ts}\n")
f.close()