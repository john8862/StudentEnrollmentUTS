import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msgbox
import re
from db import db
from LoginPage import LoginMasterPage
class RegistrationPage:

    def __init__(self, master):
        self.root = master
        self.root.title("Univeristy Enrollment System v0.0.1")
        self.root.geometry(f"640x400")
        self.create_widgets()
        self.db = db

    def create_widgets(self):
        self.name = tk.StringVar()
        self.name.trace_add("write", self.is_validate_name)

        self.email = tk.StringVar()
        self.email.trace_add("write", self.is_validate_email)

        self.password = tk.StringVar()
        self.password.trace_add("write", self.is_validate_password)

        self.password_confirmation = tk.StringVar()
        self.password_confirmation.trace_add("write", self.validate_password_confirmation)

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(10, weight=1)

        tk.Label(self.root, text="Name*:").grid(row=1, column=1, sticky="e")
        self.name_entry = tk.Entry(self.root, textvariable=self.name)
        self.name_entry.grid(row=1, column=2, sticky="w")

        self.name_error = tk.Label(self.root, text="", fg="red")
        self.name_error.grid(row=2, column=2, sticky="w")

        tk.Label(self.root, text="Email*:").grid(row=3, column=1, sticky="e")
        self.email_entry = tk.Entry(self.root, textvariable=self.email)
        self.email_entry.grid(row=3, column=2, sticky="w")

        self.email_error = tk.Label(self.root, text="", fg="red")
        self.email_error.grid(row=4, column=2, sticky="w")
        # self.email_error.grid_remove()

        tk.Label(self.root, text="Password*:").grid(row=5, column=1, sticky="e")
        self.password_entry = tk.Entry(self.root, textvariable=self.password, show="*")
        self.password_entry.grid(row=5, column=2, sticky="w")

        self.password_error = tk.Label(self.root, text="", fg="red")
        self.password_error.grid(row=6, column=2, sticky="w")
        # self.password_error.grid_remove()

        tk.Label(self.root, text="Confirm Password*:").grid(row=7, column=1,sticky="e")
        self.password_confirmation_entry = tk.Entry(self.root, textvariable=self.password_confirmation, show="*")
        self.password_confirmation_entry.grid(row=7, column=2, sticky="w")

        self.password_confirmation_error = tk.Label(self.root, text="", fg="red")
        self.password_confirmation_error.grid(row=8, column=2, sticky="w")
        # self.password_confirmation_error.grid_remove()

        tk.Button(self.root, text="Sign Up", command=self.Register).grid(row=9, column=2, sticky="w")
        tk.Button(self.root, text="Go Back", command=self.go_back).grid(row=9, column=2, sticky="e")

    def is_validate_email(self, *args):
        if self.email_entry == self.root.focus_get():
            if not re.match(r"[a-zA-Z0-9]+\.[a-zA-Z0-9]+@university\.com", self.email.get()):
                self.email_entry.config(highlightbackground="red")
                self.email_error["text"] = "Email should be in the format\nfirstname.lastname@university.com"
                self.email_error["justify"] = "left"
            else:
                self.email_entry.config(highlightbackground=self.name_entry.cget("background"))
                self.email_error["text"] = ""        

    def is_validate_password(self, *args):
        if self.password_entry == self.root.focus_get():
            if not re.match(r"^[A-Z](?=.*\d.*\d.*\d)(?=.*[a-zA-Z].*[a-zA-Z].*[a-zA-Z].*[a-zA-Z]).*$", self.password.get()):
                self.password_entry.config(highlightbackground="red")
                self.password_error["text"] = "Password must follow below rule:\n1. Start with an uppercase letter\n2. Contain at least 5 letters\n3. have 3 or more digits."
                self.password_error["justify"] = "left"
            else:
                self.password_entry.config(highlightbackground=self.name_entry.cget("background"))
                self.password_error["text"] = ""

    def is_validate_name(self):
        if not self.name_entry == self.root.focus_get():
            if not self.name.get():
                self.name_entry.config(highlightbackground="red")
                self.name_error["text"] = "This is a mandatory field!"
                self.name_error["justify"] = "left"
            else:
                self.name_entry.config(highlightbackground=self.name_entry.cget("background"))
                self.name_error["text"] = ""

    def validate_password_confirmation(self, *args):
        if self.password.get() != self.password_confirmation.get():
            self.password_confirmation_entry.config(highlightbackground="red")
            self.password_confirmation_error["text"] = "Passwords do not match. Please double check!"
        else:
            self.password_confirmation_entry.config(highlightbackground=self.name_entry.cget("background"))
            self.password_confirmation_error["text"] = ""

    def Register(self):
        if not self.name.get():
            msgbox.showerror(title="Error", message="Please enter your name!")
        elif self.email_error["text"]:
            msgbox.showerror(title="Error", message="Please change the email first!")
        elif self.password_error["text"]:
            msgbox.showerror(title="Error", message="Please correct the password first!")
        elif self.password.get() != self.password_confirmation.get():
            msgbox.showerror(title="Error", message="Passwords do not match.")
        else:
            success, message = self.db.create_newuser(self.name.get(), self.email.get(), self.password.get())
            if success:
                msgbox.showinfo(title="Success", message=message)
                self.root.destroy()
                login_page = LoginMasterPage(tk.Tk())
                login_page.mainloop()
            else:
                msgbox.showerror(title="Error", message=message)

    def go_back(self):
        self.root.destroy()
        login_page = LoginMasterPage(tk.Tk())
        login_page.mainloop()
        
if __name__ == '__main__':
    root = tk.Tk()
    RegistrationPage(master=root)
    root.mainloop()
