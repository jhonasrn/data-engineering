# src/db/connection.py

import psycopg2
from src import config

def get_connection():
    try:
        conn = psycopg2.connect(
            host=config.DB_HOST,
            port=config.DB_PORT,
            dbname=config.DB_NAME,
            user=config.DB_USER,
            password=config.DB_PASSWORD
        )
        return conn
    except Exception as e:
        print(f"❌ Error connecting to database: {e}")
        return None
