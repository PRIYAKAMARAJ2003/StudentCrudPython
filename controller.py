# from model import Student, StudentModel
# from view import StudentView

# class StudentController:
#     def __init__(self):
#         self.model = StudentModel()
#         self.view = StudentView()
#         self.page_size = 2
#         self.current_page = 1

#     def show_menu(self):
#         existing_emails = [student.email for student in self.model.get_all_students()]
#         while True:
#             self.view.show_menu()
#             choice = input("Enter your choice: ")
#             if choice == '1':
#                 students = self.model.get_all_students()
#                 total_students = len(students)
#                 total_pages = total_students // self.page_size + (1 if total_students % self.page_size > 0 else 0)
#                 self.view.show_all_students(students, self.current_page, self.page_size)
#                 self.view.show_pagination(self.current_page, total_pages)
#             elif choice == '2':
#                 email = self.view.get_student_email("Enter student email: ")
#                 student = self.model.get_student_by_email(email)
#                 self.view.show_student(student)
#             elif choice == '3':
#                 name, department, email, phone_number, dob, age = self.view.get_student_input(existing_emails)
#                 student = Student(name, department, email, phone_number, dob, age)
#                 self.model.add_student(student)
#             elif choice == '4':
#                 email = self.view.get_student_email("Enter student email: ")
#                 updated_student = Student(*self.view.get_student_input(existing_emails))
#                 if self.model.update_student(email, updated_student):
#                     print("Student details updated successfully.")
#                 else:
#                     print("Failed to update student details. Student email not found.")
#             elif choice == '5':
#                 email = self.view.get_student_email("Enter student email: ")
#                 if self.model.delete_student(email):
#                     print("Student deleted successfully.")
#                 else:
#                     print("Failed to delete student. Student email not found.")
#             elif choice == '6':
#                 department = input("Enter department to delete: ")
#                 if self.model.delete_students_by_department(department):
#                     print("Students in the department deleted successfully.")
#                 else:
#                     print("No students found in the given department.")
#             elif choice == '7':
#                 start_id = int(input("Enter start ID for range delete: "))
#                 end_id = int(input("Enter end ID for range delete: "))
#                 if self.model.delete_students_by_id_range(start_id, end_id):
#                     print("Students in the specified ID range deleted successfully.")
#                 else:
#                     print("No students found in the specified ID range.")
#             elif choice == '8':
#                 start_year = int(input("Enter start year for DOB range delete: "))
#                 end_year = int(input("Enter end year for DOB range delete: "))
#                 if self.model.delete_students_by_dob_year_range(start_year, end_year):
#                     print("Students in the specified DOB year range deleted successfully.")
#                 else:
#                     print("No students found in the specified DOB year range.")
#             elif choice == '9':
#                 print("Exiting the program.")
#                 break
#             elif choice == '10':
#                 students = self.model.get_all_students()
#                 total_students = len(students)
#                 total_pages = total_students // self.page_size + (1 if total_students % self.page_size > 0 else 0)
#                 if self.current_page < total_pages:
#                     self.current_page += 1
#                     self.view.show_all_students(students, self.current_page, self.page_size)
#                     self.view.show_pagination(self.current_page, total_pages)
#                 else:
#                     print("No more pages available.")
#             elif choice == '11':
#                 if self.current_page > 1:
#                     self.current_page -= 1
#                     students = self.model.get_all_students()
#                     total_students = len(students)
#                     total_pages = total_students // self.page_size + (1 if total_students % self.page_size > 0 else 0)
#                     self.view.show_all_students(students, self.current_page, self.page_size)
#                     self.view.show_pagination(self.current_page, total_pages)
#                 else:
#                     print("Already on the first page.")
#             else:
#                 print("Invalid choice. Please enter a valid option.")

# if __name__ == "__main__":
#     controller = StudentController()
#     controller.show_menu()


from model import Student, StudentModel
from view import StudentView

class StudentController:
    def __init__(self):
        self.model = StudentModel()
        self.view = StudentView()
        self.page_size = 2
        self.current_page = 1

    def show_menu(self):
        existing_emails = [student.email for student in self.model.get_all_students()]
        while True:
            self.view.show_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                students = self.model.get_all_students()
                total_students = len(students)
                total_pages = total_students // self.page_size + (1 if total_students % self.page_size > 0 else 0)
                self.view.show_all_students(students, self.current_page, self.page_size)
                self.view.show_pagination(self.current_page, total_pages)
            elif choice == '2':
                email = self.view.get_student_email("Enter student email: ")
                student = self.model.get_student_by_email(email)
                self.view.show_student(student)
            elif choice == '3':
                start_id = int(input("Enter start ID for range view: "))
                end_id = int(input("Enter end ID for range view: "))
                students_within_range = self.model.get_students_by_id_range(start_id, end_id)
                if students_within_range:
                    self.view.show_all_students(students_within_range, 1, len(students_within_range))
                else:
                    print("No students found in the specified ID range.")
            elif choice == '4':
                name, department, email, phone_number, dob, age = self.view.get_student_input(existing_emails)
                student = Student(name, department, email, phone_number, dob, age)
                self.model.add_student(student)
            elif choice == '5':
                email = self.view.get_student_email("Enter student email: ")
                updated_student = Student(*self.view.get_student_input(existing_emails))
                if self.model.update_student(email, updated_student):
                    print("Student details updated successfully.")
                else:
                    print("Failed to update student details. Student email not found.")
            elif choice == '6':
                email = self.view.get_student_email("Enter student email: ")
                if self.model.delete_student(email):
                    print("Student deleted successfully.")
                else:
                    print("Failed to delete student. Student email not found.")
            elif choice == '7':
                department = input("Enter department to delete: ")
                if self.model.delete_students_by_department(department):
                    print("Students in the department deleted successfully.")
                else:
                    print("No students found in the given department.")
            elif choice == '8':
                start_id = int(input("Enter start ID for range delete: "))
                end_id = int(input("Enter end ID for range delete: "))
                if self.model.delete_students_by_id_range(start_id, end_id):
                    print("Students in the specified ID range deleted successfully.")
                else:
                    print("No students found in the specified ID range.")
            elif choice == '9':
                start_year = int(input("Enter start year for DOB range delete: "))
                end_year = int(input("Enter end year for DOB range delete: "))
                if self.model.delete_students_by_dob_year_range(start_year, end_year):
                    print("Students in the specified DOB year range deleted successfully.")
                else:
                    print("No students found in the specified DOB year range.")
            elif choice == '10':
                print("Exiting the program.")
                break
            elif choice == '11':
                students = self.model.get_all_students()
                total_students = len(students)
                total_pages = total_students // self.page_size + (1 if total_students % self.page_size > 0 else 0)
                if self.current_page < total_pages:
                    self.current_page += 1
                    self.view.show_all_students(students, self.current_page, self.page_size)
                    self.view.show_pagination(self.current_page, total_pages)
                else:
                    print("No more pages available.")
            elif choice == '12':
                if self.current_page > 1:
                    self.current_page -= 1
                    students = self.model.get_all_students()
                    total_students = len(students)
                    total_pages = total_students // self.page_size + (1 if total_students % self.page_size > 0 else 0)
                    self.view.show_all_students(students, self.current_page, self.page_size)
                    self.view.show_pagination(self.current_page, total_pages)
                else:
                    print("Already on the first page.")
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    controller = StudentController()
    controller.show_menu()