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


            if grade == "Z":  # Assuming Z is a failing grade, adjust as necessary
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
        for idx, (student, subj, avg_mark, grade) in enumerate(subject_list):

            if not subj:
                print(f"{student.name} :: {student.student_id}", end="")
            else:
                print(f"{student.name} :: {student.student_id} --> GRADE: {grade} - MARK : {avg_mark}", end="")
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
        confirmation = input(Fore.RED + "\tAre you sure you want to clear the database (Y)ES/(N)O: " + Style.RESET_ALL).strip().upper()
        if confirmation == 'Y':
            students = []
            # Save the empty list to the file
            with open("students.data", "w") as file:
                json.dump([], file)  # directly dump an empty list to the file
            print(Fore.YELLOW + "\tStudents data cleared." + Style.RESET_ALL)
        elif confirmation == 'N':
            print("\tOperation cancelled.")
        else:
            print("\tInvaild operation.")
