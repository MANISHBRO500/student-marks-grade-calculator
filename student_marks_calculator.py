def get_valid_mark(subject_name):
    while True:
        try:
            mark = float(input(f"Enter marks for {subject_name}: "))
            if 0 <= mark <= 100:
                return mark
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"


def student_result():
    print("\nStudent Marks and Grade Calculator")
    student_name = input("Enter student name: ").strip()

    subjects = ["Math", "Science", "English", "History", "Computer"]
    marks = []

    for subject in subjects:
        marks.append(get_valid_mark(subject))

    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)

    passed_subjects = sum(1 for mark in marks if mark >= 40)
    result = "PASS" if passed_subjects == len(marks) else "FAIL"

    print("\n--- Report ---")
    print(f"Student Name: {student_name}")
    for subject, mark in zip(subjects, marks):
        print(f"{subject}: {mark}")

    print(f"Total Marks: {total}/{len(subjects) * 100}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
    print(f"Result: {result}")

    if result == "PASS":
        print("Excellent! Student passed all subjects.")
    else:
        print("Student needs improvement in some subjects.")


if __name__ == "__main__":
    student_result()
