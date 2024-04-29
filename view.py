import re
from datetime import datetime

class StudentView:
    def show_all_students(self, students, page_number, page_size):
        start_index = (page_number - 1) * page_size
        end_index = start_index + page_size
        students_to_display = students[start_index:end_index]

        print("ID    | Name            | Department | Email                  | Phone Number | DOB         | Age")
        print("-" * 100)  # Line separator
        for student in students_to_display:
            print(f"{student.id:<6}| {student.name:<16}| {student.department:<11}| {student.email:<23}| {student.phone_number:<13}| {student.dob:<12}| {student.age}")

    def show_student(self, student):
        if student:
            print("----- Student Details -----")
            print("ID    | Name            | Department | Email                  | Phone Number | DOB         | Age")
            print("-" * 100)  # Line separator
            print(f"{student.id:<6}| {student.name:<16}| {student.department:<11}| {student.email:<23}| {student.phone_number:<13}| {student.dob:<12}| {student.age}")
        else:
            print("Student not found.")

    def show_pagination(self, page_number, total_pages):
        print(f"Page {page_number}/{total_pages}")

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
        print("3. View Students by ID Range")  # Updated option
        print("4. Add New Student")
        print("5. Update Student Details")
        print("6. Delete Student")
        print("7. Delete Students by Department")
        print("8. Delete Students by Range")
        print("9. Delete Students by DOB Year Range")  # New option
        print("10. Exit")
        print("11. Next Page")
        print("12. Previous Page")  # Updated option

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
                age = self.calculate_age(dob)
                if 18 <= age <= 22:
                    return dob
                else:
                    print("Invalid date of birth. Age should be between 18 and 22.")
            except ValueError:
                print("Invalid date of birth format. Please use YYYY-MM-DD.")

    def calculate_age(self, dob):
        dob_date = datetime.strptime(dob, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
        return age
