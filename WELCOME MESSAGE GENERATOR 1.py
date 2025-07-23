name = input("What is your name?: "); 
title = input("What is your title")
age = int(input("What is your year of birth?: "))
hobby = input("What is your hobby?")
year = 2025 - age
name_upper =  name.upper()

print ("\n --- WELCOME MESSGAE GENERATOR ---")
print (f"Hello, {name}")
print (f"So you are {year} years old")
print (f"You said your hobby is {hobby}")
print (f"We are so elated to have you onbooard {title} {name}")