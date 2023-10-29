import os
import json
import random
import tkinter.messagebox as msgbox

class MysqlDatabases:
    def __init__(self):

        try:
            with open("./students.data", mode="r", encoding="utf-8") as f:
                self.users = json.load(f)
        except FileNotFoundError:
            self.users = []
            with open("./students.data", mode="w", encoding="utf-8") as f:
                json.dump(self.users, f, indent=4)
        except json.JSONDecodeError:
            msgbox.showerror("Error", "Failed to read the user data due to corruption. Resetting data.")
            self.users = []
            with open("./students.data", mode="w", encoding="utf-8") as f:
                json.dump(self.users, f, indent=4)
    
    # def verify_student_login(self, email, password):
    #     for user in self.users:
    #         if email.lower() == user["Email"].lower(): 
    #             if password == user["Password"]:
    #                 return True, "Login successful!"
    #             else:
    #                 return False, "Login failed! Invalid password!"
    #     return False, "Login failed! Invalid username!"

    def verify_student_login(self, email, password):
        try:
            user = next(user for user in self.users if email.lower() == user["Email"].lower())
            if user["Password"] == password:
                return True, "Login successful!"
            else:
                return False, "Login failed! Invalid password!"
        except StopIteration:
            return False, "Login failed! Invalid email!"

    def get_user_credentials(self, email):
        for user in self.users:
            if email.lower() == user["Email"].lower():
                return user["Name"], user["Email"], user["Student_ID"]
        return None, None, None

    def create_newuser(self, name, email, password):
        for user in self.users:
            if email == user["Email"].lower():
                return False, "User already exists. Please login instead."
        
        # Generate a unique student ID
        while True:
            student_id = str(random.randint(1, 999999)).zfill(6)
            if not any(user["Student_ID"] == student_id for user in self.users):
                break

        # Create a new user
        new_user = {
            "Name": name,
            "Email": email,
            "Password": password,
            "Subjects": [],
            "Student_ID": student_id
        }

        # Add the new user to the users list
        self.users.append(new_user)

        # Save the users list to the ./students.data file
        try:
            with open("./students.data", mode="w", encoding="utf-8") as f:
                json.dump(self.users, f, indent=4)
        except IOError:
            return False, "Failed to save data. Please try again."
                   
        success_message = "Registration successful!\n\n"
        success_message += f"Name: {name}\n"
        success_message += f"Email: {email}\n"
        success_message += f"Student ID: {student_id}\n"
        success_message += f"Password: {password}\n"
        success_message += "\nPlease keep a record of your personal information above."
        success_message += "\n\nPlease login to continue."

        return True, success_message
    
    def change_password(self, email, password):

        try:
            user = next(user for user in self.users if user["Email"].lower() == email.lower())
            user["Password"] = password
            
            try:
                with open("./students.data", mode="w", encoding="utf-8") as f:
                    json.dump(self.users, f, indent=4)
            except IOError:
                return False, "Error occurred while saving the data!"
            return True, "Password changed successfully!"

        except StopIteration:
            return False, "Password change failed! Invalid email!"

    def get_user_subjects(self, email):
        for user in self.users:
            if email.lower() == user["Email"].lower():
                return self.format_subjects(user["Subjects"])
        return None

    def format_subjects(self, subjects):
        table_data = []
        headers = ["Subject", "ID", "Mark", "Grade"]
        table_data.append(headers)

        for subject in subjects:
            values = [
                subject.get("Subject", ''), 
                subject.get("ID", ''),
                subject.get("Mark", ''),
                subject.get("Grade", '') 
                ]
            table_data.append(values)
        return table_data

    def add_subject(self, email, subject):
        try:
            user = next(user for user in self.users if user["Email"].lower() == email.lower())

            if any(currentSubject["Subject"].lower() == subject.lower() for currentSubject in user.get("Subjects", [])):
                return False, "You are already enrolled in this subject! Please try with another one!"

            if len(user.get("Subjects", [])) >= 4:
                return False, "Students are allowed to enrol in 4 subjects only!"
            
            while True:
                id = str(random.randint(1, 999)).zfill(3)
                if not any(s["ID"] ==  id for s in user["Subjects"]):
                    break
            suject_with_number = f"{subject}-{id}"

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

            subject_data = {
                "Subject": subject,
                "ID": id,
                "Mark": mark,
                "Grade": grade
            }

            user["Subjects"].append(subject_data)

            with open("./students.data", mode="w", encoding="utf-8") as f:
                json.dump(self.users, f, indent=4)

            return True, f"Enrolling in {suject_with_number}.\nYou are now enrolled in {len(user['Subjects'])} out of 4 subjects!"
        
        except StopIteration:
            return False, "User not found!"
        
        except IOError:
            return False, "Failed to save data. Please try again."

    def remove_subject(self, email, subject_id):
        try:
            user = next(user for user in self.users if user["Email"].lower() == email.lower())
            if not user.get("Subjects"):
                return False, "No subjects enrolled! Please enroll in subject(s) first!"

            subject_to_remove = next(subject for subject in user["Subjects"] if subject["ID"] == subject_id)
            user["Subjects"].remove(subject_to_remove)

            try:
                with open("./students.data", mode="w", encoding="utf-8") as f:
                    json.dump(self.users, f, indent=4)
            except IOError:
                return False, "Failed to save data. Please try again."

            return True, f"Dropping {subject_to_remove['Subject']}-{subject_id}.\nYou are now enrolled in {len(user['Subjects'])} out of 4 subjects!"
        
        except StopIteration:
            return False, "Subject not found!"
  
db = MysqlDatabases()
