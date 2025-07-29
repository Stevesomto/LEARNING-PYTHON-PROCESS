# Calculate the grade of a student


subject = input("What Subject?:  ")
score = int(input(f"What is your {subject}'s score?:  "))

if (score >= 70):
    print ("A")
elif (score >= 60):
    print ("B")
elif (score >= 50):
    print ("C")
elif (score >= 40):
    print ("D")
elif (score >= 30):
    print ("E")
else:
    print ("F")

