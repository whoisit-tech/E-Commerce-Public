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

st.title("Top 10 Produk Berdasarkan Penjualan")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df_penjualan, x="jumlah_penjualan", y="kategori_produk", palette="viridis", ax=ax)
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

st.title("Kategori dengan Waktu Pengiriman Terlama")
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=df_pengiriman, x="waktu_pengiriman", y="kategori_produk", palette="magma", ax=ax)
ax.set_title("Kategori dengan Waktu Pengiriman Terlama")
ax.set_xlabel("Rata-rata Waktu Pengiriman (hari)")
ax.set_ylabel("Kategori Produk")
st.pyplot(fig)

# Data untuk grafik metode pembayaran
data_pembayaran = {
    "metode_pembayaran": ["credit_card", "boleto", "voucher", "debit_card"],
    "jumlah_penggunaan": [25000, 10000, 5000, 2000]
}
df_pembayaran = pd.DataFrame(data_pembayaran)

st.title("Metode Pembayaran untuk Transaksi di Atas Rata-rata")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=df_pembayaran, x="jumlah_penggunaan", y="metode_pembayaran", palette="Blues", ax=ax)
ax.set_title("Metode Pembayaran untuk Transaksi di Atas Rata-rata")
ax.set_xlabel("Jumlah Penggunaan")
ax.set_ylabel("Metode Pembayaran")
st.pyplot(fig)

# Data untuk grafik kategori produk untuk pelanggan repeat
data_repeat = {
    "kategori_produk": [
        "kategori1", "kategori2", "kategori3", "kategori4", 
        "kategori5", "kategori6", "kategori7", "kategori8", 
        "kategori9", "kategori10"
    ],
    "jumlah_penjualan": [800, 750, 700, 680, 650, 620, 600, 580, 560, 540]
}
df_repeat = pd.DataFrame(data_repeat)

st.title("Top 10 Kategori Produk untuk Pelanggan Repeat")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=df_repeat, x="jumlah_penjualan", y="kategori_produk", palette="Oranges", ax=ax)
ax.set_title("Top 10 Kategori Produk untuk Pelanggan Repeat")
ax.set_xlabel("Jumlah Penjualan")
ax.set_ylabel("Kategori Produk")
st.pyplot(fig)
