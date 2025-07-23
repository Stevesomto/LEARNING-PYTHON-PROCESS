# LIST are collection of items, stored in a single variable

# How to create a list, Adding, Removing and Accessing Items 

shopping_list = ["Milk", "Egg", "Bread"]
print(shopping_list)

# TO add more items to the list (known as appending)
print("\n---TO add more items to the list--- ")

shopping_list.append("Butter")
print(shopping_list)

print("\n---TO insert an item to the list--- ")
shopping_list.insert(1, "Juice")
print(shopping_list)

# To remove items from the list 
print("\n---TO remove items from the list--- ")

shopping_list.remove("Milk")
print(shopping_list)

# To remove the last item in the list we use the function "pop"
print("\n---TO remove the last item from the list--- ")
shopping_list.pop()
print(shopping_list)


