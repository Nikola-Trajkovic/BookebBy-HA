import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

def calculate_top_selling_product(df):
    # Top-selling products (based on total sales amount)
    top_products = df.groupby("Product ID")["Purchase Amount"].sum().sort_values(ascending=False).head(10)
    return top_products

def calculate_top_selling_category(df):
    # Top-selling categories (based on total sales amount)
    top_categories = df.groupby("Product Category")["Purchase Amount"].sum().sort_values(ascending=False)
    return top_categories

def calculate_average_customer_spending(df):
    # Total spending per customer
    customer_spending = df.groupby("Customer ID")["Purchase Amount"].sum()

    # Average spending per customer
    average_spending = customer_spending.mean()
    return average_spending

def calculate_customer_category(df):
    # Calculate total spending and purchase frequency per customer
    customer_data = df.groupby("Customer ID").agg(
        total_spending=("Purchase Amount", "sum"),
        purchase_count=("Purchase Amount", "count")  # Number of purchases
    ).reset_index()

    # Apply K-Means clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    customer_data["Cluster"] = kmeans.fit_predict(customer_data[["total_spending", "purchase_count"]])

    # Assign intuitive labels
    cluster_labels = {0: "Low Spenders", 1: "Medium Spenders", 2: "High Spenders"}
    customer_data["Segment"] = customer_data["Cluster"].map(cluster_labels)
    return customer_data

def calculate_segment_counts(customer_data):
    # Count the number of customers in each segment
    segment_counts = customer_data["Segment"].value_counts().to_dict()
    return segment_counts

def draw_products_chart(top_products):
    # Plot top-selling products
    plt.figure(figsize=(10, 5))
    sns.barplot(x=top_products.index, y=top_products.values, hue=top_products.index, palette="viridis", legend=False)
    plt.xlabel("Product ID")
    plt.ylabel("Total Sales Amount")
    plt.title("Top-Selling Products")
    plt.xticks(rotation=45)
    # plt.show()

    # Show in Streamlit
    st.pyplot(plt.gcf())

    # Optional: Clear the figure to prevent overlap on re-renders
    plt.clf()

def draw_categories_chart(top_categories):
    # Plot top-selling categories
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_categories.index, y=top_categories.values, hue=top_categories.index, palette="viridis")

    plt.title("Top Selling Product Categories", fontsize=16)
    plt.xlabel("Product Category", fontsize=14)
    plt.ylabel("Total Sales Amount", fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    # plt.show()

    # Show in Streamlit
    st.pyplot(plt.gcf())

    # Optional: Clear the figure to prevent overlap on re-renders
    plt.clf()

def draw_cluster_chart(customer_data):
    # Visualize the clusters
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=customer_data, x="total_spending", y="purchase_count", hue="Segment", palette="viridis")
    plt.title("Customer Segmentation Based on Spending Behavior")
    plt.xlabel("Total Spending")
    plt.ylabel("Number of Purchases")
    # plt.show()

    # Show in Streamlit
    st.pyplot(plt.gcf())

    # Optional: Clear the figure to prevent overlap on re-renders
    plt.clf()

# Recommendation function using cosine similarity
def recommend_products(df, customer_id, num_recommendations=5):
    # Create the user-product matrix
    user_product_matrix = df.pivot_table(
        index='Customer ID',
        columns='Product ID',
        values='Purchase Amount',
        fill_value=0
    )

    # Calculate cosine similarity between users
    user_similarity = cosine_similarity(user_product_matrix)
    user_similarity_df = pd.DataFrame(
        user_similarity,
        index=user_product_matrix.index,
        columns=user_product_matrix.index
    )

    # Find the most similar users (excluding the target user)
    similar_users = user_similarity_df[customer_id].sort_values(ascending=False).index[1:]

    # Collect all products purchased by similar users
    recommended_products_list = []

    for similar_user in similar_users:
        products = df[df['Customer ID'] == similar_user][['Product ID', 'Purchase Amount']]
        if not products.empty:
            products_series = products.set_index('Product ID')['Purchase Amount']
            recommended_products_list.append(products_series)

    # If no products were found from similar users, return an empty list
    if not recommended_products_list:
        return []

    # Combine all recommended products into a single Series
    recommended_products = pd.concat(recommended_products_list)

    # Remove products that the target customer has already purchased
    purchased_products = df[df['Customer ID'] == customer_id]['Product ID'].unique()
    recommended_products = recommended_products[~recommended_products.index.isin(purchased_products)]

    # If no products remain after filtering, return an empty list
    if recommended_products.empty:
        return []

    # Aggregate and sort the recommended products by average purchase amount
    top_recommendations = (
        recommended_products.groupby(recommended_products.index)
        .mean()
        .sort_values(ascending=False)
    )

    # Return the top N recommended product IDs
    return list(top_recommendations.head(num_recommendations).index)


