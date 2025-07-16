import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('backend/database.db')
    c = conn.cursor()
    # c.execute('''
    #             DROP TABLE doctors;
    #   ''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS doctors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )''')


    # c.execute("drop table appointments;")
    # c.execute("drop table users;")

    c.execute('''
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        doctor_id INTEGER,
        date_time TEXT,
        FOREIGN KEY(doctor_id) REFERENCES doctors(id)
    )
''')
    
    conn.commit()
    conn.close()


def add_user(username, password):
    conn = sqlite3.connect("backend/database.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO doctors (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def verify_user(username, password):
    conn = sqlite3.connect("backend/database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM doctors WHERE username = ? AND password = ?", (username, password))
    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]  
    else:
        return None

def get_all_doctors():
    print("Fetching doctors from DB...")
    
    conn = sqlite3.connect("backend/database.db")  
    c = conn.cursor()
    
    c.execute("SELECT id, username FROM doctors")
    rows = c.fetchall()
    
    doctors = {f"{i+1}.": row[1] for i, row in enumerate(rows)}

    conn.close()
    return doctors

def create_appointment(doctor_id: int):
    print(f"Creating appointment... for doctor_id {doctor_id}")
    conn = sqlite3.connect("backend/database.db")
    c = conn.cursor()

    booking_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

    c.execute('''
        INSERT INTO appointments (doctor_id, date_time)
        VALUES (?, ?)
    ''', (doctor_id, booking_time))

    conn.commit()
    conn.close()
    print("Appointment created successfully!")

def get_appointments(doctor_id: int):
    print(f"Fetching appointments for doctor ID: {doctor_id}")
    conn = sqlite3.connect("backend/database.db")
    c = conn.cursor()

    c.execute('''
        SELECT date_time FROM appointments
        WHERE doctor_id = ?
    ''', (doctor_id,))

    results = c.fetchall()
    conn.close()

    return [row[0] for row in results] 