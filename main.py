# from model import Student
# from view import StudentView
# from controller import StudentController

# if __name__ == "__main__":
#     file_path = "studentRecord.csv"
#     controller = StudentController(file_path)
#     view = StudentView()

#     while True:
#         print("Choose operation:")
#         print("1. Create student")
#         print("2. Read student")
#         print("3. Update student")
#         print("4. Delete student")
#         print("5. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             name, age, email, department, dob, phone = view.input_student_details()
#             student = Student(name, age, email, department, dob, phone)
#             controller.create_student(student)
#             print("Student created successfully.")
#         elif choice == "2":
#             id = int(input("Enter student ID: "))
#             student = controller.get_student_by_id(id)
#             view.display_student(student)
#         elif choice == "3":
#             id = int(input("Enter student ID to update: "))
#             student = controller.get_student_by_id(id)
#             if student:
#                 name, age, email, department, dob, phone = view.input_student_details()
#                 student.name = name
#                 student.age = age
#                 student.email = email
#                 student.department = department
#                 student.dob = dob
#                 student.phone = phone
#                 controller.update_student(student)
#                 print("Student updated successfully.")
#             else:
#                 print("Student not found.")
#         elif choice == "4":
#             id = int(input("Enter student ID to delete: "))
#             if controller.delete_student(id):
#                 print("Student deleted successfully.")
#             else:
#                 print("Student not found.")
#         elif choice == "5":
#             print("Exiting program...")
#             break
#         else:
#             print("Invalid choice. Please enter a number between 1 and 5.")




from controller import StudentController

if __name__ == "__main__":
    controller = StudentController()
    controller.show_menu()
