# BUILD A DAILY JOURNAL LOGGER

# Define the journal file 

journal_file = 'edaily_journal.txt'

# Add a new entry 
def add_entry ():
    entry = input("Write your journal entry: ")
    with open (journal_file, "a") as file:
        file.write(entry + "\n")
    print ("Entry added successfully")

# View all Entries
def view_entries():
    try: 
        with open(journal_file, "r") as file:
            content = file.read()
            if content:
                print ("\n-- Your Journal Entires---")
                print (content)
            else: 
                print ("No entries found. Start writing today")
    except FileNotFoundError: 
        print ("No journal found. And an entry")
    
# Search entries by keyword
def search_entries():
    keyword = input("Enter the keyword to search for:  ").lower()
    try: 
        with open (journal_file, "r")  as file:
            content = file.readlines()
            found = False
            print("\n--- Search Results---")
            for entry in content: 
                if keyword in entry.lower():
                    print (entry.strip())
                    found = True
            if not found:
                    print ("No matching entries found")
    except FileNotFoundError:
        print("No Journal file found. Add an entry first!")
        
# DISPLAY THE MENU
def show_menu():
    print("\n---- DAILY JOURNAL LOGGER---")
    print("1. Add a new entry")
    print("2. View all entries")
    print("3. Search entires by keyword")
    print("4. Exit")

# Main program loop
while True: 
    show_menu()
    choice = int(input("Enter your choice between 1 and 4: "))
    
    if choice == 1:
        add_entry()
    elif choice == 2: 
        view_entries()
    elif choice == 3:
        search_entries()
    elif choice == 4:
        print("Thank you for using Daily Journal Logger. See you next time!")
        break
    else:
        print("Invalid option, please enter 1-4")
    
    
    
