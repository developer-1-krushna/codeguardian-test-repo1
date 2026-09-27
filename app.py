import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# [FIX 1: GITLEAKS] Load API key safely from environment variables instead of hardcoding
STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")


@app.route("/")
def home():
    return "Welcome home"


@app.route("/search")
def search_users():
    username = request.args.get("username", "")
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # [FIX 2: BANDIT & SEMGREP] Use parameterized queries to prevent SQL Injection
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    return str(cursor.fetchall())


# [FIX 3: BANDIT & SEMGREP] Removed the dangerous shell=True diagnostic endpoint entirely


if __name__ == "__main__":
    # [FIX 4: GENERAL] Turn off debug mode for production
    app.run(debug=False)
