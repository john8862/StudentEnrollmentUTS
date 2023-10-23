import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk, Image
import platform

class CustomFont:
    entryFont = ("Arial Bold", 14, "normal")
    labelFont = ("Arial Bold", 14, "normal")
    headingFont = ("Arial Bold", 24, "normal")
    subHeadingFont = ("Arial Bold", 12, "normal")
    buttonFont = ("Arial Bold", 12, "normal")
    descriptionFont = ("Arial Bold", 9, "normal")
    linkFont = ("Arial Bold", 9, "normal", "underline")
    errorFont = ("Arial Bold", 11, "italic")

    def __init__(self, font_type):
        self.font = getattr(CustomFont, font_type, None)

    @classmethod
    def get(cls, font_type):
        return getattr(cls, font_type, None)

class CustomEntry:
    def __init__(self, master, fieldName, width, fg_color, text_color, border_color, font_type, bd, anchor, pady=(0, 0), padx=(0, 0), show=None, **kwargs):
        self.master = master
        self.fieldName = fieldName
        self.width = width
        self.fgColor = fg_color
        self.textColor = text_color
        self.borderColor = border_color
        self.fontType = font_type
        self.borderWidth = bd
        self.anchor = anchor
        self.pady = pady
        self.padx = padx
        self.show = show
        self.kwargs = kwargs
        self.entryField = {}    # Create a dictionary to store the entry field
        self.create()

    def create(self):
        self.entryVar = ctk.StringVar()
        self.entry = ctk.CTkEntry(self.master, width=self.width, show=self.show, textvariable=self.entryVar)
        self.entry.pack(anchor=self.anchor, pady=self.pady, padx=self.padx)
        self.entry.configure(
            font = CustomFont.get(self.fontType),
            fg_color = self.fgColor,
            text_color = self.textColor,
            border_color = self.borderColor,
            border_width = self.borderWidth,
        )
        self.entryField[self.fieldName] = self.entry

    def get(self):
        return self.entry

class CustomLabel:
    def __init__(self, master, labelName, text, text_color, font_type, anchorc, anchorp, pady=(0, 0), padx=(0, 0), **kwargs):
        self.master = master
        self.labelName = labelName
        self.text = text
        self.textColor = text_color
        self.fontType = font_type
        self.anchorc = anchorc
        self.anchorp = anchorp
        self.pady = pady
        self.padx = padx
        self.kwargs = kwargs
        self.LabelField = {}
        self.create()

    def create(self):
        self.label = ctk.CTkLabel(self.master, text=self.text, **self.kwargs)
        self.label.pack(anchor=self.anchorp, pady=self.pady, padx=self.padx)    
        self.label.configure(
            font = CustomFont.get(self.fontType),
            text_color = self.textColor,
            anchor = self.anchorc
        )
        self.LabelField[self.labelName] = self.label

    def get(self):
        return self.label
        
class CustomButton:
    def __init__(self, master, width, text, fg_color, hover_color, text_color, font_type, anchor, pady=(0, 0), padx=(0, 0), **kwargs):
        self.master = master
        self.width = width
        self.text = text
        self.fgColor = fg_color
        self.hoverColor = hover_color
        self.fontType = font_type
        self.textColor = text_color
        self.anchor = anchor
        self.pady = pady
        self.padx = padx
        self.kwargs = kwargs
        self.create()

    def create(self):
        self.button = ctk.CTkButton(self.master, text=self.text)
        self.button.pack(anchor=self.anchor, pady=self.pady, padx=self.padx)
        self.button.configure(
            font = CustomFont.get(self.fontType),
            width = self.width,
            fg_color = self.fgColor,
            hover_color = self.hoverColor,
            text_color = self.textColor
        )
        SetCursor(self.button)

    def get(self):
        return self.button
    
class CustomFrame:
    def __init__(self, master, width, height, fg_color, propagate=None, **kwargs):
        self.master = master
        self.width = width
        self.height = height
        self.fgColor = fg_color
        self.kwargs = kwargs

        if propagate is not None:
            self.propagate = propagate
        else:
            self.propagate = False
        self.create()

    def create(self):
        self.frame = ctk.CTkFrame(self.master)
        self.frame.configure(
            width=self.width,
            height=self.height,
            fg_color=self.fgColor
        )
        self.frame.pack(**self.kwargs)
        
        if not self.propagate:
            self.frame.pack_propagate(0)

    def get(self):
        return self.frame
    
class CustomImage:
    def __init__(self, master, dark_image_path, light_image_path, size, text, **kwargs):
        self.master = master
        self.dark_image_path = dark_image_path
        self.light_image_path = light_image_path
        self.size = size
        self.text = text
        self.kwargs = kwargs
        self.create()

    def create(self):
        dark_image = Image.open(self.dark_image_path)
        light_image = Image.open(self.light_image_path)

        self.image = ctk.CTkImage(dark_image=dark_image, light_image=light_image, size=self.size)
        self.imageLabel = ctk.CTkLabel(self.master, image=self.image, text=self.text)
        self.imageLabel.pack(**self.kwargs)

    def get(self):
        return self.imageLabel

class SetCursor:
    def __init__(self, widget):
        self.widget = widget
        self.set()

    def set(self):
        if platform.system() == "Windows":
            self.widget.configure(cursor="hand2")
        elif platform.system() == "Darwin":
            self.widget.configure(cursor="pointinghand")