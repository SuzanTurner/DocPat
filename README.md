# DocPat (Protected by PyArmor)
A simple tkinter interface to login/register as a doctor and veiw patient appointments. Built with flask and tkinter

# 📌 Core Features:
👨‍⚕️ Doctor Side:
Register/Login (credentials stored in SQLite doctors table)

After login: View all their booked appointments (with timestamps)

# 🧑‍💼 Patient Side:
Anonymous usage (no login needed)

See list of all registered doctors

Click "Book" to create a new appointment with the selected doc

Appointment gets timestamped and saved in the appointments table

# ✅ Tech Stack:
Frontend: customtkinter for sleek GUI

Backend: Flask (for login control), SQLite for persistence

# Steps to run:
1. Clone the repo
```
git clone https://github.com/SuzanTurner/DocPat.git
```
2. Naviagete to the folder:
```
cd docpat
```

3. Install the requirements:
```
pip install -r requirements.txt
```

4. Navigate to folder that store `main.py` file:
```
cd armor
```
This should contain two folders named `gui` and `backend` and one `main.py` file. This is the file we're gonna run.

5. Run the main.py file
```
python main.py
```

Make sure this is running from the armor folder. 


