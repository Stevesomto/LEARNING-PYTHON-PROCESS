# A DICTIONARY IS A COLLECTION OF KEY VALUE PAIRS WHERE EACH KEY MAPS TO A VALUE 

my_dict = {
    "Name": "Stephen Somtochukwu",
    "Phone": "08123443047",
    "Email": "anyanwystevo18@gmail.com"
}

# modifying in Dictionary
my_dict["Phone"] = "08037239534"

# Accessing a key and value in Dictionary 
print(my_dict.get("Email"))

print(my_dict)

# To add a key and value to an already exisiting dictionary

my_dict["Address"] = "University of Nigeria, Nsukka"

print(my_dict)

"\n"
print(my_dict["Address"])

# to delete

del  my_dict["Address"]

print(my_dict)

# LOOPING IN BETWEEN ENTRIES 
for key, value in my_dict.items():
    print(key, value)

if "Address" in my_dict:
    print("Address found")
else: 
    print("No Address found, please add address")