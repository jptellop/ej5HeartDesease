import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('heart.csv')
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Sex', y='Cholesterol', hue='Sex', palette={'M': 'skyblue', 'F': 'lightcoral'}, legend=False)
plt.title('Distribución de Colesterol por Sexo')
plt.xlabel('Sexo')
plt.ylabel('Colesterol')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

numerical_df = df[['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak', 'HeartDisease']]
correlation_matrix = numerical_df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Numerical Features')
plt.show()

fig, axes = plt.subplots(3, 2, figsize=(16, 18))

# Plot 1: Histogram for Age
sns.histplot(df['Age'], kde=True, ax=axes[0, 0], color='skyblue')
axes[0, 0].set_title('Distribution of Age')
axes[0, 0].set_xlabel('Age')
axes[0, 0].set_ylabel('Count')

# Plot 2: Histogram for Cholesterol
sns.histplot(df['Cholesterol'], kde=True, ax=axes[0, 1], color='lightcoral')
axes[0, 1].set_title('Distribution of Cholesterol')
axes[0, 1].set_xlabel('Cholesterol')
axes[0, 1].set_ylabel('Count')

# Plot 3: Count Plot for Sex with HeartDisease hue
sns.countplot(data=df, x='Sex', hue='HeartDisease', palette='viridis', ax=axes[1, 0])
axes[1, 0].set_title('Heart Disease Distribution by Sex')
axes[1, 0].set_xlabel('Sex')
axes[1, 0].set_ylabel('Count')

# Plot 4: Histogram for RestingBP
sns.histplot(df['RestingBP'], kde=True, ax=axes[1, 1], color='lightgreen')
axes[1, 1].set_title('Distribution of Resting Blood Pressure')
axes[1, 1].set_xlabel('RestingBP')
axes[1, 1].set_ylabel('Count')

# Plot 5: Histogram for MaxHR
sns.histplot(df['MaxHR'], kde=True, ax=axes[2, 0], color='gold')
axes[2, 0].set_title('Distribution of Maximum Heart Rate')
axes[2, 0].set_xlabel('MaxHR')
axes[2, 0].set_ylabel('Count')

# Plot 6: Count Plot for HeartDisease
sns.countplot(data=df, x='HeartDisease', hue='HeartDisease', palette='coolwarm', ax=axes[2, 1], legend=False)
axes[2, 1].set_title('Heart Disease Outcome Count')
axes[2, 1].set_xlabel('HeartDisease (0: No, 1: Yes)')
axes[2, 1].set_ylabel('Count')

plt.tight_layout()
plt.show()
