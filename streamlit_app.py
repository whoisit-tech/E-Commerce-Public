import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Pertanyaan 1
data = {
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
    "revenue_contribution": [
        0.276706, 0.316559, 0.195541, 0.157748, 0.154925, 0.149998, 0.347379,
        0.277254, 0.046537, 0.302264,
    ],
}

# Create DataFrame
df = pd.DataFrame(data)

# Streamlit UI
st.title("Top Products by Sales Count")
st.write("This chart displays the top products based on their sales count.")

# Plot
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(
    data=df,
    x="sales_count",
    y="product_category_name",
    palette="viridis",
    ax=ax
)
ax.set_title("Top 10 Products by Sales Count")
ax.set_xlabel("Sales Count")
ax.set_ylabel("Product Category")

# Display plot in Streamlit
st.pyplot(fig)

# Additional table
st.write("Data Table:")
st.dataframe(df)

# Pertanyaan 2

average_shipping_time = 12.09
data = {
    "product_category_name": [
        "casa_conforto_2",
        "fashion_calcados",
        "seguros_e_servicos",
        "artigos_de_natal",
        "moveis_escritorio",
    ],
    "shipping_time": [14.066667, 14.933852, 15.000000, 15.300000, 20.386691],
}

# Create DataFrame
df = pd.DataFrame(data)

# Streamlit UI
st.title("Shipping Time Analysis")
st.write("This application displays the average shipping time and categories with the longest shipping times.")

# Display Average Shipping Time
st.subheader("Average Shipping Time for All Orders")
st.metric(label="Average Shipping Time", value=f"{average_shipping_time:.2f} days")

# Display Categories with Longest Shipping Times
st.subheader("Categories with Longest Shipping Times")
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(
    data=df,
    x="shipping_time",
    y="product_category_name",
    palette="magma",
    ax=ax
)
ax.set_title("Longest Shipping Times by Category")
ax.set_xlabel("Shipping Time (days)")
ax.set_ylabel("Product Category")

# Display plot in Streamlit
st.pyplot(fig)

# Additional table
st.write("Data Table:")
st.dataframe(df)

# Pertanyaan 3

data = {
    "payment_type": ["credit_card", "boleto", "voucher", "debit_card"],
    "count": [24875, 5292, 461, 384],
}

# Create DataFrame
df = pd.DataFrame(data)

# Streamlit UI
st.title("Most Used Payment Methods for Above-Average Transactions")
st.write("This application displays the payment methods most frequently used for transactions above the average value.")

# Plot
st.subheader("Payment Methods Usage")
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(
    x=df["count"],
    y=df["payment_type"],
    palette="coolwarm",
    ax=ax
)
ax.set_title("Most Frequent Payment Methods")
ax.set_xlabel("Count")
ax.set_ylabel("Payment Method")

# Display plot in Streamlit
st.pyplot(fig)

# Additional table
st.write("Data Table:")
st.dataframe(df)

# Pertanyaan 4

repeat_purchase_percentage = 0.00
repeat_purchase_pattern = pd.Series([], name="count")

# Streamlit UI
st.title("Repeat Purchase Analysis")
st.write("This application displays the percentage of customers who made repeat purchases and the product categories frequently purchased by repeat customers.")

# Display Repeat Purchase Percentage
st.subheader("Percentage of Customers Who Made Repeat Purchases")
st.metric(label="Repeat Purchase Percentage", value=f"{repeat_purchase_percentage:.2f}%")

# Display Repeat Purchase Patterns
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

# Additional note
st.write("Note: The data shows no repeat purchases or patterns at this time.")

