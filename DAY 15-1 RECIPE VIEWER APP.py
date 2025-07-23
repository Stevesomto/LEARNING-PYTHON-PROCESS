# Recipe Viewer App


# Load Recipes from a file

def load_recipes(file_path):
    try:
        with open("recipes.txt", "r") as file:
            content = file.read()
            recipes = content.split("\n\n")
            recipe_dict = {}
            for recipe in recipes:
                lines = recipe.strip().split("\n")
                if len(lines) >= 3:
                    name = lines[0]
                    ingredients = lines[1].replace('Ingredients:', ' ').strip()
                    instructions = lines[2].replace("Instructions:", "").strip()
                    recipe_dict[name] = {"Ingredients": ingredients, "Instructions": instructions}
            return recipe_dict
    except FileNotFoundError:
        print("The file does not exist. Please check the file name and path.")
        return {}
    
    
# DISPLAY THE RECEIPT MENU

def show_menu():
    print ("\n --- Recipe Viewer Menu---")
    print ("1. View Recipe by Name")
    print ("2. List All Recipes")
    print ("3. Exit")


# DISPLAY RECIPE DETAILS
def view_result(recipes):
    name= input("Enter the name of the recipe: ").strip()
    if name in recipes:
        print (f"\n-- Recipe {name} Details ---")
        print (f"Ingredients: {recipes[name] ['Ingredients']}")
        print (f"Instructions: {recipes[name] ['Instructions']}")
    else: 
        print ("Recipe not found")
        
# MAIN PROGRAM
recipe_file = "recipes.txt"
recipes = load_recipes(recipe_file)

while True:
    show_menu()
    choice = int(input("Enter a choice (1/2/3/):  "))
    
    if choice == 1:
        view_result(recipes)
    elif choice == 2:
        print("\n-- All Recipes--")
        for name in recipes:
            print (name)
    elif choice == 3:
        print ("Exiting the program")
        break
    else: 
        ("Invalid selection/option, please check the menu and try again")