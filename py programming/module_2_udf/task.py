# module is collection of functions.....
# ------------------
# banking System
# ------------------
# 1.account opening
#   -a/c holder Name
#   -a/c type
#   -a/c number
# 2.account details
#     -min 2000/- deposite
# 3.withdraw
#     -
# 4.statements
#    -a/c holder Name
#    -a/c type
#    -a/c number
#    -main balance

def open_account():
    print("Welcome to the banking system")
    print("Please enter your details:")
    a=input("enter your account holder name: ")

    print("Please enter your account type:")
    print("1. Savings")
    print("2. Current")
    print("3. Fixed Deposit")
    print("4. Recurring Deposit")
    print("5. NRI Account")   

    b=int(input("enter your account type:"))
    
    print("account type is:",9087 2354 234)

    c=input("enter your account details:")
    print("Account details are:", c)

    print("Please enter your initial deposit amount (minimum 2000):")
    d=float(input("enter your initial deposit amount:"))
    if d < 2000:
        print("Minimum deposit amount is 2000. Please try again.")
        return
    
    print("Initial deposit amount is:", d)
    print("Account holder name is:", a)
    print("Account type is:", b)
    print("Account number is:", c)
    print("Your account has been successfully opened with an initial deposit of:", d)
    print("Account opened successfully!")

open_account()