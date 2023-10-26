import re
import customtkinter as ctk

from Widgets import CustomFont

import logging
logging.basicConfig(level=logging.DEBUG)

class Validator:
    
    def __init__(self, fieldName, entry, errorLabel, passwordValue: str=None):
        self.fieldName = fieldName
        self.entry = entry
        self.errorLabel = errorLabel
        self.passwordValue = passwordValue
        self.validationRuleDict = {
            "Name": {
            "required": True,
            "validationFunction": None
            },
            "Email": {
                "required": True,
                "validationFunction": self.email
            },
            "Password": {
                "required": True,
                "validationFunction": self.password
            },
            "ConfirmPassword": {
                "required": True,
                "validationFunction": self.confirmPassword
            }
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
            if self.fieldName == "ConfirmPassword":
                return rules["validationFunction"](self.passwordValue)
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

    def confirmPassword(self, passwordValue):
        confirmPassword = self.entry.get().get()
        errorLabel = self.errorLabel.get()
        logging.info("ConfirmPassword: %s", confirmPassword)

        if confirmPassword != passwordValue:
            self.entry.get().configure(bg_color="#FF0000", text_color="#000000")
            self.errorLabel.get().configure(
                text="* Passwords do not match!",
                font=CustomFont.errorFont,
                text_color="#FF0000"
            )
            return False
        else:
            self.entry.get().configure(bg_color="#FFFFFF", text_color="#000000")
            self.errorLabel.get().configure(text="")
            return True
