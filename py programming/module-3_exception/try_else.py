try:
     a=int(input("enter a number:"))
     b=int(input("enter b number:"))

     print("sum:",A+b)
except Exception as rs: #value error
     print(rs)
     
else: #compluaory run
     print("execution completed")       
     #print("Mul:",a*b)