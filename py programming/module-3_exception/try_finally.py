try:
     a=int(input("enter a number:"))
     b=int(input("enter b number:"))

     print("sum:",+A+b)

except Exception as rs: #value error
     print(rs)

finally:#complusory run koi bhi conditions ma run thase
     print("execution completed")       