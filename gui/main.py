import customtkinter as ctk
from gui.doctors import Docs
from gui.pats import Pats
from tkinter import ttk
from gui.utils import Size
import requests

class Select(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack(expand = True, fill = "both")

        self.rowconfigure((0, 3), weight=2, uniform='a')  # Top & bottom padding
        self.rowconfigure((1, 2), weight=1, uniform='a')  # Button rows
        self.columnconfigure((0, 1, 2), weight=1, uniform='a')  # Center horizontally

        self.doctor()
        self.patient()

    def doctor(self):
        doc = ctk.CTkButton(self, text="Doctor", command=self.on_doctor_click)
        doc.grid(row=1, column=1, sticky="nsew", padx=20, pady=10)

    def patient(self):
        pat = ctk.CTkButton(self, text="Patient", command=self.on_patient_click)
        pat.grid(row=2, column=1, sticky="nsew", padx=20, pady=10)

    def on_doctor_click(self):
        print("Doctor selected")
        self.destroy()
        Docs(self.parent)
        # call master.show_frame(AuthPage) or set role, etc.

    def on_patient_click(self):
        print("Patient selected")
        self.destroy()
        Pats(self.parent)


class Window(ctk.CTk):
    def __init__(self, title):
        super().__init__()

        self.title(title)
        self.geometry("600x600")

        Select(self)
        Size(self)

        self.bind("<KeyPress-q>", lambda event : self.quit())
        
        self.mainloop()


if __name__ == "__main__":
    Window("Docs and Pats")