from model import Student, StudentModel
from view import StudentView

class StudentController:
    def __init__(self):
        self.model = StudentModel()
        self.view = StudentView()

    def show_menu(self):
        while True:
            self.view.show_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.view.show_all_students(self.model.get_all_students())
            elif choice == '2':
                email = self.view.get_student_email("Enter student email: ")
                student = self.model.get_student_by_email(email)
                self.view.show_student(student)
            elif choice == '3':
                existing_emails = [student.email for student in self.model.get_all_students()]
                name, department, email, phone_number, dob, age = self.view.get_student_input(existing_emails)
                student = Student(name, department, email, phone_number, dob, age)
                if email not in existing_emails:
                    self.model.add_student(student)
                    print("Student added successfully.")
                else:
                    print("Failed to add student. Email already exists.")
            elif choice == '4':
                email = self.view.get_student_email("Enter student email: ")
                updated_student = Student(*self.view.get_student_input())
                if email not in [student.email for student in self.model.get_all_students()]:
                    if self.model.update_student(email, updated_student):
                        print("Student details updated successfully.")
                    else:
                        print("Failed to update student details. Student email not found.")
                else:
                    print("Failed to update student details. Email already exists.")
            elif choice == '5':
                email = self.view.get_student_email("Enter student email: ")
                if email not in [student.email for student in self.model.get_all_students()]:
                    if self.model.delete_student(email):
                        print("Student deleted successfully.")
                    else:
                        print("Failed to delete student. Student email not found.")
                else:
                    print("Failed to delete student. Email already exists.")
            elif choice == '6':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    controller = StudentController()
    controller.show_menu()
