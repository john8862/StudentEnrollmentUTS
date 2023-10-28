import platform

def set_button_cursor(button):
    if platform.system() == "Windows":
        button.config(cursor="hand2")
    elif platform.system() == "Darwin":
        button.config(cursor="pointinghand")