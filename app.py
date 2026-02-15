import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Global Warming Simulator 🌍", layout="wide")

# -------------------- DARK GREEN BACKGROUND --------------------
st.markdown("""
<style>
.stApp {
    background-color: #0b3d2e;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# -------------------- TITLE --------------------
st.title("🌍 Global Warming Impact & Earth Survival Simulator")
st.markdown("### Small daily temperature increases can drastically change Earth's future 🌡️")

# -------------------- USER INPUT --------------------
st.header("🔧 Adjust Global Warming Growth Rate")

daily_percent = st.slider(
    "Select Daily Global Warming Increase (%)",
    0.1, 5.0, 1.0, 0.1
)

years = st.slider(
    "Select Time Duration (Years)",
    10, 150, 50
)

# -------------------- SIMULATION --------------------
days = years * 365
growth_rate = daily_percent / 100

initial_index = 100
values = []

for day in range(days):
    new_val = initial_index * ((1 + growth_rate) ** day)
    values.append(new_val)

df = pd.DataFrame({
    "Day": range(days),
    "Climate Index": values
})

# -------------------- EARTH LIFE MODEL --------------------
# Assuming Earth critical collapse index
collapse_threshold = 100000000  

life_left_days = next(
    (i for i, v in enumerate(values) if v >= collapse_threshold),
    days
)

life_left_years = life_left_days / 365

# -------------------- EARTH LIFE DISPLAY --------------------
st.header("⏳ Estimated Life Sustainability on Earth")

col1, col2 = st.columns(2)

col1.metric(
    "🌡️ Daily Increase Selected",
    f"{daily_percent}%"
)

if life_left_days == days:
    col2.success("🌱 Earth survives beyond selected timeframe")
else:
    col2.error(f"⚠️ Estimated Sustainable Life Left: {life_left_years:.1f} Years")

# -------------------- GRAPH SELECTION --------------------
st.header("📊 Select Visualization")

graph_option = st.radio(
    "Choose Graph Type",
    ["Climate Growth", "Temperature Rise", "Earth Survival Countdown"]
)

# -------------------- GRAPH 1 --------------------
if graph_option == "Climate Growth":

    fig = plt.figure()
    plt.plot(df["Day"], df["Climate Index"])
    plt.xlabel("Days")
    plt.ylabel("Climate Impact Index")
    plt.title("Compounding Global Warming Effect")

    st.pyplot(fig)

# -------------------- GRAPH 2 --------------------
elif graph_option == "Temperature Rise":

    base_temp = 14
    temperature = base_temp + np.log(df["Climate Index"]) * 0.5

    fig = plt.figure()
    plt.plot(df["Day"], temperature)
    plt.xlabel("Days")
    plt.ylabel("Average Temperature (°C)")
    plt.title("Projected Global Temperature Rise")

    st.pyplot(fig)

# -------------------- GRAPH 3 --------------------
elif graph_option == "Earth Survival Countdown":

    progress = st.progress(0)
    status = st.empty()

    for i in range(100):
        progress.progress(i + 1)
        status.write("🌎 Simulating Earth Condition...")
        time.sleep(0.01)

    remaining_percent = max(0, 100 - (life_left_days / days) * 100)

    st.subheader("🌍 Earth Stability Level")
    st.metric("Remaining Stability (%)", f"{remaining_percent:.2f}")

# -------------------- IMAGE + GIF --------------------
st.header("🧊 Real Evidence of Climate Change")

st.image("https://images.unsplash.com/photo-1610878180933-12372899fa4d")

st.image("https://media.giphy.com/media/l0HlPwMAzh13pcZ20/giphy.gif")

# -------------------- EDUCATIONAL SECTION --------------------
st.header("📚 Statistical Perspective")

st.markdown("""
✔ Climate damage follows **exponential growth**  
✔ Temperature response is **logarithmic scaling**  
✔ Small environmental changes compound drastically over time  

This simulation uses statistical modelling to demonstrate potential long-term planetary impact.
""")

# -------------------- FOOTER --------------------
st.markdown("---")
st.markdown("🌱 Every small action today affects tomorrow")

