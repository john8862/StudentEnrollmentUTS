import tkinter as tk
import customtkinter as ctk
from PIL import Image
from Widgets import *
from db import db

class MainPage:

    def __init___(self, master):
        self.main = master
        self.initialize_window()
        self.create_widgets()

if __name__ == '__main__':
    main = tk.Tk()
    mainPage = MainPage(main)
    mainPage.mainloop()