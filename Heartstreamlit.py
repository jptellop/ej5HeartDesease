# writefile app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide") # Optional: to use a wide layout by default

st.title('Heart Disease Data Analysis Dashboard')

st.write('---')
st.header('1. Data Overview')

# Load the dataset
df = pd.read_csv('heart.csv')

st.subheader('Raw Data (First 5 rows)')
st.dataframe(df.head())

st.subheader('Descriptive Statistics')
st.dataframe(df.describe())

######
st.write('---')
st.header('2. Correlation Matrix')

# Define numerical columns
numerical_cols = ['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak', 'HeartDisease']
numerical_df = df[numerical_cols]

# Calculate correlation matrix
correlation_matrix = numerical_df.corr()

# Plotting the heatmap
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
ax.set_title('Correlation Matrix of Numerical Features')
st.pyplot(fig)
#####

st.write('---')
st.header('4. Key Insights and Summary')

st.markdown("""
Based on the analysis, here are the key insights and relationships observed:

### Important Variables and their Implications:

*   **FastingBS (Fasting Blood Sugar)**: Shows a strong positive correlation with `HeartDisease` (0.26). This implies that higher fasting blood sugar levels are associated with a significantly increased likelihood of heart disease.

*   **Oldpeak (ST depression induced by exercise relative to rest)**: Exhibits a positive correlation of 0.38 with `HeartDisease`. This indicates that a greater ST depression during exercise is linked to a higher risk of heart disease.

*   **MaxHR (Maximum Heart Rate Achieved)**: Has a notable negative correlation of -0.40 with `HeartDisease`. This suggests that a lower maximum heart rate during exercise is associated with an increased risk of heart disease.

*   **Sex**: The count plot reveals that males in the dataset tend to have a higher incidence of heart disease compared to females.

*   **Age**: While having a moderate positive correlation with `HeartDisease` (0.28), age is a fundamental risk factor, and its distribution helps understand the demographic context of the dataset.

These findings suggest that a combination of metabolic indicators (FastingBS), cardiovascular stress response (Oldpeak, MaxHR), and demographic factors (Sex, Age) are crucial in assessing and understanding heart disease risk.
""")


