import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from streamlit_extras.colored_header import colored_header
from streamlit_extras.metric_cards import style_metric_cards

# Set page configuration
st.set_page_config(page_title="Landsat Data Dashboard", layout="wide")

# Custom CSS for improved styling
st.markdown("""
<style>
    .stApp {
        background-color: #ffffff;
    }
    .stHeader {
        background-color: #b0b0b0;
        color: white;
        padding: 1rem;
        border-radius: 5px;
    }
    .stSubheader {
        color: #34495e;
        font-weight: bold;
    }
    .stSidebar {
        background-color: #f5f7fa;
        padding: 2rem;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
    }
    .stText {
        color: #2c3e50;
    }
</style>
""", unsafe_allow_html=True)

# Title and introduction
st.markdown('<div class="stHeader"><h1>Landsat Data in Agriculture and Water Management</h1></div>', unsafe_allow_html=True)
st.markdown('<p class="stText">This dashboard visualizes key insights from Landsat articles and other NASA sources on satellite data usage in agriculture and water management.</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("Dashboard Sections")
    sections = st.radio("Go to", ["OpenET and Evapotranspiration", "Satellite Programs", "Impact on Agriculture", "ARSET Training Programs", "Earth Observatory Insights"])

# Main content
if sections == "OpenET and Evapotranspiration":
    colored_header(label="OpenET and Evapotranspiration", description="Explore the accuracy and components of evapotranspiration", color_name="blue-70")

    # Evapotranspiration calculation accuracy
    st.subheader("OpenET Accuracy in Calculating Evapotranspiration")
    accuracy_data = pd.DataFrame({
        'Crop Type': ['Annual Crops', 'Perennial Crops', 'Natural Landscapes'],
        'Accuracy (%)': [90, 85, 80]
    })
    fig_accuracy = go.Figure(data=[go.Bar(x=accuracy_data['Crop Type'], y=accuracy_data['Accuracy (%)'],
                                          marker_color=['#3498db', '#2980b9', '#1abc9c'])])
    fig_accuracy.update_layout(title_text="OpenET Accuracy by Land Cover Type",
                               plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
                               font=dict(color='#2c3e50'))
    st.plotly_chart(fig_accuracy, use_container_width=True)

    # Evapotranspiration components
    st.subheader("Components of Evapotranspiration")
    labels = ['Evaporation', 'Transpiration']
    values = [40, 60]
    fig_et = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3,
                                    marker_colors=['#1e3f66', '#3e73a2'])])
    fig_et.update_layout(title_text="Typical Distribution of Evapotranspiration Components",
                         plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_et, use_container_width=True)

elif sections == "Satellite Programs":
    colored_header(label="Key Satellite Programs in Agriculture", description="Impact of various satellite programs on agricultural decision making", color_name="blue-70")

    programs = ['U.S. Drought Monitor', 'NASA Harvest', 'OpenET', 'Crop Condition and Soil Moisture Analytics']
    impact = [85, 90, 95, 80]

    fig_programs = go.Figure(data=[go.Bar(x=programs, y=impact,
                                          marker_color=['#1e3f66', '#2e5984', '#3e73a2', '#4e8dc0'])])
    fig_programs.update_layout(title_text="Impact of Satellite Programs on Agricultural Decision Making",
                               yaxis_title="Estimated Impact Score",
                               plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_programs, use_container_width=True)

    st.info("These programs utilize Landsat data to provide crucial information for agricultural management and water resource planning.")

elif sections == "Impact on Agriculture":
    colored_header(label="Impact of Satellite Data on Agriculture", description="Comparing traditional methods with satellite-aided approaches", color_name="blue-70")

    # Create a sample dataset
    years = list(range(2010, 2025))
    traditional = [100 + i*3 + np.random.randint(-5, 5) for i in range(len(years))]
    satellite_aided = [100 + i*5 + np.random.randint(-3, 7) for i in range(len(years))]

    fig_impact = go.Figure()
    fig_impact.add_trace(go.Scatter(x=years, y=traditional, mode='lines', name='Traditional Methods', line=dict(color='#1e3f66')))
    fig_impact.add_trace(go.Scatter(x=years, y=satellite_aided, mode='lines', name='Satellite-Aided Methods', line=dict(color='#3e73a2')))
    fig_impact.update_layout(title_text="Agricultural Productivity Over Time",
                             xaxis_title="Year",
                             yaxis_title="Productivity Index",
                             plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_impact, use_container_width=True)

    st.info("This graph illustrates the potential improvement in agricultural productivity when using satellite-aided methods compared to traditional approaches.")

    # New section for data correlation
    st.subheader("Correlation between Evapotranspiration Accuracy and Crop Types")

    # Sample data for correlation
    crop_types = ['Corn', 'Wheat', 'Soybeans', 'Cotton', 'Rice']
    et_accuracy = [92, 88, 90, 85, 87]
    water_usage = [25, 20, 22, 30, 35]

    fig_correlation = go.Figure(data=go.Scatter(
        x=et_accuracy,
        y=water_usage,
        mode='markers',
        marker=dict(size=10, color=et_accuracy, colorscale='Viridis', showscale=True),
        text=crop_types,
        hovertemplate='<b>%{text}</b><br>ET Accuracy: %{x}%<br>Water Usage: %{y} inches<extra></extra>'
    ))
    fig_correlation.update_layout(
        title='Evapotranspiration Accuracy vs Water Usage by Crop Type',
        xaxis_title='Evapotranspiration Accuracy (%)',
        yaxis_title='Water Usage (inches)',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig_correlation, use_container_width=True)

    st.info("This interactive scatter plot shows the relationship between evapotranspiration accuracy and water usage for different crop types. Hover over the points to see more details.")

elif sections == "ARSET Training Programs":
    colored_header(label="ARSET Training Programs for Agriculture", description="Overview of NASA's Applied Remote Sensing Training", color_name="blue-70")

    st.subheader("ARSET Agriculture Training Overview")
    st.write("ARSET provides online and in-person trainings on remote sensing in agriculture, ranging from introductory to advanced levels.")

    # Sample data for ARSET training programs
    training_data = pd.DataFrame({
        'Training Type': ['Introductory', 'Intermediate', 'Advanced'],
        'Participants': [500, 300, 200],
        'Satisfaction Rate (%)': [95, 92, 90]
    })

    fig_training = go.Figure(data=[
        go.Bar(name='Participants', x=training_data['Training Type'], y=training_data['Participants'], marker_color='#1e3f66'),
        go.Bar(name='Satisfaction Rate (%)', x=training_data['Training Type'], y=training_data['Satisfaction Rate (%)'], marker_color='#3e73a2')
    ])
    fig_training.update_layout(barmode='group', title_text="ARSET Agriculture Training Statistics",
                               plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_training, use_container_width=True)

    st.subheader("Key Resources")
    col1, col2 = st.columns(2)
    with col1:
        st.button("NASA Satellite Instruments for Agriculture (PDF)")
    with col2:
        st.button("Online resource guide for agriculture training (PDF)")

elif sections == "Earth Observatory Insights":
    colored_header(label="Earth Observatory Insights on Agriculture", description="Key findings from NASA's Earth Observatory", color_name="blue-70")

    st.subheader("Key Findings from Earth Observatory")
    st.write("1. Impact of agriculture on deforestation, especially in tropical regions")
    st.write("2. Patterns of agricultural land use in various regions (e.g., Great Plains, Nile Delta)")
    st.write("3. Use of satellite data in monitoring agricultural fires and their impacts")

    # Sample data for agricultural land use changes
    land_use_data = pd.DataFrame({
        'Year': [2000, 2005, 2010, 2015, 2020],
        'Forest Area': [100, 95, 90, 85, 80],
        'Agricultural Area': [50, 55, 60, 65, 70]
    })

    fig_land_use = go.Figure()
    fig_land_use.add_trace(go.Scatter(x=land_use_data['Year'], y=land_use_data['Forest Area'], mode='lines', name='Forest Area', line=dict(color='#1e3f66')))
    fig_land_use.add_trace(go.Scatter(x=land_use_data['Year'], y=land_use_data['Agricultural Area'], mode='lines', name='Agricultural Area', line=dict(color='#3e73a2')))
    fig_land_use.update_layout(title_text="Land Use Changes Over Time",
                               xaxis_title="Year",
                               yaxis_title="Area (relative units)",
                               plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_land_use, use_container_width=True)

    st.info("This graph illustrates the inverse relationship between forest area and agricultural land expansion over time.")

# Footer
st.markdown("---")
st.write("Data sources: NASA Landsat articles, ARSET, Earth Observatory, and simulated data for visualization purposes.")
