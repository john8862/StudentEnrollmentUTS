import re
import random
import json

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
        # Generate a unique 6-digit student ID
        student_id = str(len(students) + 1).zfill(6)
        students.append(self)
        self.student_id = student_id

    @staticmethod
    def is_valid_email(email):
        email_pattern = r'^[a-zA-Z]+\.[a-zA-Z]+@university\.com$'
        return re.match(email_pattern, email)

    @staticmethod
    def is_valid_password(password):
        password_pattern = r'^[A-Z][a-zA-Z]{4,}[0-9]{3,}$'
        return re.match(password_pattern, password)

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
            print(f"You have successfully enrolled in {subject_with_number}.")
            self.save_students_file()

    def remove_subject(self, subject):
        if subject in self.subject:
            self.subject.remove(subject)
            print(f"You have successfully removed {subject} from your enrolment list.")
            self.save_students_file()
        else:
            print(f"You are not enrolled in {subject}.")

    def show_enrolment(self):
        print("You are currently enrolled in the following subjects:")
        for subject in self.subject:
            # 提取Mark和grade
            print(f"{subject}")


    def save_students_file(self):
        #__dict__ 能将每个 student 对象转换为字典形式
        data = [student.__dict__ for student in students]
        with open("students.data", "w") as file:
            #将 data 列表（它包含了所有学生的信息）转换为 JSON 格式，并写入到打开的文件中。
            json.dump(data, file)

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


    while True:
        #print(f"{students}") # Print the list of students for testing purposes, need to delete in the final version
        print("Current student list:")
        for s in students:
            print(s)
        print("Welcome to the University Enrollment System")
        print("1. Login")
        print("2. Register a new student")
        print("3. Exit")
        choice = input("Select an option: ")
        
        

        if choice == "1":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            for student in students:
                if student.email == email and student.password == password:
                    while True:
                        print("1. Enrol in a subject")
                        print("2. Remove a subject")
                        print("3. Show enrolment list")
                        print("4. Change password")
                        print("5. Logout")
                        choice = input("Select an option: ")
                        if choice == "1":
                            subject = input("Enter the subject you want to enrol in: ")
                            student.enrol_subject(subject)
                        elif choice == "2":
                            subject = input("Enter the subject you want to remove:  ")
                            student.remove_subject(subject)
                        elif choice == '3':
                            if student.subject == []:
                                print("You haven't enrolled any subjects.")
                            else:
                                student.show_enrolment()
                        elif choice == '4':
                            new_password = input("Enter your new password: ")
                            student.change_password(new_password)
                        elif choice == '5':
                            break
                        else:
                            print("Invalid choice. Please select a valid option.")
                    break
            else:
                print("Invalid email or password.")

            
        elif choice == '2':
            name = input("Enter your name: ")
            
            while True:
                email = input("Enter your email: ")
                if not Student.is_valid_email(email):
                    print("Invalid email format. Email should be in the format 'firstname.lastname@university.com'.")
                else:
                    break

            
            while True:
                password = input("Enter your password: ")
                if not Student.is_valid_password(password):
                    print("Invalid password. Password must start with an uppercase letter, contain at least 5 letters, and have 3 or more digits.")
                else:
                    break

            
            student = Student(name, email, password)
            print("Registration successful!")
            print(student)
            student.save_students_file()

            #print("Current student list:") #This function should me migrate to the admin session.
            #for s in students:
            #    print(s)
                
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()