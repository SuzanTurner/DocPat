import threading
import subprocess
import time
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

def run_flask():
    subprocess.run([sys.executable, os.path.join("backend", "main.py")])

def run_gui():
    subprocess.run([sys.executable, os.path.join("gui", "main.py")])

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    time.sleep(1)
    run_gui()