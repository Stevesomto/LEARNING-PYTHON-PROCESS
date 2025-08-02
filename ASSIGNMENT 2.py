<<<<<<< HEAD
# Develop a software using python programming language to solve
# a quadratic equation using formula method

# Import the 'math' library to be able to do square roots.

import math

print("Welcome! Let's solve a quadratic equation (ax² + bx + c = 0).")

# --- STEP 1: Get the ingredients (a, b, and c) ---
a = float(input("Enter the number for a: "))
b = float(input("Enter the number for b: "))
c = float(input("Enter the number for c: "))

# --- STEP 2: Calculate the special part under the square root (the discriminant)
discriminant = (b**2) - (4 * a * c)
print("\n--- Calculating... ---\n")

# --- STEP 3: Find the answers based on the check ---
# If the discriminant is positive or zero, the answers are real numbers
if discriminant >= 0:
    print("The answers are real numbers:")
    # Calculate the two possible answers using the formula
    sol1 = (-b - math.sqrt(discriminant)) / (2 * a)
    sol2 = (-b + math.sqrt(discriminant)) / (2 * a)
    print(f"Solution 1: {sol1}")
    print(f"Solution 2: {sol2}")

# If the discriminant is negative, the answers are complex numbers
else:
    print("The answers are complex numbers:")
    # We can't take the square root of a negative number directly
    # So we calculate the real part and the imaginary part separately
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2 * a) # use the positive version
    
    # Display the two complex solutions
    print(f"Solution 1: {real_part} - {imaginary_part}j")
    print(f"Solution 2: {real_part} + {imaginary_part}j")
=======
# Develop a software using python programming language to solve
# a quadratic equation using formula method

# Import the 'math' library to be able to do square roots.

import math

print("Welcome! Let's solve a quadratic equation (ax² + bx + c = 0).")

# --- STEP 1: Get the ingredients (a, b, and c) ---
a = float(input("Enter the number for a: "))
b = float(input("Enter the number for b: "))
c = float(input("Enter the number for c: "))

# --- STEP 2: Calculate the special part under the square root (the discriminant)
discriminant = (b**2) - (4 * a * c)
print("\n--- Calculating... ---\n")

# --- STEP 3: Find the answers based on the check ---
# If the discriminant is positive or zero, the answers are real numbers
if discriminant >= 0:
    print("The answers are real numbers:")
    # Calculate the two possible answers using the formula
    sol1 = (-b - math.sqrt(discriminant)) / (2 * a)
    sol2 = (-b + math.sqrt(discriminant)) / (2 * a)
    print(f"Solution 1: {sol1}")
    print(f"Solution 2: {sol2}")

# If the discriminant is negative, the answers are complex numbers
else:
    print("The answers are complex numbers:")
    # We can't take the square root of a negative number directly
    # So we calculate the real part and the imaginary part separately
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2 * a) # use the positive version
    
    # Display the two complex solutions
    print(f"Solution 1: {real_part} - {imaginary_part}j")
    print(f"Solution 2: {real_part} + {imaginary_part}j")
>>>>>>> 5776d637b558ed6ad1589ad51c196b7c0d84fcfe
