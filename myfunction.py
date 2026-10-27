import sqlite3

def authenticate_user_vulnerable(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
   
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    cursor.execute(query)
    user = cursor.fetchone()
    return user is not None

def authenticate_user_secure(username, password):
    conn = sqlite3.connect("users.db")
    cursor = cursor()
    
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    return user is not None
