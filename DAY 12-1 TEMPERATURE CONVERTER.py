<<<<<<< HEAD
# BUILD A TEMPERATURE CONVERTER THAT CAN CONVER CELSIUS TO FAHRENHEIT AND KELVIN AND OTHER UNITS

# TEMPERATURE CONVERTER

# DEFINE CONVERSION FUNCTIONS

def celsius_fahrenheit(celsius):
    return(celsius * 9/5) + 32                  # formular for converting celsius to fahrenheit

def celsius_kelvin(celsius):
    return celsius + 273.15                     # formular for converting celsius to kelvin        

def fahrenheit_celsius(fahrenheit):
    return(fahrenheit - 32) * 5/9               # formular for converting fahrenheit to celsius

def fahrenheit_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15     # formular for converting fahrenheit to kelvin

def kelvin_celsius(kelvin):                     
    return kelvin - 273.15                      # formular for converting kelvin to celsius 

def kelvin_fahrenheit(kelvin):
    return (kelvin + 273.15) * 9/5 + 32          # formular for kelvin celsius to fahrenheit


# DISPLAY MENU TO USERS

def show_menu():
    print("\n---- Temperature Converter Menu---")
    print("1. Celsius to Fahrenheit & Kelvin")
    print("2. Fahrenheit to Celsius & Kelvin")
    print("3. Kelvin to Celsius & Fahrenheit")
    print("4. Exit")

# ASK USER HOW MANY DECIMAL PLACES THEY WANT

decimal = int(input("Enter the number of decimal you want:  "))    
user_input = decimal / 10000

# LOOPING

while True:
    show_menu()
    choice = int(input("Enter your choice of number (1-4):  "))

    if choice == 1:
        celsius = float(input ("Enter temperature in Celsius: "))
        print (f" Fahrenheit: {celsius_fahrenheit(celsius): {user_input}}")
        print (f" Kelvin: {celsius_kelvin(celsius):{user_input}}")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in fahrenheit:  "))
        print (f"Celsius: {fahrenheit_celsius(fahrenheit):{user_input}}")
        print (f"Kelvin: {fahrenheit_kelvin(fahrenheit):{user_input}}")
    elif choice == 3:
        kelvin = float(input("Enter temperature in Kelvin:  "))
        print (f"Celsius: {kelvin_celsius(kelvin):{user_input}}")
        print (f"Fahrenheit: {kelvin_fahrenheit(kelvin):{user_input}}")
    elif choice == 4:
        print ("Goodbye")
=======
# BUILD A TEMPERATURE CONVERTER THAT CAN CONVER CELSIUS TO FAHRENHEIT AND KELVIN AND OTHER UNITS

# TEMPERATURE CONVERTER

# DEFINE CONVERSION FUNCTIONS

def celsius_fahrenheit(celsius):
    return(celsius * 9/5) + 32                  # formular for converting celsius to fahrenheit

def celsius_kelvin(celsius):
    return celsius + 273.15                     # formular for converting celsius to kelvin        

def fahrenheit_celsius(fahrenheit):
    return(fahrenheit - 32) * 5/9               # formular for converting fahrenheit to celsius

def fahrenheit_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15     # formular for converting fahrenheit to kelvin

def kelvin_celsius(kelvin):                     
    return kelvin - 273.15                      # formular for converting kelvin to celsius 

def kelvin_fahrenheit(kelvin):
    return (kelvin + 273.15) * 9/5 + 32          # formular for kelvin celsius to fahrenheit


# DISPLAY MENU TO USERS

def show_menu():
    print("\n---- Temperature Converter Menu---")
    print("1. Celsius to Fahrenheit & Kelvin")
    print("2. Fahrenheit to Celsius & Kelvin")
    print("3. Kelvin to Celsius & Fahrenheit")
    print("4. Exit")

# ASK USER HOW MANY DECIMAL PLACES THEY WANT

decimal = int(input("Enter the number of decimal you want:  "))    
user_input = decimal / 10000

# LOOPING

while True:
    show_menu()
    choice = int(input("Enter your choice of number (1-4):  "))

    if choice == 1:
        celsius = float(input ("Enter temperature in Celsius: "))
        print (f" Fahrenheit: {celsius_fahrenheit(celsius): {user_input}}")
        print (f" Kelvin: {celsius_kelvin(celsius):{user_input}}")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in fahrenheit:  "))
        print (f"Celsius: {fahrenheit_celsius(fahrenheit):{user_input}}")
        print (f"Kelvin: {fahrenheit_kelvin(fahrenheit):{user_input}}")
    elif choice == 3:
        kelvin = float(input("Enter temperature in Kelvin:  "))
        print (f"Celsius: {kelvin_celsius(kelvin):{user_input}}")
        print (f"Fahrenheit: {kelvin_fahrenheit(kelvin):{user_input}}")
    elif choice == 4:
        print ("Goodbye")
>>>>>>> 5776d637b558ed6ad1589ad51c196b7c0d84fcfe
        break