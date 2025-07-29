# Contact book

# Step 1: Initialize an empty contact book
contacts = {}

# Step 2: Display the menu

def display_menu():
    print("\n--- Contact Book Menu")
    print("1. Add contact")
    print("2. View contact")
    print("3. Search for a  contact")
    print("4. Edit contact")
    print("5. Delete contact")
    print("6. Exit contact")
    
# Add a contact
def add_contacts():
    name = input("Add your contact name:  ")
    phone = int(input("Add your contact phone:  "))
    address = input("Add your contact address:  ")
    email = input("Add your contact email:  ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"Contact {name} has been added to your contact book successfully")
    
# View all contacts
def view_contacts():
    if contacts: 
        print("\n--- Contact List----")
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}" )
            print(f"Email: {details['email']}" )
            print(f"Address: {details['address']}" )
    else: 
            print("Your contact list is empty")

# Search a contact
def search_contacts():
    name = input("Enter the name of the contact you want to search:  ")
    if name in contacts:
        print(f"\n--- Contact Detials for {name}")
        print(f"Name: {name}")
        print(f"Phone: {contacts[name] ['phone']}")
        print(f"Email: {contacts[name] ['email']}")
        print(f"Address: {contacts[name] ['address']}")
    else: 
        print(f"Contact {name} not found in your contact book")

# Edit a contact
def edit_contacts():
    name = input("Enter the name of the contact you want to edit:  ")
    if name in contacts:
        phone = int(input("Enter the new phone number: "))
        email = input("Enter the new email address: ")
        address = input("Enter the new address:  ")
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print(f"Contact {name} has been updated successfully") 
    else: 
        print(f"Contact {name} not found")
    
# Delect a contact
def del_contacts():
    name = input("Enter the name of the contact you want to delete:  ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} has been deleted successfully")
    else:
        print(f"Contact {name} not found in the contact book")

# Exit from contact book
def exit_contacts():
    print ("\n-- Thank you for your time---")
    
# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        add_contacts()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contacts()
    elif choice == "4":
        edit_contacts()
    elif choice == "5":
        del_contacts()
    elif choice == "6":
        exit_contacts()
        break
    else: 
        print("Invalid choice, please try again!")
        
    