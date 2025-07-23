# Write a python program to accept the name of your dad,
# his birth year and the year he got married, display a statement
# in the form mr Philip you are 77 years old and 50 years in marriage

# ASK FOR THE DAD NAME, DATE OF BIRTH, YEAR OF MARRIAGE

dad_title = input("Enter your dad's title (Mr/Dr/Prof):  ")
dad_name = input("Enter the name of your dad:  ")
dad_year_of_birth = int(input("Enter your dad's year of birth:  "))
dad_year_of_marriage = int(input("Enter your dad's year of marriage:  "))
current_year = 2025

dad_age = current_year - dad_year_of_birth
dad_marriage = current_year - dad_year_of_marriage

# DISPLAY THE OUTPUT

print (f"{dad_title} {dad_name} you are {dad_age} years old and {dad_marriage} years in marriage")

