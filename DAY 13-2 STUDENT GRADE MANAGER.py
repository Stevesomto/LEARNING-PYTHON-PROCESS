# STUDENT GRADE MANAGER

# Get Student score

student_scores =  input("Enter scores seperated by comma: ")
scores = [int(score) for score in student_scores.split(",")]

# Assign Grades usig List Comprehension
grades = [
    "A" if score >= 70 else
    "B" if score >= 60 else
    "C" if score >= 50 else
    "D" if score >= 40 else
    "E" if score >= 30 else
    "F"
    for score in scores    
    ]

# Filter Passing and Failling Students

passing_students = [score for score in scores if score >= 50]
failing_students = [score for score in scores if score < 40]

# Print result
print("\n--- Students Grade---")
for i, (score, grade) in enumerate(zip(scores, grades), start = 1):
    print(f"Student {i}: Score = {score}, Grade = {grade}")
    
print("\n--- Passing and Failing Students---")
print("Passing Students", passing_students)
print("Failing Students", failing_students)