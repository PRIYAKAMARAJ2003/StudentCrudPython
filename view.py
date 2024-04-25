import re
from datetime import datetime

class StudentView:
    def show_all_students(self, students):
        print("ID    | Name            | Department | Email                  | Phone Number | DOB         | Age")
        print("-" * 100)  # Line separator
        for student in students:
            print(f"{student.id:<6}| {student.name:<16}| {student.department:<11}| {student.email:<23}| {student.phone_number:<13}| {student.dob:<12}| {student.age}")

    def show_student(self, student):
        if student:
            print("----- Student Details -----")
            print("ID    | Name            | Department | Email                  | Phone Number | DOB         | Age")
            print("-" * 100)  # Line separator
            print(f"{student.id:<6}| {student.name:<16}| {student.department:<11}| {student.email:<23}| {student.phone_number:<13}| {student.dob:<12}| {student.age}")
        else:
            print("Student not found.")


    def get_student_input(self, existing_emails):
        name = self.get_valid_name("Enter student name: ")
        department = self.get_valid_department("Enter student department: ")
        email = self.get_valid_email("Enter student email: ", existing_emails)
        phone_number = self.get_valid_phone_number("Enter student phone number: ")
        dob = self.get_valid_dob("Enter student date of birth (YYYY-MM-DD): ")
        age = self.calculate_age(dob)
        return name, department, email, phone_number, dob, age

    def get_student_id(self):
        return int(input("Enter student ID: "))

    def get_student_email(self, prompt):
        return input(prompt)

    def show_menu(self):
        print("\n===== Student CRUD =====")
        print("1. View All Students")
        print("2. View Student Details")
        print("3. Add New Student")
        print("4. Update Student Details")
        print("5. Delete Student")
        print("6. Delete Students by Department")  # New option
        print("7. Exit")  # Adjusted option


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

    def get_valid_email(self, prompt, existing_emails):
        while True:
            email = input(prompt)
            if re.match(r"[^@]+@[^@]+\.[^@]+", email) and email.endswith("@gmail.com"):
                if email not in existing_emails:
                    return email
                else:
                    print("Email already exists. Please enter a unique email.")
            else:
                print("Invalid email. Email should be in the format example@gmail.com")

    def get_valid_phone_number(self, prompt):
        while True:
            phone_number = input(prompt)
            if phone_number.isdigit() and len(phone_number) == 10:
                return phone_number
            else:
                print("Invalid phone number. Phone number should be 10 digits.")

    def get_valid_dob(self, prompt):
        while True:
            dob = input(prompt)
            try:
                dob_date = datetime.strptime(dob, "%Y-%m-%d")
                if self.calculate_age(dob) >= 18:
                    return dob
                else:
                    print("Invalid date of birth. Age should be 18 or older.")
            except ValueError:
                print("Invalid date of birth format. Please use YYYY-MM-DD.")

    def calculate_age(self, dob):
        dob_date = datetime.strptime(dob, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
        return age
