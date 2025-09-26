import re

mystr="This is Python!445684564"

#x=re.findall("\w",mystr)
#x=re.findall("\W",mystr)
#x=re.findall("\s",mystr)
#x=re.findall("\S",mystr)
#x=re.findall("\d",mystr)
#x=re.findall("\D",mystr)
#x=re.findall(r"\bThis",mystr)
#x=re.findall("\B564",mystr)
#x=re.findall("\AThis",mystr)
x=re.findall("564\Z",mystr)
print(x)