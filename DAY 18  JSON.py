# JSON which means JavaScript Object Notation is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate.

# READ JSON FILE
import json              
from datetime import time       

# with open("json_data", "r") as file:
#     tasks = json.load(file) 
#     print(tasks)


# # WRITE JSON FILE
# with open("json_data", "w") as file:
#     json.dump(tasks, file)

tasks = [
    {"task": "Complete project", "status": "Incomplete"}
]

with open ('json_data2.json', "w") as file:
    json.dump(tasks, file, indent=3)
    
# MODIFY JOSON FILE

with open ("json_data2.json", "w") as file:
    tasks = json.load(file)
tasks.append({{"task": "Complete project", "status": "Incomplete", "time_completed": "date.today().year"}})

with open("json_data2.json" "w") as file:
    json.dump(tasks, file, indent=3)