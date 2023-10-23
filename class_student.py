import re
import random
import json
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
    def is_name_exists(name):
        return any(student.name == name for student in students)
    
    @staticmethod
    def is_email_exists(email):
        return any(student.email == email for student in students)
    
    @staticmethod
    def get_student_by_email(email):
        for student in students:
            if student.email == email:
                return student
        return None
    
    @staticmethod
    def is_valid_subject(subject):
        subject_pattern = r'^[a-zA-Z ]*$'
        return re.match(subject_pattern, subject)
    
    def enrol_subject(self, subject):
        if len(self.subject) >= 4:
            print(Fore.RED + "\t\tStudents are allowed to enrol in 4 subjects only." + Style.RESET_ALL)
        else:
            random_number = str(random.randint(0, 999)).zfill(3)
            # 检查生成的数字是否重复
            while any(subject.endswith(f"_{random_number}") for subject in self.subject):
                random_number = str(random.randint(0, 999)).zfill(3)
            # 将随机数字添加到subject中
            subject_with_number = f"{subject}-{random_number}"
            mark = random.randint(2500, 10000) / 100.00
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

            subject_with_grade = f"{subject}::{random_number} -- Mark = {mark} -- Grade = {grade}"

            self.subject.append(subject_with_grade)
            print(Fore.YELLOW + f"\t\tEnrolling in {subject_with_number}." + Style.RESET_ALL)
            
            self.save_students_file()

    def remove_subject(self, subject_id):
        for subject in self.subject:
            if f"::{subject_id}" in subject:
                subject_name, subject_number = subject.split('::', 1)[0], subject.split('::', 1)[1].split(' ', 1)[0]
                print(Fore.YELLOW + f"\t\tDroping {subject_name}-{subject_number}." + Style.RESET_ALL)
                self.subject.remove(subject)
                print(Fore.YELLOW + f"\t\tYou are now enrolled in {len(self.subject)} out of 4 subjects." + Style.RESET_ALL)
                # Assuming there's a method to save to a file
                self.save_students_file()
                return
        print(f"\t\tYou are not enrolled in a subject with [{subject_id}].")

    def show_enrolment(self):
        print(Fore.YELLOW + f"\t\tShowing {len(self.subject)} subjects." + Style.RESET_ALL)
        for subject in self.subject:
            # 提取Mark和grade
            # subject_1 = '\t\t\t' + '\t\t\t'.join(str(subject).splitlines(True))
            print(f"\t\t[ {subject} ]")


    def save_students_file(self):
        #__dict__ 能将每个 student 对象转换为字典形式
        data = [student.__dict__ for student in students]
        with open("students.data", "w") as file:
            #将 data 列表（它包含了所有学生的信息）转换为 JSON 格式，并写入到打开的文件中。
            json.dump(data, file, indent = 4)

    def change_password(self, new_password):
        print(Fore.YELLOW + "\t\tUpdating Password." + Style.RESET_ALL)
        if Student.is_valid_password(new_password):
            self.password = new_password
            print(Fore.YELLOW + "\t\tPassword successfully changed!" + Style.RESET_ALL)
            self.save_students_file()  # Save the updated password
        else:
            print(Fore.RED + "\t\tIncorrect password format." + Style.RESET_ALL)


    def __str__(self):
        return f"Student ID: {self.student_id}\nName: {self.name}\nEmail: {self.email}\nPassword: {self.password}\n"

    def __repr__(self):
        return f"Student ID: {self.student_id}\nName: {self.name}\nEmail: {self.email}\nPassword: {self.password}\n"
    
students = []
