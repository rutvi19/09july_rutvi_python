from functools import reduce

# List of numbers
num = [1, 2, 3, 4, 5]

# Using reduce to calculate product
product = reduce(lambda x, y: x * y, num)

print("Numbers:", num)
print("Product of numbers:", product)
