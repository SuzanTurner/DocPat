import customtkinter as ctk
from backend.db import get_all_doctors, create_appointment
from gui.utils import BackMixin
from functools import partial

class Pats(ctk.CTkFrame, BackMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack()

        self.rowconfigure((0), weight = 0, uniform = 'a')
        self.rowconfigure((1), weight = 1, uniform='a')
        self.columnconfigure((0,1,2), weight = 1,  uniform= 'a') 

        label = ctk.CTkLabel(self, text = "Yo here are the doctor list")
        label.grid(row = 0, column = 1)

        self.scroll = ctk.CTkScrollableFrame(self)
        self.scroll.grid(row = 1, column = 1)

        self.load_doctors()
        self.create_back_button(self, self.go_back)

    def load_doctors(self):  

        doctors = get_all_doctors()  

        for doc_id, doc_name in doctors.items():
            row_frame = ctk.CTkFrame(self.scroll)
            row_frame.pack(fill="x", pady=5, padx=5)

            name_label = ctk.CTkLabel(row_frame, text=f"{doc_id} {doc_name}")
            name_label.pack(side="left", padx=10)

            book_btn = ctk.CTkButton(row_frame, text="Book", command=partial(self.book_appointment, doc_id))
            book_btn.pack(side="right", padx=10)

    def book_appointment(self, doc_id):
        print(f"Booking for doctor ID: {doc_id}")
        create_appointment(doc_id)

    def go_back(self):
        self.destroy()
        print("Back")
        from gui.main import Select
        Select(self.master)
