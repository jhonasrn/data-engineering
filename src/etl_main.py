# src/etl_main.py

from src.etl.load_customers import load_customers
# from src.etl.load_products import load_products
# from src.etl.load_sales import load_sales
# from src.etl.load_employees import load_employees

def run_etl():
    print("🚀 Starting ETL process...")

    print("📥 Loading customers...")
    load_customers()

    # print("📥 Loading products...")
    # load_products()

    # print("📥 Loading sales...")
    # load_sales()

    # print("📥 Loading employees...")
    # load_employees()

    print("✅ ETL process completed.")

if __name__ == "__main__":
    run_etl()
