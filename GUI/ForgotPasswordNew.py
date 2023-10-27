import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox as msgbox
from PIL import Image
from Validation import Validator
from Widgets import *
from db import db

class ChangePasswordPage:

    def __init__(self, master):
        self.forgotPassword = master
        self.initializeWindow()
        self.createWidgets()
        self.bindEvents()

    def initializeWindow(self):
        x = int(self.forgotPassword.winfo_screenwidth() / 3 - self.forgotPassword.winfo_reqwidth() / 3)
        y = int(self.forgotPassword.winfo_screenheight() / 3 - self.forgotPassword.winfo_reqheight() / 3)

        self.forgotPassword.title("University Enrollment System v0.9.0")
        self.forgotPassword.geometry(f"600x520+{x}+{y}")
        self.forgotPassword.resizable(0, 0)

        nameIconFile = Image.open("GUI/Image/lightpurple/name-icon.png")
        emailIconFile = Image.open("GUI/Image/lightpurple/email-icon.png")
        passwordIconFile = Image.open("GUI/Image/lightpurple/password-icon.png")

        self.nameIcon = ctk.CTkImage(dark_image=nameIconFile, light_image=nameIconFile, size=(20,20))
        self.emailIcon = ctk.CTkImage(dark_image=emailIconFile, light_image=emailIconFile, size=(20,20))
        self.passwordIcon = ctk.CTkImage(dark_image=passwordIconFile, light_image=passwordIconFile, size=(17,17))

    def createWidgets(self):
        self.sideImage = CustomImage(self.forgotPassword, "GUI/Image/lightpurple/side-img.png", "GUI/Image/lightpurple/side-img.png", (300, 520), "", expand=True, side="left")
        self.forgotPasswordFrame = CustomFrame(self.forgotPassword, 300, 520, "#ffffff", False, expand=True, side="right")

        self.heading = CustomLabel(self.forgotPasswordFrame.get(), "Heading","Change Password", "#9900FF", "headingFont","w", "w", pady=(50, 5), padx=(25, 0), justify="left")
        self.subHeading = CustomLabel(self.forgotPasswordFrame.get(), "Subheading", "Choose your new password", "#7E7E7E", "subHeadingFont", "w", "w", padx=(25, 0), justify="left")

        self.emailLabel = CustomLabel(self.forgotPasswordFrame.get(), "email", "Email:", "#9900FF", "labelFont", "w", "w", pady=(38, 0), padx=(25, 0), justify="left", image=self.emailIcon, compound="left")
        self.emailEntry = CustomEntry(self.forgotPasswordFrame.get(), "email", 225, "#EEEEEE", "#000000", "#9900FF", "entryFont", 1, "w", pady=(0, 0), padx=(25, 0), show=None)
        self.emailEntryError = CustomLabel(self.forgotPasswordFrame.get(), "email", "", "#FF0000", "errorFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left")

        self.passwordLabel = CustomLabel(self.forgotPasswordFrame.get(), "Password", "New Password:", "#9900FF", "labelFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left", image=self.passwordIcon, compound="left")
        self.passwordEntry = CustomEntry(self.forgotPasswordFrame.get(), "Password", 225, "#EEEEEE", "#000000", "#9900FF", "entryFont", 1, "w", pady=(0, 0), padx=(25, 0), show="*")
        self.passwordEntryError = CustomLabel(self.forgotPasswordFrame.get(), "Password", "", "#FF0000", "errorFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left")

        self.confirmpasswordEntryLabel = CustomLabel(self.forgotPasswordFrame.get(), "ConfirmPasword", "Confirm Password:", "#9900FF", "labelFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left", image=self.passwordIcon, compound="left")
        self.confirmpasswordEntry = CustomEntry(self.forgotPasswordFrame.get(), "ConfirmPasword", 225, "#EEEEEE", "#000000", "#9900FF", "entryFont", 1, "w", pady=(0, 0), padx=(25, 0), show="*")
        self.confirmpasswordEntryError = CustomLabel(self.forgotPasswordFrame.get(), "ConfirmPasword", "", "#FF0000", "errorFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left")

        self.changePasswordButton = CustomButton(self.forgotPasswordFrame.get(), 225, "Submit", "#9900FF", "#E44982", "#ffffff", "buttonFont", "w", command=self.submitPassword, pady=(19, 0), padx=(25, 0))

    def bindEvents(self):
        self.emailEntry.get().bind("<FocusOut>", lambda event: self.entryLeave("Email"))
        self.passwordEntry.get().bind("<FocusOut>", lambda event: self.entryLeave("Password"))
        self.confirmpasswordEntry.get().bind("<FocusOut>", lambda event: self.entryLeave("ConfirmPassword"))

    def entryLeave(self, fieldName):
        entry = getattr(self, f"{fieldName.lower()}Entry")
        errorLabel = getattr(self, f"{fieldName.lower()}EntryError")

        validator = Validator(fieldName, entry, errorLabel, passwordValue=self.passwordEntry.get().get())
        validator.validate()

    def submitPassword(self):
        emailError = self.emailEntryError.get().cget("text")
        passwordError = self.passwordEntryError.get().cget("text")
        confirmpasswordError = self.confirmpasswordEntryError.get().cget("text")

        if emailError:
            msgbox.showerror("Error", message="Please enter a valid email address!")
        elif passwordError:
            msgbox.showerror("Error", message="Please enter a valid password!")
        elif confirmpasswordError:
            msgbox.showerror("Error", message="Passwords do not match!")
        else:
            email = self.emailEntry.entryVar.get()
            password = self.passwordEntry.entryVar.get()

            success, message = db.change_password(email, password)
            if success:
                msgbox.showinfo("Success", message=message)
                self.forgotPassword.destroy()
            else:
                msgbox.showerror("Error", message=message)

if __name__ == "__main__":
    forgotPassword = tk.Tk()
    forgotPasswordPage = ChangePasswordPage(forgotPassword)
    forgotPassword.mainloop()