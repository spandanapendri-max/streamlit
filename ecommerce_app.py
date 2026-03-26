
import streamlit as st

# Page setup
st.set_page_config(
    page_title="Microservices-Based E-Commerce",
    layout="wide"
)

# ----------- Styling -----------

st.markdown("""
<style>

.stApp {
    background-color: #eef5fb;
}

[data-testid="stSidebar"] {
    background-color: #d4e6f1;
}

h1 {
    text-align: center;
    color: #1f618d;
}

.stButton>button {
    background-color: #2e86c1;
    color: white;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ----------- Initialize Cart -----------

if "cart" not in st.session_state:
    st.session_state.cart = []

# ----------- Title -----------

st.title(" Microservices-Based E-Commerce")

menu = ["Products", "Cart", "Checkout", "Profile"]

choice = st.sidebar.radio("Menu", menu)

# ----------- PRODUCTS PAGE -----------

if choice == "Products":

    st.subheader(" Product Catalog")

    # Product Data
    products = [
        {"name": "Laptop", "price": 50000, "image": "laptop.jpg.avif"},
        {"name": "Mobile", "price": 20000, "image": "mobile.jpg.webp"},
        {"name": "Smart Watch", "price": 3000, "image": "watch.jpg.webp"}
    ]

    col1, col2, col3 = st.columns(3)

    for i, product in enumerate(products):

        with [col1, col2, col3][i]:

            st.image(product["image"], width=200)

            st.markdown(f"### {product['name']}")
            st.markdown(f" **₹{product['price']}**")

            if st.button(f"Add {product['name']}", key=i):

                st.session_state.cart.append(product)

                st.success(f"{product['name']} added to cart!")

# ----------- CART PAGE -----------

elif choice == "Cart":

    st.subheader(" Shopping Cart")

    if len(st.session_state.cart) == 0:

        st.warning("Cart is empty")

    else:

        total = 0

        for item in st.session_state.cart:

            st.write(
                f"{item['name']} — ₹{item['price']}"
            )

            total += item["price"]

        st.success(f"Total Amount: ₹{total}")

# ----------- CHECKOUT PAGE -----------

elif choice == "Checkout":

    st.subheader(" Checkout")

    if len(st.session_state.cart) == 0:

        st.warning("Your cart is empty!")

    else:

        name = st.text_input("Full Name")

        address = st.text_area("Delivery Address")

        payment = st.selectbox(
            "Payment Method",
            ["UPI", "Debit Card", "Credit Card", "Cash on Delivery"]
        )

        if st.button("Place Order"):

            st.success(" Order Placed Successfully!")

            st.session_state.cart = []

# ----------- PROFILE PAGE -----------

elif choice == "Profile":

    st.subheader(" User Profile")

    name = st.text_input("Name")

    email = st.text_input("Email")

    phone = st.text_input("Phone")

    if st.button("Update Profile"):

        st.success("Profile Updated Successfully")