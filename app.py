import streamlit as st
from database import register_user, login_user, get_products, add_order, get_user_orders

st.set_page_config(page_title="Nike Advanced Store", page_icon="👟", layout="wide")
st.title("🔥 Nike Advanced Store")

# Session state
if "user" not in st.session_state:
    st.session_state.user = None
if "cart" not in st.session_state:
    st.session_state.cart = []

# Login/Register
if st.session_state.user is None:
    st.subheader("Login / Register")
    tab = st.radio("Choose", ["Login", "Register"])
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if tab == "Register" and st.button("Register"):
        if register_user(username, password):
            st.success("User registered! Please login.")
        else:
            st.error("Username already exists.")
    elif tab == "Login" and st.button("Login"):
        user = login_user(username, password)
        if user:
            st.session_state.user = user
            st.success(f"Logged in as {username}")
        else:
            st.error("Invalid credentials.")
    st.stop()

# Show products
st.subheader(f"Welcome, {st.session_state.user[1]}!")

# Filter products
categories = list(set([p[4] for p in get_products()]))
categories.insert(0, "All")
selected_category = st.selectbox("Filter by category", categories)
search_query = st.text_input("Search products by name")
products = get_products()
if selected_category != "All":
    products = [p for p in products if p[4] == selected_category]
if search_query:
    products = [p for p in products if search_query.lower() in p[1].lower()]

cols = st.columns(3)
for idx, product in enumerate(products):
    with cols[idx % 3]:
        st.image(product[3], use_column_width=True)
        st.subheader(product[1])
        st.write(f"${product[2]}")
        qty = st.number_input(f"Quantity ({product[1]})", min_value=1, max_value=10, key=f"qty{product[0]}")
        if st.button("Add to Cart", key=f"add{product[0]}"):
            st.session_state.cart.append({
                "id": product[0],
                "name": product[1],
                "price": product[2],
                "quantity": qty
            })
            st.success(f"Added {qty} x {product[1]} to cart")

# Sidebar cart & order placement
st.sidebar.header("Shopping Cart")
total = 0
for item in st.session_state.cart:
    st.sidebar.write(f"{item['name']} x {item['quantity']} = ${item['quantity']*item['price']}")
    total += item['quantity']*item['price']
st.sidebar.write(f"**Total: ${total}**")
if st.sidebar.button("Place Order") and st.session_state.cart:
    for item in st.session_state.cart:
        add_order(st.session_state.user[0], item['id'], item['quantity'])
    st.sidebar.success("✅ Order placed!")
    st.session_state.cart = []

# Show order history
st.subheader("Your Orders")
orders = get_user_orders(st.session_state.user[0])
for o in orders:
    st.write(f"{o[0]} x {o[2]} = ${o[1]*o[2]}")
