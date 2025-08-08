# stdata=[{"id": 101, "name": "rutvi", "city": "rajkot"},
#           {"id": 102, "name": "john", "city": "mumbai"},
#             {"id": 103, "name": "doe", "city": "pune"}]
# print(stdata)

# for i in stdata:
#     print(i)

# for i in stdata:
#     print(i["id"]) 

# stdata={
#     "st1":{"id":101, "name":"rutvi"},
#     "st2":{"id":102, "name":"john"},
#     "st3":{"id":103, "name":"doe"}
# } 
# print(stdata)
# print(stdata["st1"])
# print(stdata["st1"]["id"])  

stdata = {}
a = int(input("how many dict you want to enter: "))

for i in range(a):
    key = input(f"Enter key for dict {i+1}: ")
    id = input("Enter id: ")
    name = input("Enter name: ")
    city = input("Enter city: ")
    stdata[key] = {"id": id, "name": name, "city": city}
print(stdata)

# for i in stdata:
#     print(i, ":", stdata[i])
# print(stdata)    


    