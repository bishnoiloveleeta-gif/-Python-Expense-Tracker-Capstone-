import sqlite3
import logging
from flask import Flask, request, jsonify

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
app = Flask(__name__)

def init_db():
    with sqlite3.connect("expenses.db") as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, title TEXT, amount REAL, category TEXT)")

init_db()

@app.route("/expenses", methods=["GET"])
def get_expenses():
    try:
        with sqlite3.connect("expenses.db") as conn:
            rows = conn.execute("SELECT * FROM expenses").fetchall()
        return jsonify([{"id": r[0], "title": r[1], "amount": r[2], "category": r[3]} for r in rows])
    except Exception as e:
        logging.error(f"Error fetching expenses: {e}")
        return jsonify({"error": "Server error"}), 500

@app.route("/expenses", methods=["POST"])
def add_expense():
    try:
        data = request.get_json()
        if not data or not data.get("title") or not data.get("amount"):
            return jsonify({"error": "Title and amount required"}), 400
        with sqlite3.connect("expenses.db") as conn:
            conn.execute("INSERT INTO expenses (title, amount, category) VALUES (?, ?, ?)",
                         (data["title"], float(data["amount"]), data.get("category", "General")))
        logging.info(f"Added expense: {data['title']}")
        return jsonify({"message": "Expense added"}), 201
    except Exception as e:
        logging.error(f"Error adding expense: {e}")
        return jsonify({"error": "Invalid input"}), 400

if __name__ == "__main__":
    app.run(debug=True)
           
