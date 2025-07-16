import customtkinter as ctk
from tkinter import ttk

class BackMixin:
    def create_back_button(self, parent, command, row=0, column=0):
        back_btn = ctk.CTkButton(
            parent,
            text="← Back",
            command=command
        )
        back_btn.grid(row=row, column=column, pady=(20, 10), sticky="nw")

class Size(ttk.Sizegrip):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side = "bottom", anchor= "se")