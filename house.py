import streamlit as st
import pandas as pd
import joblib
import random

# Page Config
st.set_page_config(page_title='🏡 House Price Predictor', layout='centered')

# Load Model
with open('models/house_pred.pkl', 'rb') as file:
    model = joblib.load(file)

# -------------------------------
# Background Styling (with gradient mask)
# -------------------------------
bg_url = "https://images.unsplash.com/photo-1600585154340-be6161a56a0c"
page_bg_style = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background: linear-gradient(rgba(255,255,255,0.7), rgba(240,240,240,0.9)), 
                url("{bg_url}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    color: black;
}}

html, body, [class*="css"] {{
    color: black !important;
    font-family: 'Segoe UI', sans-serif;
}}

.stButton > button {{
    background-color: #e50914 !important;
    color: white !important;
    border: none;
    padding: 10px 20px;
    border-radius: 10px;
    font-size: 16px;
    font-weight: bold;
}}

h1, h2, h3, h4, h5, h6, label, .stTextInput > label {{
    color: black !important;
}}

input, select, textarea {{
    background-color: #ffffffaa !important;
    color: black !important;
}}
</style>
"""


st.markdown(page_bg_style, unsafe_allow_html=True)

# -------------------------------
# Title Section
# -------------------------------
st.markdown("<h1 style='text-align: center;'>🏠 HomeValueIQ</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>Estimate the value of your dream home with ease</h5>", unsafe_allow_html=True)
st.markdown("---")

# -------------------------------
# Input Form
# -------------------------------
st.markdown("<h4 style='text-align: center;'>📝 Enter House Details</h4>", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")
with col1:
    area = st.selectbox("📏 Area (sq ft)", list(range(500, 100001)), index=2000)
    bedrooms = st.selectbox("🛏️ Bedrooms", list(range(1, 11)), index=2)
    stories = st.selectbox("🏢 Stories", list(range(1, 5)), index=1)

with col2:
    bathrooms = st.selectbox("🚿 Bathrooms", list(range(1, 11)), index=1)
    parking = st.selectbox("🚗 Parking Spots", list(range(0, 6)), index=1)
    furnishingstatus = st.selectbox("🪑 Furnishing Status", ["furnished", "semi-furnished", "unfurnished"])

st.markdown("---")
st.markdown("<h3 style='text-align: center;'>🧰 Extra Amenities</h3>", unsafe_allow_html=True)

colA, colB, colC = st.columns(3, gap="large")
with colA:
    mainroad = st.radio("🛣️ Main Road", ["yes", "no"], horizontal=True)
    guestroom = st.radio("🛋️ Guest Room", ["yes", "no"], horizontal=True)

with colB:
    basement = st.radio("🏚️ Basement", ["yes", "no"], horizontal=True)
    hotwaterheating = st.radio("🔥 Hot Water Heating", ["yes", "no"], horizontal=True)

with colC:
    airconditioning = st.radio("❄️ Air Conditioning", ["yes", "no"], horizontal=True)
    prefarea = st.radio("🌆 Preferred Area", ["yes", "no"], horizontal=True)

# -------------------------------
# Prepare Data
# -------------------------------
columns = ['area', 'bedrooms', 'bathrooms', 'stories',
           'mainroad', 'guestroom', 'basement', 'hotwaterheating',
           'airconditioning', 'parking', 'prefarea', 'furnishingstatus']

input_data = [[area, bedrooms, bathrooms, stories,
               mainroad, guestroom, basement, hotwaterheating,
               airconditioning, parking, prefarea, furnishingstatus]]

features_df = pd.DataFrame(input_data, columns=columns)

# -------------------------------
# Prediction Button
# -------------------------------
col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    predict_btn = st.button("🔮 Predict House Price", use_container_width=True)

# -------------------------------
# Prediction Result
# -------------------------------
if predict_btn:
    try:
        prediction = model.predict(features_df)
        formatted_price = f"₹{prediction[0]:,.2f}"
        st.markdown(f"""
            <div style='text-align: center; margin-top: 2rem; padding: 2rem; background-color: rgba(255, 255, 255, 0.8); border-radius: 12px;'>
                <h2 style='color:#e50914;'>💰 Estimated House Price</h2>
                <h1 style='font-size: 40px; color: black;'>🏷️ {formatted_price}</h1>
                <p>🔍 Based on your input and our trained ML model.</p>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("### ✨ Ready to Take the Next Step?")
        st.markdown("*For real-world accuracy, it's always great to check with a local property advisor — prices can vary slightly!*")



        
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")

# -------------------------------
# Sidebar Greeting 



# Sidebar - Interactive + Useful
st.sidebar.markdown("## 👋 Welcome, Home Explorer!")
st.sidebar.markdown("Get ready to discover your home's worth — fast, smart, and beautifully!")

# Mood check
mood = st.sidebar.radio("How are you feeling today?", ["😊 Great", "😐 Okay", "😟 Stressed"])
if mood == "😊 Great":
    st.sidebar.success("Awesome! Let's get you a great estimate 💸")
elif mood == "😐 Okay":
    st.sidebar.info("We'll try to brighten your day with accurate insights!")
else:
    st.sidebar.warning("Hang in there, your dream home is just a click away 🏡")

# Fun tip / fact of the day
house_facts = [
    "🏠 Fun Fact: Homes with south-facing windows are valued higher!",
    "📊 Did you know? Location can impact pricing by up to 30%.",
    "💡 Tip: Properties near schools sell 12% faster.",
    "🌿 A green view can boost your home's worth by ₹5–10L!",
    "🚪 Smart security features add resale value."
]
st.sidebar.markdown("### 🏡 House Tip of the Day")
st.sidebar.info(random.choice(house_facts))
st.sidebar.markdown("### 🤖 Ask HouseBot")
user_question = st.sidebar.selectbox(
    "Have a question?",
    (
        "💡 How does the model predict prices?",
        "🏗️ What features affect house price most?",
        "🔧 How can I improve my home's value?",
        "📍 Is location more important than size?",
        "📉 Why is my prediction low?",
        "❓ None of these – just exploring!"
    )
)

# Dynamic chatbot-like response
faq_responses = {
    "💡 How does the model predict prices?":
        "Our ML model uses past housing data — size, location, amenities — to estimate value using pattern recognition.",
    "🏗️ What features affect house price most?":
        "Usually: Area (sqft), location, furnishing, and bathrooms. Nearby amenities also matter!",
    "🔧 How can I improve my home's value?":
        "Adding bathrooms, furnishing, or upgrading kitchen/tiles often boosts price 🔼.",
    "📍 Is location more important than size?":
        "Both matter! A smaller flat in a premium area might be worth more than a big one in outskirts.",
    "📉 Why is my prediction low?":
        "Try increasing area, bathrooms, or selecting better amenities. Also, furnishing status plays a role.",
    "❓ None of these – just exploring!":
        "That’s cool 😎. Play around with the inputs and see how price responds!"
}

st.sidebar.info(f"💬 {faq_responses[user_question]}")

