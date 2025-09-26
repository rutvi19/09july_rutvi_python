import re

username=input("Enter an Username:")

x=re.findall('[A-Z]+[a-z]+[0-9]',username)

if x:
    print("Valid Username!")
else:
    print("Error!Invalid Username...")