import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os

DB_HOST = os.getenv('DATABASE_HOST', 'localhost')
DB_USER = os.getenv('DATABASE_USER', 'postgres')
DB_PASS = os.getenv('DATABASE_PASSWORD', 'postgres')
DB_NAME = os.getenv('DATABASE_NAME', 'ecommerce')

engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}')

st.title('E-Commerce Sales Dashboard (Portfolio)')

@st.cache_data
def load_summary():
    query = 'SELECT * FROM analytics.mart_sales_summary ORDER BY order_date;'
    try:
        df = pd.read_sql(query, engine)
    except Exception as e:
        st.error(f'Error querying database: {e}')
        return pd.DataFrame()
    return df

df = load_summary()

if df.empty:
    st.info('No transformed data found yet. Run the ETL DAG in Airflow to generate analytics.mart_sales_summary.')
else:
    st.subheader('Daily Revenue')
    df['order_date'] = pd.to_datetime(df['order_date'])
    st.line_chart(df.set_index('order_date')['total_revenue'])

    st.subheader('Daily Items Sold')
    st.bar_chart(df.set_index('order_date')['total_items'])

    st.write('Data table:')
    st.dataframe(df)
