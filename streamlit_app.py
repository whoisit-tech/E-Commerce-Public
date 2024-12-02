import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data untuk grafik pertama (Top Produk Berdasarkan Jumlah Penjualan)
data_penjualan = {
    "kategori_produk": [
        "moveis_decoracao", "cama_mesa_banho", "ferramentas_jardim", "ferramentas_jardim", 
        "ferramentas_jardim", "ferramentas_jardim", "informatica_acessorios", "relogios_presentes", 
        "beleza_saude", "informatica_acessorios"
    ],
    "jumlah_penjualan": [527, 488, 484, 392, 388, 373, 343, 323, 281, 274]
}

df_penjualan = pd.DataFrame(data_penjualan)

# Streamlit UI untuk Top Produk Berdasarkan Jumlah Penjualan
st.title("Top 10 Produk Berdasarkan Penjualan")
st.write("Grafik ini menunjukkan produk teratas berdasarkan jumlah penjualan.")

# Plot untuk Top Produk Berdasarkan Jumlah Penjualan
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(
    data=df_penjualan,
    x="jumlah_penjualan",
    y="kategori_produk",
    palette="viridis",
    ax=ax
)
ax.set_title("Top Produk Berdasarkan Penjualan")
ax.set_xlabel("Jumlah Penjualan")
ax.set_ylabel("Kategori Produk")
st.pyplot(fig)

# Data untuk grafik kedua (Kategori dengan Waktu Pengiriman Terlama)
data_pengiriman = {
    "kategori_produk": [
        "moveis_escritorio", "artigos_de_natal", "seguros_e_servicos", "fashion_calcados",
        "casa_conforto_2", "moveis_colchao_e_estofado", "eletrdomesticos_2", "moveis_sala",
        "fashion_underwear_e_moda_praia", "ferramentas_jardim"
    ],
    "waktu_pengiriman": [20.39, 15.30, 15.00, 14.93, 14.07, 13.40, 12.50, 11.70, 11.00, 10.20]
}

df_pengiriman = pd.DataFrame(data_pengiriman)

# Streamlit UI untuk Kategori dengan Waktu Pengiriman Terlama
st.title("Kategori dengan Waktu Pengiriman Terlama")
st.write("Grafik ini menunjukkan kategori produk dengan waktu pengiriman rata-rata terlama.")

# Plot untuk Kategori dengan Waktu Pengiriman Terlama
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(
    data=df_pengiriman,
    x="waktu_pengiriman",
    y="kategori_produk",
    palette="magma",
    ax=ax
)
ax.set_title("Kategori dengan Waktu Pengiriman Terlama")
ax.set_xlabel("Rata-rata Waktu Pengiriman (hari)")
ax.set_ylabel("Kategori Produk")
st.pyplot(fig)
