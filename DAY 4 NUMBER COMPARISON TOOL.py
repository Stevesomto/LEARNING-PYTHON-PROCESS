# NUMBER COMPARISON TOOL


# Request for input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the Ssecond number: "))
num3 = int(input("Enter the Third number: "))

#Comparison
if (num1 == num2 and num2 == num3):
    print (f"Both numbers are equal", num1)
elif (num1 < num2 and num1 > num3):
    print (f"{num1} is greater than {num2}")
else:
    print (f"{num2} is less than {num1}")

#Check if any number is zero

if (num1 == 0 or num2 == 0):
    print ("One of the numbers has a zero")
else:
    print ("None has a zero")
