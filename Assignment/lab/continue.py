# List of fruits
l1 = ['apple', 'banana', 'mango']

print("Fruits except 'banana':")
for fruit in l1:
    if fruit == 'banana':
        continue  # Skip 'banana'
    print(fruit)
