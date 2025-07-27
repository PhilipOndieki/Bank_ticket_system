# 🏦 Bank Queue System

A simple terminal-based queue management system for a bank. It allows staff to assign tickets to customers, serve them in order of arrival, and track their visit history using both file logs and an SQLite database.

## 🚀 Features

- Assign ticket numbers to customers based on arrival
- Record customer name and reason for visit
- Serve customers in a first-come-first-served order
- Log all activities to `activity_log.txt`
- Store all customer data in `queue.db` (SQLite)
- View recent activities and customer visit history

## 🧱 Project Structure
bank_queue/
├── main.py # Entry point of the app
├── ticket.py # Customer class definition
├── utils.py # Queue, logging, and DB logic
├── activity_log.txt # Text-based activity log (auto-generated)
├── queue.db # SQLite database (auto-generated)

## ▶️ Getting Started

1. Clone this repo or copy the files into a folder
2. Run the main program:
   ```bash
   python main.py
3. Follow the on-screen menu to manage the queue

💾 Requirements
Python 3.7+

No external dependencies (uses built-in sqlite3, queue, datetime)
📂 Data Storage
Logs: Stored in activity_log.txt

Database: Stored in queue.db using SQLite
