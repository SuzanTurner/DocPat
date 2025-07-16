import customtkinter as ctk
from tkinter import messagebox
import requests
from gui.utils import BackMixin


class Docs(ctk.CTkFrame, BackMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.lift()
        self.pack(expand = True, fill = "both")

        self.rowconfigure((0, 3), weight=2, uniform='a')  # Top & bottom padding
        self.rowconfigure((1, 2), weight=1, uniform='a')  # Button rows
        self.columnconfigure((0, 1, 2), weight=1, uniform='a') 

        self.login()
        self.register()
        # self.back_btn()
        self.create_back_button(self, self.go_back)

    def login(self):
        login = ctk.CTkButton(self, text = "Login", command = self.login_logic)
        # login.pack(expand = True, fill = "both")
        login.grid(row=1, column=1, sticky="nsew", padx=20, pady=10)

    def register(self):
        reg = ctk.CTkButton(self, text = "Register", command = self.register_logic)
        # reg.pack(expand = True, fill = "both")
        reg.grid(row=2, column=1, sticky="nsew", padx=20, pady=10)

    def login_logic(self):
        print("Login selected")
        self.destroy()
        login_page(self.parent)

    def register_logic(self):
        print("Register selected")
        self.destroy()
        register_page(self.parent)

    # def back_btn(self):
    #     back_btn = ctk.CTkButton(self, text="← Back", command= self.go_back)
    #     back_btn.grid(row=0, column=0, pady=(20, 10), sticky = "nw") 

    def go_back(self):
        from gui.main import Select
        self.destroy()
        Select(self.master)


class login_page(ctk.CTkFrame, BackMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.pack(expand = True, fill = "both")

        self.rowconfigure(0, weight=2)  # Top space
        self.rowconfigure(1, weight=0)  # Label (tight)
        self.rowconfigure(2, weight=0)  # Entry (tight)
        self.rowconfigure(3, weight=0)  # Label
        self.rowconfigure(4, weight=0)  # Entry
        self.rowconfigure(5, weight=0) 
        self.rowconfigure(6, weight=2) 
        self.columnconfigure((0), weight = 1)

        self.name_label()
        self.name_entry()
        self.pass_label()
        self.pass_entry()
        self.send()
        # self.back_bt()
        self.create_back_button(self, self.go_back)

    def name_label(self):
        font = ctk.CTkFont(family= "Calibri", size= 24, weight = "bold")
        name = ctk.CTkLabel(self, text = "Name:", font = font)
        name.grid(row = 1, column = 0, pady=(0, 5))

    def name_entry(self):
        self.entry = ctk.CTkEntry(self, width= 200,corner_radius= 5, border_color= "black", border_width= 1, fg_color= "white", text_color= "black")
        self.entry.grid(row = 2, column = 0, pady=(0, 5))

    def pass_label(self):
        font = ctk.CTkFont(family= "Calibri", size= 24, weight = "bold")
        pwd = ctk.CTkLabel(self, text = "Password:", font = font)
        pwd.grid(row = 3, column = 0, pady=(0, 5))

    def pass_entry(self):
        self.pwd_entry = ctk.CTkEntry(self, width= 200,corner_radius= 5, border_color= "black", border_width= 1, fg_color= "white", text_color= "black")
        self.pwd_entry.grid(row = 4, column = 0, pady=(0, 5))

    def send(self):
        send = ctk.CTkButton(self, text = "Login", command = self.send_credentials)
        send.grid(row = 5, column = 0, pady=(10, 5))

    # def back_bt(self):
    #     back_btn = ctk.CTkButton(self, text="← Back", command= self.go_back)
    #     back_btn.grid(row=0, column=0, pady=(20, 10), sticky = "nw") 

    def go_back(self):
        self.destroy()
        print("Back")
        from gui.main import Docs
        Docs(self.master)

    def send_credentials(self):
        username = self.entry.get()
        password = self.pwd_entry.get()

        try:
            response = requests.post(
                "http://127.0.0.1:5000/login",
                json={"username": username, "password": password}
            )

            if response.status_code == 200:
                doctor_id = response.json().get("id")
                print(f"Doctor_id is {doctor_id}")
                messagebox.showinfo("Success", response.json().get("message"))
                from gui.appointments import Appointments
                self.destroy()
                Appointments(self.parent, doctor_id)
            else:
                messagebox.showerror("Error", response.json().get("message"))
        except Exception as e:
            messagebox.showerror("Error", f"Could not connect to server:\n{e}")



class register_page(ctk.CTkFrame, BackMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack(expand = True, fill = "both")

        self.rowconfigure(0, weight=2)  # Top space
        self.rowconfigure(1, weight=0)  # Label (tight)
        self.rowconfigure(2, weight=0)  # Entry (tight)
        self.rowconfigure(3, weight=0)  # Label
        self.rowconfigure(4, weight=0)  # Entry
        self.rowconfigure(5, weight=0) 
        self.rowconfigure(6, weight=2) 
        self.columnconfigure((0), weight = 1)

        self.name_label()
        self.name_entry()
        self.pass_label()
        self.pass_entry()
        self.send()
        # self.back_btn()
        self.create_back_button(self, self.go_back)

    def name_label(self):
        font = ctk.CTkFont(family= "Calibri", size= 24, weight = "bold")
        name = ctk.CTkLabel(self, text = "Name:", font = font)
        name.grid(row = 1, column = 0, pady=(0, 5))

    def name_entry(self):
        self.entry = ctk.CTkEntry(self, width= 200,corner_radius= 5, border_color= "black", border_width= 1, fg_color= "white", text_color= "black")
        self.entry.grid(row = 2, column = 0, pady=(0, 5))

    def pass_label(self):
        font = ctk.CTkFont(family= "Calibri", size= 24, weight = "bold")
        pwd = ctk.CTkLabel(self, text = "Password:", font = font)
        pwd.grid(row = 3, column = 0, pady=(0, 5))

    def pass_entry(self):
        self.pwd_entry = ctk.CTkEntry(self, width= 200,corner_radius= 5, border_color= "black", border_width= 1, fg_color= "white", text_color= "black")
        self.pwd_entry.grid(row = 4, column = 0, pady=(0, 5))

    def send(self):
        send = ctk.CTkButton(self, text = "Register", command = self.send_creds)
        send.grid(row = 5, column = 0, pady=(10, 5))

    # def back_btn(self):
    #     back_btn = ctk.CTkButton(self, text="← Back", command= self.go_back)
    #     back_btn.grid(row=0, column=0, pady=(20, 10), sticky = "nw") 

    def go_back(self):
        self.destroy()
        print("Back")
        from gui.main import Docs
        Docs(self.master)

    def send_creds(self):
        username = self.entry.get()
        password = self.pwd_entry.get()

        try:
            response = requests.post(
                "http://127.0.0.1:5000/register",
                json={"username": username, "password": password}
            )

            if response.status_code == 200:
                doctor_id = response.json().get("id")
                print(f"Doctor_id is {doctor_id}")
                messagebox.showinfo("Success", response.json().get("message"))
                from gui.appointments import Appointments
                self.destroy()
                Appointments(self.parent, doctor_id)
            else:
                messagebox.showerror("Error", response.json().get("message"))
        except Exception as e:
            messagebox.showerror("Error", f"Could not connect to server:\n{e}")