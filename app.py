import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Climate Impact Tracker 🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- ENHANCED CUSTOM STYLE ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Unbounded:wght@300;500;700&display=swap');

.stApp {
    background: linear-gradient(135deg, #0a1f1a 0%, #1a3a2e 50%, #0f2922 100%);
    font-family: 'Space Mono', monospace;
}

h1, h2, h3 {
    font-family: 'Unbounded', sans-serif !important;
    color: #00ff88 !important;
    text-shadow: 0 0 20px rgba(0, 255, 136, 0.3);
    animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
    from { text-shadow: 0 0 20px rgba(0, 255, 136, 0.3); }
    to { text-shadow: 0 0 30px rgba(0, 255, 136, 0.6); }
}

p, label, div {
    color: #e0ffe0 !important;
    font-weight: 400;
}

/* Slider styling */
.stSlider > div > div > div {
    background: linear-gradient(90deg, #00ff88, #00cc70) !important;
}

/* Metric cards */
[data-testid="stMetricValue"] {
    font-size: 2rem !important;
    color: #00ff88 !important;
    font-family: 'Unbounded', sans-serif !important;
}

/* Multiselect */
.stMultiSelect {
    background: rgba(0, 255, 136, 0.05);
    border-radius: 10px;
    padding: 10px;
}

/* Real-time pulse animation */
@keyframes pulse {
    0% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.8; transform: scale(1.02); }
    100% { opacity: 1; transform: scale(1); }
}

.pulse {
    animation: pulse 2s ease-in-out infinite;
}

/* Warning boxes */
.warning-box {
    background: rgba(255, 136, 0, 0.1);
    border-left: 4px solid #ff8800;
    padding: 15px;
    border-radius: 5px;
    margin: 10px 0;
}

.success-box {
    background: rgba(0, 255, 136, 0.1);
    border-left: 4px solid #00ff88;
    padding: 15px;
    border-radius: 5px;
    margin: 10px 0;
}

.danger-box {
    background: rgba(255, 68, 68, 0.1);
    border-left: 4px solid #ff4444;
    padding: 15px;
    border-radius: 5px;
    margin: 10px 0;
}

/* Live counter styling */
.live-counter {
    font-size: 3rem;
    font-weight: bold;
    color: #ff4444;
    font-family: 'Unbounded', sans-serif;
    text-align: center;
    animation: pulse 1s ease-in-out infinite;
}

/* Card styling */
.impact-card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(0, 255, 136, 0.2);
    border-radius: 15px;
    padding: 20px;
    margin: 10px 0;
    transition: all 0.3s ease;
}

.impact-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(0, 255, 136, 0.2);
    border-color: rgba(0, 255, 136, 0.5);
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE WITH ANIMATION ----------------
st.markdown("""
<div style="text-align: center; padding: 20px 0;">
    <h1 style="font-size: 3.5rem; margin-bottom: 10px;">🌍 CLIMATE IMPACT TRACKER</h1>
    <p style="font-size: 1.2rem; color: #00ff88;">Real-Time Personal Carbon Footprint Monitor</p>
</div>
""", unsafe_allow_html=True)

# ---------------- LIVE GLOBAL CO2 COUNTER ----------------
st.markdown("### 🔴 LIVE: Global CO₂ Emissions Right Now")

# Simulate real-time counter (35,000 metric tons per hour globally)
current_time = datetime.now()
seconds_since_midnight = (current_time.hour * 3600 + current_time.minute * 60 + current_time.second)
tons_per_second = 35000 / 3600  # ~9.7 tons per second
live_emissions = tons_per_second * seconds_since_midnight

col_live1, col_live2, col_live3 = st.columns(3)

with col_live1:
    st.markdown(f"""
    <div class="impact-card">
        <p style="text-align: center; font-size: 0.9rem; color: #888;">TODAY SO FAR</p>
        <div class="live-counter">{live_emissions:,.0f}</div>
        <p style="text-align: center; color: #ff4444;">metric tons of CO₂</p>
    </div>
    """, unsafe_allow_html=True)

with col_live2:
    st.markdown(f"""
    <div class="impact-card">
        <p style="text-align: center; font-size: 0.9rem; color: #888;">PER SECOND</p>
        <div class="live-counter" style="font-size: 2.5rem; color: #ff8800;">{tons_per_second:.1f}</div>
        <p style="text-align: center; color: #ff8800;">metric tons</p>
    </div>
    """, unsafe_allow_html=True)

with col_live3:
    trees_needed = live_emissions * 45  # One tree absorbs ~22kg per year
    st.markdown(f"""
    <div class="impact-card">
        <p style="text-align: center; font-size: 0.9rem; color: #888;">TREES NEEDED</p>
        <div class="live-counter" style="font-size: 2.5rem; color: #00ff88;">{trees_needed:,.0f}</div>
        <p style="text-align: center; color: #00ff88;">to offset today</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---------------- USER INPUT ----------------
st.markdown("## 🧍 YOUR DAILY LIFESTYLE")

col1, col2 = st.columns(2)

with col1:
    car_km = st.slider("🚗 Daily Car Travel (km)", 0, 100, 10, help="Average distance driven per day")
    electricity = st.slider("⚡ Electricity Usage (kWh/day)", 0, 50, 8, help="Your daily household electricity consumption")
    flights = st.slider("✈️ Flights Per Year", 0, 20, 1, help="Number of round-trip flights annually")

with col2:
    meat_meals = st.slider("🍖 Meat Meals Per Week", 0, 21, 7, help="How many meals with meat do you eat?")
    waste = st.slider("🗑️ Daily Waste (kg)", 0.0, 5.0, 1.0, 0.1, help="Waste you produce that goes to landfill")

# ---------------- REAL-TIME CALCULATIONS ----------------
# More accurate emission factors
car_emission = car_km * 0.192  # kg CO2 per km
electricity_emission = electricity * 0.475  # kg CO2 per kWh
flight_emission = flights * 255  # kg CO2 per flight
meat_emission = (meat_meals / 7) * 6.61  # kg CO2 per day from meat
waste_emission = waste * 1.9  # kg CO2 per kg waste

daily_emission = car_emission + electricity_emission + meat_emission + waste_emission
yearly_emission = (daily_emission * 365) + flight_emission

# Calculate per-second emissions
emission_per_second = daily_emission / 86400

# ---------------- REAL-TIME TICKER ----------------
st.markdown("### ⏱️ YOUR CARBON FOOTPRINT ACCUMULATING NOW")

ticker_placeholder = st.empty()

# Create a simulated real-time counter
start_time = time.time()
elapsed = time.time() - start_time
accumulated = emission_per_second * elapsed

ticker_placeholder.markdown(f"""
<div class="impact-card" style="background: rgba(255, 68, 68, 0.1);">
    <div style="text-align: center;">
        <p style="font-size: 1rem; color: #888;">EMISSIONS SINCE YOU OPENED THIS PAGE</p>
        <div style="font-size: 2.5rem; color: #ff4444; font-family: 'Unbounded', sans-serif;">
            {accumulated:.6f} kg CO₂
        </div>
        <p style="color: #ff8800; margin-top: 10px;">
            You emit ~{emission_per_second * 1000:.2f} grams per second
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- DISPLAY FOOTPRINT WITH GAUGES ----------------
st.markdown("## 🌡️ YOUR CARBON FOOTPRINT DASHBOARD")

# Create gauge chart for daily emissions
fig_gauge = go.Figure()

# Determine color based on emission level
if daily_emission < 10:
    gauge_color = "#00ff88"
    status = "Excellent"
elif daily_emission < 20:
    gauge_color = "#ffaa00"
    status = "Moderate"
else:
    gauge_color = "#ff4444"
    status = "High"

fig_gauge.add_trace(go.Indicator(
    mode = "gauge+number+delta",
    value = daily_emission,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Daily CO₂ Emissions (kg)", 'font': {'color': '#e0ffe0', 'size': 20}},
    delta = {'reference': 13.7, 'increasing': {'color': "#ff4444"}},
    gauge = {
        'axis': {'range': [None, 50], 'tickcolor': "#00ff88"},
        'bar': {'color': gauge_color},
        'bgcolor': "rgba(0,0,0,0)",
        'borderwidth': 2,
        'bordercolor': "#00ff88",
        'steps': [
            {'range': [0, 10], 'color': 'rgba(0, 255, 136, 0.2)'},
            {'range': [10, 20], 'color': 'rgba(255, 170, 0, 0.2)'},
            {'range': [20, 50], 'color': 'rgba(255, 68, 68, 0.2)'}
        ],
        'threshold': {
            'line': {'color': "#ff4444", 'width': 4},
            'thickness': 0.75,
            'value': 13.7
        }
    }
))

fig_gauge.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font={'color': '#e0ffe0', 'family': 'Space Mono'},
    height=300
)

col_gauge1, col_gauge2 = st.columns([1, 1])

with col_gauge1:
    st.plotly_chart(fig_gauge, use_container_width=True)

with col_gauge2:
    st.markdown(f"""
    <div class="impact-card">
        <h3 style="color: {gauge_color}; margin-bottom: 20px;">STATUS: {status.upper()}</h3>
        <div style="margin: 15px 0;">
            <p style="font-size: 0.9rem; color: #888;">DAILY EMISSIONS</p>
            <p style="font-size: 2rem; color: #00ff88; font-family: 'Unbounded', sans-serif;">{daily_emission:.2f} kg</p>
        </div>
        <div style="margin: 15px 0;">
            <p style="font-size: 0.9rem; color: #888;">YEARLY TOTAL</p>
            <p style="font-size: 2rem; color: #ff8800; font-family: 'Unbounded', sans-serif;">{yearly_emission:.2f} kg</p>
        </div>
        <div style="margin: 15px 0;">
            <p style="font-size: 0.9rem; color: #888;">TREES TO OFFSET</p>
            <p style="font-size: 2rem; color: #ff4444; font-family: 'Unbounded', sans-serif;">{yearly_emission / 22:.0f} 🌳</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- BREAKDOWN PIE CHART ----------------
st.markdown("### 📊 EMISSION SOURCES BREAKDOWN")

breakdown_data = pd.DataFrame({
    'Source': ['🚗 Transport', '⚡ Electricity', '✈️ Flights', '🍖 Food', '🗑️ Waste'],
    'Emissions': [car_emission * 365, electricity_emission * 365, flight_emission, meat_emission * 365, waste_emission * 365]
})

fig_pie = px.pie(
    breakdown_data,
    values='Emissions',
    names='Source',
    title='Your Carbon Footprint by Category',
    hole=0.4,
    color_discrete_sequence=['#00ff88', '#00cc70', '#ffaa00', '#ff8800', '#ff4444']
)

fig_pie.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font={'color': '#e0ffe0', 'family': 'Space Mono', 'size': 12},
    title={'font': {'color': '#00ff88', 'size': 20}}
)

st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("---")

# ---------------- GLOBAL IMPACT ----------------
st.markdown("## 🌎 IF EVERYONE LIVED LIKE YOU")

world_population = 8_000_000_000
global_projection = yearly_emission * world_population / 1e12

col_global1, col_global2, col_global3 = st.columns(3)

with col_global1:
    st.markdown(f"""
    <div class="impact-card">
        <p style="text-align: center; color: #888;">GLOBAL EMISSIONS</p>
        <p style="text-align: center; font-size: 2.5rem; color: #ff4444; font-family: 'Unbounded', sans-serif;">
            {global_projection:.2f}
        </p>
        <p style="text-align: center; color: #ff4444;">Gigatons CO₂/year</p>
    </div>
    """, unsafe_allow_html=True)

with col_global2:
    current_global = 37.0  # Current global emissions in Gt
    difference = ((global_projection - current_global) / current_global) * 100
    st.markdown(f"""
    <div class="impact-card">
        <p style="text-align: center; color: #888;">VS CURRENT REALITY</p>
        <p style="text-align: center; font-size: 2.5rem; color: {'#ff4444' if difference > 0 else '#00ff88'}; font-family: 'Unbounded', sans-serif;">
            {difference:+.1f}%
        </p>
        <p style="text-align: center; color: #ff8800;">Difference from 37 Gt/year</p>
    </div>
    """, unsafe_allow_html=True)

with col_global3:
    paris_target = 1.5  # 1.5°C target requires ~25 Gt by 2030
    st.markdown(f"""
    <div class="impact-card">
        <p style="text-align: center; color: #888;">PARIS AGREEMENT</p>
        <p style="text-align: center; font-size: 2.5rem; color: {'#ff4444' if global_projection > 25 else '#00ff88'}; font-family: 'Unbounded', sans-serif;">
            {'❌' if global_projection > 25 else '✅'}
        </p>
        <p style="text-align: center; color: #ff8800;">Target: <25 Gt by 2030</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---------------- IMPROVEMENT OPTIONS ----------------
st.markdown("## 🌱 SUSTAINABLE LIFESTYLE CHANGES")

changes = st.multiselect(
    "Select habits you're willing to change:",
    [
        "🚌 Switch to Public Transport (50% reduction)",
        "🥗 Reduce Meat Consumption (60% reduction)",
        "☀️ Use Renewable Energy (70% reduction)",
        "♻️ Minimize Waste Production (50% reduction)",
        "🏝️ Limit Air Travel (50% reduction)"
    ],
    help="See how different lifestyle changes impact your footprint"
)

reduction = 0
reduction_breakdown = {}

if "🚌 Switch to Public Transport (50% reduction)" in changes:
    reduction_breakdown['Transport'] = car_emission * 0.5 * 365
    reduction += car_emission * 0.5

if "🥗 Reduce Meat Consumption (60% reduction)" in changes:
    reduction_breakdown['Food'] = meat_emission * 0.6 * 365
    reduction += meat_emission * 0.6

if "☀️ Use Renewable Energy (70% reduction)" in changes:
    reduction_breakdown['Electricity'] = electricity_emission * 0.7 * 365
    reduction += electricity_emission * 0.7

if "♻️ Minimize Waste Production (50% reduction)" in changes:
    reduction_breakdown['Waste'] = waste_emission * 0.5 * 365
    reduction += waste_emission * 0.5

if "🏝️ Limit Air Travel (50% reduction)" in changes:
    reduction_breakdown['Flights'] = flight_emission * 0.5
    reduction += flight_emission * 0.5 / 365

new_daily = daily_emission - reduction
new_yearly = new_daily * 365

# ---------------- COMPARISON CHARTS ----------------
st.markdown("### 📈 IMPACT OF YOUR CHANGES")

# Create before/after comparison
comparison_data = pd.DataFrame({
    'Scenario': ['Current', 'Improved'],
    'Daily': [daily_emission, new_daily],
    'Yearly': [yearly_emission, new_yearly]
})

fig_comparison = go.Figure()

fig_comparison.add_trace(go.Bar(
    name='Current Lifestyle',
    x=['Daily Emissions', 'Yearly Emissions'],
    y=[daily_emission, yearly_emission],
    marker_color='#ff4444',
    text=[f'{daily_emission:.1f} kg', f'{yearly_emission:.0f} kg'],
    textposition='auto',
))

fig_comparison.add_trace(go.Bar(
    name='Improved Lifestyle',
    x=['Daily Emissions', 'Yearly Emissions'],
    y=[new_daily, new_yearly],
    marker_color='#00ff88',
    text=[f'{new_daily:.1f} kg', f'{new_yearly:.0f} kg'],
    textposition='auto',
))

fig_comparison.update_layout(
    title='Before & After Comparison',
    barmode='group',
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font={'color': '#e0ffe0', 'family': 'Space Mono'},
    title_font={'color': '#00ff88', 'size': 20}
)

st.plotly_chart(fig_comparison, use_container_width=True)

# Show savings
if reduction > 0:
    savings_yearly = reduction * 365
    trees_saved = savings_yearly / 22
    st.markdown(f"""
    <div class="success-box">
        <h3 style="color: #00ff88;">🎉 CONGRATULATIONS ON YOUR COMMITMENT!</h3>
        <p style="font-size: 1.1rem;">
            By making these changes, you'll save <strong>{savings_yearly:.0f} kg of CO₂</strong> per year!
        </p>
        <p style="font-size: 1.1rem;">
            That's equivalent to planting <strong>{trees_saved:.0f} trees</strong> 🌳
        </p>
        <p style="font-size: 1.1rem;">
            Or taking <strong>{savings_yearly/2300:.1f} cars</strong> off the road for a year! 🚗
        </p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- 30-YEAR PROJECTION ----------------
st.markdown("### ⏳ 30-YEAR CLIMATE IMPACT PROJECTION")

years = np.arange(1, 31)
current_cumulative = yearly_emission * years / 1000  # Convert to metric tons
improved_cumulative = new_yearly * years / 1000

fig_timeline = go.Figure()

fig_timeline.add_trace(go.Scatter(
    x=years,
    y=current_cumulative,
    mode='lines',
    name='Current Lifestyle',
    line=dict(color='#ff4444', width=3),
    fill='tozeroy',
    fillcolor='rgba(255, 68, 68, 0.2)'
))

fig_timeline.add_trace(go.Scatter(
    x=years,
    y=improved_cumulative,
    mode='lines',
    name='Improved Lifestyle',
    line=dict(color='#00ff88', width=3),
    fill='tozeroy',
    fillcolor='rgba(0, 255, 136, 0.2)'
))

fig_timeline.update_layout(
    title='Cumulative CO₂ Emissions Over 30 Years',
    xaxis_title='Years',
    yaxis_title='Total CO₂ (metric tons)',
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font={'color': '#e0ffe0', 'family': 'Space Mono'},
    title_font={'color': '#00ff88', 'size': 20},
    hovermode='x unified'
)

st.plotly_chart(fig_timeline, use_container_width=True)

st.markdown("---")

# ---------------- PERSONALIZED ADVICE ----------------
st.markdown("## 💡 PERSONALIZED CLIMATE RECOMMENDATIONS")

# Determine biggest contributor
contributors = {
    '🚗 Transport': car_emission * 365,
    '⚡ Electricity': electricity_emission * 365,
    '✈️ Flights': flight_emission,
    '🍖 Food': meat_emission * 365,
    '🗑️ Waste': waste_emission * 365
}

biggest = max(contributors, key=contributors.get)
biggest_value = contributors[biggest]

col_advice1, col_advice2 = st.columns([2, 1])

with col_advice1:
    if yearly_emission > 10000:
        st.markdown(f"""
        <div class="danger-box">
            <h3>⚠️ HIGH CARBON FOOTPRINT ALERT</h3>
            <p>Your yearly emissions of <strong>{yearly_emission:.0f} kg</strong> are significantly above the global sustainable target of ~2,500 kg per person.</p>
            <p><strong>Top Priority:</strong> Your {biggest} contributes <strong>{biggest_value:.0f} kg/year</strong> - focus here first!</p>
        </div>
        """, unsafe_allow_html=True)
    elif yearly_emission > 5000:
        st.markdown(f"""
        <div class="warning-box">
            <h3>⚡ MODERATE IMPACT</h3>
            <p>You're at <strong>{yearly_emission:.0f} kg/year</strong>. You're doing better than average, but there's room for improvement.</p>
            <p><strong>Focus Area:</strong> {biggest} accounts for {biggest_value/yearly_emission*100:.0f}% of your footprint.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="success-box">
            <h3>✅ EXCELLENT CLIMATE STEWARD!</h3>
            <p>Your <strong>{yearly_emission:.0f} kg/year</strong> footprint is well below the sustainable target. You're part of the solution!</p>
            <p>Keep up the great work and inspire others to follow your example! 🌟</p>
        </div>
        """, unsafe_allow_html=True)

with col_advice2:
    # Quick wins based on their data
    st.markdown("### ⚡ QUICK WINS")
    
    quick_wins = []
    if car_km > 20:
        quick_wins.append("🚲 Try biking for trips <5km")
    if electricity > 15:
        quick_wins.append("💡 Switch to LED bulbs")
    if meat_meals > 14:
        quick_wins.append("🥗 Try Meatless Mondays")
    if waste > 2:
        quick_wins.append("♻️ Start composting")
    if flights > 2:
        quick_wins.append("💻 Consider virtual meetings")
    
    if not quick_wins:
        quick_wins = ["✨ You're already doing great!", "📚 Share your knowledge", "🌱 Plant trees"]
    
    for win in quick_wins[:3]:
        st.markdown(f"- {win}")

st.markdown("---")

# ---------------- EDUCATIONAL INSIGHTS ----------------
st.markdown("## 📚 CLIMATE SCIENCE FACTS")

col_facts1, col_facts2, col_facts3 = st.columns(3)

with col_facts1:
    st.markdown("""
    <div class="impact-card">
        <h4 style="color: #00ff88;">🌡️ Temperature Rise</h4>
        <p>Global temperatures have risen <strong>1.1°C</strong> since pre-industrial times.</p>
        <p style="font-size: 0.8rem; color: #888; margin-top: 10px;">We must limit this to 1.5°C to avoid catastrophic effects.</p>
    </div>
    """, unsafe_allow_html=True)

with col_facts2:
    st.markdown("""
    <div class="impact-card">
        <h4 style="color: #ff8800;">🏭 Emission Sources</h4>
        <p><strong>25%</strong> from transport<br>
        <strong>25%</strong> from electricity<br>
        <strong>24%</strong> from agriculture</p>
        <p style="font-size: 0.8rem; color: #888; margin-top: 10px;">Individual actions compound into massive change.</p>
    </div>
    """, unsafe_allow_html=True)

with col_facts3:
    st.markdown("""
    <div class="impact-card">
        <h4 style="color: #ff4444;">⏰ Time Remaining</h4>
        <p>We have until <strong>~2030</strong> to cut emissions by 45% to stay below 1.5°C.</p>
        <p style="font-size: 0.8rem; color: #888; margin-top: 10px;">Every year, month, and day counts.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---------------- FOOTER ----------------
st.markdown("""
<div style="text-align: center; padding: 30px 0; border-top: 1px solid rgba(0, 255, 136, 0.2);">
    <p style="font-size: 1.2rem; color: #00ff88; font-family: 'Unbounded', sans-serif;">
        🌍 EVERY ACTION COUNTS. START TODAY.
    </p>
    <p style="font-size: 0.9rem; color: #888; margin-top: 10px;">
        Data updates in real-time based on your inputs. Share this tool to amplify the impact!
    </p>
</div>
""", unsafe_allow_html=True)
