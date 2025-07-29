# SETS ARE MUTTABLE IN PYTHON BUT THEY DO NOT ACCEPT DUPLICATES

my_set = {1, 2, 3}
print(my_set)

ingredients = {"flour", "sugar", "butter"}
ingredients.add("eggs")
print(ingredients)
ingredients.remove("sugar")
print (ingredients)

# -----------------------------------
# SETS OPERATIONS 
# UNION combines two sets (| is the symbol)
# INTERSECTION is the common items in two sets ( & is the symbol)
# DIFFERENCE is the items that is in Set A and not in Set B ( -  is the symbol)

set_a = {"Yam", "Beans", "Rice"}
set_b = {"Pepper", "Yam"}
print(set_a | set_b)
print(set_a & set_b)
print(set_a - set_b)

