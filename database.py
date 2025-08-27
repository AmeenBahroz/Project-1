import sqlite3

# Connect to SQLite
conn = sqlite3.connect("nike_store.db", check_same_thread=False)
c = conn.cursor()

# Users table
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
''')

# Products table
c.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    image TEXT,
    category TEXT
)
''')

# Orders table
c.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(product_id) REFERENCES products(id)
)
''')
conn.commit()

# Add sample products if empty
c.execute("SELECT COUNT(*) FROM products")
if c.fetchone()[0] == 0:
    products = [
        ("Air Max 270", 150, "https://images.unsplash.com/photo-1606813903134-45c28b953b3f", "Running"),
        ("Jordan Retro", 200, "https://images.unsplash.com/photo-1542291026-7eec264c27ff", "Basketball"),
        ("Blazer Mid '77", 120, "https://images.unsplash.com/photo-1595950653171-47c33e5f1d6e", "Casual")
    ]
    c.executemany("INSERT INTO products (name, price, image, category) VALUES (?, ?, ?, ?)", products)
    conn.commit()

# User functions
def register_user(username, password):
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except:
        return False

def login_user(username, password):
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return c.fetchone()

# Product functions
def get_products():
    c.execute("SELECT * FROM products")
    return c.fetchall()

# Order functions
def add_order(user_id, product_id, quantity):
    c.execute("INSERT INTO orders (user_id, product_id, quantity) VALUES (?, ?, ?)", (user_id, product_id, quantity))
    conn.commit()

def get_user_orders(user_id):
    c.execute('''
        SELECT p.name, p.price, o.quantity
        FROM orders o JOIN products p ON o.product_id = p.id
        WHERE o.user_id=?
    ''', (user_id,))
    return c.fetchall()

