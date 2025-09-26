import re

mystr="This is Python!"

x=re.search("this",mystr)
print(x)

if x:
    print("Match Done!")
else:
    print("Error!") 