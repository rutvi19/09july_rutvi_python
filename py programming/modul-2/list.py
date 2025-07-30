data=['python','php','java','c#','c++','javascript']
# print(data[0:6])
# print(data[-1])
# print(data[0:3])
# print(data[1:])
# print(data[:3])

# for i in data:
#     print(f"{data.index(i)}-{i}")

print(data)
data[0] = 'python3'

#list methods
data.append("html")
data.insert(2, 'c12')
data.remove('c#')    
data.pop()  # removes the last element
data.clear()  # clears the list   
data.pop(1)
data.sort()
data.reverse()
data_copy = data.copy()     

print(data)

