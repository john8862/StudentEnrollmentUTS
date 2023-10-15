import re
import random
import json
import colorama
from colorama import Fore, init, Style


class Student:
    def __init__(self, name, email, password, subject=[], from_file = False):
        self.name = name
        self.email = email
        self.password = password
        self.subject = subject
        #self.subject = []
        if not from_file:
            self.generate_student_id()
            self.save_students_file()

    def generate_student_id(self):
        global students

        # If there are no students, start with ID '000001'
        if not students:
            self.student_id = '000001'
            students.append(self)
            return

        # Extract all existing student IDs and sort them
        existing_ids = sorted([int(student.student_id) for student in students])

        # Find the first missing ID
        missing_id = None
        for i in range(1, existing_ids[-1] + 1):
            if i not in existing_ids:
                missing_id = i
                break

        # If a missing ID is found, use it. Otherwise, use the next number after the highest existing ID.
        if missing_id:
            self.student_id = str(missing_id).zfill(6)
        else:
            self.student_id = str(existing_ids[-1] + 1).zfill(6)

        students.append(self)
    @staticmethod
    def is_valid_email(email):
        email_pattern = r'(?i)[a-zA-Z0-9]+\.[a-zA-Z0-9]+@university\.com'
        return re.match(email_pattern, email)

    @staticmethod
    def is_valid_password(password):
        password_pattern = r'^[A-Z](?=.*\d.*\d.*\d)(?=.*[a-zA-Z].*[a-zA-Z].*[a-zA-Z].*[a-zA-Z]).*$'
        return re.match(password_pattern, password)

    @staticmethod
    def is_valid_subject(subject):
        subject_pattern = r'^[a-zA-Z ]*$'
        return re.match(subject_pattern, subject)
    
    def enrol_subject(self, subject):
        if len(self.subject) >= 4:
            print("You have already enrolled in 4 subjects. You cannot enrol in more.")
        else:
            random_number = str(random.randint(0, 999)).zfill(3)
            # 检查生成的数字是否重复
            while any(subject.endswith(f"_{random_number}") for subject in self.subject):
                random_number = str(random.randint(0, 999)).zfill(3)
            # 将随机数字添加到subject中
            subject_with_number = f"{random_number}.{subject}"
            mark = random.randint(25, 100)
            # 根据分数计算等级
            if mark < 50:
                grade = "Z"
            elif mark < 65:
                grade = "P"
            elif mark < 75:
                grade = "C"
            elif mark < 85:
                grade = "D"
            else:
                grade = "HD"

            subject_with_grade = f"{subject_with_number} - Mark: {mark}, Grade: {grade}"

            self.subject.append(subject_with_grade)
            print(f"You have successfully enrolled in [ {subject_with_number} ].")
            self.save_students_file()

    def remove_subject(self, subject):
        if subject in self.subject:
            self.subject.remove(subject)
            print(f"You have successfully removed [ {subject} ] from your enrolment list.")
            self.save_students_file()
        else:
            print(f"You are not enrolled in [ {subject} ].")

    def show_enrolment(self):
        print("You are currently enrolled in the following subjects:")
        for subject in self.subject:
            # 提取Mark和grade
            print(f"[ {subject} ]")


    def save_students_file(self):
        #__dict__ 能将每个 student 对象转换为字典形式
        data = [student.__dict__ for student in students]
        with open("students.data", "w") as file:
            #将 data 列表（它包含了所有学生的信息）转换为 JSON 格式，并写入到打开的文件中。
            json.dump(data, file, indent = 4)

    def change_password(self, new_password):
        if Student.is_valid_password(new_password):
            self.password = new_password
            print("Password successfully changed!")
            self.save_students_file()  # Save the updated password
        else:
            print("Invalid password format. Password must start with an uppercase letter, contain at least 5 letters, and have 3 or more digits.")


    def __str__(self):
        return f"Student ID: {self.student_id}\nName: {self.name}\nEmail: {self.email}\nPassword: {self.password}\n"

    def __repr__(self):
        return f"Student ID: {self.student_id}\nName: {self.name}\nEmail: {self.email}\nPassword: {self.password}\n"

students = []


class Admin:
    
    admins = []
    def __init__(self, username, password, from_file = False):
        self.username = username
        self.password = password
        if not from_file:
            self.save_admins_file()

    def save_admins_file(self):
        data = [admin.__dict__ for admin in Admin.admins]
        with open("admins.data", "w") as file:
            json.dump(data, file, indent = 4)

    def view_all_students():
        print(Fore.YELLOW + "Current student list:")
        for s in students:
            print(s)

    @staticmethod
    def list_students_by_all_grades():
        grade_dict = {"Z": [], "P": [], "C": [], "D": [], "HD": []}
        for student in students:
            for subject in student.subject:
                for grade in grade_dict.keys():
                    if f"Grade: {grade}" in subject:
                        grade_dict[grade].append(student)
                        break
        return grade_dict

    def partition_students_pass_fail():
        passed_students = []
        failed_students = []
        no_record_students = []
        for student in students:
            if not student.subject:
                no_record_students.append(student)
                continue
            passed = any("Grade: P" in subject or "Grade: C" in subject or "Grade: D" in subject or "Grade: HD" in subject for subject in student.subject)
            
            if passed:
                passed_students.append(student)
            else:
                failed_students.append(student)
        return passed_students, failed_students, no_record_students
    
    @staticmethod
    def remove_student(id):
        global students
        student_to_remove = None
        for student in students:
            if student.student_id == id:
                student_to_remove = student
                break

        if student_to_remove:
            students.remove(student_to_remove)
            print(f"Student with ID {id} has been removed.")
            # Save the updated list to the file
            student_to_remove.save_students_file()
        else:
            print(f"No student found with ID {id}.")
    
    @staticmethod
    def clear_all_students():
        global students
        confirmation = input("Are you sure you want to clear the entire student list? (yes/no): ").strip().lower()
        if confirmation == 'yes':
            students = []
            # Save the empty list to the file
            if students:
                students[0].save_students_file()
            print("All students have been removed.")
        else:
            print("Operation cancelled.")

def main():
    
    try:
        with open("students.data", "r") as file:
            data = json.load(file)
            for student_data in data:
                # **student_data 是 Python 中的解包（unpacking）操作
                # 将 student_data 字典中的每一对键值对作为关键字参数传递给 Student 类的构造函数 __init__
                id = student_data['student_id']
                del student_data['student_id']

                student = Student(**student_data, from_file = True)
                student.student_id = id
                students.append(student)

    except FileNotFoundError:
        with open("students.data", "w") as file:
            json.dump({}, file)



    try:
        with open("admins.data", "r") as file:
            data = json.load(file)
            for admin_data in data:
                admin = Admin(**admin_data, from_file=True)
                Admin.admins.append(admin)

    except FileNotFoundError:
        with open("admins.data", "w") as file:
            json.dump([], file)

    while True:
        print("Current student list:")
        for s in students:
            print(s)
        print(Fore.BLUE + "Welcome to the University Enrollment System")
        print(Fore.BLUE + "\t1. Student Login")
        print(Fore.BLUE + "\t2. Register a new student")
        print(Fore.BLUE + "\t3. Admin Login")
        print(Fore.BLUE + "\t4. Exit")
        print(Style.RESET_ALL)
        choice = input("\tSelect an option: ")
        


        if choice == "1":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            for student in students:
                if student.email == email and student.password == password:
                    while True:
                        print(Fore.BLUE + "1. Enrol in a subject")
                        print(Fore.BLUE + "2. Remove a subject")
                        print(Fore.BLUE + "3. Show enrolment list")
                        print(Fore.BLUE + "4. Change password")
                        print(Fore.BLUE + "5. Logout")
                        print(Style.RESET_ALL)
                        choice = input("Select an option: ")
                        if choice == "1":
                            while True:
                                subject = input("Enter the subject you want to enrol in: ")
                                if not Student.is_valid_subject(subject):
                                    print(Fore.RED + "Invalid subject format. Subject must only contain letters and spaces.")
                                    print(Style.RESET_ALL)
                                else:
                                    break
                            student.enrol_subject(subject)
                        elif choice == "2":
                            subject = input("Enter the subject you want to remove:  ")
                            student.remove_subject(subject)
                        elif choice == '3':
                            if student.subject == []:
                                print(Fore.YELLOW + "You haven't enrolled any subjects.")
                                print(Style.RESET_ALL)
                            else:
                                student.show_enrolment()
                        elif choice == '4':
                            new_password = input("Enter your new password: ")
                            student.change_password(new_password)
                        elif choice == '5':
                            break
                        else:
                            print(Fore.RED + "Invalid choice. Please select a valid option.")
                            print(Style.RESET_ALL)
                    break
            else:
                print(Fore.RED + "Invalid email or password.")
                print(Style.RESET_ALL)

            
        elif choice == '2':
            name = input("Enter your name: ")
            
            while True:
                email = input("Enter your email: ")
                if not Student.is_valid_email(email):
                    print(Fore.Red + "Invalid email format. Email should be in the format 'firstname.lastname@university.com'.")
                    print(Style.RESET_ALL)
                else:
                    break

            
            while True:
                password = input("Enter your password: ")
                if not Student.is_valid_password(password):
                    print(Fore.Red + "Invalid password. Password must start with an uppercase letter, contain at least 5 letters, and have 3 or more digits.")
                    print(Style.RESET_ALL)
                else:
                    break

            
            student = Student(name, email, password)
            print(Fore.GREEN + "Registration successful!")
            print(Style.RESET_ALL)
            print(student)
            student.save_students_file()

        elif choice == '3':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            for admin in Admin.admins:
                if admin.username == username and admin.password == password:
                    while True:
                        print(Fore.BLUE + "Admin Operations:")
                        print(Fore.BLUE + "\t1. View all registered students")
                        print(Fore.BLUE + "\t2. View students by grade")
                        print(Fore.BLUE + "\t3. Partition and view students based on PASS/FAIL categories")
                        print(Fore.BLUE + "\t4. Remove a student")
                        print(Fore.BLUE + "\t5. Clear all students")
                        print(Fore.BLUE + "\t6. Logout")
                        print(Style.RESET_ALL)
                        admin_choice = input("Select an option: ")
                        

                        if admin_choice == "1":
                            Admin.view_all_students()
                        elif admin_choice == "2":
                            grade_students_dict = Admin.list_students_by_all_grades()
                            for grade, grade_students in grade_students_dict.items():
                                print(f"Students with grade {grade}:")
                                if not grade_students:
                                    print("\tNone")
                                else:
                                    for student in grade_students:
                                        indented_student = '\t' + '\t'.join(str(student).splitlines(True))
                                        print(indented_student)
                                print("------")
                        elif admin_choice == "3":
                            passed_students, failed_students, no_record_students = Admin.partition_students_pass_fail()
                            print("Passed Students:")
                            if not passed_students:
                                print("None")
                            else:
                                for student in passed_students:
                                    print(student)
                            print("\nFailed Students:")
                            if not failed_students:
                                print("None")
                            else:
                                for student in failed_students:
                                    print(student)
                            print("\nNo Subject Students:")
                            if not no_record_students:
                                print("None")
                            else:
                                for student in no_record_students:
                                    print(student)
                        elif admin_choice == "4":
                            student_id = input("Enter the Student ID of the student to remove: ")
                            Admin.remove_student(student_id)
                        elif admin_choice == "5":
                            Admin.clear_all_students()
                        elif admin_choice == "6":
                            break
                        else:
                            print(Fore.RED + "Invalid choice. Please select a valid option.")
                else:
                    print(Fore.RED + "Invalid email or password.")

        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print(Fore.RED + "Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()