import sqlite3

conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

# Create  table Inventory
cursor.execute("""
CREATE TABLE IF NOT EXISTS Inventory_Items(
    Item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Descriptiom TEXT NOT NULL,
    price REAL,
    quantity INTEGER NOT NULL
);
""")
# Create  table Orders
cursor.execute("""
CREATE TABLE IF NOT EXISTS Orders(
    Item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Descriptiom TEXT NOT NULL,
    price REAL,
    quantity INTEGER NOT NULL
);
""")
# Create  table transaction
cursor.execute("""
CREATE TABLE IF NOT EXISTS Tansaction(
    Item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Descriptiom TEXT NOT NULL,
    price REAL,
    quantity INTEGER NOT NULL
);
""")
conn.commit( )
c onn .close