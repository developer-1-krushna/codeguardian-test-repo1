import sqlite3
import subprocess
from flask import Flask, request

app = Flask(__name__)

# [FAILURE 1: GITLEAKS] Hardcoded API Secret Token
STRIPE_API_KEY = "sk_live_51NzFakeStripeSecretKeyForTestingOnly999"


@app.route("/")
def home():
    return "Welcome home"


@app.route("/search")
def search_users():
    username = request.args.get("username", "")
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # [FAILURE 2: BANDIT & SEMGREP] SQL Injection via string formatting (Bandit: B608)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return str(cursor.fetchall())


@app.route("/diagnostic")
def run_diagnostic():
    cmd = request.args.get("cmd", "echo ok")

    # [FAILURE 3: BANDIT & SEMGREP] Command Injection using shell=True (Bandit: B602)
    output = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return output.stdout


if __name__ == "__main__":
    app.run(debug=True)
