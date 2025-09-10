import hashlib
import logging
from database import get_db_connection

logging.basicConfig(filename="server.log", level=logging.INFO)

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def create_users_table():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            tokens INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def signup_user(username: str, password: str):
    conn = get_db_connection()
    hashed = hash_password(password)
    try:
        conn.execute("INSERT INTO users (username, password, tokens) VALUES (?, ?, ?)", (username, hashed, 0))
        conn.commit()
        logging.info(f"User {username} registered.")
        return True
    except:
        return False
    finally:
        conn.close()

def delete_user(username: str, password: str):
    conn = get_db_connection()
    hashed = hash_password(password)
    cursor = conn.execute("DELETE FROM users WHERE username = ? AND password = ?", (username, hashed))
    conn.commit()
    deleted = cursor.rowcount > 0
    if deleted:
        logging.info(f"User {username} deleted.")
    conn.close()
    return deleted

def get_tokens(username: str):
    conn = get_db_connection()
    cursor = conn.execute("SELECT tokens FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return row["tokens"]
    return None

def add_tokens(username: str, amount: int):
    conn = get_db_connection()
    cursor = conn.execute("UPDATE users SET tokens = tokens + ? WHERE username = ?", (amount, username))
    conn.commit()
    updated = cursor.rowcount > 0
    if updated:
        logging.info(f"User {username} added {amount} tokens.")
    conn.close()
    return updated