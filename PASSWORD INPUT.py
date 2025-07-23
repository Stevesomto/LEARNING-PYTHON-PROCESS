import getpass

username = input("Enter your username:  ")
password = getpass.getpass("Enter your password: ")

print("\n--- Logging in ---")
print (f" Username: {username}")
print (f" Password: [hidden for security]")
