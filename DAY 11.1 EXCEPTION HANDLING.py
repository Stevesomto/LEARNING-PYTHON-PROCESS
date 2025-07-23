# what are Exception: They are errors that occurs during the execution of a program

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result", result)
except ZeroDivisionError:
    print("Error: Division by Zero is not allowed")
except ValueError:
    print("Error: Invalid input, Please enter a number not a character or a text")
    
    # SAME CAN BE SEEN AS 
    
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result is: ", result)
except (ZeroDivisionError, ValueError):
    print("Error! Zero value is not accepted and characters or alphabets are not accepted. Please enter the correct value")

    
    
    
try:
    num = int(input("Enter a number:  "))
    result =  10 / num
except ZeroDivisionError:
    print("Error! Division by zero is not allowed")
else: 
    print("Program executed and your result is: ", result)
finally:
    print("Program has ended")