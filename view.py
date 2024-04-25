# class StudentView:
#     def show_all_students(self, students):
#         print("----- All Students -----")
#         for student in students:
#             print(f"ID: {student.id}, Name: {student.name}, Department: {student.department}, Email: {student.email}, Phone Number: {student.phone_number}, DOB: {student.dob}, Age: {student.age}")

#     def show_student(self, student):
#         if student:
#             print("----- Student Details -----")
#             print(f"ID: {student.id}, Name: {student.name}, Department: {student.department}, Email: {student.email}, Phone Number: {student.phone_number}, DOB: {student.dob}, Age: {student.age}")
#         else:
#             print("Student not found.")

#     def get_student_input(self):
#         name = input("Enter student name: ")
#         department = input("Enter student department: ")
#         email = input("Enter student email: ")
#         phone_number = input("Enter student phone number: ")
#         dob = input("Enter student date of birth (YYYY-MM-DD): ")
#         age = input("Enter student age: ")
#         return name, department, email, phone_number, dob, age

#     def get_student_id(self):
#         return int(input("Enter student ID: "))

#     def show_menu(self):
#         print("\n===== Student Management System =====")
#         print("1. View All Students")
#         print("2. View Student Details")
#         print("3. Add New Student")
#         print("4. Update Student Details")
#         print("5. Delete Student")
#         print("6. Exit")


import re

class StudentView:
    def show_all_students(self, students):
        print("----- All Students -----")
        for student in students:
            print(f"ID: {student.id}, Name: {student.name}, Department: {student.department}, Email: {student.email}, Phone Number: {student.phone_number}, DOB: {student.dob}, Age: {student.age}")

    def show_student(self, student):
        if student:
            print("----- Student Details -----")
            print(f"ID: {student.id}, Name: {student.name}, Department: {student.department}, Email: {student.email}, Phone Number: {student.phone_number}, DOB: {student.dob}, Age: {student.age}")
        else:
            print("Student not found.")

    def get_student_input(self):
        name = self.get_valid_name("Enter student name: ")
        department = self.get_valid_department("Enter student department: ")
        email = self.get_valid_email("Enter student email: ")
        phone_number = self.get_valid_phone_number("Enter student phone number: ")
        dob = input("Enter student date of birth (YYYY-MM-DD): ")
        age = input("Enter student age: ")
        return name, department, email, phone_number, dob, age

    def get_student_id(self):
        return int(input("Enter student ID: "))

    def get_student_email(self, prompt):
        return input(prompt)

    def show_menu(self):
        print("\n===== Student Management System =====")
        print("1. View All Students")
        print("2. View Student Details")
        print("3. Add New Student")
        print("4. Update Student Details")
        print("5. Delete Student")
        print("6. Exit")

    def get_valid_name(self, prompt):
        while True:
            name = input(prompt)
            if name.replace(" ", "").isalpha():
                return name
            else:
                print("Invalid name. Name should only contain alphabets and spaces.")

    def get_valid_department(self, prompt):
        while True:
            department = input(prompt)
            if department.replace(" ", "").isalpha():
                return department
            else:
                print("Invalid department. Department should only contain alphabets and spaces.")

    def get_valid_email(self, prompt):
        while True:
            email = input(prompt)
            if re.match(r"[^@]+@[^@]+\.[^@]+", email) and email.endswith("@gmail.com"):
                return email
            else:
                print("Invalid email. Email should be in the format example@gmail.com")

    def get_valid_phone_number(self, prompt):
        while True:
            phone_number = input(prompt)
            if phone_number.isdigit() and len(phone_number) == 10:
                return phone_number
            else:
                print("Invalid phone number. Phone number should be 10 digits.")
