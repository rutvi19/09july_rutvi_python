def info():
    print("Welcome to the food bill calculator")
    print("Please enter your details:")
    a=input("enter your name: ")
    b=int(input("enter your mobile number:"))

def foodname():
    print("Please select the food item you want to order:")
    print("1. Pizza")
    print("2. Burger")
    print("3. Pasta")
    print("4. Salad")
    print("5. Sandwich")  
    choice = int(input("Enter the number corresponding to your choice: "))

    if choice == 1:
        print("You have selected Pizza.")
        food_price = 500

    elif choice == 2:
        print("You have selected Burger.")
        food_price = 600

    elif choice == 3:
        print("You have selected Pasta.")
        food_price = 700
        
    elif choice == 4:
        print("You have selected Salad.")
        food_price = 800

    elif choice == 5:
        print("You have selected Sandwich.")  
        food_price = 900
        
          
    else:
        print("Invalid choice. Please try again.")


    print("Calculating your food bill...")
    qty = int(input("Enter the quantity of food item: "))
    total = qty * food_price
    print("the total bill is:",total)

    gst= total * 18 / 100
    print("GST is:", gst)

    final_total = total + gst
    print("The final total bill including GST is:", final_total)
info()    
foodname()


