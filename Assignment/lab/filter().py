# Filter out even numbers
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter with lambda
odd_num = list(filter(lambda x: x % 2 != 0, num))

print("Original List:", num)
print("Odd Numbers (even removed):", odd_num)
