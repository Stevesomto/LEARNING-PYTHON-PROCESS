# DECLARE FUNCTION 

def is_prime(n: int) -> bool:
# Return True if n is prime; otherwise False."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    limit = int(n ** 0.5) + 1
    for divisor in range(3, limit, 2):
        if n % divisor == 0:
            return False
    return True


# --- FIRST OUTPUT code ---
num = int(input("Enter an integer: "))
print(f"{num} is {'a prime' if is_prime(num) else 'not a prime'} number.")

print ("\n-------------------------------------------------")

# --- FIRST OUTPUT code ---
num = int(input("Enter an integer: "))
print(f"{num} is {'a prime' if is_prime(num) else 'not a prime'} number.")
