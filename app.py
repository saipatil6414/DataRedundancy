from flask import Flask, request, jsonify
import sqlite3
import hashlib

app = Flask(__name__)

# Database Connection
def connect_db():
    return sqlite3.connect("database.db")

# Create Table
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS data_store (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT UNIQUE,
            hash TEXT UNIQUE
        )
    """)
    conn.commit()
    conn.close()

create_table()

# Hash Function
def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

# API to Add Data
@app.route("/add-data", methods=["POST"])
def add_data():
    input_data = request.json.get("data")
    data_hash = generate_hash(input_data)

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM data_store WHERE hash = ?", (data_hash,))
    existing = cursor.fetchone()

    if existing:
        return jsonify({"message": "Duplicate data detected. Entry rejected."})

    cursor.execute(
        "INSERT INTO data_store (data, hash) VALUES (?, ?)",
        (input_data, data_hash)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Unique data stored successfully."})

# API to View Data
@app.route("/view-data", methods=["GET"])
def view_data():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM data_store")
    records = cursor.fetchall()
    conn.close()

    return jsonify(records)

if __name__ == "__main__":
    app.run(debug=True)
