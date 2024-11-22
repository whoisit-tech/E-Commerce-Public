import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set up page configuration
st.set_page_config(page_title="E-Commerce Data Analysis", layout="wide")
st.title("E-Commerce Data Analysis Dashboard")
st.write("### By Vilosa Auliya Dewinta Sentanu | ochadwnta@gmail.com")

# Data loading (modify with your own data loading code if necessary)
@st.cache_data
def load_data():
    # Assuming data is already loaded into DataFrame variables like `orders`, `order_payments`, `products`, etc.
    # Example:
    # orders = pd.read_csv("orders.csv")
    # order_items = pd.read_csv("order_items.csv")
    # products = pd.read_csv("products.csv")
    # order_payments = pd.read_csv("order_payments.csv")
    pass

# Assuming data is loaded
# orders, order_payments, products = load_data()

# Exploratory Data Analysis (EDA) - Visualizations
st.header("Exploratory Data Analysis (EDA)")

# 1.1 Monthly Orders Distribution
orders['order_purchase_month'] = pd.to_datetime(orders['order_purchase_timestamp']).dt.to_period('M')
monthly_orders = orders.groupby('order_purchase_month').size()

st.subheader("Distribusi Pesanan per Bulan")
fig, ax = plt.subplots(figsize=(10, 5))
monthly_orders.plot(kind='bar', color='skyblue', ax=ax)
plt.title('Distribusi Pesanan per Bulan', fontsize=14)
plt.xlabel('Bulan', fontsize=12)
plt.ylabel('Jumlah Pesanan', fontsize=12)
plt.xticks(rotation=45)
st.pyplot(fig)

# 1.2 Payment Method Distribution
payment_methods = order_payments.groupby('payment_type').size().reset_index(name='count')

st.subheader("Distribusi Metode Pembayaran")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=payment_methods, x='payment_type', y='count', palette='muted', ax=ax)
plt.title('Distribusi Metode Pembayaran', fontsize=14)
plt.xlabel('Metode Pembayaran', fontsize=12)
plt.ylabel('Jumlah Penggunaan', fontsize=12)
st.pyplot(fig)

# 1.3 Shipping Time Distribution
orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
orders['shipping_time'] = (orders['order_delivered_customer_date'] - pd.to_datetime(orders['order_purchase_timestamp'])).dt.days

st.subheader("Distribusi Waktu Pengiriman")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(orders['shipping_time'].dropna(), bins=30, kde=True, color='green', ax=ax)
plt.title('Distribusi Waktu Pengiriman', fontsize=14)
plt.xlabel('Waktu Pengiriman (hari)', fontsize=12)
plt.ylabel('Frekuensi', fontsize=12)
st.pyplot(fig)

# Business Insights & Questions

st.header("Business Questions Insights")

# Question 1: Top Products by Sales in Last 3 Months
top_products = order_items.groupby('product_id').agg({
    'order_item_id': 'count',
    'price': 'sum'
}).reset_index()
top_products.rename(columns={'order_item_id': 'sales_count'}, inplace=True)
top_products = top_products.merge(products, on='product_id')

# Calculate revenue contribution
total_revenue = top_products['price'].sum()
top_products['revenue_contribution'] = (top_products['price'] / total_revenue) * 100

top_10_products = top_products.nlargest(10, 'sales_count')

st.subheader("Top 10 Produk Berdasarkan Penjualan dalam 3 Bulan Terakhir")
st.dataframe(top_10_products[['product_category_name', 'sales_count', 'revenue_contribution']])

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=top_10_products, x='sales_count', y='product_category_name', palette='viridis', ax=ax)
plt.title('Top 10 Produk Berdasarkan Penjualan', fontsize=14)
plt.xlabel('Jumlah Penjualan', fontsize=12)
plt.ylabel('Kategori Produk', fontsize=12)
st.pyplot(fig)

# Question 2: Average Shipping Time by Product Category
orders_with_products = orders.merge(order_items, on='order_id')
category_shipping_time = orders_with_products.merge(products, on='product_id').groupby('product_category_name')['shipping_time'].mean().sort_values()

st.subheader("Kategori dengan Waktu Pengiriman Terlama")
st.dataframe(category_shipping_time.tail())

fig, ax = plt.subplots(figsize=(10, 5))
category_shipping_time.tail(10).plot(kind='barh', color='orange', ax=ax)
plt.title('Kategori dengan Waktu Pengiriman Terlama', fontsize=14)
plt.xlabel('Rata-rata Waktu Pengiriman (hari)', fontsize=12)
plt.ylabel('Kategori Produk', fontsize=12)
st.pyplot(fig)

# Question 3: Most Used Payment Method for Above-Average Transactions
avg_payment = order_payments['payment_value'].mean()
above_avg_payments = order_payments[order_payments['payment_value'] > avg_payment]
top_payment_methods = above_avg_payments['payment_type'].value_counts()

st.subheader("Metode Pembayaran Paling Sering Digunakan untuk Transaksi di Atas Rata-rata")
st.dataframe(top_payment_methods)

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=top_payment_methods.values, y=top_payment_methods.index, palette='coolwarm', ax=ax)
plt.title('Metode Pembayaran untuk Transaksi di Atas Rata-rata', fontsize=14)
plt.xlabel('Jumlah Penggunaan', fontsize=12)
plt.ylabel('Metode Pembayaran', fontsize=12)
st.pyplot(fig)

# Question 4: Repeat Purchase Customer Patterns
customer_order_counts = orders.groupby('customer_id').size().reset_index(name='order_count')
repeat_customers = customer_order_counts[customer_order_counts['order_count'] > 1]
repeat_percentage = (len(repeat_customers) / len(customer_order_counts)) * 100

st.subheader(f"Persentase Pelanggan yang Melakukan Pembelian Ulang: {repeat_percentage:.2f}%")

repeat_orders = orders[orders['customer_id'].isin(repeat_customers['customer_id'])]
repeat_order_items = repeat_orders.merge(order_items, on='order_id')
repeat_categories = repeat_order_items.merge(products, on='product_id')['product_category_name'].value_counts()

st.subheader("Top 10 Kategori Produk untuk Pelanggan Repeat")
st.dataframe(repeat_categories.head(10))

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=repeat_categories.head(10).values, y=repeat_categories.head(10).index, palette='magma', ax=ax)
plt.title('Top 10 Kategori Produk untuk Pelanggan Repeat', fontsize=14)
plt.xlabel('Jumlah Penjualan', fontsize=12)
plt.ylabel('Kategori Produk', fontsize=12)
st.pyplot(fig)
