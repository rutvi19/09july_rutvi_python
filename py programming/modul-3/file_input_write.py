# x=open("student.txt","a")
# a=int(input("how many student data you want to add:"))
# for i in range(a):
#     id=int(input("enter student id:"))
#     name=input("enter student name:")
#     x.write(f"id:{id}\nname:{name}\n")
#     x.write("\n------\n")  

x=open("table.txt","a")
n=int(input("which table do you want:"))
for i in range(1,11):
    x.write(f"{n}X{i}={n*i}\n")
    x.write("\n") 




