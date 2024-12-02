import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ==================================================================================
# Pertanyaan 1: Produk dengan Penjualan Terbanyak
# ==================================================================================
sales_data = {
    "product_id": [
        "aca2eb7d00ea1a7b8ebd4e68314663af",
        "99a4788cb24856965c36a24e339b6058",
        "422879e10f46682990de24d770e7f83d",
        "389d119b48cf3043d311335e499d9c6b",
        "368c6c730842d78016ad823897a372db",
        "53759a2ecddad2bb87a079a1f1519f73",
        "d1c427060a0f73f6b889a5c7c61f2ac4",
        "53b36df67ebb7c41585e8d54d6772e08",
        "154e7e31ebfa092203795c972e5804a6",
        "3dd2a17168ec895c781a9191c1e95ad7",
    ],
    "product_category_name": [
        "moveis_decoracao",
        "cama_mesa_banho",
        "ferramentas_jardim",
        "ferramentas_jardim",
        "ferramentas_jardim",
        "ferramentas_jardim",
        "informatica_acessorios",
        "relogios_presentes",
        "beleza_saude",
        "informatica_acessorios",
    ],
    "sales_count": [527, 488, 484, 392, 388, 373, 343, 323, 281, 274],
}

df_sales = pd.DataFrame(sales_data)

st.title("Top Products by Sales Count")
st.write("This chart displays the top products based on their sales count.")

fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(
    data=df_sales,
    x="sales_count",
    y="product_category_name",
    palette="viridis",
    ax=ax
)
ax.set_title("Top 10 Products by Sales Count")
ax.set_xlabel("Sales Count")
ax.set_ylabel("Product Category")
st.pyplot(fig)
st.dataframe(df_sales)

# ==================================================================================
# Pertanyaan 2: Rata-rata Waktu Pengiriman
# ==================================================================================
shipping_data = {
    "product_category_name": [
        "casa_conforto_2",
        "fashion_calcados",
        "seguros_e_servicos",
        "artigos_de_natal",
        "moveis_escritorio",
    ],
    "shipping_time": [14.07, 14.93, 15.00, 15.30, 20.39],
}

df_shipping = pd.DataFrame(shipping_data)
average_shipping_time = 12.09

st.title("Shipping Time Analysis")
st.metric("Average Shipping Time", f"{average_shipping_time} days")

st.subheader("Categories with Longest Shipping Times")
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(
    data=df_shipping,
    x="shipping_time",
    y="product_category_name",
    palette="magma",
    ax=ax
)
ax.set_title("Longest Shipping Times by Category")
ax.set_xlabel("Shipping Time (days)")
ax.set_ylabel("Product Category")
st.pyplot(fig)
st.dataframe(df_shipping)

# ==================================================================================
# Pertanyaan 3: Metode Pembayaran Paling Sering Digunakan
# ==================================================================================
payment_data = {
    "payment_type": ["credit_card", "boleto", "voucher", "debit_card"],
    "count": [24875, 5292, 461, 384],
}

df_payment = pd.DataFrame(payment_data)

st.title("Most Used Payment Methods")
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(
    x="count",
    y="payment_type",
    data=df_payment,
    palette="coolwarm",
    ax=ax
)
ax.set_title("Most Used Payment Methods for Above-Average Transactions")
ax.set_xlabel("Count")
ax.set_ylabel("Payment Method")
st.pyplot(fig)
st.dataframe(df_payment)

# ==================================================================================
# Pertanyaan 4: Persentase Repeat Purchase
# ==================================================================================
repeat_purchase_percentage = 0.00
repeat_purchase_pattern = pd.Series([], name="count")

st.title("Repeat Purchase Analysis")
st.metric("Repeat Purchase Percentage", f"{repeat_purchase_percentage:.2f}%")

st.subheader("Product Categories Frequently Purchased by Repeat Customers")
if repeat_purchase_pattern.empty:
    st.write("No data available for repeat purchase patterns.")
else:
    fig, ax = plt.subplots(figsize=(8, 6))
    repeat_purchase_pattern.sort_values(ascending=True).plot(
        kind="barh", color="skyblue", ax=ax
    )
    ax.set_title("Product Categories for Repeat Purchases")
    ax.set_xlabel("Count")
    ax.set_ylabel("Product Category")
    st.pyplot(fig)

st.write("Note: No repeat purchase patterns available in the dataset.")
