# src/etl/load_products.py

import csv
from src import config
from src.db.connection import get_connection

def load_products():
    conn = get_connection()
    if conn is None:
        print("❌ Failed to connect to the database.")
        return

    cursor = conn.cursor()

    with open(config.PRODUCTS_FILE, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute("""
                INSERT INTO etl.products_raw (
                    product_id, product_name, category, price, stock_quantity, source_file
                ) VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                row['product_id'],
                row['product_name'],
                row['category'],
                row['price'],
                row['stock_quantity'],
                'products.csv'
            ))

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Products loaded successfully.")

if __name__ == "__main__":
    load_products()
