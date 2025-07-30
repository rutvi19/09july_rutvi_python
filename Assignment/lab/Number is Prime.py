# Prime number check

number = int(input("Enter a number: "))

if number > 1:
    is_prime = True
    for i in range(2, number):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(number, "is a Prime number.")
    else:
        print(number, "is NOT a Prime number.")
else:
    print("Prime numbers are greater than 1.")
