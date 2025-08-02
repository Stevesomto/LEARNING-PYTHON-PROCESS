<<<<<<< HEAD
# Declare function and dispay output

def factorial(n: int) -> int:
# Return n! (factorial) for n ≥ 0."""
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# --- driver code ---
n = int(input("Enter a non‑negative integer: "))
print(f"{n}! = {factorial(n)}")
=======
# Declare function and dispay output

def factorial(n: int) -> int:
# Return n! (factorial) for n ≥ 0."""
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# --- driver code ---
n = int(input("Enter a non‑negative integer: "))
print(f"{n}! = {factorial(n)}")
>>>>>>> 5776d637b558ed6ad1589ad51c196b7c0d84fcfe
