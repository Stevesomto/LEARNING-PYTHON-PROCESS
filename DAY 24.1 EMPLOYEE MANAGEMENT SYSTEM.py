# EMPLOYEE MANAGEMENT SYSTEM
# This code is part of a larger project that manages employee records.

import csv
import os

# BASE CLASS: EMPLOYEE
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        
    def display_info(self):
        print(f"\n--- Employee Information ---")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: ${self.salary:.2f}")
        
    def calculate_bonus(self):
        return self.salary * 0.1

# Derived CLASS: MANAGER
class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department
        
    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
    
    def calculate_bonus(self):
        return self.salary * 0.2

# Derived CLASS: DEVELOPER
class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_language):
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

    def calculate_bonus(self):
        return self.salary * 0.5
    
# Main program
employees = []

def add_employee():
    print("\n--- Choose Employee Types ---")
    print("1. Regular Employee")
    print("2. Manager")
    print("3. Developer")
    choice = int(input("Enter employee type (Manager/Developer): ").strip())
    
    name = input("Enter employee name: ").strip()
    emp_id = input("Enter employee ID: ").strip()
    salary = float(input("Enter employee salary: "))
    
    new_employee = None
    
    if choice == 1:
        new_employee = Employee(name, emp_id, salary)
    elif choice == 2:
        department = input("Enter department: ").strip()
        new_employee = Manager(name, emp_id, salary, department)
    elif choice == 3:
        programming_language = input("Enter programming language: ").strip()
        new_employee = Developer(name, emp_id, salary, programming_language)
    else:
        print("Invalid choice. Please try again.")
        return  
    
    employees.append(new_employee)
    save_employee_to_csv(new_employee)              # 👈 Auto-save here
    print("✅ Employee added and saved to CSV.")

def display_all_employees():
    print("\n--- All Employee ---")
    for employee in employees:
        employee.display_info()
        print(f"Bonus: ${employee.calculate_bonus():.2f}")
        print("-----------------------")
        
        
# Save employee data to CSV file

def save_employee_to_csv(employee, filename='employees.csv'):
    file_exists = os.path.isfile(filename)
    
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            # Write header if file does not exist
            writer.writerow(['Name', 'Employee ID', 'Salary', 'Bonus', 'Role', 'Extra Info'])

        bonus = employee.calculate_bonus()
        if isinstance(employee, Manager):
            writer.writerow([employee.name, employee.emp_id, employee.salary, bonus, 'Manager', employee.department])
        elif isinstance(employee, Developer):
            writer.writerow([employee.name, employee.emp_id, employee.salary, bonus, 'Developer', employee.programming_language])
        else:
            writer.writerow([employee.name, employee.emp_id, employee.salary, bonus, 'Employee', 'N/A'])



# Menu
while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Exit")
    choice = int(input("Enter your choice: ").strip())

    if choice == 1:
        add_employee()
    elif choice == 2:
        display_all_employees()
    elif choice == 3:
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again and choose from 1-3.")
