import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data for the first chart (Top Products by Sales Count)
data_sales = {
    "product_category_name": [
        "moveis_decoracao", "cama_mesa_banho", "ferramentas_jardim", "ferramentas_jardim", 
        "ferramentas_jardim", "ferramentas_jardim", "informatica_acessorios", "relogios_presentes", 
        "beleza_saude", "informatica_acessorios"
    ],
    "sales_count": [527, 488, 484, 392, 388, 373, 343, 323, 281, 274]
}

df_sales = pd.DataFrame(data_sales)

# Streamlit UI for Top Products by Sales Count
st.title("Top 10 Produk Berdasarkan Penjualan")
st.write("Grafik ini menunjukkan produk teratas berdasarkan jumlah penjualan.")

# Plot for Top Products by Sales Count
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(
    data=df_sales,
    x="sales_count",
    y="product_category_name",
    palette="viridis",
    ax=ax
)
ax.set_title("Top Produk Berdasarkan Penjualan")
ax.set_xlabel("Jumlah Penjualan")
ax.set_ylabel("Kategori Produk")
st.pyplot(fig)

# Data for the second chart (Categories with Longest Shipping Times)
data_shipping = {
    "product_category_name": [
        "moveis_escritorio", "artigos_de_natal", "seguros_e_servicos", "fashion_calcados",
        "casa_conforto_2", "moveis_colchao_e_estofado", "eletrdomesticos_2", "moveis_sala",
        "fashion_underwear_e_moda_praia", "ferramentas_jardim"
    ],
    "shipping_time": [20.39, 15.30, 15.00, 14.93, 14.07, 13.40, 12.50, 11.70, 11.00, 10.20]
}

df_shipping = pd.DataFrame(data_shipping)

# Streamlit UI for Categories with Longest Shipping Times
st.title("Kategori dengan Waktu Pengiriman Terlama")
st.write("Grafik ini menunjukkan kategori produk dengan waktu pengiriman rata-rata terlama.")

# Plot for Categories with Longest Shipping Times
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(
    data=df_shipping,
    x="shipping_time",
    y="product_category_name",
    palette="magma",
    ax=ax
)
ax.set_title("Kategori dengan Waktu Pengiriman Terlama")
ax.set_xlabel("Rata-rata Waktu Pengiriman (hari)")
ax.set_ylabel("Kategori Produk")
st.pyplot(fig)
