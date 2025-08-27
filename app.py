import streamlit as st
from database import register_user, login_user, get_products, add_order, get_user_orders

# Page config
st.set_page_config(page_title="Nike Store", page_icon="👟", layout="wide")

# --- Session state ---
if "user" not in st.session_state:
    st.session_state.user = None
if "cart" not in st.session_state:
    st.session_state.cart = []

# --- Login/Register ---
if st.session_state.user is None:
    st.title("👟 Nike Store Login / Register")
    tab = st.radio("Select Option", ["Login", "Register"])
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if tab == "Register" and st.button("Register"):
        success, message = register_user(username.strip(), password.strip())
        if success:
            st.success(message + " Please login below.")
        else:
            st.error(message)

    if tab == "Login" and st.button("Login"):
        success, result = login_user(username.strip(), password.strip())
        if success:
            st.session_state.user = result
            st.success(f"Logged in as {username}")
        else:
            st.error(result)

# --- Dashboard ---
if st.session_state.user is not None:
    user = st.session_state.user
    st.title(f"Welcome, {user[1]} 👟")

    # --- Sidebar: Shopping Cart ---
    st.sidebar.header("🛒 Shopping Cart")
    total = 0
    for item in st.session_state.cart:
        st.sidebar.write(f"{item['name']} x {item['quantity']} = ${item['price']*item['quantity']}")
        total += item['price']*item['quantity']
    st.sidebar.write(f"**Total: ${total}**")
    if st.sidebar.button("Place Order") and st.session_state.cart:
        for item in st.session_state.cart:
            add_order(user[0], item['id'], item['quantity'])
        st.sidebar.success("✅ Order placed!")
        st.balloons()
        st.session_state.cart = []

    # --- Product Catalog ---
    st.subheader("🏷️ Product Catalog")
    products = get_products()
    if products:
        categories = ["All"] + list({p[4] if len(p) > 4 else "Uncategorized" for p in products})
    else:
        categories = ["All"]

    selected_category = st.selectbox("Filter by Category", categories)
    search_query = st.text_input("Search by Name")

    filtered_products = []
    for p in products:
        category = p[4] if len(p) > 4 else "Uncategorized"
        if (selected_category == "All" or category == selected_category) and (search_query.lower() in p[1].lower() if search_query else True):
            filtered_products.append(p)

    # --- Display products in responsive multi-row layout ---
    num_cols = 3
    for i in range(0, len(filtered_products), num_cols):
        cols = st.columns(num_cols)
        for idx, product in enumerate(filtered_products[i:i+num_cols]):
            with cols[idx]:
                with st.container():
                    st.image(product[3], use_column_width=True)
                    st.markdown(f"**{product[1]}**")
                    st.markdown(f"**${product[2]}**")
                    qty = st.number_input("Qty", min_value=1, max_value=10, key=f"qty{product[0]}")
                    if st.button("Add to Cart", key=f"add{product[0]}"):
                        st.session_state.cart.append({
                            "id": product[0],
                            "name": product[1],
                            "price": product[2],
                            "quantity": qty
                        })
                        st.success(f"Added {qty} x {product[1]} to cart")

    # --- Dashboard Stats ---
    st.subheader("📊 Dashboard Stats")
    orders = get_user_orders(user[0])
    total_orders = len(orders)
    total_spent = sum([o[1]*o[2] for o in orders])
    total_products = sum([o[2] for o in orders])

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Orders", total_orders, delta=f"+{total_orders*2}")
    col2.metric("Total Spent ($)", total_spent, delta=f"+${total_spent*0.05:.2f}")
    col3.metric("Products Bought", total_products, delta=f"+{total_products}")

    # --- Order History ---
    st.subheader("📄 Order History")
    if orders:
        for o in orders:
            st.write(f"{o[0]} x {o[2]} = ${o[1]*o[2]}")
    else:
        st.info("No orders yet.")
