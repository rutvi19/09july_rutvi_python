stdata={
    "id":101,
    "name":"rutvi",
    "city":"rajkot",
}
# print(stdata)
# print(stdata['id'])
# print(stdata.get('name'))
# print(stdata.keys())
# print(stdata.values())
# print(len(stdata))

#---------------------#
# for i in stdata:
#     print(i)

# for i in stdata.values():
#     print(i)    

for i in stdata.items():
    print(i)    

for i,j in stdata.items():
    print(i,j)        