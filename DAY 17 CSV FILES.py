<<<<<<< HEAD
# WHAT ARE CSV FILES? COMMA SEPERATED VALUES

# CREATING STUDENTS FILE

with open ("students.csv", "w") as file:
    file.write( "NAME, MATH, SCIENCE, ENGLISH \n" )
   
with open ("students.csv", "a") as file:
       file.write("Alice, 85, 90, 88 \n")
       
with open ("students.csv", "a") as file:
       file.write("Bob, 75, 80, 72 \n")

with open ("students.csv", "a") as file:
       file.write("Charlie, 95, 98, 97\n")
       
with open ("students.csv", "r") as file:
    content = file.read()
    print (content)
    

# IMPORT CSV

import csv

with open ("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"{row}\n") 

# TO READ WITH DICTIONARY -  THIS WILL SEPERATE EACH OF THE FILE IN ROW AND GIVEN ITS STUDENTS THEIR SCORE IN A SINGLE ROW. THE FORMER STEP WE TOOK ABOVE IS IN LIST FORMAT WHILE THIS ONE BELOW IS IN DICTIONARY FORMAT

with open ("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# TO WRITE INTO A CSV FILE
# import csv
from datetime import date
current_year = date.today().year
age =  current_year -  2000
age1 = current_year - 2005

with open ("students2.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'Gender'])
    writer.writerow(['Stephen', age, 'M'])
    writer.writerow(['Vivian', age1, 'F'])
    
# AS A DICTIONARY 

with open ("students3.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'Gender'])
    writer.writeheader()
    writer.writerow({'Name': 'Stephen', 'Age': age, 'Gender': 'Male', })
=======
# WHAT ARE CSV FILES? COMMA SEPERATED VALUES

# CREATING STUDENTS FILE

with open ("students.csv", "w") as file:
    file.write( "NAME, MATH, SCIENCE, ENGLISH \n" )
   
with open ("students.csv", "a") as file:
       file.write("Alice, 85, 90, 88 \n")
       
with open ("students.csv", "a") as file:
       file.write("Bob, 75, 80, 72 \n")

with open ("students.csv", "a") as file:
       file.write("Charlie, 95, 98, 97\n")
       
with open ("students.csv", "r") as file:
    content = file.read()
    print (content)
    

# IMPORT CSV

import csv

with open ("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"{row}\n") 

# TO READ WITH DICTIONARY -  THIS WILL SEPERATE EACH OF THE FILE IN ROW AND GIVEN ITS STUDENTS THEIR SCORE IN A SINGLE ROW. THE FORMER STEP WE TOOK ABOVE IS IN LIST FORMAT WHILE THIS ONE BELOW IS IN DICTIONARY FORMAT

with open ("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# TO WRITE INTO A CSV FILE
# import csv
from datetime import date
current_year = date.today().year
age =  current_year -  2000
age1 = current_year - 2005

with open ("students2.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'Gender'])
    writer.writerow(['Stephen', age, 'M'])
    writer.writerow(['Vivian', age1, 'F'])
    
# AS A DICTIONARY 

with open ("students3.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'Gender'])
    writer.writeheader()
    writer.writerow({'Name': 'Stephen', 'Age': age, 'Gender': 'Male', })
>>>>>>> 5776d637b558ed6ad1589ad51c196b7c0d84fcfe
    writer.writerow({'Name': 'Vivian', 'Age': age1, 'Gender': 'Female', })