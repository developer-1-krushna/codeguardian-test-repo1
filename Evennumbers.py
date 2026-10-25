import sqlite3

# Simulated user input from a form or web request
user_provided_input = "admin' OR '1'='1"

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# BAD PRACTICE: Directly inserting user input into SQL string (Vulnerable to SQL Injection)
query = (
    f"SELECT * FROM users WHERE username = '{user_provided_input}'"
)

# If executed, this bypasses authentication entirely because
# the query becomes: SELECT * FROM users WHERE username = 'admin' OR '1'='1'
print("Generated Query:", query)
