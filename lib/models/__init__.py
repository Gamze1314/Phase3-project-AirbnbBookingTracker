#lib/models/__init__.py
import sqlite3


# create a db connection with CURSOR  and CONNECTION objects.
CONN = sqlite3.connect('booking_tracker.db')
CURSOR = CONN.cursor()
# cursor object allow us to execute SQL queries, and retrieve results from database.
