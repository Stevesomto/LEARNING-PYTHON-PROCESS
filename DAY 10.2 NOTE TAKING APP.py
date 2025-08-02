<<<<<<< HEAD
# BUILD AN INTERACTIVE APP WHERE USERS CAN ADD NEW NOTE, VIEW, DELETE AND EXIT NOTE

# Define the file name

FILE_NAME = "myNotes.txt"

# Display menu option
def show_menu():
    print("\n--- NOTES TAKING APP MENU")
    print("1.  Add a New note")
    print("2.  View all note")
    print("3.  Delete all notes")
    print("4.  Exit")

# Add All Notes
def add_note():
    note = input("Enter your note:  ")
    with open(FILE_NAME, "a") as file:
        file.write(f"{note} \n")
    print("Note added successfully")
    
    
# VIEW ALL NOTES
def view_note():
    try:
        with open(FILE_NAME, "r") as file:
            contents = file.read()
            if contents: 
                print("\n --- Your Notes----")
                print(contents)
            else:
                print("\n No note found")
    except FileNotFoundError:
            print("No notes found.")

# DELETE ALL NOTE
def del_notes():
    confirm = input("Are you sure you want to delete all nores (Use: Yes/no):  ")
    if confirm == "Yes":
        with open(FILE_NAME, "w") as file:
            # file.write("")
            pass
        print("All notes has been deleted")
    else: 
        print("Deletion cancelled")

# EXT NOTE
def exit_note():
    print("Thank you for using SomtoNotes. Will be glad to have you again.")

# LOOPING

while True:
    show_menu()
    choice = int(input("Enter a number btw 1-4:  "))
    if choice == 1:
        add_note()
    elif choice == 2:
        view_note()
    elif choice == 3:
        del_notes()
    elif choice == 4:
        exit_note()
        break
    else: 
=======
# BUILD AN INTERACTIVE APP WHERE USERS CAN ADD NEW NOTE, VIEW, DELETE AND EXIT NOTE

# Define the file name

FILE_NAME = "myNotes.txt"

# Display menu option
def show_menu():
    print("\n--- NOTES TAKING APP MENU")
    print("1.  Add a New note")
    print("2.  View all note")
    print("3.  Delete all notes")
    print("4.  Exit")

# Add All Notes
def add_note():
    note = input("Enter your note:  ")
    with open(FILE_NAME, "a") as file:
        file.write(f"{note} \n")
    print("Note added successfully")
    
    
# VIEW ALL NOTES
def view_note():
    try:
        with open(FILE_NAME, "r") as file:
            contents = file.read()
            if contents: 
                print("\n --- Your Notes----")
                print(contents)
            else:
                print("\n No note found")
    except FileNotFoundError:
            print("No notes found.")

# DELETE ALL NOTE
def del_notes():
    confirm = input("Are you sure you want to delete all nores (Use: Yes/no):  ")
    if confirm == "Yes":
        with open(FILE_NAME, "w") as file:
            # file.write("")
            pass
        print("All notes has been deleted")
    else: 
        print("Deletion cancelled")

# EXT NOTE
def exit_note():
    print("Thank you for using SomtoNotes. Will be glad to have you again.")

# LOOPING

while True:
    show_menu()
    choice = int(input("Enter a number btw 1-4:  "))
    if choice == 1:
        add_note()
    elif choice == 2:
        view_note()
    elif choice == 3:
        del_notes()
    elif choice == 4:
        exit_note()
        break
    else: 
>>>>>>> 5776d637b558ed6ad1589ad51c196b7c0d84fcfe
        print ("Option not found, please check well and try again")