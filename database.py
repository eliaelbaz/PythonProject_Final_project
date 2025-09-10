import sqlite3

def get_db_connection():
    conn = sqlite3.connect("ml_server.db")
    conn.row_factory = sqlite3.Row
    return conn