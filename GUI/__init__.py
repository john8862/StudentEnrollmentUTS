import platform

def set_button_cursor(button):
    system = platform.system()
    
    if system == "Windows":
        button.config(cursor="hand2")
    elif system == "Darwin":
        button.config(cursor="pointinghand")