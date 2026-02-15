import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Global Warming Estimator 🌍", layout="wide")

# ---------------- CUSTOM STYLE ----------------
st.markdown("""
<style>
.stApp {
    background-color: #0b3d2e;
}

h1, h2, h3, p, label, div {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LIVE COUNTER ----------------
st.title("🌍 Global Warming Estimator")

counter_placeholder = st.empty()

if "climate_index" not in st.session_state:
    st.session_state.climate_index = 1.2

# Simulate slight realtime change
change = random.uniform(-0.002, 0.004)
st.session_state.climate_index += change

trend = "⬆ Increasing" if change > 0 else "⬇ Decreasing"

counter_placeholder.metric(
    "🌡️ Global Temperature Change Trend (°C above pre-industrial)",
    f"{st.session_state.climate_index:.3f} °C",
    f"{change:.4f} {trend}"
)

# ---------------- IMAGE / GIF ----------------
col_img1, col_img2 = st.columns(2)

with col_img1:
    st.image("https://images.unsplash.com/photo-1610878180933-12372899fa4d",
             caption="Melting Glaciers")

with col_img2:
    st.image("https://media.giphy.com/media/3o7TKsQ8UQ3IuZ8Jsk/giphy.gif")

# ---------------- USER INPUT ----------------
st.header("🧍 Your Lifestyle Habits")

col1, col2 = st.columns(2)

with col1:
    car_km = st.slider("🚗 Daily Car Travel (km)", 0, 100, 10)
    electricity = st.slider("⚡ Daily Electricity Usage (kWh)", 0, 50, 8)
    flights = st.slider("✈️ Flights Per Year", 0, 20, 1)

with col2:
    meat_meals = st.slider("🍖 Meat Meals Per Week", 0, 21, 7)
    waste = st.slider("🗑️ Waste Produced Per Day (kg)", 0.0, 5.0, 1.0)

# ---------------- EMISSION MODEL ----------------
car_emission = car_km * 0.192
electricity_emission = electricity * 0.475
flight_emission = flights * 255
meat_emission = meat_meals * 7 * 0.3
waste_emission = waste * 1.9

daily_emission = car_emission + electricity_emission + meat_emission + waste_emission
yearly_emission = (daily_emission * 365) + flight_emission

# ---------------- FOOTPRINT DISPLAY ----------------
st.header("🌡️ Your Carbon Footprint")

colA, colB, colC = st.columns(3)

colA.metric("Daily CO₂", f"{daily_emission:.2f} kg")
colB.metric("Yearly CO₂", f"{yearly_emission:.2f} kg")
colC.metric("Trees Needed to Offset", f"{yearly_emission/22:.0f}")

# ---------------- GLOBAL IMPACT ----------------
st.header("🌎 If Everyone Lived Like You")

world_population = 8_000_000_000
global_projection = yearly_emission * world_population / 1e12

st.metric("Projected Global CO₂ Emission", f"{global_projection:.2f} Gigatons/year")

# ---------------- IMPROVEMENTS ----------------
st.header("🌱 Choose Sustainable Changes")

changes = st.multiselect(
    "Select changes:",
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

# ---------------- SMALL GRAPH 1 ----------------
st.header("📊 Lifestyle Change Comparison")

comparison = pd.DataFrame({
    "Scenario": ["Current", "Improved"],
    "Yearly CO₂": [yearly_emission, new_yearly]
})

fig = plt.figure(figsize=(5,3))
plt.bar(comparison["Scenario"], comparison["Yearly CO₂"])
plt.ylabel("Yearly CO₂ (kg)")
plt.title("Emission Comparison")
st.pyplot(fig)

# ---------------- SMALL GRAPH 2 ----------------
st.header("⏳ 30-Year Climate Projection")

years = np.arange(1, 31)
current_projection = yearly_emission * years
improved_projection = new_yearly * years

fig2 = plt.figure(figsize=(5,3))
plt.plot(years, current_projection, label="Current")
plt.plot(years, improved_projection, label="Improved")
plt.xlabel("Years")
plt.ylabel("Total CO₂")
plt.legend()
st.pyplot(fig2)

# ---------------- REAL TIME ADVICE ----------------
st.header("💡 Climate Advice")

if yearly_emission > 5000:
    st.error("High footprint — reduce transport or electricity usage.")

elif yearly_emission > 2500:
    st.warning("Moderate footprint — small improvements recommended.")

else:
    st.success("Excellent sustainable lifestyle!")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("🌍 Small habits create global climate impact")
