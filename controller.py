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
                name, department, email, phone_number, dob, age = self.view.get_student_input()
                student = Student(name, department, email, phone_number, dob, age)
                self.model.add_student(student)
            elif choice == '4':
                email = self.view.get_student_email("Enter student email: ")
                updated_student = Student(*self.view.get_student_input())
                if self.model.update_student(email, updated_student):
                    print("Student details updated successfully.")
                else:
                    print("Failed to update student details. Student email not found.")
            elif choice == '5':
                email = self.view.get_student_email("Enter student email: ")
                if self.model.delete_student(email):
                    print("Student deleted successfully.")
                else:
                    print("Failed to delete student. Student email not found.")
            elif choice == '6':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    controller = StudentController()
    controller.show_menu()
