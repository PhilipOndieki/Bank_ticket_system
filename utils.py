import sqlite3
from queue import Queue
from datetime import datetime

# Queue of customers in order of arrival
waiting_list = Queue()

# Dictionary of customers to store customer records using ticket_no as key 
customer_records = {}

# Tickets available
available_tickets = set(range(10, 50)) # ticket numbers from 10 to 50 

# Track the currently serving ticket number
currently_serving = None

# Save activity log to a file
def log_to_file(message):
    with open("activity_log.txt", "a") as file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f"[{timestamp}] {message}\n")

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect("queue.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS customer_log (
                    ticket_no INTEGER PRIMARY KEY,
                    name TEXT,
                    reason TEXT,
                    joined_at TEXT,
                    served_at TEXT
                )''')
    conn.commit()
    conn.close()

# Save to database
def save_to_db(ticket_no, name, reason, joined_at, served_at=None):
    conn = sqlite3.connect("queue.db")
    c = conn.cursor()
    c.execute('''
        INSERT OR REPLACE INTO customer_log (ticket_no, name, reason, joined_at, served_at)
        VALUES (?, ?, ?, ?, ?)
    ''', (ticket_no, name, reason, joined_at, served_at))
    conn.commit()
    conn.close()

def view_logs():
    try:
        with open("activity_log.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("\n📭 No activity logged yet.")
                return
            print("\n📄 Activity Log:")
            for line in lines[-10:]:  # show last 10 lines
                print(line.strip())
    except FileNotFoundError:
        print("\n🚫 Log file not found.")

def view_db_records():
    conn = sqlite3.connect("queue.db")
    c = conn.cursor()
    c.execute("SELECT * FROM customer_log ORDER BY ticket_no ASC")
    records = c.fetchall()
    conn.close()

    if not records:
        print("\n📭 No records in database.")
        return

    print("\n📋 Customer Records:")
    print(f"{'Ticket':<8}{'Name':<15}{'Reason':<20}{'Joined':<20}{'Served'}")
    print("-" * 75)
    for ticket_no, name, reason, joined, served in records:
        served = served if served else "Not served"
        print(f"{ticket_no:<8}{name:<15}{reason:<20}{joined:<20}{served}")


