import csv
import os

FILE_NAME = "students.csv"
FIELDNAMES = ["ID", "Name", "Age", "Course", "Email"]


# Create CSV file if it does not exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()


# Add a new student
def add_student():
    try:
        student_id = input("Enter Student ID: ").strip()
        name = input("Enter Student Name: ").strip()
        age = int(input("Enter Age: "))
        course = input("Enter Course: ").strip()
        email = input("Enter Email: ").strip()

        if not student_id or not name or not course or not email:
            print("Error: All fields are required.")
            return

        if age <= 0:
            print("Error: Age must be greater than zero.")
            return

        students = read_students()

        for student in students:
            if student["ID"] == student_id:
                print("Error: Student ID already exists.")
                return

        student = {
            "ID": student_id,
            "Name": name,
            "Age": age,
            "Course": course,
            "Email": email
        }

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writerow(student)

        print("Student added successfully!")

    except ValueError:
        print("Error: Please enter a valid number for age.")
    except OSError as error:
        print(f"File error: {error}")


# Read all student records
def read_students():
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)

    except FileNotFoundError:
        create_file()
        return []

    except OSError as error:
        print(f"File error: {error}")
        return []


# View all students
def view_students():
    students = read_students()

    if not students:
        print("No student records found.")
        return

    print("\n========== STUDENT RECORDS ==========")

    for student in students:
        print(f"\nStudent ID : {student['ID']}")
        print(f"Name       : {student['Name']}")
        print(f"Age        : {student['Age']}")
        print(f"Course     : {student['Course']}")
        print(f"Email      : {student['Email']}")

    print("\n=====================================")


# Search for a student
def search_student():
    student_id = input("Enter Student ID to search: ").strip()
    students = read_students()

    for student in students:
        if student["ID"] == student_id:
            print("\nStudent Found!")
            print(f"ID     : {student['ID']}")
            print(f"Name   : {student['Name']}")
            print(f"Age    : {student['Age']}")
            print(f"Course : {student['Course']}")
            print(f"Email  : {student['Email']}")
            return

    print("Student not found.")


# Update a student record
def update_student():
    student_id = input("Enter Student ID to update: ").strip()
    students = read_students()

    for student in students:
        if student["ID"] == student_id:
            print("Enter the updated details.")

            name = input(
                f"Name [{student['Name']}]: "
            ).strip()

            age_input = input(
                f"Age [{student['Age']}]: "
            ).strip()

            course = input(
                f"Course [{student['Course']}]: "
            ).strip()

            email = input(
                f"Email [{student['Email']}]: "
            ).strip()

            try:
                if age_input:
                    age = int(age_input)

                    if age <= 0:
                        print("Error: Age must be greater than zero.")
                        return

                    student["Age"] = str(age)

            except ValueError:
                print("Error: Age must be a valid number.")
                return

            if name:
                student["Name"] = name

            if course:
                student["Course"] = course

            if email:
                student["Email"] = email

            save_students(students)
            print("Student record updated successfully!")
            return

    print("Student not found.")


# Save all student records
def save_students(students):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(students)


# Delete a student record
def delete_student():
    student_id = input("Enter Student ID to delete: ").strip()
    students = read_students()

    updated_students = [
        student for student in students
        if student["ID"] != student_id
    ]

    if len(updated_students) == len(students):
        print("Student not found.")
        return

    save_students(updated_students)
    print("Student deleted successfully!")


# Main menu
def main():
    create_file()

    while True:
        print("\n======================================")
        print("   STUDENT RECORD MANAGEMENT SYSTEM")
        print("======================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("======================================")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank you for using the Student Record Management System!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


# Run the program
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram stopped.")
    except OSError as error:
        print(f"An unexpected file error occurred: {error}")