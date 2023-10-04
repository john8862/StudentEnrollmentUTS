import tkinter as tk
import tkinter.messagebox as msgbox
from db import db
from MainPage import MainPage
from RegistrationPage import RegistrationPage

class LoginPage:

    def __init__(self,master):
               
        self.root = master

        x = int(root.winfo_screenwidth()/3 - root.winfo_reqwidth()/2)
        y = int(root.winfo_screenheight()/3 - root.winfo_reqheight()/2)

        self.root.title("GUIUniApp")
        self.root.geometry(f"640x400+{x}+{y}")

        self.email = tk.StringVar()
        self.password = tk.StringVar()

        self.login_page = tk.Frame(root)
        self.login_page.pack()

        tk.Label(self.login_page).grid(row=0, column=0)

        tk.Label(self.login_page, text="Welcome to University Enrollment System", font=("Georgia", 25)).grid(row=1, column=1, columnspan=3, pady=10)

        tk.Label(self.login_page, text="Email:").grid(row=5, column=1)
        tk.Entry(self.login_page, textvariable=self.email).grid(row=5, column=2)
        tk.Label(self.login_page, text="Password:").grid(row=6, column=1)
        tk.Entry(self.login_page, textvariable=self.password).grid(row=6, column=2)

        tk.Button(self.login_page, text="Login", command=self.login).grid(row=7, column=1,pady=10)
        tk.Button(self.login_page, text="Register").grid(row=7, column=2,pady=10)
        tk.Button(self.login_page, text="Exit", command=self.login_page.quit).grid(row=7, column=3,pady=10)

    def login(self):
        user = self.email.get()
        pwd = self.password.get()
        flag, message = db.verify_login(user, pwd)
        if flag:
            msgbox.showinfo(title="Success", message=message)
            self.login_page.destroy()
            MainPage(self.root)
        else:
            msgbox.showerror(title="Error", message=message)
    
    def Registration(self):
        self.login_page.destroy()
        RegistrationPage(self.root)

if __name__ == '__main__':
    root = tk.Tk()
    LoginPage(master=root)
    root.mainloop()