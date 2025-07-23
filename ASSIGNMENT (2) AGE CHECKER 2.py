from datetime import date

def dad_summary(name: str, birth_year: int, marriage_year: int) -> str:
    """Return a formatted status line for dad's age and marriage duration."""
    current_year = date.today().year
    age = current_year - birth_year
    years_married = current_year - marriage_year
    return f"Mr {name.title()}, you are {age} years old and {years_married} years in marriage."


# --- driver code ---
dad_name = input("Enter your dad's first name: ")
birth_yr = int(input("Enter his birth year (YYYY): "))
marriage_yr = int(input("Enter his marriage year (YYYY): "))
print(dad_summary(dad_name, birth_yr, marriage_yr))
