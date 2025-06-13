import ssl
import streamlit as st
import pandas as pd
import plotly.express as px
import psycopg2

# PSQL Connection
conn = psycopg2.connect(
    host=st.secrets["DB_HOST"],
    port=st.secrets["DB_PORT"],
    dbname=st.secrets["DB_NAME"],
    user=st.secrets["DB_USER"],
    password=st.secrets["DB_PASSWORD"]
)
query = "SELECT * FROM mv_fame_distribution_1k;"
df = pd.read_sql(query, conn)

st.title("PSQL Test Dashboard")

# 선 그래프
st.subheader("Line Chart (Plotly)")
fig = px.bar(
    df,
    x="fame_bin",
    y="count",
    title="명성 1000단위 분포",
    labels={"fame_bin": "명성 구간", "count": "캐릭터 수"},
)
st.plotly_chart(fig)