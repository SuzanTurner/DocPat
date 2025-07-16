# DocPat
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

2. Install the requirements:
```
pip install -r requirements.txt
```

3. Run the main.py file
```
python main.py
```

Make sure this is running from the root folder. 


