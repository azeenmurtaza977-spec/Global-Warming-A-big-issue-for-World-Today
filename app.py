import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="🌍 Global Warming Impact Simulator",
    page_icon="🌡️",
    layout="wide"
)

# -------------------------
# Title Section
# -------------------------
st.title("🌍 Global Warming Daily Impact Simulator")
st.subheader("How small daily climate changes reshape the planet")

st.markdown("""
🔥 Even a **1% daily environmental impact** can compound into massive global change.  
Use this app to simulate and understand the statistical and real-world effects.
""")

# -------------------------
# Sidebar Controls
# -------------------------
st.sidebar.header("⚙️ Simulation Controls")

daily_effect = st.sidebar.slider(
    "🌡️ Daily Environmental Impact (%)",
    0.1, 5.0, 1.0, 0.1
)

years = st.sidebar.slider(
    "📅 Years to Simulate",
    1, 100, 30
)

# Convert years to days
days = years * 365

# -------------------------
# Load Image + GIF
# -------------------------
st.image(
    "https://images.unsplash.com/photo-1470114716159-e389f8712fda",
    caption="🌎 Earth Climate Changes"
)

st.markdown("### ❄️ Melting Ice Evidence")
st.image(
    "https://media.giphy.com/media/3o7TKsQ8UQ3IuZ8Jsk/giphy.gif"
)

# -------------------------
# Statistical Simulation
# -------------------------
initial_value = 100
growth_rate = daily_effect / 100

values = []

for day in range(days):
    new_value = initial_value * ((1 + growth_rate) ** day)
    values.append(new_value)

df = pd.DataFrame({
    "Days": range(days),
    "Climate Impact Index": values
})

# -------------------------
# Chart 1 – Compounding Impact
# -------------------------
st.header("📊 Compounding Climate Impact Over Time")

fig1 = plt.figure()
plt.plot(df["Days"], df["Climate Impact Index"])
plt.xlabel("Days")
plt.ylabel("Impact Index")
plt.title("Compounding Effect of Daily Climate Change")
st.pyplot(fig1)

# -------------------------
# Chart 2 – Temperature Simulation
# -------------------------
st.header("🌡️ Simulated Global Temperature Rise")

base_temp = 14  # Approx global average temp
temp_rise = np.log(df["Climate Impact Index"]) * 0.5
temperature = base_temp + temp_rise

fig2 = plt.figure()
plt.plot(df["Days"], temperature)
plt.xlabel("Days")
plt.ylabel("Average Global Temperature (°C)")
plt.title("Projected Temperature Increase")
st.pyplot(fig2)

# -------------------------
# Statistical Insights
# -------------------------
st.header("📈 Statistical Insights")

col1, col2, col3 = st.columns(3)

col1.metric(
    "🔥 Total Impact Growth",
    f"{values[-1]:.2f}"
)

col2.metric(
    "🌡️ Final Temperature",
    f"{temperature.iloc[-1]:.2f} °C"
)

col3.metric(
    "📅 Simulation Period",
    f"{years} Years"
)

# -------------------------
# Explanation Section
# -------------------------
st.markdown("""
## 📚 Why This Matters

✔ Climate change effects are **non-linear**  
✔ Small daily environmental damage compounds exponentially  
✔ Temperature increase accelerates ice melt, sea level rise, and biodiversity loss  

### 🧮 Statistical Concept Used
- Exponential Growth Model
- Logarithmic Temperature Scaling
""")

# -------------------------
# User Awareness Section
# -------------------------
st.header("🌱 What Can Individuals Do?")

actions = st.multiselect(
    "Select sustainable actions:",
    [
        "🚲 Use Public Transport",
        "🌳 Plant Trees",
        "⚡ Reduce Electricity Usage",
        "🥗 Reduce Food Waste",
        "♻️ Recycling"
    ]
)

if actions:
    st.success("Great! Small actions collectively reduce global warming.")

# -------------------------
# Footer
# -------------------------
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
