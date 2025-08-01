# database.py

import sqlite3

conn = sqlite3.connect('restaurant.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer TEXT,
    item TEXT,
    price REAL
)
""")
conn.commit()

def save_order_to_db(customer, items):
    for item in items:
        cursor.execute('INSERT INTO orders (customer, item, price) VALUES (?, ?, ?)',
                       (customer.name, item.name, item.price))
    conn.commit()
