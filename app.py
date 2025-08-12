# vulnerable_app.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import os
import sqlite3

# --- Setup a temporary in-memory database for the SQLi example ---
db_connection = sqlite3.connect(":memory:", check_same_thread=False)
db_cursor = db_connection.cursor()
db_cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
db_cursor.execute("INSERT INTO users (name) VALUES ('Alice'), ('Bob')")
db_connection.commit()
# ----------------------------------------------------------------

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return "<h1>Vulnerable Test App for DefenSys</h1>"

# 1. Vulnerable endpoint for XSS testing
@app.get("/xss", response_class=HTMLResponse)
def xss_test(query: str = ""):
    # DANGEROUS: Directly embedding user input into the HTML.
    return f"<h2>Search results for: {query}</h2>"

# 2. Vulnerable endpoint for SQL Injection testing
@app.get("/sqli", response_class=HTMLResponse)
def sqli_test(id: str = "1"):
    try:
        # DANGEROUS: Directly concatenating user input into the SQL query.
        query = f"SELECT name FROM users WHERE id = {id}"
        db_cursor.execute(query)
        result = db_cursor.fetchone()
        user_name = result[0] if result else "User not found"
        return f"<h3>User found: {user_name}</h3>"
    except Exception as e:
        # If the query fails, it returns the error message, confirming the vulnerability.
        return f"<h4>SQL Error: {e}</h4>"

# 3. Vulnerable endpoint for Command Injection testing
@app.get("/commandi", response_class=HTMLResponse)
def command_injection_test(ip: str = "8.8.8.8"):
    # DANGEROUS: Directly concatenating user input into a shell command.
    cmd_output = os.popen(f"ping -n 1 {ip}").read() # Use "-c 1" for Linux/macOS
    return f"<pre>{cmd_output}</pre>"