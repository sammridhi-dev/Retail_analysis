import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


st.title("Data Visualization Dashboard")


df = pd.read_csv("cleaned_data.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

# Ensure InvoiceDate is datetime
#df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# ---------------- BAR CHART ----------------
st.subheader("Bar Chart: Count by Description")

description_counts = df['Description'].value_counts().head(20)  # top 20 for clarity

fig, ax = plt.subplots()
description_counts.plot(kind='bar', ax=ax)
ax.set_title("Count of Records by Description")
ax.set_xlabel("Description")
ax.set_ylabel("Number of Records")
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

st.write(
    "Insight: This bar chart shows the frequency of records for the top 20 products. "
    "Higher bars indicate products with more sales activity."
)

# ---------------- LINE CHART ----------------
st.subheader("Line Chart: Revenue Trend Over Time")

df_sorted = df.sort_values('InvoiceDate')
fig, ax = plt.subplots()
ax.plot(df_sorted['InvoiceDate'], df_sorted['Revenue'])
ax.set_title("Revenue Trend Over Time")
ax.set_xlabel("Date")
ax.set_ylabel("Revenue")
st.pyplot(fig)

st.write(
    "Insight: The line chart represents revenue trends over time, helping identify growth, "
    "decline, or seasonal patterns."
)

# ---------------- BOX PLOT ----------------
st.subheader("Boxplot: Revenue Distribution")

fig, ax = plt.subplots()
ax.boxplot(df['Revenue'], vert=False)
ax.set_title("Boxplot of Revenue")
ax.set_xlabel("Revenue")
st.pyplot(fig)

st.write(
    "Insight: The boxplot summarizes revenue distribution, highlighting the median, "
    "spread, and presence of outliers."
)

# ---------------- HISTOGRAM ----------------
st.subheader("Histogram: Revenue Frequency Distribution")

fig, ax = plt.subplots()
ax.hist(df['Revenue'], bins=10)
ax.set_title("Histogram of Revenue")
ax.set_xlabel("Revenue")
ax.set_ylabel("Frequency")
st.pyplot(fig)

st.write(
    "Insight: The histogram shows how revenue values are distributed across different ranges, "
    "indicating data skewness and concentration."
)

# ---------------- PARETO CHART ----------------
st.subheader("Pareto Chart: Revenue by Description")

pareto_data = df.groupby('Description')['Revenue'].sum().sort_values(ascending=False).head(20)  # top 20
cumulative_percentage = pareto_data.cumsum() / pareto_data.sum() * 100

fig, ax = plt.subplots()
pareto_data.plot(kind='bar', ax=ax)
ax.set_ylabel("Total Revenue")
ax2 = ax.twinx()
ax2.plot(cumulative_percentage.values, color='red', marker='o', linestyle='-')
ax2.set_ylabel("Cumulative %")
plt.xticks(rotation=45, ha='right')
ax.set_title("Pareto Chart of Revenue by Description")
st.pyplot(fig)

st.write(
    "Insight: The Pareto chart shows that a small number of products contribute "
    "to a large portion of total revenue, illustrating the 80/20 principle."
)
