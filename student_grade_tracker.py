# THE STUDENT GRADE TRACKER

def calculate_average(grades):
    total = sum(grades)
    return total / len(grades)

def get_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    print("\nWelcome to the Student Grade Tracker!\n")
    student_name = input("Enter student name: ")
    num_subjects = int(input("Enter number of subjects: "))
    
    grades = []
    for i in range(num_subjects):
        grade = float(input(f"Enter grade for subject {i+1}: "))
        grades.append(grade)
    
    average = calculate_average(grades)
    letter_grade = get_letter_grade(average)
    
    print(f"\nStudent Name: {student_name}")
    print(f"Average Grade: {average:.2f}")
    print(f"Letter Grade: {letter_grade}")
    
    if letter_grade == 'A':
        gpa = 4.0
    elif letter_grade == 'B':
        gpa = 3.0
    elif letter_grade == 'C':
        gpa = 2.0
    elif letter_grade == 'D':
        gpa = 1.0
    else:
        gpa = 0.0
    
    print(f"GPA: {gpa:.2f}")

if _name_ == "_main_":
    main()
