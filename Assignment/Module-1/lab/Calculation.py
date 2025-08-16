# Calculate grade based on percentage

p = float(input("Enter your percentage: "))

if p >= 90:
    print("Grade: A+")
elif p >= 80:
    print("Grade: A")
elif p >= 70:
    print("Grade: B")
elif p >= 60:
    print("Grade: C")
elif p >= 50:
    print("Grade: D")
else:
    print("Grade: Fail")
