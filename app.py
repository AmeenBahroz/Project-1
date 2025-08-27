import streamlit as st
from database import get_products, add_order

# Page config
st.set_page_config(page_title="Nike Store", page_icon="👟", layout="wide")
st.title("🔥 Nike Advanced Store")

# Sidebar for cart
if "cart" not in st.session_state:
    st.session_state.cart = []

st.sidebar.header("Shopping Cart")
total = 0
for item in st.session_state.cart:
    st.sidebar.write(f"{item['name']} x {item['quantity']} = ${item['quantity']*item['price']}")
    total += item['quantity']*item['price']
st.sidebar.write(f"**Total: ${total}**")
if st.sidebar.button("Place Order") and st.session_state.cart:
    for item in st.session_state.cart:
        add_order(item['id'], item['quantity'])
    st.sidebar.success("✅ Order placed!")
    st.session_state.cart = []

# Search products
search_query = st.text_input("Search Products")
products = get_products()
if search_query:
    products = [p for p in products if search_query.lower() in p[1].lower()]

# Display products
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
