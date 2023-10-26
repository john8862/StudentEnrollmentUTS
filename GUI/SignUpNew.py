import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox as msgbox
from PIL import Image
from Validation import Validator
from Widgets import *
from db import db

class SignUpPage:
    def __init__(self, master):
        self.register = master
        self.initializeWindow()
        self.createWidgets()
        self.bindValidationEvents()

    def initializeWindow(self):
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

    def createWidgets(self):
        self.sideImage = CustomImage(self.register, "GUI/Image/orange/side-img.png", "GUI/Image/orange/side-img.png", (300, 600), "", expand=True, side="left")
        # self.registerFrame = CustomFrame(self.register, 300, 480, "#ffffff", False, expand=True, side="right")
        self.registerFrame = CustomFrame(self.register, 300, 600, "#ffffff", False, expand=True, side="right")

        self.heading = CustomLabel(self.registerFrame.get(), "Heading", "Create New Account", "#FF6633", "headingFont","w", "w", pady=(50, 5), padx=(25, 0), justify="left")
        self.subHeading = CustomLabel(self.registerFrame.get(), "Subheading", "Sign up a new student account", "#7E7E7E", "subHeadingFont", "w", "w", padx=(25, 0), justify="left")

        self.nameLabel = CustomLabel(self.registerFrame.get(), "Name", "Name:", "#FF6633", "labelFont", "w", "w", pady=(18, 0), padx=(25, 0), justify="left", image=self.nameIcon, compound="left")
        self.nameEntry = CustomEntry(self.registerFrame.get(), "Name", 225, "#EEEEEE", "#000000", "#FF6633", "entryFont", 1, "w", pady=(0, 0), padx=(25, 0), show=None)
        self.nameEntryError = CustomLabel(self.registerFrame.get(), "Name", "", "#FF0000", "errorFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left")

        self.emailLabel = CustomLabel(self.registerFrame.get(), "Email", "Email:", "#FF6633", "labelFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left", image=self.emailIcon, compound="left")
        self.emailEntry = CustomEntry(self.registerFrame.get(), "Email", 225, "#EEEEEE", "#000000", "#FF6633", "entryFont", 1, "w", pady=(0, 0), padx=(25, 0), show=None)
        self.emailEntryError = CustomLabel(self.registerFrame.get(), "Email", "", "#FF0000", "errorFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left")

        self.passwordLabel = CustomLabel(self.registerFrame.get(), "Password", "Password:", "#FF6633", "labelFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left", image=self.passwordIcon, compound="left")
        self.passwordEntry = CustomEntry(self.registerFrame.get(), "Password", 225, "#EEEEEE", "#000000", "#FF6633", "entryFont", 1, "w", pady=(0, 0), padx=(25, 0), show="*")
        self.passwordEntryError = CustomLabel(self.registerFrame.get(), "Password", "", "#FF0000", "errorFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left")

        self.confirmpasswordLabel = CustomLabel(self.registerFrame.get(), "ConfirmPassword", "Confirm Password:", "#FF6633", "labelFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left", image=self.passwordIcon, compound="left")
        self.confirmpasswordEntry = CustomEntry(self.registerFrame.get(), "ConfirmPassword", 225, "#EEEEEE", "#000000", "#FF6633", "entryFont", 1, "w", pady=(0, 0), padx=(25, 0), show="*")
        self.confirmpasswordEntryError = CustomLabel(self.registerFrame.get(), "ConfirmPassword", "", "#FF0000", "errorFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left")

        self.registerButton = CustomButton(self.registerFrame.get(), 225, "Sign Up", "#FF6633", "#E44982", "#ffffff", "buttonFont", "w", self.SignUpAction, pady=(15, 0), padx=(25, 0))
        self.goBackButton = CustomButton(self.registerFrame.get(), 225, "Go Back", "#EEEEEE", "#c0c0c0", "#FF0000", "buttonFont", "w", self.GoBack, pady=(15, 0), padx=(25, 0))

    def bindValidationEvents(self):
        self.nameEntry.get().bind("<FocusOut>", lambda event: self.entryLeave("Name"))
        self.emailEntry.get().bind("<FocusOut>", lambda event: self.entryLeave("Email"))
        self.passwordEntry.get().bind("<FocusOut>", lambda event: self.entryLeave("Password"))
        self.confirmpasswordEntry.get().bind("<FocusOut>", lambda event: self.entryLeave("ConfirmPassword"))

    def entryLeave(self, fieldName):
        entry = getattr(self, f"{fieldName.lower()}Entry")
        errorLabel = getattr(self, f"{fieldName.lower()}EntryError")

        validator = Validator(fieldName, entry, errorLabel, passwordValue=self.passwordEntry.get().get())
        validator.validate()

    def SignUpAction(self):
        nameError = self.nameEntryError.LabelField["Name"].cget("text")
        emailError = self.emailEntryError.LabelField["Email"].cget("text")
        passwordError = self.passwordEntryError.LabelField["Password"].cget("text")
        confirmPasswordError = self.confirmPasswordEntryError.LabelField["ConfirmPassword"].cget("text")

        if nameError:
            msgbox.showerror("Error", "Name is required!")
        elif emailError:
            msgbox.showerror("Error", "Please enter a valid email address!")
        elif passwordError:
            msgbox.showerror("Error", "Please enter a valid password!")
        elif confirmPasswordError:
            msgbox.showerror("Error", "Passwords do not match!")

        else:
            name = self.nameEntry.entryVar.get()
            email = self.emailEntry.entryVar.get()
            password = self.passwordEntry.entryVar.get()

            success, message = db.create_newuser(name, email, password)
            if success:
                msgbox.showinfo("Success", message=message)
                self.register.destroy()
                from SignInNew import SignInPage
                loginPage = SignInPage(tk.Tk())
            else:
                msgbox.showerror("Error", message=message)
        
    
    def GoBack(self):
        self.register.destroy()
        from SignInNew import SignInPage
        loginPage = SignInPage(tk.Tk())

if __name__ == "__main__":
    register = tk.Tk()
    registerPage = SignUpPage(register)
    register.mainloop()