import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = 'Athlete_events.xlsx'
df = pd.read_excel(file_path)

# Title of the app
st.title('Olympic Athletes Analysis')

# Sidebar for user input
sport = st.sidebar.selectbox('Select a Sport', df['Sport'].unique())

# Filter data based on the selected sport
filtered_data = df[df['Sport'] == sport]

# Plotting
fig, ax = plt.subplots()
sns.histplot(filtered_data['Age'].dropna(), kde=True, ax=ax)
ax.set_title(f'Age Distribution of Athletes in {sport}')
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')

# Plotting - Pie Chart for Medal Distribution
st.header("Medal Distribution")
medal_counts = filtered_data['Medal'].value_counts()
fig_pie = px.pie(values=medal_counts.values, names=medal_counts.index, title=f'Medal Distribution in {sport} from {country}')
st.plotly_chart(fig_pie)

# Display the plot
st.pyplot(fig)
