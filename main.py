import streamlit as st
import pandas as pd
import functions as f
import creat_csv_script as csv
import random
import os

# Page settings
st.set_page_config(page_title="Purchase Recommendation System", layout="wide")

st.title("🛒 Purchase Recommendation System")

# Sidebar for CSV handling
st.sidebar.header("Upload or Generate Data")

# Define a flag to check if synthetic CSV should be loaded
use_synthetic_csv = False

uploaded_file = st.sidebar.file_uploader("Upload your CSV", type=["csv"])
if st.sidebar.button("Generate Synthetic CSV"):
    csv.create()
    st.success("Synthetic CSV generated as 'synthetic_purchases.csv'")
    use_synthetic_csv = True
    st.rerun()  # Rerun to refresh the session with the flag

# Load data
if uploaded_file:
    df = pd.read_csv(uploaded_file)
elif use_synthetic_csv or os.path.exists("synthetic_purchases.csv"):
    df = pd.read_csv("synthetic_purchases.csv")
else:
    st.warning("Upload a CSV or generate one to continue.")
    st.stop()

# Calculations
top_products = f.calculate_top_selling_product(df)
top_categories = f.calculate_top_selling_category(df)
average_spending = f.calculate_average_customer_spending(df)
customer_data = f.calculate_customer_category(df)
segment_counts = f.calculate_segment_counts(customer_data)


# Tabs for sections
tab1, tab2, tab3, tab4 = st.tabs(["📊 Stats", "📈 Charts", "🧑 Recommendations", "📄 Raw Data"])

with tab1:
    st.header("Top-Selling Products")
    st.dataframe(top_products)

    st.header("Top-Selling Categories")
    st.dataframe(top_categories)

    st.header("Average Customer Spending")
    st.metric("Average Spending", f"${average_spending:.2f}")

    st.header("Customer Data")

    # Show segment counts before the table
    st.subheader("Customer Segment Counts")
    for segment, count in segment_counts.items():
        st.write(f"{segment}: {count} customers")

    st.dataframe(customer_data)

with tab2:
    st.header("Product Sales Chart")
    f.draw_products_chart(top_products)

    st.header("Category Sales Chart")
    f.draw_categories_chart(top_categories)

    st.header("Customer Cluster Chart")
    f.draw_cluster_chart(customer_data)

with tab3:
    st.header("Get Product Recommendations")
    customer_ids = df["Customer ID"].unique()
    selected_customer = st.selectbox("Select a customer", customer_ids)
    recommended_products = f.recommend_products(df, selected_customer)
    if recommended_products:
        st.success(f"Recommended products for {selected_customer}:")
        st.write(recommended_products)
    else:
        st.warning(f"No recommendations available for {selected_customer}.")

    if st.button("Random Customer Recommendation"):
        random_customer = random.choice(customer_ids)
        random_recommendations = f.recommend_products(df, random_customer)
        st.info(f"Random customer: {random_customer}")
        st.write(random_recommendations)

with tab4:
    st.header("Raw CSV Data")
    st.dataframe(df)
