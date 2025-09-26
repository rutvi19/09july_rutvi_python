# 1.account opening
#     -a/c number
#     -a/c name
#     -a/c type
# 2.deposit
#   -min.2000/- rs.
# 3.withdraw
# 4.statement
#     -a/c number
#     -a/c name
#     -a/c type
#     -total balance
class bank:
    def open_account(self):
        print("Welcome to the banking system")
        print("Please enter your details:")
        self.a=input("enter your account holder name: ")
        print("Account holder name is:", self.a)

        print("Please enter your account type:")
        print("1. Savings")
        print("2. Current")
        print("3. Fixed Deposit")
        print("4. Recurring Deposit")
        print("5. NRI Account")   

        self.b=int(input("enter your account type:"))
        print("account type is:", self.b)
       
class deposits(bank):
    def deposits(self):
        self.c=input("enter your account deposits:")
        print("Account deposits are:", self.c)

        print("Please enter your initial deposit amount (minimum 2000):")
        self.d=float(input("enter your initial deposit amount:"))
        if self.d < 2000:
            print("Minimum deposit amount is 2000. Please try again.")
            return
        print("Initial deposit amount is:", self.d)

class withdraw(deposits):
    def withdraw(self):
        self.e = float(input("Enter your withdrawal amount: "))
        if self.e > self.d:
            print("Insufficient balance. Please try again.")
            return
        else:
            self.d = self.d - self.e
            print("Withdrawal successful. Remaining balance:", self.d)
  

class statement(withdraw):
    def print_statement(self):   
        print("-----Account Statement-----")          
        print("Initial deposit amount is:", self.d)

        print("----After Withdraw-----")
        print("Account holder name is:", self.a)
        print("Account type is:", self.b)
        print("Account number is:", self.c)
        print("Your account has been successfully opened with an initial deposit of:", self.d)
        print("Your remaining balance after withdrawal is:", self.e)
        print("Account opened successfully!")    

st=statement()
st.open_account()
st.deposits()
st.withdraw()
st.print_statement()        