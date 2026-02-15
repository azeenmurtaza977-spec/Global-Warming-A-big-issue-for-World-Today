import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Personal Climate Impact 🌍", layout="wide")

# ---------------- CUSTOM STYLE ----------------
st.markdown("""
<style>
.stApp {
    background-color: #0b3d2e;
}

h1, h2, h3, p, label, div {
    color: black !important;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🌍 Personal Climate Impact & Improvement Tracker")
st.markdown("### Understand how your daily habits influence global warming")

# ---------------- USER INPUT ----------------
st.header("🧍 Your Daily Lifestyle Habits")

col1, col2 = st.columns(2)

with col1:
    car_km = st.slider("🚗 Daily Car Travel (km)", 0, 100, 10)
    electricity = st.slider("⚡ Daily Electricity Usage (kWh)", 0, 50, 8)
    flights = st.slider("✈️ Flights Per Year", 0, 20, 1)

with col2:
    meat_meals = st.slider("🍖 Meat Meals Per Week", 0, 21, 7)
    waste = st.slider("🗑️ Waste Produced Per Day (kg)", 0.0, 5.0, 1.0)

# ---------------- SCIENTIFIC APPROX EMISSIONS ----------------
# Approximate emission factors (accepted climate averages)

car_emission = car_km * 0.192  # kg CO2 per km
electricity_emission = electricity * 0.475
flight_emission = flights * 255
meat_emission = meat_meals * 7 * 0.3
waste_emission = waste * 1.9

daily_emission = car_emission + electricity_emission + meat_emission + waste_emission
yearly_emission = (daily_emission * 365) + flight_emission

# ---------------- DISPLAY FOOTPRINT ----------------
st.header("🌡️ Your Estimated Carbon Footprint")

colA, colB, colC = st.columns(3)

colA.metric("Daily CO₂ Emission", f"{daily_emission:.2f} kg")
colB.metric("Yearly CO₂ Emission", f"{yearly_emission:.2f} kg")
colC.metric("Equivalent Trees Needed", f"{yearly_emission / 22:.0f} Trees")

# ---------------- GLOBAL IMPACT SIMULATION ----------------
st.header("🌎 If Everyone Lived Like You")

world_population = 8_000_000_000
global_projection = yearly_emission * world_population / 1e12  # gigatons

st.metric(
    "Projected Global CO₂ Emission",
    f"{global_projection:.2f} Gigatons/year"
)

# ---------------- IMPROVEMENT OPTIONS ----------------
st.header("🌱 Choose Sustainable Changes")

changes = st.multiselect(
    "Select habits you are willing to change:",
    [
        "Use Public Transport",
        "Reduce Meat Consumption",
        "Use Renewable Energy",
        "Reduce Waste",
        "Limit Flights"
    ]
)

reduction = 0

if "Use Public Transport" in changes:
    reduction += car_emission * 0.5

if "Reduce Meat Consumption" in changes:
    reduction += meat_emission * 0.6

if "Use Renewable Energy" in changes:
    reduction += electricity_emission * 0.7

if "Reduce Waste" in changes:
    reduction += waste_emission * 0.5

if "Limit Flights" in changes:
    reduction += flight_emission * 0.5 / 365

new_daily = daily_emission - reduction
new_yearly = new_daily * 365

# ---------------- COMPARISON ----------------
st.header("📊 Impact of Your Lifestyle Changes")

comparison = pd.DataFrame({
    "Scenario": ["Current Lifestyle", "Improved Lifestyle"],
    "Yearly CO₂": [yearly_emission, new_yearly]
})

fig = plt.figure()
plt.bar(comparison["Scenario"], comparison["Yearly CO₂"])
plt.ylabel("Yearly CO₂ Emission (kg)")
plt.title("Impact of Lifestyle Changes")
st.pyplot(fig)

# ---------------- LONG TERM EFFECT ----------------
st.header("⏳ Long-Term Climate Influence")

years = np.arange(1, 31)
current_projection = yearly_emission * years
improved_projection = new_yearly * years

fig2 = plt.figure()
plt.plot(years, current_projection, label="Current Lifestyle")
plt.plot(years, improved_projection, label="Improved Lifestyle")
plt.xlabel("Years")
plt.ylabel("Total CO₂ Emission")
plt.legend()
plt.title("30-Year Climate Impact Projection")
st.pyplot(fig2)

# ---------------- EDUCATIONAL INSIGHT ----------------
st.header("📚 Why Individual Actions Matter")

st.markdown("""
• Transportation contributes nearly **25% of global emissions**  
• Meat production significantly increases methane release  
• Electricity from fossil fuels accelerates global warming  
• Waste increases landfill methane emissions  

Small individual changes collectively produce massive climate improvements.
""")

# ---------------- REAL-TIME TIPS ----------------
st.header("💡 Personalized Climate Advice")

if yearly_emission > 5000:
    st.error("Your carbon footprint is above global sustainable average. Consider reducing travel or energy usage.")

elif yearly_emission > 2500:
    st.warning("You are close to sustainable range. Small improvements can help.")

else:
    st.success("Excellent! Your lifestyle supports climate sustainability.")

st.markdown("---")
st.markdown("🌍 Protecting Earth starts with individual responsibility")

