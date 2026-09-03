student_records = []
def display_welcome():
    print("\n" + "=" * 60)
    print("          WELCOME TO THE STUDENT DATA ORGANIZER!")
    print("=" * 60)
    print("This program manages student records using:")
    print("List, Tuple, Set and Dictionary.")
    print("You can add, display, update and delete student records.")
    print("=" * 60)

# ADD STUDENT

def add_student():
    print("\n--- Add Student ---")
    print("Enter student details:")

    # Student ID
    while True:
        try:
            student_id = int(input("Student ID: "))

            # Check whether ID already exists
            duplicate = False

            for student in student_records:
                if student["personal_info"][0] == student_id:
                    duplicate = True
                    break

            if duplicate:
                print("Error: Student ID already exists.")
                continue

            break

        except ValueError:
            print("Error: Student ID must be a number.")

    # Name
    while True:
        name = input("Name: ").strip()

        if name == "":
            print("Error: Name cannot be empty.")
        else:
            break

    # Age - type casting from string to integer
    while True:
        try:
            age = int(input("Age: "))

            if age <= 0:
                print("Error: Age must be greater than 0.")
            else:
                break

        except ValueError:
            print("Error: Please enter a valid age.")

    # Grade
    grade = input("Grade: ").strip()

    while grade == "":
        print("Error: Grade cannot be empty.")
        grade = input("Grade: ").strip()

    # Date of Birth
    date_of_birth = input("Date of Birth (YYYY-MM-DD): ").strip()

    while date_of_birth == "":
        print("Error: Date of birth cannot be empty.")
        date_of_birth = input("Date of Birth (YYYY-MM-DD): ").strip()

    # Subjects
    subjects_input = input(
        "Subjects (comma-separated): "
    )

    # Convert comma-separated string into a SET
    subjects = set()

    for subject in subjects_input.split(","):
        subject = subject.strip()

        if subject != "":
            subjects.add(subject)

    # Tuple containing unchangeable information
    # Student ID and Date of Birth are stored in a tuple.
    personal_info = (student_id, date_of_birth)

    # Dictionary containing student information
    student = {
        "personal_info": personal_info,
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": subjects
    }

    # Add dictionary to the main LIST
    student_records.append(student)

    print("\nStudent added successfully!")

# DISPLAY ALL STUDENTS
def display_all_students():
    print("\n--- Display All Students ---")

    if len(student_records) == 0:
        print("No student records available.")
        return

    for student in student_records:

        student_id = student["personal_info"][0]
        date_of_birth = student["personal_info"][1]

        # Formatted output using f-string
        subjects = ", ".join(sorted(student["subjects"]))

        print("\nStudent ID: {}".format(student_id))
        print(f"Name: {student['name']}")
        print("Age: %d" % student["age"])
        print(f"Grade: {student['grade']}")
        print(f"Date of Birth: {date_of_birth}")
        print(f"Subjects: {subjects}")
        print("-" * 50)
# UPDATE STUDENT INFORMATION
def update_student():
    print("\n--- Update Student Information ---")

    if len(student_records) == 0:
        print("No student records available.")
        return

    try:
        student_id = int(input("Enter Student ID to update: "))
    except ValueError:
        print("Error: Student ID must be a number.")
        return

    selected_student = None

    # Search student using Student ID
    for student in student_records:
        if student["personal_info"][0] == student_id:
            selected_student = student
            break

    if selected_student is None:
        print("Student not found.")
        return

    print("\nStudent found.")
    print("Name:", selected_student["name"])
    print("Age:", selected_student["age"])
    print("Grade:", selected_student["grade"])
    print(
        "Subjects:",
        ", ".join(sorted(selected_student["subjects"]))
    )

    print("\nWhat would you like to update?")
    print("1. Name")
    print("2. Age")
    print("3. Grade")
    print("4. Subjects")

    choice = input("Enter your choice: ")

    if choice == "1":

        new_name = input("Enter new name: ").strip()

        if new_name == "":
            print("Error: Name cannot be empty.")
        else:
            selected_student["name"] = new_name
            print("Name updated successfully.")

    elif choice == "2":

        try:
            new_age = int(input("Enter new age: "))

            if new_age <= 0:
                print("Error: Age must be greater than 0.")
            else:
                # Demonstrates mutability of dictionary/list data
                selected_student["age"] = new_age
                print("Age updated successfully.")

        except ValueError:
            print("Error: Age must be a number.")

    elif choice == "3":

        new_grade = input("Enter new grade: ").strip()

        if new_grade == "":
            print("Error: Grade cannot be empty.")
        else:
            selected_student["grade"] = new_grade
            print("Grade updated successfully.")

    elif choice == "4":

        new_subjects_input = input(
            "Enter new subjects (comma-separated): "
        )

        new_subjects = set()

        for subject in new_subjects_input.split(","):
            subject = subject.strip()

            if subject != "":
                new_subjects.add(subject)

        # Update mutable SET
        selected_student["subjects"] = new_subjects

        print("Subjects updated successfully.")

    else:
        print("Invalid choice.")


# DELETE STUDENT
def delete_student():
    print("\n--- Delete Student ---")

    if len(student_records) == 0:
        print("No student records available.")
        return

    try:
        student_id = int(input("Enter Student ID to delete: "))
    except ValueError:
        print("Error: Student ID must be a number.")
        return

    student_found = False

    # Find student by ID
    for index in range(len(student_records)):

        if student_records[index]["personal_info"][0] == student_id:

            # del keyword is used as required
            del student_records[index]

            student_found = True

            print("Student deleted successfully.")
            break

    if not student_found:
        print("Student not found.")
# DISPLAY SUBJECTS OFFERED

def display_subjects():
    print("\n--- Display Subjects Offered ---")

    if len(student_records) == 0:
        print("No student records available.")
        return

    # Set is used to ensure unique subjects
    all_subjects = set()

    for student in student_records:
        all_subjects.update(student["subjects"])

    if len(all_subjects) == 0:
        print("No subjects available.")
        return

    print("Unique Subjects Offered:")

    for subject in sorted(all_subjects):
        print("-", subject)
# MAIN MENU

def display_menu():
    print("\n" + "=" * 40)
    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    print("=" * 40)
# MAIN PROGRAM
def main():

    display_welcome()

    while True:

        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":

            add_student()

        elif choice == "2":

            display_all_students()

        elif choice == "3":

            update_student()

        elif choice == "4":

            delete_student()

        elif choice == "5":

            display_subjects()

        elif choice == "6":

            print("\nThank you for using the Student Data Organizer!")
            print("Program exited successfully.")
            break

        else:

            print("\nInvalid choice.")
            print("Please select an option from 1 to 6.")

# PROGRAM START
if __name__ == "__main__":
    main()