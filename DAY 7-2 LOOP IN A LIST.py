
shopping_list = ["Yam", "Egg", "Tea", "Bread"]
print(shopping_list)

for items in shopping_list:
    print(f" - {items}")
    
print("\n--- For numbering ---")

for index, items in enumerate(shopping_list):
    print(f"{index + 1}. {items}")
    