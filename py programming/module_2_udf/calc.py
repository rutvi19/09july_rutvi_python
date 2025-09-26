def addition(a, b):
    print("The sum is:", a + b)

def subtraction(a, b):
    print("The difference is:", a - b)

def multiplication(a, b):
    print("The product is:", a * b)

def division(a, b):
    print("The quotient is:", a / b)

def modulus(a, b):
    print("The modulus is:", a % b)


print("\n--- Calculator Menu ---")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Exit")
choice = input("Enter your choice (1-6): ")
    
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

if choice == '1':
    addition(a,b)  
elif choice == '2':
    subtraction(a,b)
elif choice == '3':
    multiplication()
elif choice == '4':
    division(a,b)
elif choice == '5':
    modulus(a, b)  
elif choice == '6':
    print("Exiting the calculator. Goodbye!")
else:
    print("Invalid choice. Please try again.")    


