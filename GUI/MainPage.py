import tkinter as tk

class MainPage:
    def __init__(self, master: tk.Tk):
        self.root = master
        self.root.title("Univeristy Enrollment System v0.0.1")
        self.root.geometry(f"800x600")
        self.create_page()

    def create_page(self):
        menubar = tk.Menu(self.root)
        menubar.add_command(label="Enrollment")
        menubar.add_command(label="Mark")
        self.root.config(menu=menubar)

if __name__ == '__main__':
    root = tk.Tk()
    MainPage(root)
    root.mainloop()