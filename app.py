import streamlit as st
import pandas as pd
import xgboost as xgb
import joblib
import numpy as np

# ── Page config ──
st.set_page_config(
    page_title="Nairobi House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# ── Load model & metadata (cached) ──
@st.cache_resource
def load_model_and_info():
    data = joblib.load("model.pkl") 
    return (
        data['model'],           
        data['features'],        
        data['mae']             
    )

model, trained_features, mae = load_model_and_info()

# ── App title & description ──
st.title("🏠 Nairobi House Price Predictor")
st.markdown("""
This tool estimates apartment/house prices in Nairobi using an  trained on real estate data.  
Enter the details below to get a prediction.
""")

# ── Input section ──
st.subheader("Property Details")

col1, col2 = st.columns(2)

with col1:
    location = st.selectbox(
        "Location",
        options=["Kilimani", "Westlands", "Karen", "Runda", "Other"],
        index=0
    )
    bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3, step=1)
    bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2, step=1)

with col2:
    size_sqft = st.number_input("Size (sqft)", min_value=200, max_value=20000, value=1500, step=50)
    amenities_count = st.number_input("Number of Nearby Amenities", min_value=0, max_value=20, value=4, step=1)

# ── Prepare input exactly like training data ──
input_dict = {
    "size_sqft": size_sqft,
    "Amenities_count": amenities_count,   
    "Bedrooms": bedrooms,
    "Bathrooms": bathrooms,
}

# All location categories your model was trained on
possible_locations = [
    'donholm', 'embakasi', 'gigiri', 'industrial area', 'karen', 'kasarani',
    'kiambu road', 'kileleshwa', 'kilimani', 'kitisuru', 'langata', 'lavington',
    'loresho', 'mirema', 'parklands', 'rhapta road', 'riruta', 'riverside',
    'runda', 'south c', 'spring valley', 'syokimau', 'upper hill', 'uthiru',
    'westlands'
]

# Set the selected location to 1, all others to 0
selected_loc_lower = location.lower()
for loc in possible_locations:
    # Using lower() to handle possible case differences
    input_dict[f"Location_{loc}"] = 1 if selected_loc_lower == loc.lower() else 0



# Create DataFrame
input_df = pd.DataFrame([input_dict])

# Reorder columns to match exactly what the model expects
try:
    input_df = input_df[trained_features]
except KeyError as e:
    st.error("Column mismatch between app and model.")
    st.write("Missing columns:", str(e))
    st.stop()

# ── Make prediction ──
if st.button("Predict Price", type="primary"):
    try:
        dmatrix = xgb.DMatrix(input_df)
        prediction = model.predict(dmatrix)[0]
        
        
        prediction = max(prediction, 0)
        
        low = prediction - mae
        high = prediction + mae
        
        st.success("Prediction Complete!")
        
        st.metric(
            label="Estimated Price (KES)",
            value=f"{prediction:,.0f}",
            delta=None
        )
        
        st.markdown(f"**Realistic range** : **{low:,.0f} – {high:,.0f} KES**")
    except Exception as e:
        st.error("Error during prediction.")
        st.write(str(e))   


        
    
