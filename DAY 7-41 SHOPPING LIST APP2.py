<<<<<<< HEAD
# SHOPPING LIST APP

# Step 1: Initialize an empty shopping list
shopping_list = []

# Step 2: Define the main menu 
import time

def show_menu():
    print("\n--- SHOPPING LIST MENU---")
    print("1. View the shopping list")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. Clear list")
    print("5. Exit")
    
# Step 3: Main Program Loop

while True:
    time.sleep(3)   # number of time (in seconds) it will take to display options
    show_menu()
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        print("\n--- Shopping List---")
        if not shopping_list:
           print("Your Shopping list is empty")
        else:
           for index, item in enumerate(shopping_list):
            print (f"{index + 1}. {item}")
            
            
    elif choice == "2":
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"{item}  has been added to the shopping list." )
        
        
    
    elif choice == "3":
        item = input("Emter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item}  has been removed to the shopping list." )
        else: 
            print(f"{item} is not in the shopping list")
    
    
    elif choice == "4":
        shopping_list.clear()
        print("The shopping list has been cleared")
    
        
    elif choice == "5":
        print("\n Thank you for shopping with us, Goodbye!!\n")
        break
    
    
    else:
        print("Invalid choice, Please check well and try again. Thank You!")
        
=======
# SHOPPING LIST APP

# Step 1: Initialize an empty shopping list
shopping_list = []

# Step 2: Define the main menu 
import time

def show_menu():
    print("\n--- SHOPPING LIST MENU---")
    print("1. View the shopping list")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. Clear list")
    print("5. Exit")
    
# Step 3: Main Program Loop

while True:
    time.sleep(3)   # number of time (in seconds) it will take to display options
    show_menu()
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        print("\n--- Shopping List---")
        if not shopping_list:
           print("Your Shopping list is empty")
        else:
           for index, item in enumerate(shopping_list):
            print (f"{index + 1}. {item}")
            
            
    elif choice == "2":
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"{item}  has been added to the shopping list." )
        
        
    
    elif choice == "3":
        item = input("Emter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item}  has been removed to the shopping list." )
        else: 
            print(f"{item} is not in the shopping list")
    
    
    elif choice == "4":
        shopping_list.clear()
        print("The shopping list has been cleared")
    
        
    elif choice == "5":
        print("\n Thank you for shopping with us, Goodbye!!\n")
        break
    
    
    else:
        print("Invalid choice, Please check well and try again. Thank You!")
        
>>>>>>> 5776d637b558ed6ad1589ad51c196b7c0d84fcfe
        