# 📊 E-Commerce Price Tracker

## 🛠 Tools Used
- Python (BeautifulSoup, Pandas)
- MySQL
- Power BI


## 📌 Project Overview

The **E-Commerce Price Tracker** project collects laptop product data
from an e‑commerce platform using web scraping and analyzes price
trends, ratings, and product distribution.

The project demonstrates how **Python, data analysis, database
management, and business intelligence tools** can be integrated to
analyze online product pricing.

------------------------------------------------------------------------

## 🎯 Project Objective

The objective of this project is to build an automated system that:

-   Scrapes product data from an e‑commerce website (Amazon)
-   Cleans and processes the collected dataset
-   Stores structured data for analysis
-   Analyzes price and rating trends
-   Visualizes insights using a Power BI dashboard

------------------------------------------------------------------------

## 🛠 Tools & Technologies

  Tool            Purpose
  --------------- --------------------------------
  Python          Web scraping & data processing
  BeautifulSoup   Extract HTML data
  Pandas          Data cleaning & analysis
  MySQL           Data storage
  Power BI        Dashboard visualization

------------------------------------------------------------------------

## 📂 Project Structure

    ecommerce-price-tracker
    │
    ├── scraping
    │   └── scrape_amazon.py
    │
    ├── analysis
    │   ├── clean_data.py
    │   └── analysis.py
    │
    ├── data
    │   ├── raw
    │   │   └── products_raw.csv
    │   └── cleaned
    │       └── products_cleaned.csv
    │
    ├── sql
    │   └── schema.sql
    │
    ├── dashboard
    │   └── ecommerce_price_tracker_dashboard.pbix
    │
    ├── Project Objectives.pdf
    ├── Project Insight.pdf
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## ⚙️ Project Workflow

    Web Scraping → Data Cleaning → Data Storage → Data Analysis → Dashboard Visualization

1.  Scrape laptop product data using Python.
2.  Store raw data in CSV format.
3.  Clean and transform the dataset.
4.  Store structured data in a database.
5.  Analyze product price trends.
6.  Visualize insights using Power BI.

------------------------------------------------------------------------

## 📊 Dashboard Features

The dashboard provides insights such as:

-   Total number of products
-   Average product price
-   Average product rating
-   Product price distribution
-   Top expensive laptops
-   Price vs rating analysis

------------------------------------------------------------------------

## 📈 Key Insights

-   Most laptops fall within the **mid‑range price category**
-   Premium laptops usually have **higher ratings**
-   The majority of laptops have ratings above **4.0**
-   The market is competitive in the **₹40,000 -- ₹60,000 price range**

------------------------------------------------------------------------

## 🚀 How to Run the Project

### 1️⃣ Install dependencies

``` bash
pip install -r requirements.txt
```

### 2️⃣ Run the scraper

``` bash
python scrape_amazon.py
```

Output:

    products_raw.csv

### 3️⃣ Clean the dataset

``` bash
python clean_data.py
```

Output:

    products_cleaned.csv

### 4️⃣ Run analysis

``` bash
python analysis.py
```

### 5️⃣ Open Dashboard

Open the Power BI dashboard file in **Microsoft Power BI Desktop** and
click **Refresh**.

------------------------------------------------------------------------

## 🔮 Future Improvements

-   Add Flipkart scraping
-   Automate daily price tracking
-   Implement price drop alerts
-   Add brand analysis
-   Build a web dashboard

------------------------------------------------------------------------

## 👩‍💻 Author

**Priyanka Durge**\
Data Analytics Project -- E‑Commerce Price Tracker
