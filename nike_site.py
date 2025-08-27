# nike_site.py
import streamlit as st

# Set page config
st.set_page_config(page_title="Nike Style Landing", page_icon="👟", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #f9f9f9;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .hero {
        background: linear-gradient(to right, #000000, #333333);
        color: white;
        padding: 100px 20px;
        text-align: center;
        border-radius: 20px;
    }
    .hero h1 {
        font-size: 60px;
        font-weight: bold;
    }
    .hero p {
        font-size: 20px;
        max-width: 600px;
        margin: auto;
    }
    .shop-button {
        background-color: #ff4b4b;
        color: white;
        padding: 12px 30px;
        border-radius: 50px;
        font-size: 18px;
        text-decoration: none;
    }
    .shop-button:hover {
        background-color: #ff1f1f;
    }
    .product-card {
        background: white;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        text-align: center;
        transition: transform 0.3s ease;
    }
    .product-card:hover {
        transform: scale(1.05);
    }
    .product-card img {
        border-radius: 20px;
        width: 100%;
        height: 250px;
        object-fit: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Hero section
st.markdown(
    """
    <div class='hero'>
        <h1>Step Into Style</h1>
        <p>Explore our premium sneakers designed for comfort, performance, and unbeatable style.</p>
        <br>
        <a class='shop-button' href='#products'>Shop Now</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Product section
st.markdown("<h2 id='products' style='text-align: center; margin-top: 50px;'>🔥 Featured Sneakers</h2>", unsafe_allow_html=True)

# Product data
products = [
    {
        "name": "Air Max 270",
        "price": "$150",
        "image": "https://images.unsplash.com/photo-1606813903134-45c28b953b3f"
    },
    {
        "name": "Jordan Retro",
        "price": "$200",
        "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff"
    },
    {
        "name": "Blazer Mid '77",
        "price": "$120",
        "image": "https://images.unsplash.com/photo-1595950653171-47c33e5f1d6e"
    }
]

# Product cards
cols = st.columns(3)
for idx, product in enumerate(products):
    with cols[idx]:
        st.markdown(
            f"""
            <div class='product-card'>
                <img src='{product["image"]}' alt='{product["name"]}' />
                <h3>{product["name"]}</h3>
                <p style='font-size:18px; color: gray;'>{product["price"]}</p>
                <a class='shop-button' href='#'>Add to Cart</a>
            </div>
            """,
            unsafe_allow_html=True
        )

# Call to action
st.markdown(
    """
    <div style='background-color:black; color:white; text-align:center; padding:50px; margin-top:50px; border-radius:20px;'>
        <h2 style='font-size:40px;'>Elevate Your Game</h2>
        <p style='font-size:18px;'>Experience sneakers that blend cutting-edge design with ultimate comfort.</p>
        <a class='shop-button' href='#'>Explore Collection</a>
    </div>
    """,
    unsafe_allow_html=True
)

