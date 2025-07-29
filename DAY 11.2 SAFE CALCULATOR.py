# BUILD A CALCULATOR THAT ACCEPTS TWO NUMBERS FROM THE USER 
# SAFE CALCULATOR

# Define Calculator Functions

def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError ("Cannot divide by zero")
    return x / y

# Display the menu

def show_menu():
    print("\n---- Safe Calculator Menu---")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

# Main Program

while True:
    show_menu()
    choice = int(input("Enter your choice of number for the menu (1-5): "))
    
    if choice == 5:
        print("Exit the calculor, Goodbye")
    break

# I STOPED HERE BECUASE I AM NOT UNDERSTANDING IT
    