import sqlite3

conn = sqlite3.connect('calendar.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT, title TEXT, text TEXT)''')
conn.commit()
conn.close()

def db_work(db_str):
    conn = sqlite3.connect('calendar.db')
    cursor = conn.cursor()
    cursor.execute(db_str)
    answer = cursor.fetchall()
    conn.commit()
    conn.close()
    return (answer)
