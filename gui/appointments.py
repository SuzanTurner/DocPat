import customtkinter as ctk
from gui.utils import BackMixin
from backend.db import get_appointments


class Appointments(ctk.CTkFrame, BackMixin):
    def __init__(self, parent, doctor_id):
        super().__init__(parent)
        self.parent = parent
        self.doctor_id = doctor_id
        self.pack(expand=True, fill="both")

        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure(0, weight=1)

        # Title
        title = ctk.CTkLabel(self, text="🩺 Your Appointments", font=ctk.CTkFont(size=20, weight="bold"))
        title.grid(row=0, column=0, pady=(20, 10), sticky="n")

        # Scrollable appointment list in the center
        self.scroll_frame = ctk.CTkScrollableFrame(self, width=400)
        self.scroll_frame.grid(row=1, column=0, padx=30, pady=(0, 20), sticky="nsew")

        self.view_appointments()
        self.create_back_button(self, self.go_back)

    def view_appointments(self):
        appointments = get_appointments(self.doctor_id)

        if not appointments:
            empty_label = ctk.CTkLabel(self.scroll_frame, text="No appointments yet.")
            empty_label.pack(pady=10)
            return

        for i, appt in enumerate(appointments, start=1):
            appt_label = ctk.CTkLabel(self.scroll_frame, text=f"📅 Booking made at {appt}")
            appt_label.pack(anchor="w", pady=4, padx=20)

    def go_back(self):
        self.destroy()
        print("Back")
        from gui.doctors import Docs
        Docs(self.master)
