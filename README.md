# 🛠️ Data Engineering Project - Simulated Analytical Database

This repository showcases practical projects and studies in data engineering, including ETL pipelines, data modeling, system integration, and data visualization. It simulates a complete data engineering pipeline focused on ingesting, transforming, and analyzing customer, product, sales, and employee data. The project is ideal for testing ETL workflows, analytical modeling, and building dashboards using tools like Power BI, dbt, or Python.

---

## 📦 Project Structure

```bash
data-engineering-project/
│
├── setup/
│   └── setup_database.sql       # Full SQL script to create schemas, tables, and views
│
├── data/
│   ├── customers.csv            # Simulated raw data (optional)
│   ├── products.csv
│   ├── sales.csv
│   └── employees.csv
│
├── scripts/
│   ├── load_data.py             # Python scripts for data loading (optional)
│   └── transform_data.py
│
├── notebooks/
│   └── etl_pipeline.ipynb       # ETL pipeline in Jupyter Notebook (optional)
│
├── dbt/
│   └── models/                  # dbt models for transformation (optional)
│
└── docs/
    └── schema_diagram.png       # Database schema diagram (optional)
🧱 Database Architecture
Schemas
etl: stores raw data imported from files or APIs

analytics: stores cleaned and transformed data for analysis

Tables
etl (raw data)
customers_raw

products_raw

sales_raw

employees_raw

analytics (clean data)
customers

products

sales

employees

Views
analytics.customers_view

analytics.products_view

analytics.sales_view

analytics.employees_view

🚀 How to Run
Clone the repository:

bash
git clone https://github.com/your-username/data-engineering-project.git
Access the folder and connect to PostgreSQL:

bash
cd data-engineering-project/setup
psql -U your_user -d data_engineering_db -f setup_database.sql
(Optional) Load data using Python scripts or CSV import.

📊 Sample Queries
sql
-- Total sales and revenue
SELECT COUNT(*) AS total_sales, SUM(total_amount) AS revenue
FROM analytics.sales_view;

-- Products by category
SELECT category, COUNT(*) FROM analytics.products_view GROUP BY category;

-- Join sales with customers and products
SELECT s.id, c.full_name, p.product_name, s.total_amount
FROM analytics.sales_view s
JOIN analytics.customers_view c ON s.customer_id = c.id
JOIN analytics.products_view p ON s.product_id = p.id;
📌 Author
Project created by Jhonas, focused on learning and showcasing data engineering skills.
