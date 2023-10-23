import re
import customtkinter as ctk
from Widgets import CustomFont

class Validator:
    
    def __init__(self, fieldName, entry, errorLabel, passwordEntry=None):
        
        self.fieldName = fieldName
        self.entry = entry
        self.errorLabel = errorLabel
        self.passwordEntry = passwordEntry
        self.validationRuleDict = {
            "name": {
            "required": True,
            "validationFunction": None
            },
            "email": {
                "required": True,
                "validationFunction": self.email
            },
            "password": {
                "required": True,
                "validationFunction": self.password
            },
            # "confirmPassword": {
            #     "required": True,
            #     "validationFunction": self.confirmPassword
            # }
        }

    def validate(self):
        currentText = self.entry.get()
        rules = self.validationRuleDict[self.fieldName]

        if rules["required"] and currentText.get() == "":
            self.entry.get().configure(bg_color="#FF0000", text_color="#000000")
            self.errorLabel.get().configure(
                text="*This is a required field!", 
                font=CustomFont.errorFont, 
                text_color="#FF0000"
            )
            return False
        else:
            self.entry.get().configure(bg_color="#FFFFFF", text_color="#000000")
            self.errorLabel.get().configure(text="")

        if rules["validationFunction"]:
            # if self.fieldName == "confirmPassword":
            #     rules["validationFunction"] = lambda: self.confirmPassword(self.passwordEntry.get())
            return rules["validationFunction"]()

        return True

    def email(self):
        email = self.entry.get()
        errorLabel = self.errorLabel.get()

        if not re.match(r"(?i)[a-zA-Z0-9]+\.[a-zA-Z0-9]+@university\.com", email.get()):
            self.entry.get().configure(bg_color="#FF0000", text_color="#000000")
            self.errorLabel.get().configure(
                text="*Invalid email format!",
                font=CustomFont.errorFont,
                text_color="#FF0000"
            )
            return False
        else:
            self.entry.get().configure(bg_color="#FFFFFF", text_color="#000000")
            self.errorLabel.get().configure(text="")
            return True

    def password(self):
        password = self.entry.get()
        errorLabel = self.errorLabel.get()

        if not re.match(r"^[A-Z](?=.*\d.*\d.*\d)(?=.*[a-zA-Z].*[a-zA-Z].*[a-zA-Z].*[a-zA-Z]).*$", password.get()):
            self.entry.get().configure(bg_color="#FF0000", text_color="#000000")
            self.errorLabel.get().configure(
                text="* Invalid password format!",
                font=CustomFont.errorFont,
                text_color="#FF0000"
            )
            return False
        else:
            self.entry.get().configure(bg_color="#FFFFFF", text_color="#000000")
            self.errorLabel.get().configure(text="")
            return True

    # def confirmPassword(self, passwordEntry):
    #     confirmPassword = self.entry.get()
    #     password = self.passwordEntry.get() if self.passwordEntry else None

    #     if password != confirmPassword:
    #         self.entry.get().configure(bg_color="#FF0000", text_color="#000000")
    #         self.errorLabel.get().configure(
    #             text="* Passwords do not match!",
    #             font=CustomFont.errorFont,
    #             text_color="#FF0000"
    #         )
    #         return False
    #     else:
    #         self.entry.get().configure(bg_color="#FFFFFF", text_color="#000000")
    #         self.errorLabel.get().configure(text="")
    #         return True
