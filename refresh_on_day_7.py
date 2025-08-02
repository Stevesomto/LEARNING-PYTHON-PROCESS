<<<<<<< HEAD

import time
roban_shop_list = []

# if len (roban_shop_list) > 5:
#     print("\nYour shopping list is filled\n")
# else:
#      print("{show_menu()}") 


def show_menu():
    print("\n---- LIST OF SHOOPING LIST")
    print("1. View List of shopping list")
    print("2. Add an item to list")
    print("3. Remove an item from list")
    print("4. Clear the list")
    print("5. Exit ")
    

while True:
    show_menu()
    choice = int(input("Enter your choice number between 1-5:  "))
    time.sleep(1.5)
        
    if choice == 1:
        print("\n---- The shopping list---")
        if not roban_shop_list:
            print("\n Shopping list is empty\n")
        else: 
            for index, item in enumerate (roban_shop_list):
                print(f"{index + 1}. {item}")
    
    elif choice == 2:
        item = input("\nEnter the item you want to add: \n")
        roban_shop_list.append(item)
        print(f"\n{item} has been added to the shopping list\n")
        
          
        
    
    elif choice == 3:
        item = input("Enter the item you want to remove:  ")
        if item in roban_shop_list:
            roban_shop_list.remove(item)
            print(f"\n{item} has been removed from the shopping list\n")
        else:
            print(f"\n{item} not found in the shopping list.\n")
    
    
    elif choice == 4:
        roban_shop_list.clear()
        print("\nShopping list has been cleared\n")
    
    elif choice == 5:
        print("\nThank you for shopping with us, See you next time!\n")
        break
    
    else: 
        ("\nYour input is invalid\n")
        break
        
    
        
=======

import time
roban_shop_list = []

# if len (roban_shop_list) > 5:
#     print("\nYour shopping list is filled\n")
# else:
#      print("{show_menu()}") 


def show_menu():
    print("\n---- LIST OF SHOOPING LIST")
    print("1. View List of shopping list")
    print("2. Add an item to list")
    print("3. Remove an item from list")
    print("4. Clear the list")
    print("5. Exit ")
    

while True:
    show_menu()
    choice = int(input("Enter your choice number between 1-5:  "))
    time.sleep(1.5)
        
    if choice == 1:
        print("\n---- The shopping list---")
        if not roban_shop_list:
            print("\n Shopping list is empty\n")
        else: 
            for index, item in enumerate (roban_shop_list):
                print(f"{index + 1}. {item}")
    
    elif choice == 2:
        item = input("\nEnter the item you want to add: \n")
        roban_shop_list.append(item)
        print(f"\n{item} has been added to the shopping list\n")
        
          
        
    
    elif choice == 3:
        item = input("Enter the item you want to remove:  ")
        if item in roban_shop_list:
            roban_shop_list.remove(item)
            print(f"\n{item} has been removed from the shopping list\n")
        else:
            print(f"\n{item} not found in the shopping list.\n")
    
    
    elif choice == 4:
        roban_shop_list.clear()
        print("\nShopping list has been cleared\n")
    
    elif choice == 5:
        print("\nThank you for shopping with us, See you next time!\n")
        break
    
    else: 
        ("\nYour input is invalid\n")
        break
        
    
        
>>>>>>> 5776d637b558ed6ad1589ad51c196b7c0d84fcfe
    