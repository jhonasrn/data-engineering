# src/config.py

import os

# Database connection settings
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "data_engineering_db")
DB_USER = os.getenv("DB_USER", "USER")
DB_PASSWORD = os.getenv("DB_PASSWORD", "your_password")

# Data file paths
DATA_PATH = os.path.join(os.getcwd(), "data")
CUSTOMERS_FILE = os.path.join(DATA_PATH, "customers.csv")
PRODUCTS_FILE = os.path.join(DATA_PATH, "products.csv")
SALES_FILE = os.path.join(DATA_PATH, "sales.csv")
EMPLOYEES_FILE = os.path.join(DATA_PATH, "employees.csv")
