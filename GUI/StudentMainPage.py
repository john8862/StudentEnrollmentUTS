import tkinter as tk
import tkinter.messagebox as msgbox
import customtkinter as ctk
import time
# from customtkinter import CTkScrollableFrame as CTkSF
from CTkTable import CTkTable
from PIL import Image
from Widgets import *
from db import db

import logging
logging.basicConfig(level=logging.DEBUG)

class MainPage:
    def __init__(self, master, name, studentId, email):
        self.main = master
        self.name = name
        self.studentId = studentId
        self.email = email

        self.initializeWindow()
        self.createWidgets()
        print(f"{self.name}\n{self.studentId}\n{self.email}")

    def initializeWindow(self):
        x = int(self.main.winfo_screenwidth() / 3 - self.main.winfo_reqwidth() / 3)
        y = int(self.main.winfo_screenheight() / 3 - self.main.winfo_reqheight() / 3)

        self.main.title("University Enrollment System v0.9.0")
        self.main.geometry(f"856x645+{x}+{y}")
        self.main.resizable(0, 0)

        logoImg = Image.open("GUI/Image/system/logo.png")
        enrollImg = Image.open("GUI/Image/system/list_icon.png")
        removeImg = Image.open("GUI/Image/system/remove_icon.png")
        accountImg = Image.open("GUI/Image/system/person_icon.png")
        settingImg = Image.open("GUI/Image/system/settings_icon.png")
        logoutImg = Image.open("GUI/Image/system/logout_icon.png")

        self.logoImg = ctk.CTkImage(dark_image=logoImg, light_image=logoImg, size=(77.68, 85.42))
        self.enrollImg = ctk.CTkImage(dark_image=enrollImg, light_image=enrollImg, size=(25, 25))
        self.removeImg = ctk.CTkImage(dark_image=removeImg, light_image=removeImg, size=(25,25))
        self.accountImg = ctk.CTkImage(dark_image=accountImg, light_image=accountImg, size=(20, 20))
        self.settingImg = ctk.CTkImage(dark_image=settingImg, light_image=settingImg, size=(20, 20))
        self.logoutImg = ctk.CTkImage(dark_image=logoutImg, light_image=logoutImg, size=(20, 20))

        self.toplevelWindow = None

    def createWidgets(self):
        self.sidebarFrame = CustomFrame(self.main, 260, 650, "#2A8C55", False, expand=False, fill="y", anchor="w", side="left")
        self.sidebarFrame.get().configure(corner_radius=0)

        self.sidebarLogoImgLabel = CustomImage(self.sidebarFrame.get(), "GUI/Image/system/logo.png", "GUI/Image/system/logo.png", (77.68, 85.42), "", expand=False, anchor="center", pady=(38, 0))
        # self.enrollButton = CustomButton(self.sidebarFrame.get(), "", "Enrollment", "transparent", "#207244", "#fff", "buttonFont", "center", self.enrollAction, pady=(60, 0))
        
        self.accountLabel = CustomLabel(self.sidebarFrame.get(), "account", "  Student Information:", "#FFFFFF", "largeLabelFont", "w", "w", pady=(60, 0), padx=(25, 0), justify="left", image=self.accountImg, compound="left")
        self.accountStudentIdLabel = CustomLabel(self.sidebarFrame.get(), "accountStudentId", f"  {self.studentId}", "#FFFFFF", "labelFont", "w", "w", pady=(15, 0), padx=(25, 0), justify="left")
        self.accountNameLabel = CustomLabel(self.sidebarFrame.get(), "accountName", f"  {self.name}", "#FFFFFF", "labelFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left")
        self.accountEmailLabel = CustomLabel(self.sidebarFrame.get(), "accountEmail", f"  {self.email}", "#FFFFFF", "labelFont", "w", "w", pady=(0, 0), padx=(25, 0), justify="left")

        self.changePasswordButton = CustomButton(self.sidebarFrame.get(), 240, "CHANGE PASSWORD", "transparent", "#207244", "#fff", "largeButtonFont", "center", self.changePasswordAction, image=self.settingImg, pady=(220, 0))
        self.changePasswordButton.get().configure(anchor="w")
        self.changePasswordButton.get().pack_configure(ipady=5)
        self.logoutButton = CustomButton(self.sidebarFrame.get(), 240, "LOG OUT", "transparent", "#207244", "#fff", "largeButtonFont", "center", self.logoutAction, image=self.logoutImg, pady=(5, 0))
        self.logoutButton.get().configure(anchor="w")
        self.logoutButton.get().pack_configure(ipady=5)

        self.mainViewFrame = CustomFrame(self.main, 596, 650, "#FFF", False, side="left")
        self.mainViewFrame.get().configure(corner_radius=0)

        self.titleFrame = CustomFrame(self.mainViewFrame.get(), None, None, "transparent", True, anchor="n", fill="x", padx=27, pady=(36,0))
        self.titleLabel = CustomLabel(self.titleFrame.get(), "Heading", "Welcome!", "#2ABC55", "largeHeadingFont", "w", "nw", pady=(10, 0), padx=(10, 0), justify="left")
        self.subtitleLabel = CustomLabel(self.titleFrame.get(), "Subheading", "Please choose your action using below buttons", "#7E7E7E", "largeSubheadingFont", "w", "nw", padx=(10, 0), justify="left")

        self.actionFrame = CustomFrame(self.mainViewFrame.get(), None, None, "#F0F0F0", True, anchor="n", fill="x", padx=27, pady=(10, 0))
        self.enrollButton = CustomButton(self.actionFrame.get(), 251, "ENROLL", "#2A8C55", "#207244", "#FFF", "largeButtonFont", "w", self.enrollAction, image=self.enrollImg, padx=10, pady=10)
        self.enrollButton.get().configure(anchor="center")
        self.enrollButton.get().pack(side="left", ipady=5)
        self.removeButton = CustomButton(self.actionFrame.get(), 251, "DROP", "#FF5733", "#900C3F", "#FFF", "largeButtonFont", "e", self.dropAction, image=self.enrollImg, padx=10, pady=10)
        self.removeButton.get().configure(anchor="center")
        self.removeButton.get().pack(side="right", ipady=5)

        self.tableFrame = CustomFrame(self.mainViewFrame.get(), None, None, "transparent", True, anchor="n", fill="both", expand=True, padx=27, pady=21)
        self.table = CTkTable(master=self.tableFrame.get(), values=db.get_user_subjects(self.email), corner_radius=5, colors=["#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
        logging.info("table: %s", self.table.get())
        self.table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
        numRows = len(self.table.get())
        for row in range(1, numRows):  # Starting from 1 to skip the header row
            self.table.edit_row(row, text_color="#000000")
        self.table.pack(anchor="n", expand=True)

    def enrollAction(self):

        enrollDialog = ctk.CTkInputDialog(text="Enter the subject name you want to enroll:", title="Enroll")

        def getSubjectInput():
            subject = enrollDialog.get_input()
            enrollDialog.destroy()
            return subject         
        
        subject = getSubjectInput()

        if subject is None:
            return

        elif not subject.strip():
            msgbox.showerror(title="Error", message="Subject name cannot be empty!")
            self.main.after(10, self.enrollAction)
            return

        email = self.email
        success, message = db.add_subject(email, subject)
        if success:
            msgbox.showinfo(title="Success", message=message)
            self.refreshTable()
            enrollDialog.destroy()
        else:
            msgbox.showerror(title="Error", message=message)
            enrollDialog.destroy()
    
    def dropAction(self):
        dropDialog = ctk.CTkInputDialog(text="Enter the subject ID you want to drop:", title="Drop")
        
        subject = dropDialog.get_input()
        dropDialog.destroy()  # Close the dialog after getting input

        # Check if the user pressed "Cancel"
        if subject is None:
            return

        elif not subject.strip():
            msgbox.showerror(title="Error", message="Subject ID cannot be empty!")
            self.main.after(10, self.dropAction)
            return

        email = self.email
        success, message = db.remove_subject(email, subject)
        if success:
            msgbox.showinfo(title="Success", message=message)
            self.refreshTable()
        else:
            msgbox.showerror(title="Error", message=message)



    def refreshTable(self):

        newData = db.get_user_subjects(self.email)

        totalRowNeeded = len(newData)
        self.table.configure(rows=totalRowNeeded)
        self.table.update_values(newData)
        logging.info("newData: %s", newData)
        logging.info("table: %s", self.table.get())
        self.table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
        numRows = len(self.table.get())
        for row in range(1, numRows):  # Starting from 1 to skip the header row
            self.table.edit_row(row, text_color="#000000")
        self.table.pack(anchor="n", expand=True)


    def changePasswordAction(self):
        from ForgotPasswordNew import ChangePasswordPage as cPP
        
        if self.toplevelWindow is not None:
            self.toplevelWindow.destroy()

        self.toplevelWindow = tk.Toplevel(self.main)    
        changePasswordPage = cPP(self.toplevelWindow)
        changePasswordPage.emailEntry.entryField["email"].insert(0, self.email)
        changePasswordPage.emailEntry.entryField["email"].configure(state="readonly")
        
    def logoutAction(self):
        result = msgbox.askquestion("Logout", "Are you sure you want to logout?")
        logging.info("result: %s", result)
        if result == "yes": 
            self.main.destroy()
            from SignInNew import SignInPage
            loginPage = SignInPage(tk.Tk())

    
if __name__ == '__main__':
    main = tk.Tk()
    dummyName = "Sherlock Zhao"
    dummyStudentId = "000001"
    dummyEmail = "sherlock.zhao@university.com"
    mainPage = MainPage(main
        ,
        dummyName,
        dummyStudentId,
        dummyEmail
    )
    main.mainloop()