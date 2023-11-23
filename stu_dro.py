import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Student Dropout Analytics", page_icon="📊")  

# Load data 
@st.cache
@st.cache
def load_data():
    df = pd.read_csv("DOR.csv")

    df["Primary_Total"] = pd.to_numeric(df["Primary_Total"], errors="coerce")
    df["Upper Primary_Total"] = pd.to_numeric(df["Upper Primary_Total"], errors="coerce")
    df["Secondary _Total"] = pd.to_numeric(df["Secondary _Total"], errors="coerce")  
    df["HrSecondary_Total"] = pd.to_numeric(df["HrSecondary_Total"], errors="coerce")

    return df

df = load_data()

# Page title
st.title("Student Dropout Analytics")  
st.header("Right to education is a key concern. Dropout rates are high due to poverty and socio-economic reasons.")
st.markdown("Analyzing dropouts across categories can help design focused interventions.")

# Selectboxes  
state = st.selectbox("Select State", df["State_UT"].unique())  
gender = st.selectbox("Select Gender", ["Boys", "Girls", "Total"])
school_type = st.selectbox("Select School Type", ["Primary", "Upper Primary", "Secondary", "HrSecondary"])

# Filter data
filtered_df = df[(df["State_UT"]==state) & (df["Primary_Boys"].notnull())]
filtered_df = df[(df["State_UT"]==state) & (df["Primary_Girls"].notnull())]
filtered_df = df[(df["State_UT"]==state) & (df["Upper Primary_Boys"].notnull())]
filtered_df = df[(df["State_UT"]==state) & (df["Upper Primary_Girls"].notnull())]
filtered_df = df[(df["State_UT"]==state) & (df["Secondary _Boys"].notnull())]
filtered_df = df[(df["State_UT"]==state) & (df["Secondary _Boys"].notnull())]
chart_df = filtered_df[["State_UT", "year", school_type+"_Total"]]

# Metrics
dropout_rate = chart_df[school_type+"_Total"].mean()  
st.metric("Average Dropout Rate (%)", dropout_rate)

# Chart 
st.header("Dropout Rate Over Time")
fig_line = px.line(chart_df, x="year", y=school_type+"_Total")  
st.plotly_chart(fig_line, use_container_width=True)

# Analysis by state
if st.checkbox("Show State-wise Analysis"):
    state_df = df.groupby("State_UT")[["Primary_Total", "Upper Primary_Total", "Secondary _Total", "HrSecondary_Total"]].mean().sort_values("Secondary _Total", ascending=False)  
    st.dataframe(state_df)

# Conclusion
st.header("Conclusions & Recommendations")
st.markdown("""
- High secondary school dropout rates need urgent focus, followed by secondary school
- Large inter-state variations exist, targeted state-specific plans needed  
- Data on dropouts by social segments needed for further analysis
- Counseling for girl students in vulnerable locations 
- Financial support, transport facilities & residential schools in remote regions
""")