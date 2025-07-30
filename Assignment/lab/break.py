# List of fruits
l1 = ['apple', 'banana', 'mango']

print("Stop loop when 'banana' is found:")
for fruit in l1:
    if fruit == 'banana':
        print("Found 'banana', stopping loop.")
        break 
    print(fruit)
