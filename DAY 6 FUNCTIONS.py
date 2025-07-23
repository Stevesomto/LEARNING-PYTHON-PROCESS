
title = input("What is your title?:  ")
name = input("What is your name?:  ")

def greetings():

    print(f"Good morning {title}{name}")

greetings()

# Alternatively

print ("\n----- Alternatively---")



def greetings1(username):
    print(f"Good morning {username}")

greetings1("Miss Obettaa")

print ("\n----- Alternatively---")

def num (a , b):
    print (f" The sum of a and b is {a + b}")

num(6, 7)

print ("\n----- Alternatively---")

def mul(a, b):
    return a * b
result = mul(10, 6)
print (f'The result is  {result}')