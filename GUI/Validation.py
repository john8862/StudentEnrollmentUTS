import re
import customtkinter as ctk
from Widgets import CustomFont

class ValidationRule:
    def __init__(self, fieldName, entry, errorLabel,):
        self.fieldName = fieldName
        self.entry = entry
        self.errorLabel = errorLabel

    def validate(self):
        pass

class RequiredRule(ValidationRule):
    def validate(self):
        if not self.entry.get():
            self.entry.config(bg_color="#FF0000", text_color="#000000")
            self.errorLabel.configure(
                text="*This is a required field!",
                font=CustomFont.errorFont,
                text_color="#FF0000"
            )
            return False
        else:
            self.entry.configure(bg_color="#FFFFFF", text_color="#000000")
            self.error_label.configure(text="")
            return True

class EmailRule(ValidationRule):
    def validate(self):
        email = self.entry.get()
        if not re.match(r"(?i)[a-zA-Z0-9]+\.[a-zA-Z0-9]+@university\.com", email):
            self.entry.configure(bg_color="#FF0000", text_color="#000000")
            self.errorLabel.configure(
                text="*Invalid email format!",
                font=CustomFont.errorFont,
                text_color="#FF0000"
            )
            return False
        else:
            self.entry.configure(bg_color="#FFFFFF", text_color="#000000")
            self.errorLabel.configure(text="")
            return True

class PasswordRule(ValidationRule):
    def validate(self):
        password = self.entry.get()
        if not re.match(r"^[A-Z](?=.*\d.*\d.*\d)(?=.*[a-zA-Z].*[a-zA-Z].*[a-zA-Z].*[a-zA-Z]).*$", password):
            self.entry.configure(bg_color="#FF0000", text_color="#000000")
            self.errorLabel.configure(
                text="* Invalid password format!",
                font=CustomFont.errorFont,
                text_color="#FF0000"
            )
            return False
        else:
            self.entry.configure(bg_color="#FFFFFF", text_color="#000000")
            self.error_label.configure(text="")
            return True

class ConfirmPasswordRule(ValidationRule):
    def __init__(self, passwordEntry, confirmPasswordEntry, errorLabel):
        self.passwordEntry = passwordEntry
        self.confirmPasswordEntry = confirmPasswordEntry
        self.errorLabel = errorLabel

    def validate(self):
        password = self.passwordEntry.get()
        confirmPassword = self.confirmPasswordEntry.get()
        if password != confirmPassword:
            self.confirmPasswordEntry.configure(bg_color="#FF0000", text_color="#000000")
            self.errorLabel.configure(
                text="* Passwords do not match!",
                font=CustomFont.errorFont,
                text_color="#FF0000"
            )
            return False
        else:
            self.confirmPasswordEntry.configure(bg_color="#FFFFFF", text_color="#000000")
            self.errorLabel.configure(text="")
            return True

