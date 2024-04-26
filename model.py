import csv
import os
from functools import lru_cache

class Student:
    def __init__(self, name, department, email, phone_number, dob, age):
        self.id = None
        self.name = name
        self.department = department
        self.email = email
        self.phone_number = phone_number
        self.dob = dob
        self.age = age

class StudentModel:
    def __init__(self):
        self.file_path = "studentRecord.csv"
        self.students = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    student = Student(*row[1:])
                    student.id = int(row[0])
                    self.students.append(student)

    # Decorate the method with LRU cache to cache the result
    @lru_cache(maxsize=None)
    def get_all_students(self):
        return self.students

    def save_data(self):
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Student Id", "Name", "Department", "Email", "Phone Number", "DOB", "Age"])
            for student in self.students:
                writer.writerow([student.id, student.name, student.department, student.email, student.phone_number, student.dob, student.age])

    def generate_id(self):
        if not self.students:
            return 1
        else:
            return self.students[-1].id + 1

    def add_student(self, student):
        student.id = self.generate_id()
        self.students.append(student)
        self.save_data()

    def update_student(self, student_email, updated_student):
        for student in self.students:
            if student.email == student_email:
                student.name = updated_student.name
                student.department = updated_student.department
                student.email = updated_student.email
                student.phone_number = updated_student.phone_number
                student.dob = updated_student.dob
                student.age = updated_student.age
                self.save_data()
                return True
        return False

    def delete_student(self, student_email):
        for student in self.students:
            if student.email == student_email:
                self.students.remove(student)
                self.save_data()
                return True
        return False

    def get_all_students(self):
        return self.students

    def get_student_by_email(self, student_email):
        for student in self.students:
            if student.email == student_email:
                return student
        return None

    def delete_students_by_department(self, department):
        students_to_delete = [student for student in self.students if student.department == department]
        if students_to_delete:
            self.students = [student for student in self.students if student not in students_to_delete]
            self.save_data()
            return True
        else:
            return False