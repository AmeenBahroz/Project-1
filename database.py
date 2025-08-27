import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("nike_store.db", check_same_thread=False)
c = conn.cursor()

# Create products table
c.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    image TEXT
)
''')

# Create orders table
c.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY(product_id) REFERENCES products(id)
)
''')

conn.commit()

# Add sample products (if table is empty)
c.execute("SELECT COUNT(*) FROM products")
if c.fetchone()[0] == 0:
    products = [
        ("Air Max 270", 150, "https://images.unsplash.com/photo-1606813903134-45c28b953b3f"),
        ("Jordan Retro", 200, "https://images.unsplash.com/photo-1542291026-7eec264c27ff"),
        ("Blazer Mid '77", 120, "https://images.unsplash.com/photo-1595950653171-47c33e5f1d6e")
    ]
    c.executemany("INSERT INTO products (name, price, image) VALUES (?, ?, ?)", products)
    conn.commit()

# Functions to get products
def get_products():
    c.execute("SELECT * FROM products")
    return c.fetchall()

# Add order
def add_order(product_id, quantity):
    c.execute("INSERT INTO orders (product_id, quantity) VALUES (?, ?)", (product_id, quantity))
    conn.commit()
