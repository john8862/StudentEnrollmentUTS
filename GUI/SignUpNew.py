import tkinter as tk
import customtkinter as ctk
from PIL import Image
from Widgets import *
from db import db

class SignUpPage:
    def __init__(self, master):
        self.register = master
        self.initialize_window()
        self.create_widgets()
        # self.validationRules = {
        #     "name": {
        # }

    def initialize_window(self):
        x = int(self.register.winfo_screenwidth() / 3 - self.register.winfo_reqwidth() / 3)
        y = int(self.register.winfo_screenheight() / 3 - self.register.winfo_reqheight() / 3)

        self.register.title("University Enrollment System v0.9.0")
        self.register.geometry(f"600x600+{x}+{y}")
        # self.register.geometry(f"600x480+{x}+{y}")
        self.register.resizable(0, 0)

        nameIconFile = Image.open("GUI/Image/orange/name-icon.png")
        emailIconFile = Image.open("GUI/Image/orange/email-icon.png")
        passwordIconFile = Image.open("GUI/Image/orange/password-icon.png")

        self.nameIcon = ctk.CTkImage(dark_image=nameIconFile, light_image=nameIconFile, size=(20,20))
        self.emailIcon = ctk.CTkImage(dark_image=emailIconFile, light_image=emailIconFile, size=(20,20))
        self.passwordIcon = ctk.CTkImage(dark_image=passwordIconFile, light_image=passwordIconFile, size=(17,17))

    def create_widgets(self):
        self.sideImage = CustomImage(self.register, "GUI/Image/orange/side-img.png", "GUI/Image/orange/side-img.png", (300, 600), "", expand=True, side="left")
        # self.registerFrame = CustomFrame(self.register, 300, 480, "#ffffff", False, expand=True, side="right")
        self.registerFrame = CustomFrame(self.register, 300, 600, "#ffffff", False, expand=True, side="right")

        self.heading = CustomLabel(self.registerFrame.get(), "Create New Account", "#FF6633", "headingFont","w", "w", pady=(50, 5), padx=(25, 0), justify="left")
        self.subHeading = CustomLabel(self.registerFrame.get(), "Sign up a new student account", "#7E7E7E", "subHeadingFont", "w", "w", padx=(25, 0), justify="left")

        self.nameLabel = CustomLabel(self.registerFrame.get(), "Name:", "#FF6633", "labelFont", "w", "w", pady=(38, 0), padx=(25, 0), justify="left", image=self.nameIcon, compound="left")
        self.nameEntry = CustomEntry(self.registerFrame.get(), 225, "#EEEEEE", "#000000", "#FF6633", "entryFont", 1, "w", pady=(0, 0), padx=(25, 0), show=None)
        self.nameEntryError = CustomLabel(self.registerFrame.get(), "", "#FF0000", "errorFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left")

        self.emailLabel = CustomLabel(self.registerFrame.get(), "Email:", "#FF6633", "labelFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left", image=self.emailIcon, compound="left")
        self.emailEntry = CustomEntry(self.registerFrame.get(), 225, "#EEEEEE", "#000000", "#FF6633", "entryFont", 1, "w", pady=(0, 0), padx=(25, 0), show=None)
        self.emailEntryError = CustomLabel(self.registerFrame.get(), "", "#FF0000", "errorFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left")

        self.passwordLabel = CustomLabel(self.registerFrame.get(), "Password:", "#FF6633", "labelFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left", image=self.passwordIcon, compound="left")
        self.passwordEntry = CustomEntry(self.registerFrame.get(), 225, "#EEEEEE", "#000000", "#FF6633", "entryFont", 1, "w", pady=(0, 0), padx=(25, 0), show="*")
        self.passwordEntryError = CustomLabel(self.registerFrame.get(), "", "#FF0000", "errorFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left")

        self.passwordConfirmationLabel = CustomLabel(self.registerFrame.get(), "Confirm Password:", "#FF6633", "labelFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left", image=self.passwordIcon, compound="left")
        self.passwordConfirmationEntry = CustomEntry(self.registerFrame.get(), 225, "#EEEEEE", "#000000", "#FF6633", "entryFont", 1, "w", pady=(0, 0), padx=(25, 0), show="*")
        self.passwordConfirmationEntryError = CustomLabel(self.registerFrame.get(), "", "#FF0000", "errorFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left")

        self.registerButton = CustomButton(self.registerFrame.get(), 225, "Sign Up", "#FF6633", "#E44982", "#ffffff", "buttonFont", "w", pady=(25, 0), padx=(25, 0))

if __name__ == "__main__":
    register = tk.Tk()
    registerPage = SignUpPage(register)
    register.mainloop()