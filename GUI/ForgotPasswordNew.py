import tkinter as tk
import customtkinter as ctk
from PIL import Image
from Widgets import *
from db import db

class ChangePassword:

    def __init__(self, master):
        self.forgotPassword = master
        self.initialize_window()
        self.create_widgets()

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

        self.heading = CustomLabel(self.forgotPasswordFrame.get(), "Change Password", "#9900FF", "headingFont","w", "w", pady=(50, 5), padx=(25, 0), justify="left")
        self.subHeading = CustomLabel(self.forgotPasswordFrame.get(), "Choose your new password", "#7E7E7E", "subHeadingFont", "w", "w", padx=(25, 0), justify="left")

        self.emailLabel = CustomLabel(self.forgotPasswordFrame.get(), "Email:", "#9900FF", "labelFont", "w", "w", pady=(38, 0), padx=(25, 0), justify="left", image=self.emailIcon, compound="left")
        self.emailEntry = CustomEntry(self.forgotPasswordFrame.get(), 225, "#EEEEEE", "#000000", "#9900FF", "entryFont", 1, "w", pady=(0, 0), padx=(25, 0), show=None)
        self.emailEntryError = CustomLabel(self.forgotPasswordFrame.get(), "", "#FF0000", "errorFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left")

        self.passwordLabel = CustomLabel(self.forgotPasswordFrame.get(), "Password:", "#9900FF", "labelFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left", image=self.passwordIcon, compound="left")
        self.passwordEntry = CustomEntry(self.forgotPasswordFrame.get(), 225, "#EEEEEE", "#000000", "#9900FF", "entryFont", 1, "w", pady=(0, 0), padx=(25, 0), show="*")
        self.passwordEntryError = CustomLabel(self.forgotPasswordFrame.get(), "", "#FF0000", "errorFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left")

        self.passwordConfirmationLabel = CustomLabel(self.forgotPasswordFrame.get(), "Confirm Password:", "#9900FF", "labelFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left", image=self.passwordIcon, compound="left")
        self.passwordConfirmationEntry = CustomEntry(self.forgotPasswordFrame.get(), 225, "#EEEEEE", "#000000", "#9900FF", "entryFont", 1, "w", pady=(0, 0), padx=(25, 0), show="*")
        self.passwordConfirmationEntryError = CustomLabel(self.forgotPasswordFrame.get(), "", "#FF0000", "errorFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left")

        self.changePasswordButton = CustomButton(self.forgotPasswordFrame.get(), 225, "Submit", "#9900FF", "#E44982", "#ffffff", "buttonFont", "w", pady=(19, 0), padx=(25, 0))

if __name__ == "__main__":
    forgotPassword = tk.Tk()
    forgotPasswordPage = ChangePassword(forgotPassword)
    forgotPassword.mainloop()