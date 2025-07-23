# FILE HANDLING IS THE WAY TO STORE AND ACCESS DATA IN FILES ON YOUR COMPUTERS

file = open("ERRORS.txt", "r+")
file.close() 

# READ FROM FILES
# the "with" function helps the file to close automatically after making use of the file 

with open("ERRORS.txt", "r") as file:
    content = file.read()
    print(content)
    
# WRITE IN THE FILES -  this deletes existing contents and replace with the new ones
with open("filehandling.txt", "w") as file:
    file.write("So Don't forget to debug it and know what the issue might be\n")
    
# APPENDING TO FILE =if you dont want to delete existing
with open("filehandling.txt", "a") as file:
    file.write("Please dont forget to do so")
    
