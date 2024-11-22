import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Setup halaman
st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

# Sidebar
st.sidebar.title("E-Commerce Data Analysis")
st.sidebar.subheader("Oleh: Vilosa Auliya Dewinta Sentanu")
st.sidebar.markdown("""
- **Email**: ochadwnta@gmail.com  
- **ID Dicoding**: ochaaa
""")

# Header
st.title("📊 Dashboard Analisis Data E-Commerce")
st.markdown("""
Dashboard ini memvisualisasikan data e-commerce untuk menjawab beberapa pertanyaan bisnis:
1. Produk dengan jumlah penjualan terbanyak dan kontribusinya terhadap total pendapatan.
2. Rata-rata waktu pengiriman dan kategori dengan waktu pengiriman terlama.
3. Metode pembayaran yang paling sering digunakan untuk transaksi di atas nilai rata-rata.
4. Persentase pelanggan yang melakukan pembelian ulang.
""")

# Load data
@st.cache_data
def load_data():
    url = "https://github.com/whoisit-tech/E-Commerce-Public/blob/main/archive%20(2).zip?raw=true"
    response = requests.get(url)
    zip_file = zipfile.ZipFile(io.BytesIO(response.content))
    zip_file.extractall("ecommerce_data")

    orders = pd.read_csv("ecommerce_data/archive/olist_orders_dataset.csv")
    order_items = pd.read_csv("ecommerce_data/archive/olist_order_items_dataset.csv")
    products = pd.read_csv("ecommerce_data/archive/olist_products_dataset.csv")
    order_payments = pd.read_csv("ecommerce_data/archive/olist_order_payments_dataset.csv")
    customers = pd.read_csv("ecommerce_data/archive/olist_customers_dataset.csv")
    return orders, order_items, products, order_payments, customers

orders, order_items, products, order_payments, customers = load_data()

# Preprocessing
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
today = datetime.now()
three_months_ago = today - timedelta(days=90)
recent_orders = orders[orders['order_purchase_timestamp'] >= three_months_ago]
orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
orders['shipping_time'] = (orders['order_delivered_customer_date'] - orders['order_purchase_timestamp']).dt.days

# Pertanyaan 1: Produk dengan Penjualan Terbanyak
st.header("1️⃣ Produk dengan Penjualan Terbanyak")
top_products = order_items.groupby('product_id').agg({'order_item_id': 'count', 'price': 'sum'}).reset_index()
top_products = top_products.rename(columns={'order_item_id': 'sales_count'})
top_products = top_products.merge(products, on='product_id')
top_products['revenue_contribution'] = (top_products['price'] / top_products['price'].sum()) * 100
top_10_products = top_products.nlargest(10, 'sales_count')

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=top_10_products, x='sales_count', y='product_category_name', palette='viridis', ax=ax)
ax.set_title('Top 10 Produk Berdasarkan Penjualan')
ax.set_xlabel('Jumlah Penjualan')
ax.set_ylabel('Kategori Produk')
st.pyplot(fig)

# Pertanyaan 2: Waktu Pengiriman
st.header("2️⃣ Rata-rata Waktu Pengiriman dan Kategori dengan Waktu Terlama")
avg_shipping_time = orders['shipping_time'].mean()
st.write(f"Rata-rata waktu pengiriman semua pesanan: **{avg_shipping_time:.2f} hari**")

orders_with_products = orders.merge(order_items, on='order_id').merge(products, on='product_id')
category_shipping_time = orders_with_products.groupby('product_category_name')['shipping_time'].mean().sort_values()

fig, ax = plt.subplots(figsize=(10, 5))
category_shipping_time.tail(10).plot(kind='barh', color='orange', ax=ax)
ax.set_title('Kategori dengan Waktu Pengiriman Terlama')
ax.set_xlabel('Rata-rata Waktu Pengiriman (hari)')
ax.set_ylabel('Kategori Produk')
st.pyplot(fig)

# Pertanyaan 3: Metode Pembayaran
st.header("3️⃣ Metode Pembayaran yang Paling Sering Digunakan")
payment_methods = order_payments.groupby('payment_type').size().reset_index(name='count')

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=payment_methods, x='payment_type', y='count', palette='muted', ax=ax)
ax.set_title('Distribusi Metode Pembayaran')
ax.set_xlabel('Metode Pembayaran')
ax.set_ylabel('Jumlah Transaksi')
st.pyplot(fig)

# Pertanyaan 4: Pembelian Ulang
st.header("4️⃣ Persentase Pelanggan yang Melakukan Pembelian Ulang")
repeat_customers = customers.groupby('customer_unique_id').size().reset_index(name='order_count')
repeat_percentage = (repeat_customers[repeat_customers['order_count'] > 1].shape[0] / repeat_customers.shape[0]) * 100
st.write(f"Persentase pelanggan yang melakukan pembelian ulang: **{repeat_percentage:.2f}%**")
