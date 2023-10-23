import tkinter as tk
import customtkinter as ctk
from PIL import Image
from Validation import Validator
from Widgets import *
from db import db

class ChangePassword:

    def __init__(self, master):
        self.forgotPassword = master
        self.initialize_window()
        self.create_widgets()
        self.bindValidationEvents()

    def initialize_window(self):
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

    def create_widgets(self):
        self.sideImage = CustomImage(self.forgotPassword, "GUI/Image/lightpurple/side-img.png", "GUI/Image/lightpurple/side-img.png", (300, 520), "", expand=True, side="left")
        self.forgotPasswordFrame = CustomFrame(self.forgotPassword, 300, 520, "#ffffff", False, expand=True, side="right")

        self.heading = CustomLabel(self.forgotPasswordFrame.get(), "heading","Change Password", "#9900FF", "headingFont","w", "w", pady=(50, 5), padx=(25, 0), justify="left")
        self.subHeading = CustomLabel(self.forgotPasswordFrame.get(), "subheading", "Choose your new password", "#7E7E7E", "subHeadingFont", "w", "w", padx=(25, 0), justify="left")

        self.emailLabel = CustomLabel(self.forgotPasswordFrame.get(), "email", "Email:", "#9900FF", "labelFont", "w", "w", pady=(38, 0), padx=(25, 0), justify="left", image=self.emailIcon, compound="left")
        self.emailEntry = CustomEntry(self.forgotPasswordFrame.get(), "email", 225, "#EEEEEE", "#000000", "#9900FF", "entryFont", 1, "w", pady=(0, 0), padx=(25, 0), show=None)
        self.emailEntryError = CustomLabel(self.forgotPasswordFrame.get(), "email", "", "#FF0000", "errorFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left")

        self.passwordLabel = CustomLabel(self.forgotPasswordFrame.get(), "password", "Password:", "#9900FF", "labelFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left", image=self.passwordIcon, compound="left")
        self.passwordEntry = CustomEntry(self.forgotPasswordFrame.get(), "password", 225, "#EEEEEE", "#000000", "#9900FF", "entryFont", 1, "w", pady=(0, 0), padx=(25, 0), show="*")
        self.passwordEntryError = CustomLabel(self.forgotPasswordFrame.get(), "password", "", "#FF0000", "errorFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left")

        self.confirmPasswordEntryLabel = CustomLabel(self.forgotPasswordFrame.get(), "confirmPassword", "Confirm Password:", "#9900FF", "labelFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left", image=self.passwordIcon, compound="left")
        self.confirmPasswordEntry = CustomEntry(self.forgotPasswordFrame.get(), "confirmPassword", 225, "#EEEEEE", "#000000", "#9900FF", "entryFont", 1, "w", pady=(0, 0), padx=(25, 0), show="*")
        self.confirmPasswordEntryError = CustomLabel(self.forgotPasswordFrame.get(), "confirmPassword", "", "#FF0000", "errorFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left")

        self.changePasswordButton = CustomButton(self.forgotPasswordFrame.get(), 225, "Submit", "#9900FF", "#E44982", "#ffffff", "buttonFont", "w", pady=(19, 0), padx=(25, 0))

    def bindValidationEvents(self):
        self.emailEntry.get().bind("<FocusOut>", lambda event: self.entryLeave("email"))
        self.passwordEntry.get().bind("<FocusOut>", lambda event: self.entryLeave("password"))
        self.confirmPasswordEntry.get().bind("<FocusOut>", lambda event: self.confirmPassword(event))

    def entryLeave(self, fieldName):
        entry = getattr(self, f"{fieldName}Entry")
        errorLabel = getattr(self, f"{fieldName}EntryError")

        validator = Validator(fieldName, entry, errorLabel, passwordEntry=self.passwordEntry)
        validator.validate()

    def confirmPassword(self, event):
        confirmPassword = self.confirmPasswordEntry.entryField["confirmPassword"].get()
        password = self.passwordEntry.entryField["password"].get()

        if password != confirmPassword:
            self.confirmPasswordEntry.get().configure(bg_color="#FF0000", text_color="#000000")
            self.confirmPasswordEntryError.get().configure(
                text="* Passwords do not match!",
                font=CustomFont.errorFont,
                text_color="#FF0000"
            )
        else:
            self.confirmPasswordEntry.get().configure(bg_color="#FFFFFF", text_color="#000000")
            self.confirmPasswordEntryError.get().configure(text="")

if __name__ == "__main__":
    forgotPassword = tk.Tk()
    forgotPasswordPage = ChangePassword(forgotPassword)
    forgotPassword.mainloop()