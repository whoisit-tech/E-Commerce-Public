import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import requests
import zipfile
import io
import os

# Page configuration
st.set_page_config(page_title="E-Commerce Data Analysis", layout="wide")
st.title("E-Commerce Data Analysis Dashboard")
st.write("### By Vilosa Auliya Dewinta Sentanu | ochadwnta@gmail.com")

# Sidebar
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["Home", "Data Overview", "EDA & Insights", "Business Questions"])

# Data loading and processing
@st.cache_data
def load_data():
    try:
        # Data URL
        url = "https://github.com/whoisit-tech/E-Commerce-Public/raw/main/archive%20(2).zip"
        response = requests.get(url)
        zip_file = zipfile.ZipFile(io.BytesIO(response.content))

        # Extract files
        os.makedirs("ecommerce_data", exist_ok=True)
        zip_file.extractall("ecommerce_data")
        data_folder = "ecommerce_data"
        
        # Load datasets
        orders = pd.read_csv(os.path.join(data_folder, "olist_orders_dataset.csv"))
        order_items = pd.read_csv(os.path.join(data_folder, "olist_order_items_dataset.csv"))
        products = pd.read_csv(os.path.join(data_folder, "olist_products_dataset.csv"))
        order_payments = pd.read_csv(os.path.join(data_folder, "olist_order_payments_dataset.csv"))
        customers = pd.read_csv(os.path.join(data_folder, "olist_customers_dataset.csv"))
        return orders, order_items, products, order_payments, customers
    except Exception as e:
        st.error(f"Error loading the data: {e}")
        return None, None, None, None, None

orders, order_items, products, order_payments, customers = load_data()

if orders is not None:
    # Process Data
    orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
    orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
    orders['shipping_time'] = (orders['order_delivered_customer_date'] - orders['order_purchase_timestamp']).dt.days

    three_months_ago = datetime.now() - timedelta(days=90)
    recent_orders = orders[orders['order_purchase_timestamp'] >= three_months_ago]
else:
    st.stop()

# Define functions for business questions
def top_products(order_items, products):
    top_products_df = order_items.groupby('product_id').agg({
        'order_item_id': 'count', 
        'price': 'sum'
    }).reset_index()
    top_products_df.rename(columns={'order_item_id': 'sales_count'}, inplace=True)
    top_products_df = top_products_df.merge(products, on='product_id')
    total_revenue = top_products_df['price'].sum()
    top_products_df['revenue_contribution'] = (top_products_df['price'] / total_revenue) * 100
    return top_products_df.nlargest(10, 'sales_count')

def avg_shipping_time_by_category(orders, order_items, products):
    merged = orders.merge(order_items, on='order_id').merge(products, on='product_id')
    return merged.groupby('product_category_name')['shipping_time'].mean().sort_values()

def most_used_payment(order_payments):
    avg_payment_value = order_payments['payment_value'].mean()
    filtered_payments = order_payments[order_payments['payment_value'] > avg_payment_value]
    return filtered_payments['payment_type'].value_counts()

# Render pages
if options == "Home":
    st.header("Welcome to the E-Commerce Analysis Dashboard")
    st.markdown("""This dashboard provides insights into e-commerce data, helping businesses make informed decisions. Use the navigation panel to explore data or answer key business questions.""")
    st.image("https://source.unsplash.com/featured/?ecommerce", use_column_width=True)

elif options == "Data Overview":
    st.header("Data Overview")
    st.subheader("Orders Dataset")
    st.dataframe(orders.head())
    st.write("### Orders Info")
    st.text(orders.info())

    st.subheader("Order Items Dataset")
    st.dataframe(order_items.head())

    st.subheader("Products Dataset")
    st.dataframe(products.head())

elif options == "EDA & Insights":
    st.header("Exploratory Data Analysis")
    st.subheader("Monthly Order Distribution")
    orders['order_purchase_month'] = orders['order_purchase_timestamp'].dt.to_period('M')
    monthly_orders = orders.groupby('order_purchase_month').size()
    fig, ax = plt.subplots(figsize=(10, 5))
    monthly_orders.plot(kind='bar', color='skyblue', ax=ax)
    plt.title("Monthly Order Distribution", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Order Count", fontsize=12)
    st.pyplot(fig)

    st.subheader("Payment Method Distribution")
    payment_methods = order_payments['payment_type'].
