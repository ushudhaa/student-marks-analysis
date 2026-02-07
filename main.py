# Student Marks Analysis using Python

students = [
    {"name": "Amit", "math": 78, "science": 85, "english": 74},
    {"name": "Sita", "math": 88, "science": 90, "english": 92},
    {"name": "Ram", "math": 65, "science": 70, "english": 68},
    {"name": "Gita", "math": 92, "science": 89, "english": 95}
]

# Function to calculate total and average marks for each student
def calculate_results(students):
    for student in students:
        total = student["math"] + student["science"] + student["english"]
        average = total / 3
        student["total"] = total
        student["average"] = round(average, 2)

# Function to find topper in a subject
def subject_topper(students, subject):
    topper = students[0]
    for student in students:
        if student[subject] > topper[subject]:
            topper = student
    return topper["name"], topper[subject]

# Function to calculate class average for each subject
def class_average(students, subject):
    total = 0
    for student in students:
        total += student[subject]
    return round(total / len(students), 2)

# Function to assign pass/fail status
def assign_status(students, pass_mark=40):
    for student in students:
        if (
            student["math"] >= pass_mark and
            student["science"] >= pass_mark and
            student["english"] >= pass_mark
        ):
            student["status"] = "Pass"
        else:
            student["status"] = "Fail"

# Function to rank students based on total marks
def rank_students(students):
    students.sort(key=lambda x: x["total"], reverse=True)

# ------------------ MAIN PROGRAM ------------------

calculate_results(students)
assign_status(students)
rank_students(students)

print("📊 STUDENT PERFORMANCE REPORT\n")

for idx, student in enumerate(students, start=1):
    print(f"Rank {idx}")
    print(f"Name     : {student['name']}")
    print(f"Total    : {student['total']}")
    print(f"Average  : {student['average']}")
    print(f"Status   : {student['status']}")
    print("-" * 30)

# Subject toppers
print("\n🏆 SUBJECT TOPPERS")
for subject in ["math", "science", "english"]:
    name, marks = subject_topper(students, subject)
    print(f"{subject.capitalize()} Topper: {name} ({marks})")

# Class averages
print("\n📈 CLASS AVERAGES")
for subject in ["math", "science", "english"]:
    avg = class_average(students, subject)
    print(f"{subject.capitalize()} Average: {avg}")
