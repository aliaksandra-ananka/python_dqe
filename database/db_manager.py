import sqlite3


class DatabaseManager:
    def __init__(self, db_path="news.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        """Create tables if they do not exist"""

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            city TEXT,
            date TEXT,
            UNIQUE(text, city, date)
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS private_ad (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            expiration_date TEXT,
            days_left INTEGER,
            UNIQUE(text, expiration_date)
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            temperature INTEGER,
            UNIQUE(text, temperature)
        )
        """)

        self.conn.commit()

    # --------------------------
    # INSERT METHODS
    # --------------------------

    def insert_news(self, text, city, date):
        try:
            self.cursor.execute("""
                INSERT INTO news (text, city, date)
                VALUES (?, ?, ?)
            """, (text, city, date))
            self.conn.commit()
            print("News saved to DB")
        except sqlite3.IntegrityError:
            print("Duplicate News skipped")

    def insert_private_ad(self, text, expiration_date, days_left):
        try:
            self.cursor.execute("""
                INSERT INTO private_ad (text, expiration_date, days_left)
                VALUES (?, ?, ?)
            """, (text, expiration_date, days_left))
            self.conn.commit()
            print("PrivateAd saved to DB")
        except sqlite3.IntegrityError:
            print("Duplicate PrivateAd skipped")

    def insert_weather(self, text, temperature):
        try:
            self.cursor.execute("""
                INSERT INTO weather (text, temperature)
                VALUES (?, ?)
            """, (text, temperature))
            self.conn.commit()
            print("Weather saved to DB")
        except sqlite3.IntegrityError:
            print("Duplicate Weather skipped")

    def close(self):
        self.conn.close()