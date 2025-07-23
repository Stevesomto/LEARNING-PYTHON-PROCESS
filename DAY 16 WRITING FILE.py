# FILE WRITING SAVING DATA IN FILES FOR REFERENCE PURPOSE

with open ("jorunal.txt", "w") as file:
    file.write("Day 16: Today I learnt about writng file in Python. \n")
    
with open ("jorunal.txt", "a") as file: 
    file.write("Day 16: After the learning, I built a Daily Journal Logger App ")

try:
    with open ("/restriction/journal.txt") as file:
        file.write ("Test Entry")
except PermissionError:
    print("You do not have permission to write to the file")

