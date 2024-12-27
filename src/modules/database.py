import sqlite3
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.setup_database()

    def setup_database(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                user_input TEXT,
                eva_response TEXT,
                sentiment REAL
            )
        ''')
        self.conn.commit()

    def save_interaction(self, user_input, response):
        timestamp = datetime.now().isoformat()
        self.cursor.execute('''
            INSERT INTO conversations (timestamp, user_input, eva_response)
            VALUES (?, ?, ?)
        ''', (timestamp, user_input, response))
        self.conn.commit()