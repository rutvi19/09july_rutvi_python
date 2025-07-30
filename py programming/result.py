a=int(input("enter marks of first subject:"))
b=int(input("enter marks of second subject:"))
c=int(input("enter marks of third subject:"))
d=int(input("enter marks of fourth subject:"))

if a>=40 and b>=40 and c>=40 and d>=40:


    total = a + b + c + d
    print("Total marks:", total)

    avg = total / 4 
    print("Percentage:", avg)

    if avg>70:
        print("distinction")
    elif avg>60:
        print("first class")
    elif avg>50:
        print("second class")
    elif avg>40:
        print("third class")    
else:
    print("fail")

    


