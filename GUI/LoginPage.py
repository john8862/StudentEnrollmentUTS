import tkinter as tk
import tkinter.messagebox as msgbox
from db import db

class LoginMasterPage:

    def __init__(self,master):
               
        self.root = master

        x = int(self.root.winfo_screenwidth()/3 - self.root.winfo_reqwidth()/3)
        y = int(self.root.winfo_screenheight()/3 - self.root.winfo_reqheight()/3)

        self.root.title("University Enrollment System v0.0.1")
        self.root.geometry(f"640x400+{x}+{y}")

        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.role = tk.StringVar()

        self.login_page = tk.Frame(self.root)
        self.login_page.pack()

        tk.Label(self.login_page, text="Welcome to University Enrollment System", font=("Georgia", 25)).grid(row=1, column=1, columnspan=3, pady=25)

        # Role Selection
        tk.Label(self.login_page, text="Role:").grid(row=2, column=1, sticky="e", pady=25)
        role_options = ["","Student", "Admin"]
        self.role.set(role_options[0])  # Set the default value
        tk.OptionMenu(self.login_page, self.role, *role_options).grid(row=2, column=2, columnspan=3, sticky="w", pady=25)

        tk.Label(self.login_page, text="Username:").grid(row=3, column=1, sticky="e")
        tk.Entry(self.login_page, textvariable=self.username).grid(row=3, column=2, columnspan=2, sticky="w")
        self.username_hint = tk.Label(self.login_page, text="", fg="gray", font=("Helvetica", 12, "italic"))
        self.username_hint.grid(row=4, column=2, columnspan=2, sticky="w")
        self.role.trace("w", self.update_username_hint)

        tk.Label(self.login_page, text="Password:").grid(row=5, column=1, sticky="e", pady=(0,25))
        tk.Entry(self.login_page, textvariable=self.password, show="*").grid(row=5, column=2, columnspan=3, sticky="w", pady=(0,25))

        tk.Button(self.login_page, text="Login", command=self.login).grid(row=6, column=2, sticky="w")
        tk.Button(self.login_page, text="Register", command=self.registration).grid(row=6, column=2, sticky="e")
    
    def update_username_hint(self, *args):
        if self.role.get() == "Student":
            self.username_hint.config(text="Please enter your email address!")
        elif self.role.get() == "":
            self.username_hint.config(text="")
        else:
            self.username_hint.config(text="Please enter your admin username!")

    def login(self):
        user = self.username.get()
        pwd = self.password.get()
        role = self.role.get()
        if self.role.get() == "Student":
            flag, message = db.verify_student_login(user, pwd)
            if flag:
                msgbox.showinfo(title="Success", message=message)
                self.login_page.destroy()
                from StudentMainPage import MainPage
                MainPage(self.root)
            else:
                msgbox.showerror(title="Error", message=message)
        elif self.role.get() == "Admin":
            flag, message = db.verify_admin_login(user, pwd)
            if flag:
                msgbox.showinfo(title="Success", message=message)
                self.login_page.destroy()
                from AdminMainPage import MainPage
                MainPage(self.root)
            else:
                msgbox.showerror(title="Error", message=message)
        else:
            msgbox.showerror(title="Error", message="Please select a role!")

    def registration(self):
        self.login_page.destroy()
        from RegistrationPage import RegistrationPage
        RegistrationPage(self.root)
        

if __name__ == '__main__':
    root = tk.Tk()
    Login_page = LoginMasterPage(root)
    root.mainloop()