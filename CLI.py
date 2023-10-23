import re
import random
import json
import colorama
from colorama import Fore, init, Style
from class_student import Student, students
from class_admin import Admin

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
        choice = input(Fore.CYAN + "University System: (A)dmin, (S)tudent, or X :" + Style.RESET_ALL).upper()


        if choice == "S":
            while True:
                student_choice = input(Fore.CYAN + "\tStudent System(l/r/x):" + Style.RESET_ALL).lower()
                if student_choice == "l":
                    while True:
                        print(Fore.GREEN + "\tStudent Sign In" + Style.RESET_ALL)
                        email = input("\tEnter your email: ")
                        password = input("\tEnter your password: ")
                        # Check the validity of email and password formats
                        if not Student.is_valid_email(email) or not Student.is_valid_password(password):
                            print(Fore.RED + "\tIncorrect email or password format." + Style.RESET_ALL)
                            continue
                        else:
                            print(Fore.YELLOW + "\tEmail and password formats acceptable." + Style.RESET_ALL)

                        if not Student.is_email_exists(email):
                            print(Fore.RED + "\tStudent does not exist." + Style.RESET_ALL)
                            continue

                        matched_student = None

                        for student in students:
                            if student.email == email and student.password == password:
                                print(Fore.YELLOW + "\t\tSign in successful." + Style.RESET_ALL)
                                matched_student = student
                                break
                        if not matched_student:
                            print(Fore.RED + "\t\tInvalid email or password." + Style.RESET_ALL)
                        if matched_student:  # If a student was matched, proceed to the student menu.
                            break
                                                                   

                    while True:
                        student_menu_choice = input(Fore.BLUE + "\t\tStudent Course Menu (c/e/r/s/x):" + Style.RESET_ALL).lower()
                        if student_menu_choice == "c":
                            while True:
                                new_password = input("\t\tNew password: ")
                                confirm_password = input("\t\tConfirm password: ")
                                if new_password == confirm_password:
                                    student.change_password(new_password)
                                    break
                                else:
                                    print(Fore.RED + "\t\tThe password is not the same twice" + Style.RESET_ALL)
                        elif student_menu_choice == "e":
                            while True:
                                subject = input("\t\tEnter the subject you want to enrol in: ")
                                if not Student.is_valid_subject(subject):
                                    print(Fore.RED + "\t\t\tInvalid subject format. Subject must only contain letters and spaces.")
                                    print(Style.RESET_ALL)
                                else:
                                    student.enrol_subject(subject)
                                    print(f"\t\tYou are now enrolled in {len(student.subject)} out of 4 subjects.")
                                    break
                        elif student_menu_choice == "r":
                            subject_id = input("\t\tRemove subject by ID:  ")
                            student.remove_subject(subject_id)
                        elif student_menu_choice == "s":
                            student.show_enrolment()
                        elif student_menu_choice == "x":
                            break
                        else:
                            print(Fore.RED + "\t\tInvalid choice. Please select a valid option." + Style.RESET_ALL)

                elif student_choice == "r":
                    print(Fore.GREEN + "\tStudent Sign Up" + Style.RESET_ALL)
                    
                    while True:
                        while True:
                            email = input("\tEnter your email: ")
                            password = input("\tEnter your password: ")
                            if not Student.is_valid_email(email) or not Student.is_valid_password(password):
                                print(Fore.RED + "\tIncorrect email or password format." + Style.RESET_ALL)
                            else:
                                existing_student = Student.get_student_by_email(email)
                                if existing_student:
                                    print(Fore.RED + f"\tStudent {existing_student.name} already exists" + Style.RESET_ALL)
                                else:
                                    print(Fore.YELLOW + "\tEmail and password formats acceptable" + Style.RESET_ALL)
                                    break



                    
                        while True:
                            name = input("\tEnter your name: ")
                            # Extract the prefix from the email and replace '.' with ' '
                            email_name = email.split('@')[0].replace('.', ' ')
                            if name != email_name:
                                print(Fore.RED + "\tName does not match with the email prefix." + Style.RESET_ALL)
                            else:
                                break

                        
                        

                        student = Student(name, email, password)
                        print(Fore.YELLOW + f"\tEnrolling Student {name}." + Style.RESET_ALL)
                        student_1 = '\t\t' + '\t\t'.join(str(student).splitlines(True))
                        # print(student_1)
                        student.save_students_file()
                        break # Exit the outer loop once registration is successful

                elif student_choice == "x":
                    break

                else:
                    print(Fore.RED + "\tInvalid choice. Please select a valid option." + Style.RESET_ALL)
                    continue
            


        elif choice == 'A':

            while True:
                admin_choice = input(Fore.BLUE + "\tAdmin System (c/g/p/r/s/x): " + Style.RESET_ALL)
                if admin_choice == "c":
                    Admin.clear_all_students()
                    
                elif admin_choice == "g":
                    grade_students_dict = Admin.list_students_by_all_grades()
                    print(Fore.YELLOW + "\tGrade Grouping" + Style.RESET_ALL)
                    for grade, grade_subjects in grade_students_dict.items():
                        if grade_subjects:  # Check if the grade has any students
                            print(f"\t{grade} --> ", end="")
                            Admin.print_student_subjects(grade_subjects)
                        

                elif admin_choice == "p":
                    passed_subjects, failed_subjects, no_record_subjects = Admin.partition_students_pass_fail()
                    print(Fore.YELLOW + "\tPASS/FALL Partition" + Style.RESET_ALL)
                    # Your code to print passed subjects
                    print("\tPASS --> ", end="")
                    Admin.print_student_subjects(passed_subjects)

                    # Similar code for failed_subjects and no_record_subjects
                    print("\tFAIL --> ", end="")
                    Admin.print_student_subjects(failed_subjects)

                    print("\tNORECORD --> ", end="")
                    Admin.print_student_subjects(no_record_subjects, is_no_record=True)
                elif admin_choice == "r":
                    id = input("\tRemove by ID: ")
                    Admin.remove_student(id)

                elif admin_choice == "s":
                    Admin.view_all_students()

                elif admin_choice == "x":
                    break
                else:
                    print(Fore.RED + "\tInvalid choice. Please select a valid option.")

        elif choice == 'X':
            print(Fore.YELLOW + "Thank you" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice. Please select a valid option." + Style.RESET_ALL)
            continue


if __name__ == "__main__":
    main()