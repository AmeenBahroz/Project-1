# nike_site.py
import streamlit as st

# Page settings
st.set_page_config(page_title="Nike Style Landing", page_icon="👟", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
        font-family: 'Arial', sans-serif;
    }
    .hero {
        background: linear-gradient(to right, #000000, #333333);
        color: white;
        padding: 80px 20px;
        text-align: center;
        border-radius: 20px;
    }
    .hero h1 {
        font-size: 50px;
        font-weight: bold;
    }
    .hero p {
        font-size: 20px;
        margin-bottom: 20px;
    }
    .button {
        background: #ff4b4b;
        padding: 12px 30px;
        border-radius: 30px;
        color: white;
        text-decoration: none;
        font-weight: bold;
    }
    .button:hover {
        background: #ff1f1f;
    }
    .product-card {
        background: white;
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    .product-card:hover {
        transform: scale(1.05);
    }
    .product-card img {
        border-radius: 15px;
        width: 100%;
        height: 250px;
        object-fit: cover;
    }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class="hero">
        <h1>Step Into Style</h1>
        <p>Premium sneakers for comfort, performance, and unbeatable style.</p>
        <a href="#products" class="button">Shop Now</a>
    </div>
""", unsafe_allow_html=True)

# Product Section
st.markdown("<h2 id='products' style='text-align:center; margin-top:50px;'>🔥 Featured Sneakers</h2>", unsafe_allow_html=True)

products = [
    {"name": "Air Max 270", "price": "$150", "img": "https://images.unsplash.com/photo-1606813903134-45c28b953b3f"},
    {"name": "Jordan Retro", "price": "$200", "img": "https://images.unsplash.com/photo-1542291026-7eec264c27ff"},
    {"name": "Blazer Mid '77", "price": "$120", "img": "https://images.unsplash.com/photo-1595950653171-47c33e5f1d6e"}
]

cols = st.columns(3)
for idx, product in enumerate(products):
    with cols[idx]:
        st.markdown(f"""
            <div class="product-card">
                <img src="{product['img']}" alt="{product['name']}">
                <h3>{product['name']}</h3>
                <p style="color:gray; font-size:18px;">{product['price']}</p>
                <a href="#" class="button">Add to Cart</a>
            </div>
        """, unsafe_allow_html=True)

# Call to Action
st.markdown("""
    <div style="background:black; color:white; padding:50px; margin-top:50px; border-radius:20px; text-align:center;">
        <h2 style="font-size:40px;">Elevate Your Game</h2>
        <p style="font-size:18px;">Experience sneakers that blend cutting-edge design with ultimate comfort.</p>
        <a href="#" class="button">Explore Collection</a>
    </div>
""", unsafe_allow_html=True)

