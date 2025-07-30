# Generator function to generate first 10 even numbers
def generate_even_numbers():
    number = 0
    for _ in range(10):
        yield number
        number += 2

# Using the generator
print("First 10 even numbers:")
for even in generate_even_numbers():
    print(even)
