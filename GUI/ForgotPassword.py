import tkinter as tk
import json
import re
from PIL import ImageTk, Image
from tkinter import messagebox as msgbox
from __init__ import set_button_cursor
from db import db

class ForgotPasswordPage:

    def __init__(self, master):
        self.forgot_password = master
        self.initialize_window()
        self.create_widgets()
        self.validation_rules = {
            "Email": {
                "required": True,
                "validation_function": self.validate_email
            },
            "New Password": {
                "required": True,
                "validation_function": self.validate_password
            },
            "Confirm Password": {
                "required": True,
                "validation_function": self.validate_confirm_password
            }
        }

    def initialize_window(self):

        x = int(self.forgot_password.winfo_screenwidth() / 3 - self.forgot_password.winfo_reqwidth() / 3)
        y = int(self.forgot_password.winfo_screenheight() / 3 - self.forgot_password.winfo_reqheight() / 3)

        self.forgot_password.title("Change Password")
        self.forgot_password.geometry(f"790x512+{x}+{y}")
        self.forgot_password.resizable(0, 0)

    def create_widgets(self):
        self.entry_fields = {}
        self.error_labels = {}
        self.create_background_image()
        self.submission_frame()
        self.create_heading_label()
        self.create_entry("Email", "magenta2", 1)
        self.create_error_label("Email", 2)
        self.create_entry("New Password", "magenta2", 3)
        self.create_error_label("New Password", 4)
        self.create_entry("Confirm Password", "magenta2", 5)
        self.create_error_label("Confirm Password", 6)
        self.create_button("Submit", 7, self.SubmitAction)

        self.error_labels = {
            "Email": self.create_error_label("Email", 2),
            "New Password": self.create_error_label("New Password", 4),
            "Confirm Password": self.create_error_label("Confirm Password", 6)
        }

    def create_background_image(self):
        self.bgImage = ImageTk.PhotoImage(file="GUI/Image/background.jpg")
        bgLabel = tk.Label(self.forgot_password, image=self.bgImage)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

    def submission_frame(self):
        self.frame = tk.Frame(self.forgot_password, bg="white")
        self.frame.place(x=451, y=38)
        self.frame.grid_columnconfigure(0, weight=1, minsize=30)
        self.frame.grid_columnconfigure(2, weight=1, minsize=30)

    def create_heading_label(self):
        self.heading = tk.Label(self.frame, text="Reset Your Password")
        self.heading.grid(row=0, column=1, pady=(60,40), sticky="nsew")
        self.heading.config(
            font=("Helvetica", 22, "bold"),
            bg="white",
            fg="magenta2"
        )

    def create_entry(self, field_name, text_color, row, show=None):
        entry_var = tk.StringVar()
        entry = tk.Entry(self.frame, fg=text_color, show=show if show else None, textvariable=entry_var)
        entry.insert(0, field_name)
        entry.grid(row=row, column=1)
        entry.bind("<FocusIn>", lambda event: self.on_entry_click(event, field_name))
        entry.bind("<FocusOut>", lambda event: self.on_entry_leave(event, field_name))
        entry.config(
            font=("Helvetica", 15),
            bg="white",
            fg="magenta2",
            width=25,
            highlightthickness=1,
            highlightbackground="magenta2",
            highlightcolor="magenta2"
        )
        self.entry_fields[field_name] = entry
        return entry

    def create_error_label(self, field_name, row):
        error = tk.Label(self.frame, text="")
        error.grid(row=row, column=1, padx=10, pady=10, sticky="w")
        error.config(
            font=("Helvetica", 12, "italic"),
            bg="white",
            fg="red"
        )
        self.error_labels[field_name] = error
        return error
    
    def create_button(self, text, row, command):
        button = tk.Button(self.frame, text=text, command=command)
        button.grid(row=row, column=1, pady=(15, 73))
        button.config(
            font=("Helvetica", 16, "bold"),
            bg="magenta2",
            fg="white",
            width=23,
            bd=0,
            highlightthickness=0
        )
        set_button_cursor(button)
        return button
    
    def on_entry_click(self, event, field_name): 
        entry = event.widget
        current_text = entry.get()
        if "password" in field_name.lower():
            show_text = "*"
        else:
            show_text = ""
        if current_text == field_name:
            entry.delete(0, "end")
        entry.config(show=show_text)

    def on_entry_leave(self, event, field_name):
        entry = event.widget
        current_text = entry.get()
        show_text = ""
        if current_text == "":
            entry.delete(0, "end")
            entry.insert(0, field_name)
            if "password" in field_name.lower():
                show_text = ""
        else:
            if "password" in field_name.lower():
                show_text = "*"
        entry.config(show=show_text)

        self.validate_field(field_name=field_name)
    
    def validate_email(self):
        email = self.entry_fields["Email"].get()
        store_email = []
        with open('students.data', mode='r', encoding='utf-8') as f:
            student_data = json.load(f)
            store_email = [student["Email"] for student in student_data]
        if email.lower() not in store_email:
            self.entry_fields["Email"].config(bg="magenta2", fg="white")
            self.error_labels["Email"].config(
                text="* Email does not exist!",
                font=("Helvetica", 12, "italic"),
                fg="red"
            )
            return False
        else:
            self.entry_fields["Email"].config(bg="white", fg="magenta2")
            self.error_labels["Email"].config(text="")
            return True

    
    def validate_password(self):
        password = self.entry_fields["New Password"].get()
        if not re.match(r"^[A-Z](?=.*\d.*\d.*\d)(?=.*[a-zA-Z].*[a-zA-Z].*[a-zA-Z].*[a-zA-Z]).*$", password):
            self.entry_fields["New Password"].config(bg="magenta2", fg="white")
            self.error_labels["New Password"].config(
                text="* Invalid password format!",
                font=("Helvetica", 12, "italic"),
                fg="red"
            )
            return False
        else:
            self.entry_fields["New Password"].config(bg="white", fg="magenta2")
            self.error_labels["New Password"].config(text="")
            return True

    def validate_confirm_password(self):
        password = self.entry_fields["New Password"].get()
        confirm_password = self.entry_fields["Confirm Password"].get()
        if password != confirm_password:
            self.entry_fields["Confirm Password"].config(bg="magenta2", fg="white")
            self.error_labels["Confirm Password"].config(
                text="* Passwords do not match!",
                font=("Helvetica", 12, "italic"),
                fg="red"
            )
            return False
        else:
            self.entry_fields["Confirm Password"].config(bg="white", fg="magenta2")
            self.error_labels["Confirm Password"].config(text="")
            return True                                       

    def validate_field(self, field_name):
        current_text = self.entry_fields[field_name].get()
        rules = self.validation_rules[field_name]
        
        if rules["required"] and current_text.strip() == field_name:
            self.entry_fields[field_name].config(bg="magenta2", fg="white")
            self.error_labels[field_name].config(
                text="*This is a required field!", 
                font=("Helvetica", 12, "italic"), 
                fg="red"
            )
            return False
        else:
            self.entry_fields[field_name].config(bg="white", fg="magenta2")
            self.error_labels[field_name].config(text="")
        if rules["validation_function"]:
            return rules["validation_function"]()
        return True
    
    def SubmitAction(self):
        email = self.entry_fields["Email"].get()
        new_password = self.entry_fields["New Password"].get()
        confirm_password = self.entry_fields["Confirm Password"].get()

        if not (email and new_password and confirm_password):
            msgbox.showerror("Error", "Please fill in all fields!")
            return
        
        elif self.validate_field("Email") == False:
            msgbox.showerror("Error", "Please change the email first!")
            return
        
        elif self.validate_field("New Password") == False:
            msgbox.showerror("Error", "Please correct the new password first!")
            return
        
        elif self.validate_field("Confirm Password") == False:
            msgbox.showerror("Error", "Passwords do not match.")
            return

        elif all([self.validate_field(field_name) for field_name in self.validation_rules.keys()]):
            success, message = db.change_password(email, new_password)
            if success:
                msgbox.showinfo(title="Success", message=message)
                self.forgot_password.destroy()
            else:
                msgbox.showerror(title="Error", message=message)
                return

if __name__ == '__main__':
    FPP = tk.Tk()
    change_password_page = ForgotPasswordPage(FPP)
    FPP.mainloop()