# Develop a software using python programming language to enter the name of a
# person,the birth year of the person and the height of the person
# display a message saying Sunday prince ,you are 35yrs old and 5.2ft tall

# ASK THE USER TO INPUT HIS/HER DETAILS

name = input("What is your name?:  ")
year_of_birth = int(input("What is your year of birth?:  "))
age = 2025 - year_of_birth
height = float(input("What is your height in feet?:  "))

# DISPLAY THIS DETAILS HE/SHE ENTERED

print ("\n--- THE DISPLAYED DETAILS---")
print (f" My name is {name}")
print (f" I am {age} years old")
print (f" My height is {height} feet \n")

print (f"Therefore, {name}, you are {age} years old and {height} ft tall.")




