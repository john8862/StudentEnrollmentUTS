import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

class SignInPage:

    def __init__(self, master):
        self.login = master
        self.initialize_window()
        self.create_widgets()
        self.configure_widgets()

    def initialize_window(self):
        x = int(self.login.winfo_screenwidth() / 3 - self.login.winfo_reqwidth() / 3)
        y = int(self.login.winfo_screenheight() / 3 - self.login.winfo_reqheight() / 3)

        self.login.title("University Enrollment System v0.0.2")
        self.login.geometry(f"990x660+{x}+{y}")
        self.login.resizable(0, 0)

    def create_widgets(self):
        self.create_background_image()
        self.create_heading_label()
        self.create_username_entry()
        self.create_password_entry()
        self.closeeye_label()
        self.forgot_password_label()
        self.login_button()
        self.signup_label()
        self.create_account_label()

    def configure_widgets(self):
        self.configure_heading_label()
        self.configure_username_entry()
        self.configure_password_entry()
        self.configure_closeeye_label()
        self.configure_forgot_password()
        self.configure_login_button()
        self.configure_signup_label()
        self.configure_create_account_label()

    def create_background_image(self):
        self.bgImage = ImageTk.PhotoImage(file="Image/bg.jpg")
        bgLabel = tk.Label(self.login, image=self.bgImage)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

    def create_heading_label(self):
        self.heading = tk.Label(self.login, text="STUDENT LOGIN") 
        self.heading.place(x=590, y=140)

    def create_username_entry(self):
        self.username_entry = self.create_entry("Username", "firebrick1")
        self.username_entry.place(x=580, y=220)
        self.username_entry.bind("<FocusIn>", self.on_username_entry_click)
        self.username_entry.bind("<FocusOut>", self.on_username_entry_leave)
        tk.Frame(self.login, width=230, height=2, bg="firebrick1").place(x=580, y=240)  # Add frame widget

    def create_password_entry(self):
        self.password_entry = self.create_entry("Password", "firebrick1", show=None)
        self.password_entry.place(x=580, y=290)
        self.password_entry.bind("<FocusIn>", self.on_password_entry_click)  # Change the event handler
        self.password_entry.bind("<FocusOut>", self.on_password_entry_leave)  # Change the event handler
        tk.Frame(self.login, width=230, height=2, bg="firebrick1").place(x=580, y=310)  # Add frame widget

    def closeeye_label(self):
        self.closeeye = ImageTk.PhotoImage(file="Image/closeye.png")
        self.openeye = ImageTk.PhotoImage(file="Image/openeye.png")
        self.show_password = False

        self.closeeye_label = tk.Label(self.login, image=self.closeeye)
        self.closeeye_label.place(x=785, y=286)
        self.closeeye_label.bind("<Button-1>", lambda event: self.toggle_password_visibility())

    def forgot_password_label(self):
        self.forgot_password_label = tk.Label(self.login, text="Forgot Password?")
        self.forgot_password_label.place(x=715, y=321)
        self.forgot_password_label.bind("<Button-1>", lambda event: self.forgort_password())

    def login_button(self):
        self.login_button = tk.Button(self.login, text="Login")
        self.login_button.place(x=580, y=380)

    def signup_label(self):
        self.signup_label = tk.Label(self.login, text="Don't have a student account?")
        self.signup_label.place(x=585, y=450)

    def create_account_label(self):
        self.create_account_label = tk.Label(self.login, text="Create new one")
        self.create_account_label.place(x=735, y=450)
    
    def create_entry(self, default_text, text_color, show=None):
        entry = tk.Entry(self.login, fg=text_color, show=show if show else None)
        entry.insert(0, default_text)
        return entry

    def configure_heading_label(self):
        self.heading.config(font=("Helvetica", 25, "bold"), bg="white", fg="firebrick1")

    def configure_username_entry(self):
        self.username_entry.config(width=25, font=("Helvetica", 15), bg="white", bd=0, highlightthickness=0)

    def configure_password_entry(self):
        self.password_entry.config(width=25, font=("Helvetica", 15), bg="white", bd=0, highlightthickness=0)

    def configure_closeeye_label(self):
        self.closeeye_label.config(bd=0, bg="white", highlightbackground="white", activebackground="white", cursor="pointinghand")

    def configure_forgot_password(self):
        self.forgot_password_label.config(font=("Helvetica", 12), fg="firebrick1", bg="white", bd=0, highlightthickness=0, activebackground="white", cursor="pointinghand")

    def configure_login_button(self):
        self.login_button.config(width=23, font=("Helvetica", 15, "bold"), bg="firebrick1", fg="white", bd=0, highlightthickness=0, cursor="pointinghand", activebackground="firebrick1", activeforeground="white")

    def configure_signup_label(self):
        self.signup_label.config(font=("Helvetica", 11), fg="firebrick1", bg="white", bd=0, highlightthickness=0, activebackground="white")
    
    def configure_create_account_label(self):
        self.create_account_label.config(font=("Helvetica", 11, "bold underline "), fg="blue", bg="white", bd=0, highlightthickness=0, activebackground="white", cursor="pointinghand")

    def on_username_entry_click(self, event):
        entry = event.widget
        default_text = entry.get()
        if default_text == "Username":
            entry.delete(0, "end")

    def on_username_entry_leave(self, event):
        entry = event.widget
        default_text = entry.get()
        if default_text == "":
            entry.insert(0, "Username")

    def on_password_entry_click(self, event):
        entry = event.widget
        default_text = entry.get()
        if default_text == "Password":
            entry.delete(0, "end")
            entry.config(show='*')  # Show "*" when the user starts entering a password

    def on_password_entry_leave(self, event):
        entry = event.widget
        default_text = entry.get()
        if default_text == "":
            entry.insert(0, "Password")
            entry.config(show='')  # Hide "*" when not focused

    def forgort_password(self):
        pass

    def toggle_password_visibility(self):
        if self.show_password:
            self.password_entry.config(show='*')
            self.closeeye_label.config(image=self.closeeye, activebackground="white")
        else:
            self.password_entry.config(show='')
            self.closeeye_label.config(image=self.openeye, activebackground="white")
        self.show_password = not self.show_password

if __name__ == "__main__":
    login = tk.Tk()
    login_page = SignInPage(login)
    login.mainloop()
