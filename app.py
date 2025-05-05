import streamlit as st
from modules.fetch_data import generate_mock_data, save_to_csv
from modules.analyze_data import load_job_data, get_top_skills, get_jobs_by_location, get_jobs_over_time
from modules.visualize import plot_bar_chart, plot_time_series

# -------------------------------
# Streamlit App Configuration
# -------------------------------
st.set_page_config(page_title="Job Market Analyzer", layout="wide")

st.title("📊 Job Market Analyzer")
st.write("This app analyzes mock job listings to show trends in skills, locations, and posting times.")

# -------------------------------
# Data Generation Button
# -------------------------------
if st.button("🔄 Regenerate Mock Data"):
    # Generate new job data and save to CSV
    df = generate_mock_data()
    save_to_csv(df)
    st.success("Mock job data regenerated!")

# Load existing job data
df = load_job_data()

# -------------------------------
# Raw Data Viewer (Expandable)
# -------------------------------
with st.expander("📄 View Raw Job Data"):
    st.dataframe(df)

# -------------------------------
# Top Skills Visualization
# -------------------------------
st.subheader("🔥 Top Skills in Demand")
top_skills = get_top_skills(df)
fig1 = plot_bar_chart(
    top_skills, 
    x_col="Skill", 
    y_col="Count", 
    title="Top Skills", 
    xlabel="Skill", 
    ylabel="Count"
)
st.pyplot(fig1)

# -------------------------------
# Job Locations Visualization
# -------------------------------
st.subheader("📍 Job Postings by Location")
locations = get_jobs_by_location(df)
fig2 = plot_bar_chart(
    locations, 
    x_col="Location", 
    y_col="Count", 
    title="Jobs by Location", 
    xlabel="Location", 
    ylabel="Count"
)
st.pyplot(fig2)

# -------------------------------
# Time Series Trend Visualization
# -------------------------------
st.subheader("📅 Job Postings Over Time")
trend_df = get_jobs_over_time(df, freq="W")  # Weekly trend
fig3 = plot_time_series(
    trend_df, 
    x_col="Date Posted", 
    y_col="Job Count", 
    title="Job Posting Trend (Weekly)", 
    xlabel="Date", 
    ylabel="Job Count"
)
st.pyplot(fig3)

# -------------------------------
# Footer Note
# -------------------------------
st.caption("📁 This project uses mock data and is designed as a portfolio showcase.")
