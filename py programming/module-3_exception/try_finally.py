try:
     a=int(input("enter a number:"))
     b=int(input("enter b number:"))

     print("sum:",a+b)
except Exception as rs: #value error
     print(rs)
finally:#compluaory run koi bhi conditions ma run thase
     print("execution completed")       