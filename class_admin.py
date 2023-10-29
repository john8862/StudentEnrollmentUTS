import re
import random
import json
import colorama
from colorama import Fore, init, Style
from class_student import Student, students

class Admin:
    

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
    def average_mark(student):
        if not student.subject:
            return 0
        total = 0
        for subj in student.subject:
            total += subj['Mark']
        return round(total / len(student.subject), 2)
    

    @staticmethod
    def list_students_by_all_grades():
        grade_dict = {
            'Z': [],
            'P': [],
            'C': [],
            'D': [],
            'HD': []
        }
        if not students:
            print("\t\t< Nothing to Display >")
            return grade_dict
        else:
            for student in students:
                if student.subject == []:
                    continue
                else:
                    avg_mark = Admin.average_mark(student)

                    if 0 <= avg_mark < 50:
                        grade = 'Z'
                    elif 50 <= avg_mark < 65:
                        grade = 'P'
                    elif 65 <= avg_mark < 75:
                        grade = 'C'
                    elif 75 <= avg_mark < 85:
                        grade = 'D'
                    else:
                        grade = 'HD'
                    
                    grade_dict[grade].append((student, student.subject, avg_mark, grade))
            return grade_dict


    @staticmethod
    def partition_students_pass_fail():
        passed_subjects = []
        failed_subjects = []
        no_record_subjects = []
        
        for student in students:
            avg_mark = Admin.average_mark(student)
            if 0 <= avg_mark < 50:
                grade = 'Z'
            elif 50 <= avg_mark < 65:
                grade = 'P'
            elif 65 <= avg_mark < 75:
                grade = 'C'
            elif 75 <= avg_mark < 85:
                grade = 'D'
            else:
                grade = 'HD'
            
            if not student.subject:
                no_record_subjects.append((student, None))
                continue


            if grade == "Z":
                failed_subjects.append((student, student.subject, avg_mark, grade))
            else:
                passed_subjects.append((student, student.subject, avg_mark, grade))

        return passed_subjects, failed_subjects, no_record_subjects
    
    @staticmethod
    def print_student_subjects(subject_list):
        if not subject_list:
            print("[]")
            return

        print("[", end="")
        for idx, item in enumerate(subject_list):

            if len(item) == 2:
                student, _ = item
                print(f"{student.name} :: {student.student_id}", end="")
            else:
                student, subj, avg_mark, grade = item
                print(f"{student.name} :: {student.student_id} --> GRADE: {grade} - MARK : {avg_mark}", end="")
                
            if idx != len(subject_list) - 1:
                print(", ", end="")
        print("]")

    @staticmethod
    def remove_student(id):
        global students
        student_to_remove = next((student for student in students if student.student_id == id), None)

        if student_to_remove is None:
            raise ValueError(f"Student {id} does not exist.")
        
        students.remove(student_to_remove)
        student_to_remove.save_students_file()
        
        return f"Removing student {id} Account."

    @staticmethod
    def clear_all_students():
        global students
        confirmation = input().strip().upper()
        if confirmation == 'Y':
            students = []
            with open("students.data", "w") as file:
                json.dump([], file)
            return "\tStudents data cleared."
        elif confirmation == 'N':
            return "\tOperation cancelled."
        else:
            raise ValueError("Invalid operation.")
