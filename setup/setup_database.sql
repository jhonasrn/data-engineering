-- Criação do banco (executar fora do script se já estiver criado)
-- CREATE DATABASE data_engineering_db;

-- Selecionar o banco
-- \c data_engineering_db

-- Criação dos schemas
CREATE SCHEMA IF NOT EXISTS etl;
CREATE SCHEMA IF NOT EXISTS analytics;

-- Tabelas brutas (ETL)
CREATE TABLE etl.customers_raw (
    customer_id TEXT,
    full_name TEXT,
    email TEXT,
    phone TEXT,
    registration_date TEXT,
    source_file TEXT,
    load_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE etl.products_raw (
    product_id TEXT,
    product_name TEXT,
    category TEXT,
    price TEXT,
    stock_quantity TEXT,
    source_file TEXT,
    load_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE etl.sales_raw (
    sale_id TEXT,
    customer_id TEXT,
    product_id TEXT,
    sale_date TEXT,
    quantity TEXT,
    total_amount TEXT,
    source_file TEXT,
    load_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE etl.employees_raw (
    employee_id TEXT,
    full_name TEXT,
    position TEXT,
    salary TEXT,
    hire_date TEXT,
    source_file TEXT,
    load_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabelas tratadas (Analytics)
CREATE TABLE analytics.customers (
    id SERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    email TEXT,
    phone TEXT,
    registration_date DATE
);

CREATE TABLE analytics.products (
    id SERIAL PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT,
    price NUMERIC(10,2),
    stock_quantity INTEGER
);

CREATE TABLE analytics.sales (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES analytics.customers(id),
    product_id INTEGER REFERENCES analytics.products(id),
    sale_date DATE,
    quantity INTEGER,
    total_amount NUMERIC(10,2)
);

CREATE TABLE analytics.employees (
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    position TEXT,
    salary NUMERIC(10,2),
    hire_date DATE
);

-- Views de transformação
CREATE OR REPLACE VIEW analytics.customers_view AS
SELECT
    customer_id::INTEGER AS id,
    full_name,
    email,
    phone,
    registration_date::DATE AS registration_date
FROM etl.customers_raw;

CREATE OR REPLACE VIEW analytics.products_view AS
SELECT
    product_id::INTEGER AS id,
    product_name,
    category,
    price::NUMERIC(10,2) AS price,
    stock_quantity::INTEGER AS stock_quantity
FROM etl.products_raw;

CREATE OR REPLACE VIEW analytics.sales_view AS
SELECT
    sale_id::INTEGER AS id,
    customer_id::INTEGER,
    product_id::INTEGER,
    sale_date::DATE AS sale_date,
    quantity::INTEGER,
    total_amount::NUMERIC(10,2) AS total_amount
FROM etl.sales_raw;

CREATE OR REPLACE VIEW analytics.employees_view AS
SELECT
    employee_id::INTEGER AS id,
    split_part(full_name, ' ', 1) AS first_name,
    split_part(full_name, ' ', 2) AS last_name,
    position,
    salary::NUMERIC(10,2) AS salary,
    hire_date::DATE AS hire_date
FROM etl.employees_raw;
