import sqlite3

DB_NAME = "telegram_bot.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER UNIQUE NOT NULL,
            username TEXT,
            first_name TEXT,
            balance REAL DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()


def add_user(telegram_id, username, first_name):
    conn = sqlite3.connect(DB_NAME)

    conn.execute("""
        INSERT OR IGNORE INTO users
        (telegram_id, username, first_name)
        VALUES (?, ?, ?)
    """, (telegram_id, username, first_name))

    conn.commit()
    conn.close()
