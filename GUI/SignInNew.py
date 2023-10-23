import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox as msgbox
from PIL import Image
from Widgets import *
from Validation import Validator
from db import db

class SignInPage:
    def __init__(self, master):
        self.login = master
        self.initializeWindow()
        self.createWidgets()
        self.bindValidationEvents()

    def initializeWindow(self):
        x = int(self.login.winfo_screenwidth() / 3 - self.login.winfo_reqwidth() / 3)
        y = int(self.login.winfo_screenheight() / 3 - self.login.winfo_reqheight() / 3)

        self.login.title("University Enrollment System v0.9.0")
        self.login.geometry(f"600x480+{x}+{y}")
        self.login.resizable(0, 0)

        emailIconFile = Image.open("GUI/Image/purple/email-icon.png")
        passwordIconFile = Image.open("GUI/Image/purple/password-icon.png")

        self.emailIcon = ctk.CTkImage(dark_image=emailIconFile, light_image=emailIconFile, size=(20,20))
        self.passwordIcon = ctk.CTkImage(dark_image=passwordIconFile, light_image=passwordIconFile, size=(17,17))


    def createWidgets(self):
        self.sideImage = CustomImage(self.login, "GUI/Image/purple/side-img.png", "GUI/Image/purple/side-img.png", (300, 480), "", expand=True, side="left")
        self.loginFrame = CustomFrame(self.login, 300, 480, "#ffffff", False, expand=True, side="right")

        self.heading = CustomLabel(self.loginFrame.get(), "heading","Welcome Back!", "#601E88", "headingFont","w", "w", pady=(50, 5), padx=(25, 0), justify="left")
        self.subHeading = CustomLabel(self.loginFrame.get(), "subheading","Sign in to your account", "#7E7E7E", "subHeadingFont", "w", "w", padx=(25, 0), justify="left")

        self.emailLabel = CustomLabel(self.loginFrame.get(), "email", "Email:", "#601E88", "labelFont", "w", "w", pady=(38, 0), padx=(25, 0), justify="left", image=self.emailIcon, compound="left")
        self.emailEntry = CustomEntry(self.loginFrame.get(), "email", 225, "#EEEEEE", "#000000", "#601E88", "entryFont", 1, "w", pady=(0, 0), padx=(25, 0), show=None)
        self.emailEntryError = CustomLabel(self.loginFrame.get(), "email","", "#FF0000", "errorFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left")

        self.passwordLabel = CustomLabel(self.loginFrame.get(), "password", "Password:", "#601E88", "labelFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left", image=self.passwordIcon, compound="left")
        self.passwordEntry = CustomEntry(self.loginFrame.get(), "password", 225, "#EEEEEE", "#000000", "#601E88", "entryFont", 1, "w", pady=(0, 0), padx=(25, 0), show="*")
        self.passwordEntryError = CustomLabel(self.loginFrame.get(), "password","", "#FF0000", "errorFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left")

        self.loginButton = CustomButton(self.loginFrame.get(), 225, "Login", "#601E88", "#E44982", "#ffffff", "buttonFont", "w", self.LoginAction, pady=(19, 0), padx=(25, 0))
        self.RegisterButton = CustomButton(self.loginFrame.get(), 225, "Create New Account", "#EEEEEE", "#c0c0c0", "#601E88", "buttonFont", "w", self.SignUp, pady=(20, 0), padx=(25, 0))

    def bindValidationEvents(self):
        self.emailEntry.get().bind("<FocusOut>", lambda event: self.entryLeave("email"))
        self.passwordEntry.get().bind("<FocusOut>", lambda event: self.entryLeave("password"))

    def entryLeave(self, fieldName):
        entry = getattr(self, f"{fieldName}Entry")
        errorLabel = getattr(self, f"{fieldName}EntryError")

        validator = Validator(fieldName, entry, errorLabel)
        validator.validate()

    def LoginAction(self):
        email = self.emailEntry.entryField["email"].get()
        password = self.passwordEntry.entryField["password"].get()
        success, message = db.verify_student_login(email, password)
        if success:
            msgbox.showinfo(title="Success", message=message)
            self.login.destroy()
            from StudentMainPage import MainPage
            Enrollment_Page = MainPage(tk.Tk())
            # Enrollment_Page.mainloop()
        else:
            msgbox.showerror(title="Error", message=message)

    def SignUp(self):
        self.login.destroy()
        from SignUpNew import SignUpPage
        SignUp_Page = SignUpPage(tk.Tk())

if __name__ == "__main__":
    login = tk.Tk()
    loginPage = SignInPage(login)
    login.mainloop()

    