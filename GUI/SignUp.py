import tkinter as tk
import tkinter.messagebox as msgbox
import re
from PIL import ImageTk, Image


class SignUpPage:

    def __init__(self, master):
        self.signup = master
        self.initialize_window()
        self.create_widgets()
        self.validation_rules = {
            "Name": {
                "required": True,
                "validation_function": None
            },
            "Email": {
                "required": True,
                "validation_function": self.validate_email
            },
            "Password": {
                "required": True,
                "validation_function": self.validate_password
            },
            "Confirm Password": {
                "required": True,
                "validation_function": self.validate_confirm_password
            }
        }

    def initialize_window(self):
        x = int(self.signup.winfo_screenwidth() / 3 - self.signup.winfo_reqwidth() / 3)
        y = int(self.signup.winfo_screenheight() / 3 - self.signup.winfo_reqheight() / 3)

        self.signup.title("Registration")
        self.signup.geometry(f"990x660+{x}+{y}")
        self.signup.resizable(0, 0)

    def create_widgets(self):
        self.entry_fields = {}
        self.error_labels = {}
        self.create_background_image()
        self.registration_frame()
        self.create_heading_label()
        self.create_entry("Name", "firebrick1", 2)
        self.name_error = self.create_error_label("NameError", 3)
        self.create_entry("Email", "firebrick1", 4)
        self.email_error = self.create_error_label("EmailError", 5)
        self.create_entry("Password", "firebrick1", 6)
        self.password_error = self.create_error_label("PasswordError", 7)
        self.create_entry("Confirm Password", "firebrick1", 8)
        self.password_confirmation_error = self.create_error_label("PasswordConfirmationError", 9)
        self.create_signup_button()
        self.already_have_account_label()
        self.login_label()

        self.error_labels = {
            "Name": self.name_error,
            "Email": self.email_error,
            "Password": self.password_error,
            "Confirm Password": self.password_confirmation_error
        }    

    def create_background_image(self):
        self.bgImage = ImageTk.PhotoImage(file="GUI/Image/bg.jpg")
        bgLabel = tk.Label(self.signup, image=self.bgImage)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

    def registration_frame(self):
        self.frame = tk.Frame(self.signup, bg="white")
        self.frame.place(x=553, y=99)
        self.frame.grid_columnconfigure(0, weight=1, minsize=20)
        self.frame.grid_columnconfigure(2, weight=1, minsize=20)

    def create_heading_label(self):
        self.heading = tk.Label(self.frame, text="CREATE AN ACCOUNT")
        self.heading.grid(row=1, column=1, pady=40)
        self.heading.config(
            font=("Helvetica", 22, "bold"),
            bg="white",
            fg="firebrick1"
            )

    def create_entry(self, field_name, text_color, row, show=None):
        entry_var = tk.StringVar()
        entry = tk.Entry(self.frame, fg=text_color, show=show if show else None, textvariable=entry_var)
        entry.insert(0, field_name)
        entry.grid(row=row, column=1)
        entry.bind("<FocusIn>", lambda event: self.on_entry_click(event, field_name))
        entry.bind("<FocusOut>", lambda event: self.on_entry_leave(event, field_name))
        entry.config(
            font=("Helvetica", 15),
            bg="white",
            fg="firebrick1",
            width=25,
            highlightthickness=1,
            highlightbackground="firebrick1",
            highlightcolor="firebrick1"
        )
        self.entry_fields[field_name] = entry
        return entry
    
    def create_error_label(self, field_name, row):
        error = tk.Label(self.frame, text="")
        error.grid(row=row, column=1, padx=10, sticky="w")
        error.config(
            font=("Helvetica", 12, "italic"),
            bg="white",
            fg="red"
        )
        self.error_labels[field_name] = error
        return error

    def create_signup_button(self):
        self.signup_button = tk.Button(self.frame, text="Sign Up")
        self.signup_button.grid(row=10, column=1, pady=20)
        self.signup_button.config(
            font=("Helvetica", 15, "bold"),
            bd=0,
            bg="firebrick1",
            fg="white",
            width=23,
            highlightthickness=0,  # Set to 0 to remove the default border
            activebackground="firebrick1",
            activeforeground="white",
            cursor="pointinghand"
        )

    def already_have_account_label(self):
        self.already_have_account = tk.Label(self.frame, text="Already have an account?")
        self.already_have_account.grid(row=11, column=1, padx=35, pady=20, sticky="w")
        self.already_have_account.config(
            font=("Helvetica", 11, "bold"),
            bd=0,
            bg="white",
            fg="firebrick1",
            highlightthickness=0,  # Set to 0 to remove the default border
            activebackground="white"
        )

    def login_label(self):
        self.login = tk.Label(self.frame, text="Log in")
        self.login.place(x=195, y=373)
        self.login.config(
            font=("Helvetica", 11, "bold underline "),
            bd=0,
            bg="white",
            fg="blue",
            highlightthickness=0,  # Set to 0 to remove the default border
            activebackground="white",
            activeforeground="blue",
            cursor="pointinghand"
        )
    def on_entry_click(self, event, field_name):
        entry = event.widget
        current_text = entry.get()
        if "password" in field_name.lower():
            show_text = "*"
        else:
            show_text = ""
        if current_text == field_name:
            entry.delete(0, "end")
        entry.config(show=show_text)

    def on_entry_leave(self, event, field_name):
        entry = event.widget
        current_text = entry.get()
        show_text = ""
        if current_text == "":
            entry.delete(0, "end")
            entry.insert(0, field_name)
            if "password" in field_name.lower():
                show_text = ""
        else:
            if "password" in field_name.lower():
                show_text = "*"
        entry.config(show=show_text)

        self.validate_field(field_name=field_name)

    def validate_email(self):
        email = self.entry_fields["Email"].get()
        if not re.match(r"(?i)[a-zA-Z0-9]+\.[a-zA-Z0-9]+@university\.com", email):
            self.entry_fields["Email"].config(bg="firebrick1", fg="white")
            self.error_labels["Email"].config(
                text="*Invalid email format!",
                font=("Helvetica", 12, "italic"),
                fg="red"
            )
            return False
        else:
            self.entry_fields["Email"].config(bg="white", fg="firebrick1")
            self.error_labels["Email"].config(text="")
            return True

    def validate_password(self):
        password = self.entry_fields["Password"].get()
        if not re.match(r"^[A-Z](?=.*\d.*\d.*\d)(?=.*[a-zA-Z].*[a-zA-Z].*[a-zA-Z].*[a-zA-Z]).*$", password):
            self.entry_fields["Password"].config(bg="firebrick1", fg="white")
            self.error_labels["Password"].config(
                text="* Invalid password format!",
                font=("Helvetica", 12, "italic"),
                fg="red"
            )
            return False
        else:
            self.entry_fields["Password"].config(bg="white", fg="firebrick1")
            self.error_labels["Password"].config(text="")
            return True

    def validate_confirm_password(self):
        password = self.entry_fields["Password"].get()
        confirm_password = self.entry_fields["Confirm Password"].get()
        if password != confirm_password:
            self.entry_fields["Confirm Password"].config(bg="firebrick1", fg="white")
            self.error_labels["Confirm Password"].config(
                text="* Passwords do not match!",
                font=("Helvetica", 12, "italic"),
                fg="red"
            )
            return False
        else:
            self.entry_fields["Confirm Password"].config(bg="white", fg="firebrick1")
            self.error_labels["Confirm Password"].config(text="")
            return True                                       

    def validate_field(self, field_name):
        current_text = self.entry_fields[field_name].get()
        rules = self.validation_rules[field_name]
        
        if rules["required"] and current_text.strip() == field_name:
            self.entry_fields[field_name].config(bg="firebrick1", fg="white")
            self.error_labels[field_name].config(
                text="*This is a required field!", 
                font=("Helvetica", 12, "italic"), 
                fg="red"
            )
            return False
        else:
            self.entry_fields[field_name].config(bg="white", fg="firebrick1")
            self.error_labels[field_name].config(text="")
        if rules["validation_function"]:
            return rules["validation_function"]()
        return True

if __name__ == "__main__":
    signup = tk.Tk()
    signup_page = SignUpPage(signup)
    signup.mainloop()
