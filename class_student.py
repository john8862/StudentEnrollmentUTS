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
        if not from_file:
            self.generate_student_id()
            self.save_students_file()

    @staticmethod
    def load_students_from_file():
        global students
        students.clear()
        try:
            with open("students.data", "r") as file:
                data = json.load(file)
                for student_data in data:
                    id = student_data['Student_ID']
                    del student_data['Student_ID']
                    student_data = {
                        'name': student_data['Name'],
                        'email': student_data['Email'],
                        'password': student_data['Password'],
                        'subject': student_data['Subjects'],
                    }

                    student = Student(**student_data, from_file=True)
                    student.student_id = id
                    students.append(student)

        except FileNotFoundError:
            with open("students.data", "w") as file:
                json.dump([], file)


    def generate_student_id(self):
        global students

        generated_id = str(random.randint(0, 999999)).zfill(6)


        existing_ids = [student.student_id for student in students]
        while generated_id in existing_ids:
            generated_id = str(random.randint(0, 999999)).zfill(6)

        self.student_id = generated_id
        students.append(self)
    @staticmethod
    def is_valid_email(email):
        email_pattern = r'(?i)[a-zA-Z0-9]+\.[a-zA-Z0-9]+@university\.com'
        return re.match(email_pattern, email)

    @staticmethod
    def is_valid_password(password):
        password_pattern = r'^[A-Z](?=(?:[^0-9]*[0-9]){3})(?=(?:[^a-zA-Z]*[a-zA-Z]){5}).*$'
        return re.match(password_pattern, password)
    
    @staticmethod
    def is_name_exists(name):
        return any(student.name == name for student in students)
    
    @staticmethod
    def is_email_exists(email):
        return any(student.email.lower() == email.lower() for student in students)
    
    @staticmethod
    def get_student_by_email(email):
        for student in students:
            if student.email == email:
                return student
        return None
    
    @staticmethod
    def is_valid_subject(subject):
        subject_pattern = r'^[^\s]+$'
        return re.match(subject_pattern, subject)
    
    def enrol_subject(self, subject):
        if len(self.subject) >= 4:
            raise ValueError("Students are allowed to enrol in 4 subjects only.")

        for subj in self.subject:
            if subj['Subject'].lower() == subject.lower():
                raise ValueError(f"You are already enrolled in {subject}.")

        random_number = str(random.randint(1, 999)).zfill(3)

        while any(s['ID'] == random_number for s in self.subject):
            random_number = str(random.randint(1, 999)).zfill(3)
        
        subject_with_number = f"{subject}-{random_number}"
        mark = random.randint(2500, 10000) / 100.00

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

        subject_dict = {
            "Subject": subject,
            "ID": random_number,
            "Mark": mark,
            "Grade": grade
        }
        self.subject.append(subject_dict)
        self.save_students_file()
        
        success_message = f"Enrolling in {subject_with_number}." \
                        f"\nYou are now enrolled in {len(self.subject)} out of 4 subjects."
        return success_message


    def remove_subject(self, subject_id):

        for subject in self.subject:
            if str(subject['ID']) == str(subject_id):
                self.subject.remove(subject)
                self.save_students_file()
                return f"Dropping {subject['Subject']}-{subject['ID']}." \
                       f"\nYou are now enrolled in {len(self.subject)} out of 4 subjects."
                
        raise ValueError(f"You are not enrolled in a subject with ID [{subject_id}].")

    def show_enrolment(self):
        print(Fore.YELLOW + f"\t\tShowing {len(self.subject)} subjects." + Style.RESET_ALL)
        for subject in self.subject:
            subj_str = f"{subject['Subject']}::{subject['ID']} -- Mark = {subject['Mark']} -- Grade = {subject['Grade']}"
            print(f"\t\t[ {subj_str} ]")


    def save_students_file(self):
        def extract_subject_info(subj_str):
            if isinstance(subj_str, str):

                subj_name, rest = subj_str.split("::", 1)
                subj_id, rest = rest.split(" -- Mark = ", 1)
                mark, grade = rest.split(" -- Grade = ", 1)
                return {
                    "Subject": subj_name.strip(),
                    "ID": int(subj_id.strip()),
                    "Mark": float(mark.strip()),
                    "Grade": grade.strip()
                }
            elif isinstance(subj_str, dict):
                return subj_str
        data = [{
            "Name": student.name,
            "Email": student.email,
            "Password": student.password,
            "Subjects": [extract_subject_info(subject) for subject in student.subject],
            "Student_ID": student.student_id,
            }
            for student in students
        ]
            
        with open("students.data", "w") as file:
            json.dump(data, file, indent=4)
    def change_password(self, new_password):
        
        if Student.is_valid_password(new_password):
            self.password = new_password
            print(Fore.YELLOW + "\t\tPassword successfully changed!" + Style.RESET_ALL)
            self.save_students_file()
        else:
            print(Fore.RED + "\t\tIncorrect password format." + Style.RESET_ALL)


    def __str__(self):
        return f"Student ID: {self.student_id}\nName: {self.name}\nEmail: {self.email}\nPassword: {self.password}\n"

    def __repr__(self):
        return f"Student ID: {self.student_id}\nName: {self.name}\nEmail: {self.email}\nPassword: {self.password}\n"
    
students = []
