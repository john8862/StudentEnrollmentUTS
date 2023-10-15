import tkinter as tk
from PIL import ImageTk, Image
from db import db

class ForgotPasswordPage:

    def __init__(self, master):
        self.forgot_password = master
        self.initialize_window()
        self.create_widgets()

    def initialize_window(self):

        x = int(self.forgot_password.winfo_screenwidth() / 3 - self.forgot_password.winfo_reqwidth() / 3)
        y = int(self.forgot_password.winfo_screenheight() / 3 - self.forgot_password.winfo_reqheight() / 3)

        self.forgot_password.title("Change Password")
        self.forgot_password.geometry(f"790x512+{x}+{y}")
        self.forgot_password.resizable(0, 0)

    def create_widgets(self):
        self.entry_fields = {}
        self.error_labels = {}
        self.create_background_image()
        self.submission_frame()
        self.create_heading_label()
        self.create_entry("Email", "magenta2", 1)
        self.create_error_label("Email", 2)
        self.create_entry("New Password", "magenta2", 3)
        self.create_error_label("New Password", 4)
        self.create_entry("Confirm Password", "magenta2", 5)
        self.create_error_label("Confirm Password", 6)
        self.create_button("Submit", 7, self.SubmitAction)

    def create_background_image(self):
        self.bgImage = ImageTk.PhotoImage(file="GUI/Image/background.jpg")
        bgLabel = tk.Label(self.forgot_password, image=self.bgImage)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

    def submission_frame(self):
        self.frame = tk.Frame(self.forgot_password, bg="white")
        self.frame.place(x=451, y=38)
        self.frame.grid_columnconfigure(0, weight=1, minsize=30)
        self.frame.grid_columnconfigure(2, weight=1, minsize=30)

    def create_heading_label(self):
        self.heading = tk.Label(self.frame, text="Reset Your Password")
        self.heading.grid(row=0, column=1, pady=(60,40), sticky="nsew")
        self.heading.config(
            font=("Helvetica", 22, "bold"),
            bg="white",
            fg="magenta2"
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
            fg="magenta2",
            width=25,
            highlightthickness=1,
            highlightbackground="magenta2",
            highlightcolor="magenta2"
        )
        self.entry_fields[field_name] = entry
        return entry

    def create_error_label(self, field_name, row):
        error = tk.Label(self.frame, text="")
        error.grid(row=row, column=1, padx=10, pady=10, sticky="w")
        error.config(
            font=("Helvetica", 12, "italic"),
            bg="white",
            fg="red"
        )
        self.error_labels[field_name] = error
        return error
    
    def create_button(self, text, row, command):
        button = tk.Button(self.frame, text=text, command=command)
        button.grid(row=row, column=1, pady=(15, 73))
        button.config(
            font=("Helvetica", 16, "bold"),
            bg="magenta2",
            fg="white",
            width=23,
            bd=0,
            highlightthickness=0
        )
        return button
    
    def on_entry_click():
        pass

    def on_entry_leave():
        pass
    
    def SubmitAction(self):
        pass


if __name__ == '__main__':
    FPP = tk.Tk()
    change_password_page = ForgotPasswordPage(FPP)
    FPP.mainloop()