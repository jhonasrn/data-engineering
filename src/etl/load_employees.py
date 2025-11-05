# src/etl/load_employees.py

import csv
from src import config
from src.db.connection import get_connection

def load_employees():
    conn = get_connection()
    if conn is None:
        print("❌ Failed to connect to the database.")
        return

    cursor = conn.cursor()

    with open(config.EMPLOYEES_FILE, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute("""
                INSERT INTO etl.employees_raw (
                    employee_id, full_name, department, email, hire_date, source_file
                ) VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                row['employee_id'],
                row['full_name'],
                row['department'],
                row['email'],
                row['hire_date'],
                'employees.csv'
            ))

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Employees loaded successfully.")

if __name__ == "__main__":
    load_employees()
