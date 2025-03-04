import pandas as pd
import random
from faker import Faker

def create():
    from datetime import datetime, timedelta

    # Initialize Faker library
    fake = Faker()

    # Define the number of entities
    num_customers = 500
    num_products = 50
    num_purchases = 5000

    # Generate lists of customers and products
    customers = [f"CUST_{i}" for i in range(1, num_customers + 1)]
    products = [f"PROD_{i}" for i in range(1, num_products + 1)]
    product_categories = ["Electronics", "Clothing", "Food", "Home", "Toys"]

    # Generate purchase records
    data = []
    for _ in range(num_purchases):
        customer_id = random.choice(customers)
        product_id = random.choice(products)
        product_category = random.choice(product_categories)
        purchase_amount = random.randint(5, 500)  # Price between 5 and 500 (integer)
        purchase_date = fake.date_between(start_date="-1y", end_date="today")  # Date within the last year

        data.append([customer_id, product_id, product_category, purchase_amount, purchase_date])

    # Create DataFrame
    df = pd.DataFrame(data,
                      columns=["Customer ID", "Product ID", "Product Category", "Purchase Amount", "Purchase Date"])

    # Save to CSV file
    df.to_csv("synthetic_purchases.csv", index=False)

    print("Synthetic dataset generated and saved as synthetic_purchases.csv!")