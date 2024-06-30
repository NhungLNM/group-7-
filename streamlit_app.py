import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px  # Import plotly express

# Load the data
file_path = 'Athlete_events.xlsx'
df = pd.read_excel(file_path)

# Title of the app
st.title('Olympic Athletes Analysis')

# Sidebar for user input
sport = st.sidebar.selectbox('Select a Sport', df['Sport'].unique())

# Filter data based on the selected sport
filtered_data = df[df['Sport'] == sport]

# Plotting - Age Distribution Histogram
if not filtered_data.empty:
    fig, ax = plt.subplots()
    sns.histplot(filtered_data['Age'].dropna(), kde=True, ax=ax)
    ax.set_title(f'Age Distribution of Athletes in {sport}')
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')

    # Display the plot
    st.pyplot(fig)
else:
    st.warning(f"No data available for {sport}")

# Plotting - Pie Chart for Medal Distribution
st.header("Medal Distribution")
if not filtered_data['Medal'].dropna().empty:
    medal_counts = filtered_data['Medal'].value_counts()
    fig_pie = px.pie(values=medal_counts.values, names=medal_counts.index, title=f'Medal Distribution in {sport}')
    st.plotly_chart(fig_pie)
else:
    st.warning(f"No medal data available for {sport}")

# Plotting - Line Graph for Number of Athletes over the Years
st.header("Number of Athletes Over the Years")
year_counts = filtered_data['Year'].value_counts().sort_index()
fig_line = px.line(x=year_counts.index, y=year_counts.values, labels={'x':'Year', 'y':'Number of Athletes'}, title=f'Number of Athletes Over the Years in {sport} from {country}')
st.plotly_chart(fig_line)
