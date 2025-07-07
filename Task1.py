#  Task 1: Create a Dictionary of Student Marks

student_marks = {'Seema': 75, 'Sunil': 65, 'Akash': 35, 'Radha': 52}

name = str(input("Please Enter the name of Student : "))

if name in student_marks:
    print(f"{name}'s marks are: {student_marks[name]}")
else :
    print(f"Student not found .")




