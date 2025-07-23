# FILE READING IS THE PROCESS OF PROVIDING DATA FROM A FILE 


with open("recipe.txt", "w") as file:
    file.write("\n1. Spaghetti Bolognese")
    file.write("\n2. Rice \n")

with open("recipe.txt" , "r") as file:
    content = file.read()
    print(content)
    
with open ("recipe.txt", "r") as file:
    for line in file:
        print(line.strip())

with open ("recipe.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
        

# HANDLING FILE IN FILE READING
        
try: 
    with open("recipes.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file does not exist. Please check the file name and path.")