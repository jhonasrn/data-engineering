# src/etl/load_customers.py

import csv
from src import config
from src.db.connection import get_connection

def load_customers():
    conn = get_connection()
    if conn is None:
        print("❌ Failed to connect to the database.")
        return

    cursor = conn.cursor()

    with open(config.CUSTOMERS_FILE, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute("""
                INSERT INTO etl.customers_raw (
                    customer_id, full_name, email, phone, registration_date, source_file
                ) VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                row['customer_id'],
                row['full_name'],
                row['email'],
                row['phone'],
                row['registration_date'],
                'customers.csv'
            ))

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Customers loaded successfully.")

if __name__ == "__main__":
    load_customers()
