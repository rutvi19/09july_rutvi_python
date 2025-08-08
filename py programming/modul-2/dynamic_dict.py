# stdata={}
# a=int(input("how many pair you want to enter: "))

# for i in range(a):
#     key=input("enter key:")
#     value=input("enter value:")
#     stdata[key]=value
# print(stdata)

stdata={}
keys=["id", "name", "city"]
for i in keys:
    value=input(f"enter value for {i}:")
    stdata[i]=value
print(stdata)