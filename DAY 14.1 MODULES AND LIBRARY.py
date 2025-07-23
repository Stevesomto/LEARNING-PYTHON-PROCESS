# MODULE IS A PYTHON FILE CONTAINING FUNCTIONS, CLASSES AND VARIABLE YOU CAN RESUE IN YOUR CODE
# LIBRARY IS A COLLECTION OF MODULE DESIGNED FOR SPECIFIC TASKS (EG. MATH LIBRARY)

import math

print(math.sqrt(60))


import random
print (random.randint(1, 20))

# FOR CHOICE RANDOM 

from random import choices
print(choices(["Apples", "Banana", "Oranges"]))

# PASSWORD

import random
password = '' .join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890', k=8))
print(password)

# CUSTOM IMPORTING OF MODULES FROM ALREADY SAVED .py FILE
import ERRORS
print(ERRORS)

