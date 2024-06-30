import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the data
file_path = 'Athlete_events.xlsx'
df = pd.read_excel(file_path)

# Title of the app
st.title('Olympic Athletes Analysis')

# Sidebar for user input
st.sidebar.title("Filter Options")

# General filter for sport
sport = st.sidebar.selectbox('Select a Sport', df['Sport'].unique())

# Filter data based on the selected sport
filtered_data = df[df['Sport'] == sport]

# Age Distribution Filter
st.sidebar.header('Age Distribution Filter')
age_min, age_max = int(filtered_data['Age'].min()), int(filtered_data['Age'].max())
age_range = st.sidebar.slider('Select Age Range', age_min, age_max, (age_min, age_max))

# Filter data for Age Distribution
age_filtered_data = filtered_data[(filtered_data['Age'] >= age_range[0]) & (filtered_data['Age'] <= age_range[1])]

# Plotting - Age Distribution Histogram
st.header("Age Distribution of Athletes")
if not age_filtered_data.empty:
    fig, ax = plt.subplots()
    sns.histplot(age_filtered_data['Age'].dropna(), kde=True, ax=ax)
    ax.set_title(f'Age Distribution of Athletes in {sport}')
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)
else:
    st.warning(f"No data available for the selected age range in {sport}")

# Medal Distribution Filter
st.sidebar.header('Medal Distribution Filter')
medal_options = ['Gold', 'Silver', 'Bronze', 'No Medal']
selected_medals = st.sidebar.multiselect('Select Medals', medal_options, medal_options)

# Filter data for Medal Distribution
if 'No Medal' in selected_medals:
    medal_filtered_data = filtered_data[(filtered_data['Medal'].isna()) | (filtered_data['Medal'].isin(selected_medals))]
else:
    medal_filtered_data = filtered_data[filtered_data['Medal'].isin(selected_medals)]

# Plotting - Pie Chart for Medal Distribution
st.header("Medal Distribution")
if not medal_filtered_data['Medal'].dropna().empty:
    medal_counts = medal_filtered_data['Medal'].value_counts()
    fig_pie = px.pie(values=medal_counts.values, names=medal_counts.index, title=f'Medal Distribution in {sport}')
    st.plotly_chart(fig_pie)
else:
    st.warning(f"No medal data available for the selected medals in {sport}")

# Yearly Distribution Filter
st.sidebar.header('Yearly Distribution Filter')
year_min, year_max = int(filtered_data['Year'].min()), int(filtered_data['Year'].max())
year_range = st.sidebar.slider('Select Year Range', year_min, year_max, (year_min, year_max))

# Filter data for Yearly Distribution
year_filtered_data = filtered_data[(filtered_data['Year'] >= year_range[0]) & (filtered_data['Year'] <= year_range[1])]

# Plotting - Line Graph for Number of Athletes over the Years
st.header("Number of Athletes Over the Years")
if not year_filtered_data.empty:
    year_counts = year_filtered_data['Year'].value_counts().sort_index()
    fig_line = px.line(x=year_counts.index, y=year_counts.values, labels={'x': 'Year', 'y': 'Number of Athletes'}, title=f'Number of Athletes Over the Years in {sport}')
    st.plotly_chart(fig_line)
else:
    st.warning(f"No data available for the selected year range in {sport}")

