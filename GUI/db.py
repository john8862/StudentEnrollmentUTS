import os
import json
import random
import tkinter.messagebox as msgbox

class MysqlDatabases:
    def __init__(self):
        self.check_users_file()

        with open("./students.data", mode="r", encoding="utf-8") as f:
            text = f.read()
        self.users = json.loads(text)

    def check_users_file(self):
        if not os.path.exists("./students.data"):
            with open("./students.data", mode="w", encoding="utf-8") as f:
                f.write("[]")
    
    def verify_student_login(self, email, password):
        for user in self.users:
            if email.lower() == user["Email"].lower(): 
                if password == user["Password"]:
                    return True, "Login successful!"
                else:
                    return False, "Login failed! Invalid password!"
        return False, "Login failed! Invalid username!"

    def get_user_credentials(self, email):
        for user in self.users:
            if email.lower() == user["Email"].lower():
                return user["Name"], user["Email"], user["Student_ID"], user["Subjects"]
        return None, None, None, None

    # def verify_admin_login(self, username, password):
    #     with open("admin.json", mode="r", encoding="utf-8") as f:
    #         admin_data = json.load(f)
    #     for admin in admin_data:
    #         if username.lower() == admin["username"].lower():
    #             if password == admin["Password"]:
    #                 return True, "Login successful!"
    #             else:
    #                 return False, "Login failed! Invalid password!"
    #     return False, "Login failed! Invalid username!"

    def create_newuser(self, name, email, password):
        for user in self.users:
            if email == user["Email"].lower():
                return False, "User already exists. Please login instead."
        
        # Generate a unique student ID
        # student_id = str(len(self.users) + 1).zfill(6)
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
        with open("./students.data", mode="w", encoding="utf-8") as f:
            json.dump(self.users, f, indent=4)
            
        success_message = "Registration successful!\n\n"
        success_message += f"Name: {name}\n"
        success_message += f"Email: {email}\n"
        success_message += f"Student ID: {student_id}\n"
        success_message += f"Password: {password}\n"
        success_message += "\nPlease keep a record of your personal information above."
        success_message += "\n\nPlease login to continue."

        return True, success_message
    
    def change_password(self, email, password):
        for user in self.users:
            if email == user["Email"]:
                user["Password"] = password
                with open("./students.data", mode="w", encoding="utf-8") as f:
                    json.dump(self.users, f, indent=4)
                return True, "Password changed successfully!"
        return False, "Password change failed! Invalid email!"

    def get_user_subjects(self, email):
        for user in self.users:
            if email == user["Email"].lower():
                return self.format_subjects(user["Subjects"])
        return None

    def format_subjects(self, subjects):
        table_data = []
        headers = ["Subject", "ID", "Mark", "Grade"]
        table_data.append(headers)

        for subject in subjects:
            values = [
                subject.get("Subject", ""), 
                subject.get("ID", ""),
                subject.get("Mark", ""),
                subject.get("Grade", "") 
                ]
            table_data.append(values)
        return table_data

    
    
    def remove_subject(self, subject):
        pass


db = MysqlDatabases()
