import sqlite3
import bcrypt

# Connect to the SQLite database (or create if not exists)
conn = sqlite3.connect('todo_app.db')

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Create a table for users if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')
conn.commit()

def register_user(username, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    cursor.execute('''
        INSERT INTO users (username, password)
        VALUES (?, ?)
    ''', (username, hashed_password))
    conn.commit()

def verify_user(username, password):
    cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
    stored_password = cursor.fetchone()

    if stored_password and bcrypt.checkpw(password.encode('utf-8'), stored_password[0]):
        return True
    return False

# Example usage
register_user("user1", "password123")

username = "user1"
password = "password123"
if verify_user(username, password):
    print("Login successful")
else:
    print("Login failed")

# Close the database connection when done
conn.close()
