import re
import random
import json
import colorama
from colorama import Fore, init, Style
from class_student import Student, students

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
        print(Fore.YELLOW + "\tStudent list:" + Style.RESET_ALL)
        if not students:
            print("\t\t< Nothing to Display >")
        else:
            for s in students:
                print(f"\t{s.name} :: {s.student_id} --> Email: {s.email}")

    @staticmethod
    def list_students_by_all_grades():
        grade_dict = {
            'Z': [],
            'P': [],
            'C': [],
            'D': [],
            'HD': []
        }

        for student in students:
            for subj in student.subject:
                grade = subj.split(' -- Grade = ')[1].split(' ')[0]
                if grade in grade_dict:
                    grade_dict[grade].append((student, subj))

        return grade_dict
    @staticmethod
    def partition_students_pass_fail():
        passed_subjects = []
        failed_subjects = []
        no_record_subjects = []
        
        for student in students:
            for subj in student.subject:
                mark = float(subj.split(' -- Mark = ')[1].split(' ')[0])
                grade = subj.split(' -- Grade = ')[1].split(' ')[0]

                if grade == "Z":  # Assuming Z is a failing grade, adjust as necessary
                    failed_subjects.append((student, subj))
                elif mark == 0:   # Assuming 0 mark means no record
                    no_record_subjects.append((student, subj))
                else:
                    passed_subjects.append((student, subj))

        return passed_subjects, failed_subjects, no_record_subjects
    
    @staticmethod
    def print_student_subjects(subject_list, is_no_record = False):
        if not subject_list:
            print("[]")
            return

        print("[", end="")
        for idx, (student, subj) in enumerate(subject_list):
            if is_no_record:
                print(f"{student.name} :: {student.student_id}", end="")
            else:
                grade = subj.split(' -- Grade = ')[1].split(' ')[0]
                mark = float(subj.split(' -- Mark = ')[1].split(' ')[0])
                print(f"{student.name} :: {student.student_id} --> GRADE: {grade} - MARK : {mark}", end="")
            if idx != len(subject_list) - 1:
                print(", ", end="")
        print("]")

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
            print(Fore.YELLOW + f"\tRemoving student {id} Account." + Style.RESET_ALL)
            # Save the updated list to the file
            student_to_remove.save_students_file()
        else:
            print(Fore.RED + f"\tStudent {id} does not exist." + Style.RESET_ALL)

    @staticmethod
    def clear_all_students():
        global students
        print(Fore.YELLOW + "\tClearing students database" + Style.RESET_ALL)
        confirmation = input(Fore.RED + "\tAre you sure you want to clear the database (Y)es/(N)O: " + Style.RESET_ALL).strip().upper()
        if confirmation == 'Y':
            students = []
            # Save the empty list to the file
            if students:
                students[0].save_students_file()
            print(Fore.YELLOW + "\tStudents data cleared." + Style.RESET_ALL)
        elif confirmation == 'N':
            print("\tOperation cancelled.")
        else:
            print("\tInvaild operation.")
