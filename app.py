import streamlit as st

# 🌾 Title and subtitle
st.title("🌾 SmartAgri Agentic AI")
st.write("Your AI-powered farming assistant 🚜")

# 🧩 Input fields
crop = st.text_input("Enter Crop Name (e.g., Rice, Wheat, Maize):")
soil = st.text_input("Enter Soil Type (e.g., Loamy, Clay, Sandy):")

# 🧠 AI Recommendation Logic
def get_recommendation(crop, soil):
    crop = crop.lower()
    soil = soil.lower()

    # Sample knowledge base (you can expand this)
    recommendations = {
        "rice": {
            "loamy": "Use 100kg N, 50kg P, 50kg K per acre. Keep field flooded during early growth.",
            "clay": "Ensure proper drainage. Apply 80kg N, 40kg P, 40kg K per acre.",
            "sandy": "Use organic manure and maintain moisture regularly."
        },
        "wheat": {
            "loamy": "Apply 120kg N, 60kg P, 40kg K per acre. Irrigate at tillering and grain filling stages.",
            "clay": "Add gypsum for soil conditioning. Use balanced fertilizer.",
            "sandy": "Increase irrigation frequency, add compost for soil retention."
        },
        "maize": {
            "loamy": "Apply 150kg N, 60kg P, 60kg K per acre. Maintain consistent watering.",
            "clay": "Ensure aeration and drainage, reduce nitrogen slightly.",
            "sandy": "Apply frequent irrigation and add organic mulch."
        }
    }

    # Find matching advice
    if crop in recommendations and soil in recommendations[crop]:
        return recommendations[crop][soil]
    else:
        return "No data found for this combination. Try another crop or soil type."

# 🚀 Button to get result
if st.button("Get Recommendation"):
    if crop and soil:
        result = get_recommendation(crop, soil)
        st.success(result)
    else:
        st.warning("Please enter both crop name and soil type.")
