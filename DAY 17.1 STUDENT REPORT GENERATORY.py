# BUILD A STUDENT REPORT GENERATOR THAT WILL READ STUDENTS SCORE FROM A CSV FILE, CALCUALTE THE AVERAGE SCORE FOR EACH STUDENT AND THEN IDENTIFY TOP PERFORMING STUDENTS AND FINALLY, WRITE THE PROCESS DATA INTO A NEW CSV FILE

import csv

# READ STUDENT DATA, CALCULATE AVERAGES, IDENTIFY TOP PERFORMERS
def process_student_data(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            reader = csv.DictReader(infile)
            student_report = []
            top_average = 0.0
            top_students = []

            for row in reader:
                name = row['Name']
                math = int(row['Math'])
                science = int(row['Science'])
                english = int(row['English'])
                average = round((math + science + english) / 3, 2)
                status = "Pass" if average >= 60 else "Fail"

                student_report.append({
                    'Name': name,
                    'Math': math,
                    'Science': science,
                    'English': english,
                    'Average': average,
                    'Status': status
                })

                # Track top-performing students
                if average > top_average:
                    top_average = average
                    top_students = [name]
                elif average == top_average:
                    top_students.append(name)

        # WRITE PROCESSED REPORT TO NEW CSV
        with open(output_file, 'w', newline='') as outfile:
            fieldnames = ['Name', 'Math', 'Science', 'English', 'Average', 'Status']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(student_report)
            print(f"✅ Student report generated in '{output_file}' successfully.\n")

        # Print top performer(s)
        print(f"🎯 Top-performing student(s) with average score {top_average}:")
        for student in top_students:
            print(f" - {student}")

    except FileNotFoundError:
        print(f"❌ Error: File '{input_file}' not found.")
    except KeyError as e:
        print(f"❌ Error: Missing or incorrect column name: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# MAIN PROGRAM ENTRY
if __name__ == "__main__":
    input_file = 'students.csv'      
    output_file = 'students_report.csv'      
    process_student_data(input_file, output_file)
