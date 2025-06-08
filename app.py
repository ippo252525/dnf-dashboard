import streamlit as st
import pandas as pd
import plotly.express as px

# CSV 로드
df = pd.read_csv("data/sample.csv")

st.title("Plotly 그래프 예제")

# 데이터 표
st.subheader("Raw Data")
st.dataframe(df)

# 선 그래프
st.subheader("Line Chart (Plotly)")
fig_line = px.line(df, y="value", title="Line Chart")
st.plotly_chart(fig_line)

# 바 그래프
st.subheader("Bar Chart (Plotly)")
fig_bar = px.bar(df, y="value", title="Bar Chart")
st.plotly_chart(fig_bar)