import tkinter as tk
import customtkinter as ctk
from PIL import Image
from Widgets import *
from Validation import *
from db import db

class SignInPage:
    def __init__(self, master):
        self.login = master
        self.initializeWindow()
        self.createWidgets()
        # self.initializeValidationRules()
        # self.bindValidationEvents()

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

        self.heading = CustomLabel(self.loginFrame.get(), "Welcome Back!", "#601E88", "headingFont","w", "w", pady=(50, 5), padx=(25, 0), justify="left")
        self.subHeading = CustomLabel(self.loginFrame.get(), "Sign in to your account", "#7E7E7E", "subHeadingFont", "w", "w", padx=(25, 0), justify="left")

        self.emailLabel = CustomLabel(self.loginFrame.get(), "Email:", "#601E88", "labelFont", "w", "w", pady=(38, 0), padx=(25, 0), justify="left", image=self.emailIcon, compound="left")
        self.emailEntry = CustomEntry(self.loginFrame.get(), 225, "#EEEEEE", "#000000", "#601E88", "entryFont", 1, "w", pady=(0, 0), padx=(25, 0), show=None, name="email")
        self.emailEntryError = CustomLabel(self.loginFrame.get(), "", "#FF0000", "errorFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left")

        self.passwordLabel = CustomLabel(self.loginFrame.get(), "Password:", "#601E88", "labelFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left", image=self.passwordIcon, compound="left")
        self.passwordEntry = CustomEntry(self.loginFrame.get(), 225, "#EEEEEE", "#000000", "#601E88", "entryFont", 1, "w", pady=(0, 0), padx=(25, 0), show="*", name="password")
        self.passwordEntryError = CustomLabel(self.loginFrame.get(), "", "#FF0000", "errorFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left")

        self.loginButton = CustomButton(self.loginFrame.get(), 225, "Login", "#601E88", "#E44982", "#ffffff", "buttonFont", "w", pady=(19, 0), padx=(25, 0))
        self.RegisterButton = CustomButton(self.loginFrame.get(), 225, "Create New Account", "#EEEEEE", "#c0c0c0", "#601E88", "buttonFont", "w", pady=(20, 0), padx=(25, 0))

    # def initializeValidationRules(self):
    #     self.validationRuleDict = {
    #         "email": [RequiredRule, EmailRule],
    #         "password": [RequiredRule, PasswordRule]
    #     }

    # def validateField(self, fieldName):
    #     entryWidget = getattr(self, f"{fieldName}Entry")
    #     errorWidget = getattr(self, f"{fieldName}EntryError")
    #     isValid = True

    #     for RuleClass in self.validationRuleDict[fieldName]:
    #         ruleInstance = RuleClass(fieldName, entryWidget, errorWidget)
    #         if not ruleInstance.validate():
    #             isValid = False

    #     return isValid


if __name__ == "__main__":
    login = tk.Tk()
    loginPage = SignInPage(login)
    login.mainloop()

    