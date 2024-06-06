import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
print("openpyxl is installed correctly")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May'],
    'Value': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)

# Title of the app
st.title('Line Graph and Bar Chart Example')

# Line chart
st.subheader('Line Chart')
fig, ax = plt.subplots()
ax.plot(df['Month'], df['Value'], marker='o')
ax.set_xlabel('Month')
ax.set_ylabel('Value')
st.pyplot(fig)

# Bar chart
st.subheader('Bar Chart')
fig, ax = plt.subplots()
ax.bar(df['Month'], df['Value'])
ax.set_xlabel('Month')
ax.set_ylabel('Value')
st.pyplot(fig)
import streamlit as st