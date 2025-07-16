from flask import Flask, jsonify, request
import sqlite3
from backend.db import init_db, add_user, verify_user

app = Flask(__name__)
init_db()

# users = {
#     "Yadh": "Dwink",
# }

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    id = data.get("id")

    if not username or not password:
        return jsonify({"status": "fail", "message": "Username and password required"}), 400

    success = add_user(username, password)
    if success:
        return jsonify({"status": "success", "message": "User registered successfully", "id" : id}), 200
    else:
        return jsonify({"status": "fail", "message": "Username already exists"}), 409



# @app.route("/login", methods=["POST"])
# def login():
#     data = request.json
#     username = data.get("username")
#     password = data.get("password")
#     id = data.get("id")

#     if not username or not password:
#         return jsonify({"status": "fail", "message": "Missing credentials"},), 400

#     if verify_user(username, password):
#         return jsonify({"status": "success", "message": "Login successful", "id" : id}), 200
#     else:
#         return jsonify({"status": "fail", "message": "Invalid credentials"}), 401

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"status": "fail", "message": "Missing credentials"}), 400

    doctor_id = verify_user(username, password)

    if doctor_id is not None:
        return jsonify({
            "status": "success",
            "message": "Login successful",
            "id": doctor_id  # ✅ Real doctor ID
        }), 200
    else:
        return jsonify({"status": "fail", "message": "Invalid credentials"}), 401
    

@app.route('/doctors', methods=['GET'])
def list_doctors():
    return jsonify([])

@app.route('/appointments', methods=['POST'])

def create_appointment():
    return jsonify({'message': 'Appointment made'})

@app.route('/doctor/appointments/<doctor_id>', methods=['GET'])
def view_appointments(doctor_id):
    return jsonify([])

if __name__ == "__main__":
    app.run(debug = True)