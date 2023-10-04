import tkinter as tk
import tkinter.messagebox as msgbox
import re
from db import db

class RegistrationPage:

    def __init__(self, master):
        self.root = master
        self.root.title("Univeristy Enrollment System v0.0.1")
        self.root.geometry(f"400x250")
        self.create_widgets()

    def create_widgets(self):
        self.name = tk.StringVar()
        
        self.email = tk.StringVar()
        self.email.trace_add("write", self.is_validate_email)

        self.password = tk.StringVar()
        self.password.trace_add("write", self.is_validate_password)

        self.password_confirmation = tk.StringVar()
        self.password_confirmation.trace_add("write", self.validate_password_confirmation)

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(8, weight=1)

        tk.Label(self.root, text="Name*:").grid(row=1, column=1, sticky="e")
        self.name_entry = tk.Entry(self.root, textvariable=self.name)
        self.name_entry.grid(row=1, column=2, sticky="w")
        # self.name_entry.config(validate="focusout", validatecommand=self.validate_required_fields)

        tk.Label(self.root, text="Email*:").grid(row=2, column=1, sticky="e")
        self.email_entry = tk.Entry(self.root, textvariable=self.email)
        self.email_entry.grid(row=2, column=2, sticky="w")
        # self.email_entry.config(validate="focusout", validatecommand=self.validate_required_fields)

        self.email_error = tk.Label(self.root, text="", fg="red")
        self.email_error.grid(row=3, column=2, sticky="w")
        # self.email_error.grid_remove()

        tk.Label(self.root, text="Password*:").grid(row=4, column=1, sticky="e")
        self.password_entry = tk.Entry(self.root, textvariable=self.password, show="*")
        self.password_entry.grid(row=4, column=2, sticky="w")
        # self.password_entry.config(validate="focusout", validatecommand=self.validate_required_fields)

        self.password_error = tk.Label(self.root, text="", fg="red")
        self.password_error.grid(row=5, column=2, sticky="w")
        # self.password_error.grid_remove()

        tk.Label(self.root, text="Confirm Password*:").grid(row=6, column=1,sticky="e")
        self.password_confirmation_entry = tk.Entry(self.root, textvariable=self.password_confirmation, show="*")
        self.password_confirmation_entry.grid(row=6, column=2, sticky="w")
        # self.password_confirmation_entry.config(validate="focusout", validatecommand=self.validate_required_fields)

        # self.password_confirmation_error = tk.Label(self.root, text="", fg="red")
        # self.password_confirmation_error.grid(row=5, column=2, sticky="w")
        # self.password_confirmation_error.grid_remove()

        tk.Button(self.root, text="Register", command=self.Register).grid(row=7, column=1, pady=10, sticky="w")

    def is_validate_email(self, *args):
        if not re.match(r"[a-z]+\.[a-z]+@university\.com", self.email.get()):
            self.email_error["text"] = "Invalid email format. Email should be in the format 'firstname.lastname@university.com'"
        else:
            self.email_error["text"] = ""        

    def is_validate_password(self, *args):
        if not re.match(r"[A-Z][a-zA-Z]{4,}\d{3,}", self.password.get()):
            self.password_error["text"] = "Invalid password format. Password must start with an uppercase letter, contain at least 5 letters, and have 3 or more digits."
        else:
            self.password_error["text"] = ""

    def validate_required_fields(self):
        if not self.name.get():
            self.name_entry.config

    def validate_password_confirmation(self, *args):
        if self.password.get() != self.password_confirmation.get():
            self.password_confirmation_error["text"] = "Passwords do not match. Please double check!"
        else:
            self.password_confirmation_error["text"] = ""

    def Register(self):
        if self.email_error["text"]:
            msgbox.showerror(title="Error", message="Please change the email first!")
        elif self.password_error["text"]:
            msgbox.showerror(title="Error", message="Please correct the password first!")
        elif self.password.get() != self.password_confirmation.get():
            msgbox.showerror(title="Error", message="Passwords do not match.")
        else:
            success, message = self.db.create_newuser(self.name.get(), self.email.get(), self.password.get())
            if success:
                msgbox.showinfo(title="Success", message=message)
            else:
                msgbox.showerror(title="Error", message=message)

if __name__ == '__main__':
    root = tk.Tk()
    RegistrationPage(master=root)
    root.mainloop()
