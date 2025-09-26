import re

# Simple Email Validation
username = input("Enter your email: ")

# Regex for email (letters, numbers, ., _, % allowed before @)
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.fullmatch(pattern, username):
    print("Valid email")
else:
    print("Invalid email")
#abbc10@gmail.com