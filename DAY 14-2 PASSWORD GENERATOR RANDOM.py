<<<<<<< HEAD
# BUILD A RANDOM PASSWORD GENERATOR

import random
import string

# DEFINE PASSWORD GENERATION FUNCTION

def generate_password (lenght = 12):
    if lenght < 5:
        raise ValueError("Password length must be at least 4 characters")
    
    # Charater for the password    
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    letters = string.ascii_letters
    special_chars = "!@#$%^&*())_{}[]\';.,./?><"

    # Ensure at least one of each character type
    password = [
        random.choice(uppercase), 
        random.choice(lowercase),
        random.choice(digits), 
        random.choice(letters),
        random.choice(special_chars)
    ]

    # Fill the remaining lenght with random choices from all sets
    all_chars = uppercase + lowercase + letters + special_chars + digits
    password += random.choices(all_chars, k=lenght - 4)

    # Shuffle the password to make it more random
    random.shuffle(password)

    # Convert the list to a string and return
    return '' .join(password)

# User interaction

try:
    lenght = int(input("Enter the desired number of password (minimum of 4):  "))
    password = generate_password(lenght)
    print ("Generated Password: ", password)
except ValueError as e:
    print(e)

=======
# BUILD A RANDOM PASSWORD GENERATOR

import random
import string

# DEFINE PASSWORD GENERATION FUNCTION

def generate_password (lenght = 12):
    if lenght < 5:
        raise ValueError("Password length must be at least 4 characters")
    
    # Charater for the password    
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    letters = string.ascii_letters
    special_chars = "!@#$%^&*())_{}[]\';.,./?><"

    # Ensure at least one of each character type
    password = [
        random.choice(uppercase), 
        random.choice(lowercase),
        random.choice(digits), 
        random.choice(letters),
        random.choice(special_chars)
    ]

    # Fill the remaining lenght with random choices from all sets
    all_chars = uppercase + lowercase + letters + special_chars + digits
    password += random.choices(all_chars, k=lenght - 4)

    # Shuffle the password to make it more random
    random.shuffle(password)

    # Convert the list to a string and return
    return '' .join(password)

# User interaction

try:
    lenght = int(input("Enter the desired number of password (minimum of 4):  "))
    password = generate_password(lenght)
    print ("Generated Password: ", password)
except ValueError as e:
    print(e)

>>>>>>> 5776d637b558ed6ad1589ad51c196b7c0d84fcfe
