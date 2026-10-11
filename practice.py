import csv
import json
import os


def greet(name):
    return"Hello " + name

message=greet("Udita")
print(message)


square=lambda x:x*x
print(square(5))

numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print(squares)

with open("test.txt", "w") as file:
    file.write("Hello, this is my Python file handling practice.")

print("File created successfully.")

with open("test.txt", "r") as file:
    content = file.read()

print(content)

students = [
    ["ID", "Name", "Age", "Course", "Email"],
    [101, "Udita", 22, "Data Science", "udita@gmail.com"],
    [102, "Riya", 21, "Computer Science", "riya@gmail.com"]
]

# Write data to a CSV file
with open("practice_students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("CSV file created successfully!")

# Read data from the CSV file
with open("practice_students.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)

except ValueError:
    print("Please enter a valid number.")

try:
    number = int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Invalid input.")

finally:
    print("Program completed.")