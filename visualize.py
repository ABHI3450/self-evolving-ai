import sqlite3
import matplotlib.pyplot as plt

DB_PATH = "database/memory.db"


def plot_scores():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT score FROM memory ORDER BY id")
    scores = [row[0] for row in cursor.fetchall()]

    conn.close()

    if len(scores) < 2:
        return None

    plt.figure()
    plt.plot(scores)
    plt.xlabel("Attempts")
    plt.ylabel("Score")
    plt.title("Self-Improvement Over Time")

    return plt
