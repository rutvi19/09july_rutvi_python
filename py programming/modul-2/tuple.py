city=[]
a=int(input("how many city you want to enter: "))
for i in range(a):
    b=input("enter the name of the city:")
    city.append(b)
print(tuple(city))