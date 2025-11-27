class DuplicateStudentError(ValueError):
    """Raised when a duplicate of student was found"""
    pass

class BadNameError(ValueError):
    """Raised when the student name is wrong"""
    pass

class InvalidInput(ValueError):
    """Raised when user enter a wrong input"""
    pass

def check_student_name(name: str) -> bool:
    """Function to check the validity of the entered student name."""
    return not any(character.isdigit() for character in name) and len(name) != 0

def get_student_name() -> str:
    """Function that asks the student name from user and checks it for valid."""
    student_name = " ".join([part.capitalize() for part in input("Enter student name: ").strip().split()])
    if not check_student_name(student_name):
        raise BadNameError("Enter a valid student name")
    return student_name

def add_a_new_student(students: list) -> None:
    """Function for adding a new student to the student list."""
    try:
        student_name = get_student_name()
        if not any(student_name == student["name"] for student in students):
            students.append({"name": student_name, "grades": []})
        else:
            raise DuplicateStudentError(f"Student '{student_name}' is already in list")
    except DuplicateStudentError as e:
        print(str(e))
    except BadNameError as e:
        print(str(e))

def add_grades(students: list) -> None:
    """Function for adding grades for a student."""
    try:
        student_name = get_student_name()
        is_found = False
        for student in students:
            if student["name"] == student_name:
                is_found = True
                while True:
                    try:
                        user_input = input("Enter a grade (or 'done' to finish): ")
                        if str(user_input).lower() == "done":
                            break
                        user_input = int(user_input)
                        if user_input >= 0 and user_input <= 100:
                            student["grades"].append(user_input)
                        else:
                            print("Grade must be between 0 and 100.")
                    except ValueError as e:
                        print("Invalid input. Please enter a number.")
        if not is_found:
            print("There is no student with this name")
    except BadNameError as e:
        print(str(e))

def show_report(students: list) -> None:
    """
    The function displays a report for all students in the list\n,
    including the average grades of each, the minimum and maximum values\n
    ​​of the average grades, and the average of the averages.
    """
    if students:
        print("--- Student Report ---")
    else:
        print("There is no students in list")
        return
    avgs = []
    for student in students:
        try:
            grades_avg = round(sum(student["grades"]) / len(student["grades"]), 1)
            avgs.append(grades_avg)
        except ZeroDivisionError:
            grades_avg = "N/A"
        print(f"{student["name"]}'s average grade is {grades_avg}.")
    if avgs:
        print("----------------------------")
        print(f"Max Average: {max(avgs)}")    
        print(f"Min Average: {min(avgs)}")
        print(f"Overall Average: {round(sum(avgs) / len(avgs), 1)}")

def find_top_performer(students: list) -> dict | None:
    """
        The function searches for a student from the list\n
        with the maximum average grade value, using lambda functions.
    """
    if not students:
        print("There is no students in list")
        return None
    students_with_grades = [s for s in students if s["grades"]]
    if not students_with_grades:
        print("There is no students with grades in list")
        return None
    top_student = max(
        students_with_grades,
        key=lambda student: sum(student["grades"]) / len(student["grades"])
    )
    avg_grade = round(
        sum(top_student["grades"]) / len(top_student["grades"]), 
        1
    )
    print(f"The student with the highest average is {top_student['name']} with a grade of {avg_grade}.")
    return top_student

def main() -> None:
    """
        Program manages and analyzes student grades, using concepts like\n
        collictions, functions, error handling and loops.
    """
    # Create an empty students list to fill
    students = []
    # Infinity loop for user choice
    while True:
        # Print menu for user
        print("--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add a new grades for a student")
        print("3. Show report (all students)")
        print("4. Find top rerformer")
        print("5. Exit")
        
        # Error handling
        try:
            user_input = int(input("Enter your choice: "))
            if user_input < 1 or user_input > 5:
                print("Choice must be between 1 and 5.")
                continue
            if user_input == 1:
                add_a_new_student(students)
            elif user_input == 2:
                add_grades(students)
            elif user_input == 3:
                show_report(students)
            elif user_input == 4:
                find_top_performer(students)
            elif user_input == 5:
                print("Exiting program.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\nExiting program.")
            break

if __name__ == "__main__":
    main()