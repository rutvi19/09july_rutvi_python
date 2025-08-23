# Initial list
my_list = [10, 20, 30, 40, 50]

print("Original List:", my_list)

# Using pop() → removes element at a given index (default: last element)
popped_element = my_list.pop()   # removes last element
print("After pop():", my_list)

popped_element = my_list.pop(1)  # removes element at index 1
print("After pop(1):", my_list)
my_list.remove(40)   # removes the value 40
print("After remove(40):", my_list)
