import sqlite3

def initialize_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def log_attendance(db_path, name, timestamp):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO attendance (name, timestamp) VALUES (?, ?)
    ''', (name, timestamp))
    conn.commit()
    conn.close()

def fetch_attendance(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT name, timestamp FROM attendance ORDER BY timestamp DESC')
    records = cursor.fetchall()
    conn.close()
    return records
