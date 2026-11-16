# 💰 Python Expense Tracker Capstone (Module 06)

A full-stack Expense Tracker application built with a **Python Flask + SQLite** REST backend (with structured logging and exception safety) and a responsive web frontend.

## 🏗️ Architecture & Database Schema
- **Backend (`app.py`):** Flask REST API with `logging` module and `try-except` error handling.
- **Database (`expenses.db`):** SQLite table `expenses (id INTEGER PRIMARY KEY, title TEXT, amount REAL, category TEXT)`.
- **Frontend (`index.html`):** Interactive web interface deployed via GitHub Pages.

## ⚙️ Setup Instructions
1. Install Flask: `pip install flask`
2. Run server: `python app.py`
