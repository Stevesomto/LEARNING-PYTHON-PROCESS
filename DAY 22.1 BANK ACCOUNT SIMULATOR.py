# BANK ACCOUNT SIMULATOR 

class BankAccount:
    """
    Represents a single bank account with methods to deposit, withdraw, and show details.
    """
    # The __init__ method is the constructor for the class. It's called when you create a new BankAccount object.
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = float(initial_balance) # Ensure balance is always a float

    # Deposit Money
    def deposit(self, amount):
        """Adds a positive amount to the account balance."""
        if amount > 0:
            # BUG FIX: Changed 'self.balance += 0' to 'self.balance += amount'
            # This ensures the deposit amount is actually added to the balance.
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    # Withdraw Money
    def withdraw(self, amount):
        """Subtracts an amount from the balance if funds are sufficient."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New Balance: ${self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient balance for this withdrawal.")
        else:
            print("Invalid withdrawal amount. Amount must be greater than 0.")
    
    # Show Account details
    def show_details(self):
        """Prints the details of the account."""
        print("\n--- Account Details ---")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Balance: ${self.balance:.2f}")


# --- Main Program Logic ---

# This dictionary will store the BankAccount objects, with the account holder's name as the key.
accounts = {}

def create_account():
    """Handles the creation of a new BankAccount object and adds it to the accounts dictionary."""
    name = input("Enter account holder's name: ").strip()
    if not name:
        print("Account holder name cannot be empty.")
        return
    if name in accounts:
        print("An account with this name already exists.")
        return
        
    try:
        initial_deposit = float(input("Enter initial deposit: "))
        if initial_deposit < 0:
            print("Initial deposit cannot be negative.")
            return
        # BUG FIX: Create an instance of the BankAccount class, not a tuple.
        account = BankAccount(name, initial_deposit)
        accounts[name] = account
        print(f"\nAccount for {name} created successfully!")
        account.show_details()
    except ValueError:
        print("Invalid input. Please enter a number for the deposit.")


def access_account():
    """Allows a user to access an existing account and perform actions."""
    name = input("Enter your account holder name: ").strip()
    if name in accounts:
        # Retrieve the BankAccount object from the dictionary
        account = accounts[name]
        
        while True:
            print("\n--- Account Menu ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show details")
            print("4. Exit to Main Menu")
            
            choice_str = input("Enter your choice (1-4): ")
            if not choice_str.isdigit():
                print("Invalid choice. Please enter a number.")
                continue

            choice = int(choice_str)
            
            try:
                if choice == 1:
                    amount = float(input("Enter deposit amount: "))
                    # BUG FIX: Corrected typo from 'desposit' to 'deposit'
                    account.deposit(amount)
                elif choice == 2:
                    amount = float(input("Enter amount you want to withdraw: "))
                    account.withdraw(amount)
                elif choice == 3:
                    # BUG FIX: Called show_details() on the 'account' object, not 'amount'.
                    account.show_details()
                elif choice == 4:
                    print("Exiting account menu...")
                    break
                else:
                    print("Invalid choice. Please select a valid option (1-4).")
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
    else:  
        print("Account not found. Please create an account first.")

# --- Main Menu Loop ---
def main():
    """The main function to run the bank simulator program."""
    while True:
        print("\n--- Bank Account Simulator ---")
        print("1. Create Account")
        print("2. Access Account")
        print("3. Exit")
        
        choice_str = input("Enter your choice (1-3): ")
        if not choice_str.isdigit():
            print("Invalid option. Please choose 1, 2, or 3.")
            continue

        choice = int(choice_str)

        if choice == 1:
            create_account()
        elif choice == 2:
            access_account()
        elif choice == 3:
            print("\nThank you for using the Bank Account Simulator!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

# This line ensures the main() function runs when the script is executed
if __name__ == "__main__":
    main()
