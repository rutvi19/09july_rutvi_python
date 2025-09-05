# x=open('temp.txt',"w")

# x.write("Good Evening,hello rutvi")
# f = open("temp.txt", "r+")
# print("Before writing:", f.read())
# f.seek(0)   # Move cursor to start
# f.write("Replaced text")
# f.close()

with open("myfile.txt", "w") as f:
    content = f.write()   # read entire file

# Print file content on the console
print("File contents:\n")
print(content)
