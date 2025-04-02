import streamlit as st
import pickle
import numpy as np
import time

# Load model
data = pickle.load(open('bhp_model.pkl', 'rb'))
lr_clf = data['model']
columns = data['columns']

def set_bg():
    bg_style = f"""
    <style>
   
    
    /* Make text bolder */
    .stMarkdown, .stTextInput, .stNumberInput, .stSelectbox, .stButton > button {{
        font-weight: bold !important;
    
    .green-bar {{
        background-color: #28a745; /* Green solid bar */
        color: white;
        padding: 15px;
        border-radius: 10px;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        margin-top: 15px;
    }}
    </style>
    """
    st.markdown(bg_style, unsafe_allow_html=True)

# Call function to set background and styling
set_bg()


# Streamlit UI components
st.markdown(
    """
    <h1 style="text-align: center; font-size: 50px;">🏡Bengaluru Home Price Prediction</h1>
    <p style="text-align: center; font-size: 20px;"></p>
    """,
    unsafe_allow_html=True
)
st.markdown("<p style='font-weight: bold; font-size: 20px;'>Enter details below to estimate the house price.</p>", unsafe_allow_html=True)

# User Inputs
sqft = st.number_input("**📏Enter area in square feet**", min_value=1000, step=100)
bhk = st.number_input("**🛏️Enter number of bedrooms**", min_value=1, step=1)
bath = st.number_input("**🛁Enter number of bathrooms**", min_value=1, step=1)
location = st.selectbox("**📍Select location**", columns[3:])

# Price Prediction Function
def predict_price(location, sqft, bath, bhk):
    x = np.zeros(len(columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    
    if location in columns:
        loc_index = columns.index(location)
        x[loc_index] = 1
    
    return lr_clf.predict([x])[0]   # Convert to Lakhs

# Estimate Button
st.markdown('<div class="blue-btn">', unsafe_allow_html=True)
if st.button("🚀 **Estimate Price**"):
    with st.spinner("🔄 Calculating price... Please wait!"):
        time.sleep(1)  # Simulate processing time

    # Display progress bar animation
    progress_bar = st.progress(0)
    for percent in range(1, 101):
        time.sleep(0.01)  # Simulate loading
        progress_bar.progress(percent)
    price = predict_price(location, sqft, bath, bhk)
    st.markdown(f'<div class="green-bar">🏠 Estimated House Price: ₹{price:,.2f} Lakhs</div>', unsafe_allow_html=True)



    

    
