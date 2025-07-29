# BUILD AN INGREDIENT CHECKER THAT HELPS USERS INDENTIFY MISSING INGREDIENTS FROM A RECEIPE AND EXTRA INGREDIENT NOT LISTED IN THE RECEIPE

# DEFINE THE RECIPE INGREDIENTS

recipe_ingredients =  {"Flour", "Sugar", "Butter", "Eggs", "Milk"}

# GET THE USERS INPUTS
user_input = input("Enter the ingredient you have (seperated by commas):  ")
user_ingredients = set(user_input.split(", "))

# COMPARE THE INGREDIENTS
missing_ingredients = recipe_ingredients - user_ingredients
extra_ingredients = user_ingredients - recipe_ingredients

# DISPLAY THE RESULT
print("/n--- Ingredients check result----")
if missing_ingredients:
    print(f"You are missing the following ingredient: {', ' .join(missing_ingredients)}")
else:
    print("You have all the ingredients needed")

if extra_ingredients:
    print(f"You have extra ingredients: {',  '  .join(extra_ingredients)}")
else:
    print("You have all the ingredients needed for this receipe")