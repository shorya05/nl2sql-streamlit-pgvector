CREATE EXTENSION IF NOT EXISTS vector;

-- Departments
CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Employees
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department_id INT REFERENCES departments(id),
    email VARCHAR(255),
    salary DECIMAL(10,2)
);

-- Orders
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    employee_id INT REFERENCES employees(id),
    order_total DECIMAL(10,2),
    order_date DATE
);

-- Products
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2)
);
