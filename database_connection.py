import sqlite3

DB_NAME = "airline_management.db"

def get_connection():
    return sqlite3.connect(DB_NAME)