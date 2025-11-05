# src/etl/load_sales.py

import csv
from src import config
from src.db.connection import get_connection

def load_sales():
    conn = get_connection()
    if conn is None:
        print("❌ Failed to connect to the database.")
        return

    cursor = conn.cursor()

    with open(config.SALES_FILE, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute("""
                INSERT INTO etl.sales_raw (
                    sale_id, customer_id, product_id, quantity, total_amount, sale_date, source_file
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                row['sale_id'],
                row['customer_id'],
                row['product_id'],
                row['quantity'],
                row['total_amount'],
                row['sale_date'],
                'sales.csv'
            ))

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Sales loaded successfully.")

if __name__ == "__main__":
    load_sales()
