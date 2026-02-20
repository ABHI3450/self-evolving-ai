import sqlite3
import pandas as pd

DB_PATH = "database/memory.db"


def get_stats():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM memory", conn)
    conn.close()

    if len(df) == 0:
        return {
            "total": 0,
            "avg_score": 0
        }

    return {
        "total": len(df),
        "avg_score": round(df["score"].mean(), 2)
    }
