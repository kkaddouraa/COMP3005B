
import psycopg2

# Kareem Kaddoura
# Student #: 101140255
# COMP 3005 B Assignment 3 Q1

# Connection to PostgreSQL
connection = psycopg2.connect(
    database = "A3Q1",
    host = "localhost",
    user="postgres",
    password="kareem872001",
    port="5432"
)

cursor = connection.cursor()

# Application Functions
"""
Retrieves and displays all records from the students table.
"""
def getAllStudents():
    try:
        cursor.execute("SELECT * FROM students")
        print(cursor.fetchall())
    except psycopg2.Error as err:
        print(err.pgerror)
        exit()

"""
Inserts a new student record into the students table.
"""
def addStudent(first_name, last_name, email, enrollment_date):
    try:
        query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"
        data = (first_name, last_name, email, enrollment_date)
        cursor.execute(query, data)
        connection.commit()
    except psycopg2.Error as err:
        print(err.pgerror)
        exit()

"""
Updates the email address for a student with the specified student_id.
"""
def updateStudentEmail(student_id, new_email):
    try:
        query = "UPDATE students SET email = %s WHERE student_id = %s"
        data = (new_email, student_id)
        cursor.execute(query, data)
        connection.commit()
    except psycopg2.Error as err:
        print(err.pgerror)
        exit()

"""
Deletes the record of the student with the specified student_id.
"""
def deleteStudent(student_id):
    try:
        query = "DELETE FROM students WHERE student_id = %s"
        data = (student_id)
        cursor.execute(query, data)
        connection.commit()
    except psycopg2.Error as err:
        print(err.pgerror)
        exit()

def main():
    loop = True
    while loop:
        print("\nApplication Functions for the students Database\n")
        request = input(""" Please select which application you would like to use:
    1: Retrieve and display all records of the students table
    2: Insert a new student record
    3: Update the email address for an existing student
    4: Delete a student from the table
    5: Quit
    
    Selection: """)
        print("\n")
        if request == "1":
            getAllStudents()
        elif request == "2":
            addStudent(
                input("First Name: "),
                input("Last Name: "),
                input("Email: "),
                input("Enrollment Date (YYYY-MM-DD): "),
            )
        elif request == "3":
            updateStudentEmail(input("Student ID: "), input("New Email: "))
        elif request == "4":
            deleteStudent(input("Student ID: "))
        elif request == "5":
            connection.close()
            loop = False
        else:
            print("Incorrect input, please try again.")

main()