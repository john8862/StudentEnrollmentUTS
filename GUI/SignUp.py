import tkinter as tk
import tkinter.messagebox as msgbox
import re
from PIL import ImageTk, Image


class SignUpPage:

    def __init__(self, master):
        self.signup = master
        self.initialize_window()
        self.create_widgets()
        self.configure_widgets()
        self.validation_rules = {
            "Name": {
                "required": True,
                "validation_function": None
            },
            "Email": {
                "required": True,
                "validation_function": self.is_validate_email
            },
            "Password": {
                "required": True,
                "validation_function": self.is_validate_password
            },
            "Confirm Password": {
                "required": True,
                "validation_function": None
            }
        }  # Initialize the validation_rules dictionary

    def initialize_window(self):
        x = int(self.signup.winfo_screenwidth() / 3 - self.signup.winfo_reqwidth() / 3)
        y = int(self.signup.winfo_screenheight() / 3 - self.signup.winfo_reqheight() / 3)

        self.signup.title("Registration")
        self.signup.geometry(f"990x660+{x}+{y}")
        self.signup.resizable(0, 0)

    def create_widgets(self):
        self.create_background_image()
        self.registration_frame()
        self.create_heading_label()
        # self.create_entry("Name", "firebrick1", row=2)
        self.create_name_entry()
        self.name_error_label()
        # self.create_entry("Email", "firebrick1", row=4)
        self.create_email_entry()
        self.email_error_label()
        # self.create_entry("Password", "firebrick1", row=6)
        self.create_password_entry()
        self.password_error_label()
        # self.create_entry("Confirm Password", "firebrick1", row=8)
        self.create_password_confirmation_entry()
        self.password_confirmation_error_label()
        self.create_signup_button()
        self.already_have_account_label()
        self.login_label()

    def configure_widgets(self):
        self.configure_frame()
        self.configure_heading_label()
        # self.configure_entry("Name")
        self.configure_name_entry()
        self.configure_name_error()
        # self.configure_entry("Email")
        self.configure_email_entry()
        self.configure_email_error()
        # self.configure_entry("Password")
        self.configure_password_entry()
        self.configure_password_error()
        # self.configure_entry("Confirm Password")
        self.configure_password_confirmation_entry()
        self.configure_password_confirmation_error()
        self.configure_signup_button()
        self.configure_already_have_account()
        self.configure_login_label()

    # def initialize_validation_rules(self):
    #     self.validation_rules = {
    #         "Name": {
    #             "required": True,
    #             "field": None,  # Initialize the "field" attribute
    #             "validation_function": None
    #         },
    #         "Email": {
    #             "required": True,
    #             "field": None,
    #             "validation_function": self.is_validate_email
    #         },
    #         "Password": {
    #             "required": True,
    #             "field": None,
    #             "validation_function": self.is_validate_password
    #         },
    #         "Confirm Password": {
    #             "required": True,
    #             "field": None,
    #             "validation_function": None
    #         }
    #     }

    def create_background_image(self):
        self.bgImage = ImageTk.PhotoImage(file="Image/bg.jpg")
        bgLabel = tk.Label(self.signup, image=self.bgImage)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

    def registration_frame(self):
        self.frame = tk.Frame(self.signup, bg="white")
        self.frame.place(x=553, y=99)

    def create_heading_label(self):
        self.heading = tk.Label(self.frame, text="CREATE AN ACCOUNT")
        self.heading.grid(row=1, column=1, pady=40)

    # def create_entry(self, field_name, default_text, row, textvariable=None, show=None):
    #     entry_var = tk.StringVar()
    #     entry = tk.Entry(self.frame, show=show if show else None, textvariable=entry_var)
    #     entry.insert(0, default_text)
    #     entry.grid(row=row, column=1)
    #     entry.bind("<FocusIn>", lambda event: self.on_entry_click(event, default_text, entry))
    #     entry.bind("<FocusOut>", lambda event: self.on_entry_leave(event, default_text, entry))

    #     # Store the entry widget in the validation_rules dictionary
    #     self.validation_rules[field_name]["field"] = entry

    def create_name_entry(self):
        name_var = tk.StringVar()
        self.name_entry = self.create_entry("Name", "firebrick1", textvariable=name_var)
        self.name_entry.grid(row=2, column=1)
        self.name_entry.bind("<FocusIn>", lambda event: self.on_entry_click(event, "Name"))
        self.name_entry.bind("<FocusOut>", lambda event: self.on_entry_leave(event, "Name"))

    def name_error_label(self):
        self.name_error = tk.Label(self.frame, text="")
        self.name_error.grid(row=3, column=1, sticky="w")

    def create_email_entry(self):
        email_var = tk.StringVar()
        self.email_entry = self.create_entry("Email", "firebrick1", textvariable=email_var)
        self.email_entry.grid(row=4, column=1)
        self.email_entry.bind("<FocusIn>", lambda event: self.on_entry_click(event, "Email"))
        self.email_entry.bind("<FocusOut>", lambda event: self.on_entry_leave(event, "Email"))

    def email_error_label(self):
        self.email_error = tk.Label(self.frame, text="")
        self.email_error.grid(row=5, column=1, sticky="w")

    def create_password_entry(self):
        password_var = tk.StringVar()
        self.password_entry = self.create_entry("Password", "firebrick1", textvariable=password_var, show=None)
        self.password_entry.grid(row=6, column=1)
        self.password_entry.bind("<FocusIn>", lambda event: self.on_entry_click(event, "Password"))
        self.password_entry.bind("<FocusOut>", lambda event: self.on_entry_leave(event, "Password"))

    def password_error_label(self):
        self.password_error = tk.Label(self.frame, text="")
        self.password_error.grid(row=7, column=1, sticky="w")

    def create_password_confirmation_entry(self):
        password_confirmation_var = tk.StringVar()
        self.password_confirmation_entry = self.create_entry("Confirm Password", "firebrick1", textvariable=password_confirmation_var, show=None)
        self.password_confirmation_entry.grid(row=8, column=1)
        self.password_confirmation_entry.bind("<FocusIn>", lambda event: self.on_entry_click(event, "Confirm Password"))
        self.password_confirmation_entry.bind("<FocusOut>", lambda event: self.on_entry_leave(event, "Confirm Password"))

    def password_confirmation_error_label(self):
        self.password_confirmation_error = tk.Label(self.frame, text="")
        self.password_confirmation_error.grid(row=9, column=1, sticky="w")

    def create_signup_button(self):
        self.signup_button = tk.Button(self.frame, text="Sign Up")
        self.signup_button.grid(row=10, column=1, pady=20)

    def already_have_account_label(self):
        self.already_have_account = tk.Label(self.frame, text="Already have an account?")
        self.already_have_account.grid(row=11, column=1, padx=35, pady=20, sticky="w")

    def login_label(self):
        self.login = tk.Label(self.frame, text="Log in")
        self.login.place(x=195, y=373)

    def configure_frame(self):
        self.frame.grid_columnconfigure(0, weight=1, minsize=20)
        self.frame.grid_columnconfigure(2, weight=1, minsize=20)
    
    def configure_heading_label(self):
        self.heading.config(
            font=("Helvetica", 22, "bold"),
            bg="white",
            fg="firebrick1"
            )
        
    # def configure_entry(self, field_name):
    #     entry = self.validation_rules[field_name]["field"]
    #     entry.config(
    #         font=("Helvetica", 15),
    #         bg="white",
    #         fg="firebrick1",
    #         width=25,
    #         highlightthickness=1,
    #         highlightbackground="firebrick1",
    #         highlightcolor="firebrick1"
    #     )

    def configure_name_entry(self):
        self.name_entry.config(
            font=("Helvetica", 15), 
            bg="white", 
            fg="firebrick1",
            width=25,
            highlightthickness=1,  # Set to 0 to remove the default border
            highlightbackground="firebrick1",  # Set the border color
            highlightcolor="firebrick1"  # Set the border color
            )
        
    def configure_name_error(self):
        self.name_error.config(
            font=("Helvetica", 12, "italic"),
            bg="white",
            fg="red"
        )
        
    def configure_email_entry(self):
        self.email_entry.config(
            font=("Helvetica", 15), 
            bg="white", 
            fg="firebrick1",
            width=25,
            highlightthickness=1,  # Set to 0 to remove the default border
            highlightbackground="firebrick1",  # Set the border color
            highlightcolor="firebrick1"  # Set the border color
            )
        
    def configure_email_error(self):
        self.email_error.config(
            font=("Helvetica", 12, "italic"),
            bg="white",
            fg="red"
        )

    def configure_password_entry(self):
        self.password_entry.config(
            font=("Helvetica", 15), 
            bg="white", 
            fg="firebrick1",
            width=25,
            highlightthickness=1,  # Set to 0 to remove the default border
            highlightbackground="firebrick1",  # Set the border color
            highlightcolor="firebrick1"  # Set the border color
            )
    
    def configure_password_error(self):
        self.password_error.config(
            font=("Helvetica", 12, "italic"),
            bg="white",
            fg="red"
        )
    
    def configure_password_confirmation_entry(self):
        self.password_confirmation_entry.config(
            font=("Helvetica", 15), 
            bg="white", 
            fg="firebrick1",
            width=25,
            highlightthickness=1,  # Set to 0 to remove the default border
            highlightbackground="firebrick1",  # Set the border color
            highlightcolor="firebrick1"  # Set the border color
            )
        
    def configure_password_confirmation_error(self):
        self.password_confirmation_error.config(
            font=("Helvetica", 12, "italic"),
            bg="white",
            fg="red"
        )

    def configure_signup_button(self):
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

    def configure_already_have_account(self):
        self.already_have_account.config(
            font=("Helvetica", 11, "bold"),
            bd=0,
            bg="white",
            fg="firebrick1",
            highlightthickness=0,  # Set to 0 to remove the default border
            activebackground="white"
        )

    def configure_login_label(self):
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

    def create_entry(self, default_text, text_color, show=None, textvariable=None):
        entry = tk.Entry(self.frame, fg=text_color, show=show if show else None, textvariable=textvariable)
        entry.insert(0, default_text)
        return entry
    
    def validate_field(self, entry, error_label, field_name):
        current_text = entry.get()
        rules = self.validation_rules[field_name]

        if rules["required"] and current_text.strip() == "":
            entry.config(highlightbackground="firebrick1", fg="white")
            error_label.config(text="This field is required!")
            return False
        else:
            entry.config(highlightbackground=self.name_entry.cget("background"))
            error_label.config(text="")

        if rules["validation_function"]:
            return rules["validation_function"]()
        return True
    
    def is_validate_email(self, event):
        # Check if the email entry is focused and user left the field
        if event.widget == self.email_entry and not self.email_entry.focus_get():
            email = self.email_var.get()
            if not re.match(r"[a-zA-Z0-9]+\.[a-zA-Z0-9]+@university\.com(?i)", email):
                # Email format is incorrect
                self.email_entry.config(
                    highlightbackground="firebrick1",
                    highlightcolor="firebrick1",
                    bg="firebrick1",
                    fg="white"
                )
                self.email_error["text"] = "Email should be in the format\nfirstname.lastname@university.com"
            else:
                # Email format is correct
                self.email_entry.config(
                    highlightbackground=self.name_entry.cget("background"),
                    highlightcolor=self.name_entry.cget("background"),
                    bg=self.name_entry.cget("background"),
                    fg="firebrick1"
                )
                self.email_error["text"] = ""

    def is_validate_password(self, event):
        if event.widget == self.password_entry and not self.password_entry.focus_get():
            password = self.password_var.get()
            if not re.match(r"^[A-Z](?=.*\d.*\d.*\d)(?=.*[a-zA-Z].*[a-zA-Z].*[a-zA-Z].*[a-zA-Z]).*$", password):
                self.password_entry.config(
                    highlightbackground="firebrick1", 
                    highlightcolor="firebrick1", 
                    fg="white"
                    )
                self.password_error.config(text="Password must follow the rules:\n1. Start with an uppercase letter\n2. Contain at least 5 letters\n3. Have 3 or more digits.")
            else:
                self.password_entry.config(
                    highlightbackground=self.name_entry.cget("background"), 
                    highlightcolor=self.name_entry.cget("background"),
                    bg=self.name_entry.cget("background"),
                    fg="firebrick1"
                    )
                self.password_error.config(text="")
    
    def on_entry_click(self, event, default_text):
        entry = event.widget
        current_text = entry.get()
        if "password" in default_text.lower():
            show_text = "*"
        else:
            show_text = ""
        if current_text == default_text:
            entry.delete(0, "end")
            entry.config(show=show_text)

    def on_entry_leave(self, event, default_text):
        entry = event.widget
        current_text = entry.get()
        if "password" in default_text.lower():
            show_text = "*"
        else:
            show_text = ""
        if current_text == "":
            entry.insert(0, default_text)
            entry.config(show=show_text)

if __name__ == "__main__":
    signup = tk.Tk()
    signup_page = SignUpPage(signup)
    signup.mainloop()
