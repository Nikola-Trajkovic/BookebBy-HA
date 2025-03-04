# 🛒 Purchase Recommendation System

This project is a **Streamlit web application** that analyzes purchase data, performs customer segmentation with K-Means clustering, and provides **product recommendations** based on purchase behavior.

## 🌐 Live Demo

Check out the live demo (if available) at:  
[Live Demo](https://bookedby-nikola-trajkovic.streamlit.app/)

⚠️ **Note**: If the deployed app is not working, follow the guide below to run it locally.

---

## 🚀 How to Run the Project Locally

### 1️⃣ Install Python

Ensure Python 3.12.5+ is installed on your system.  
You can download it from:  
[Python Downloads](https://www.python.org/downloads/)

### 2️⃣ Download the Project

Clone the repository or download the ZIP and extract it:

```bash
git clone https://github.com/Nikola-Trajkovic/BookebBy-HA.git
cd BookebBy-HA
```

### 3️⃣ (Optional) Create a Virtual Environment

It's a good practice to create a virtual environment for this project:

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 4️⃣ Install Dependencies

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 5️⃣ Run the Streamlit App

Run the application using Streamlit:

```bash
streamlit run main.py
```

---

# 🧪 How to Test the App

## Create or Generate CSV:
You can either upload your own dataset (which must include columns like Customer ID, Product ID, and Purchase Amount) or use the built-in generator to create synthetic data.

## Explore Tabs:
- 📊 **Statistics**: View top products, categories, and spending statistics.
- 📈 **Charts**: Visualize sales trends and customer clusters.
- 🧑 **Recommendations**: Get personalized product recommendations.
- 📄 **Raw Data**: Inspect and download the raw dataset.
- 🔄 **Random Customer Recommendation**: Test the recommender system on a random customer.

## ⚠️ Common Issues & Solutions

| **Issue**             | **Solution**                                                                 |
|-----------------------|-------------------------------------------------------------------------------|
| **ModuleNotFoundError** | Re-run `pip install -r requirements.txt`                                      |
| **Port already in use** | Run with `--server.port`: `streamlit run app.py --server.port 8502`         |
| **CSV upload errors**   | Verify your CSV matches the expected format.                                 |

## Documentation and Testing

- **Documentation**: This guide provides instructions for how to use the app, including CSV generation, data exploration, and common troubleshooting solutions.
- **Tested**: The app has been tested using the file `synthetic_purchases-original.csv`. If you are testing any functionalities in the **Recommendations** tab (whether it's changing the user or using the **Random Customer Recommendation**), please note that it may take some time. You will see an indicator in the top-right corner saying "Running..." while the system processes your request.

---

## 📌 Features
- Customer segmentation with K-Means clustering (Low, Medium, High spenders).
- Product recommendation system using Cosine Similarity.
- Interactive charts and statistics.
- Synthetic data generation for testing.

---

## 📬 Contact

For questions or support, feel free to contact me at:  
[trajkovicnikola75@gmail.com](mailto:trajkovicnikola75@gmail.com)
