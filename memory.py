import sqlite3
import os

DB_PATH = "database/memory.db"


def init_db():
    os.makedirs("database", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        answer TEXT,
        feedback TEXT,
        score INTEGER
    )
    """)

    conn.commit()
    conn.close()


def save_memory(question, answer, feedback, score):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO memory (question, answer, feedback, score)
    VALUES (?, ?, ?, ?)
    """, (question, answer, feedback, score))

    conn.commit()
    conn.close()


def get_similar(question, limit=3):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT question, feedback
    FROM memory
    ORDER BY id DESC
    LIMIT ?
    """, (limit,))

    data = cursor.fetchall()
    conn.close()

    return data


def get_all_history(limit=50):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT question, answer, feedback, score
    FROM memory
    ORDER BY id DESC
    LIMIT ?
    """, (limit,))

    data = cursor.fetchall()
    conn.close()

    return data
