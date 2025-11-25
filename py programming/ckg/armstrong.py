def armstrong(num):
    total=0
    n=num
    while num>0:
        digit = num % 10
        total += digit ** 3
        num = num // 10
    print(n)
    return total==n
num=int(input("Enter a number: "))
if armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")