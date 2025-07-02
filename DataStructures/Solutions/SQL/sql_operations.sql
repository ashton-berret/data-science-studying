-- =============================================================================
-- DATABASE SETUP - REALISTIC DATASETS
-- =============================================================================

-- E-commerce Database
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    registration_date DATE,
    country VARCHAR(50),
    age INTEGER
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    supplier_id INTEGER
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    total_amount DECIMAL(10,2),
    status VARCHAR(20)
);

CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    unit_price DECIMAL(10,2)
);

CREATE TABLE reviews (
    review_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    customer_id INTEGER,
    rating INTEGER,
    review_text TEXT,
    review_date DATE
);

-- Employee/HR Database
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY,
    department_name VARCHAR(50),
    budget DECIMAL(12,2)
);

CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    department_id INTEGER,
    salary DECIMAL(10,2),
    hire_date DATE,
    manager_id INTEGER,
    job_title VARCHAR(100)
);

CREATE TABLE salaries (
    employee_id INTEGER,
    salary DECIMAL(10,2),
    from_date DATE,
    to_date DATE
);

-- Financial Database
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    account_type VARCHAR(20),
    balance DECIMAL(15,2),
    opened_date DATE
);

CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY,
    account_id INTEGER,
    transaction_date DATE,
    amount DECIMAL(15,2),
    transaction_type VARCHAR(20),
    description TEXT
);

-- Social Media Database
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    signup_date DATE,
    last_login DATE,
    is_active BOOLEAN
);

CREATE TABLE posts (
    post_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    content TEXT,
    post_date TIMESTAMP,
    likes_count INTEGER,
    shares_count INTEGER
);

CREATE TABLE follows (
    follower_id INTEGER,
    following_id INTEGER,
    follow_date DATE
);

-- Sample Data Insertion
INSERT INTO customers VALUES
(1, 'Alice Johnson', 'alice@email.com', '2023-01-15', 'USA', 28),
(2, 'Bob Smith', 'bob@email.com', '2023-02-01', 'Canada', 35),
(3, 'Carol Davis', 'carol@email.com', '2023-01-20', 'UK', 42),
(4, 'David Wilson', 'david@email.com', '2023-03-01', 'USA', 31),
(5, 'Eve Brown', 'eve@email.com', '2023-02-15', 'Germany', 29);

INSERT INTO products VALUES
(1, 'Laptop Pro', 'Electronics', 1299.99, 1),
(2, 'Wireless Mouse', 'Electronics', 29.99, 1),
(3, 'Office Chair', 'Furniture', 249.99, 2),
(4, 'Standing Desk', 'Furniture', 599.99, 2),
(5, 'Notebook', 'Office Supplies', 12.99, 3);

INSERT INTO orders VALUES
(1, 1, '2024-01-15', 1329.98, 'completed'),
(2, 2, '2024-01-16', 29.99, 'completed'),
(3, 1, '2024-01-17', 249.99, 'shipped'),
(4, 3, '2024-01-18', 612.98, 'completed'),
(5, 4, '2024-01-19', 1299.99, 'pending');

INSERT INTO order_items VALUES
(1, 1, 1, 1, 1299.99),
(2, 1, 2, 1, 29.99),
(3, 2, 2, 1, 29.99),
(4, 3, 3, 1, 249.99),
(5, 4, 4, 1, 599.99),
(6, 4, 5, 1, 12.99),
(7, 5, 1, 1, 1299.99);

INSERT INTO departments VALUES
(1, 'Engineering', 2000000.00),
(2, 'Sales', 1500000.00),
(3, 'Marketing', 800000.00),
(4, 'HR', 600000.00);

INSERT INTO employees VALUES
(1, 'Alice Johnson', 1, 95000, '2023-01-15', NULL, 'Senior Engineer'),
(2, 'Bob Smith', 1, 85000, '2023-02-01', 1, 'Software Engineer'),
(3, 'Carol Davis', 2, 75000, '2023-01-20', NULL, 'Sales Manager'),
(4, 'David Wilson', 2, 70000, '2023-03-01', 3, 'Sales Rep'),
(5, 'Eve Brown', 3, 80000, '2023-02-15', NULL, 'Marketing Manager'),
(6, 'Frank Miller', 1, 90000, '2023-01-30', 1, 'Senior Engineer');




-- =============================================================================
-- FUNDAMENTALS
-- =============================================================================

-- Select all customers from USA
SELECT * FROM customers WHERE country = 'USA';

-- Find products with price between $50 and $500
SELECT * FROM products WHERE price BETWEEN 50 AND 500;

-- Get customers whose names start with 'A'
SELECT * FROM customers WHERE name LIKE 'A%';

-- Find orders placed in January 2024
SELECT * FROM orders WHERE order_date >= '2024-01-01' AND order_date < '2024-02-01';

-- Count the total number of customers by country
SELECT country, COUNT(*) as customer_count
FROM customers
GROUP BY country
ORDER BY customer_count DESC;

-- Calculate average product price by category
SELECT category, AVG(price) as avg_price, COUNT(*) as product_count
FROM products
GROUP BY category;

-- Find the total revenue (sum of all order amounts)
SELECT SUM(total_amount) as total_revenue FROM orders;

-- Get the highest and lowest salaries in each department
SELECT d.department_name,
    MAX(e.salary) as max_salary,
    MIN(e.salary) as min_salary,
FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_id, d.department_name;




-- =============================================================================
-- FILTERING AND SORTING SOLUTIONS
-- =============================================================================

-- Find employees hired in 2023 who earn more than $80k
SELECT name, salary, hire_date
FROM employees
WHERE hire_date >= '2023-01-01' AND hire_date < '2024-01-01' AND salary > 80000
ORDER BY salary DESC;

-- Get products that are either Electronics under 100 or Furniture over 200
SELECT product_name, category, price
FROM products
WHERE (category = 'Electronics' AND price < 100) OR (category = 'Furniture' AND price > 200)
ORDER BY category, price;

-- Find customers who registered in Q1 2023 and are from english-speaking countries
SELECT name, registration_date, country
FROM customers
WHERE registration_date >= '2023-01-01' AND registration_date < '2023-04-01' AND country IN ('USA', 'UK', 'Canada', 'Australia')
ORDER BY registration_date;

-- Find product categories with average price > 100
SELECT category, AVG(price) as avg_price
FROM products
GROUP BY category
HAVING avg_price > 100
ORDER BY avg_price DESC;

-- Get departments where the total salary budget exceeds $200k
select d.department_name, SUM(e.salary) as total_salaries, COUNT(e.employee_id) as employee_count, d_budget
FROM departments d
JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name, d.budget,
HAVING total_salaries > 200000
ORDER BY total_salaries DESC;


-- =============================================================================
-- JOINS SOLUTIONS
-- =============================================================================

-- Get customer names with their order details
SELECT c.name, c.email, o.order_id, o.order_date, o.total_amount, o.status
FROM customers c
INNER JOIN orders o on c.customer_id = o.customer_id
ORDER BY c.name, o.order_date

-- Show product names with their order quantities
SELECT p.product_name, p.category, oi.quantity, oi.unit_price, (oi.quantity * oi.unit_price) as line_total
FROM products p
INNER JOIN order_items oi ON p.product_id = oi.order_id
ORDER BY p.product_name;

-- List all customers and their orders, including customers with no orders
SELECT c.name. c.email, o.order_id, o.order_date, o.total_amount
FROM customers.c
LEFT JOIN order o ON c.customer_id = o.customer_id
ORDER BY c.name, o.order_date;

-- Show all employees and their department names
SELECT e.name, e.job_title, e.salary, d.department_name, d.budget
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
ORDER BY d.department_name, e.name;

-- Show all products and any orders, including products never ordered
SELECT p.product_name, p.category, p.price, oi.quantity, oi.unit_price
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
ORDER BY p.product_name;

-- Complete view of customers and orders
SELECT c.name, c.email, o.order_id, o.order_date, o.total_amount
FROM customers c
FULL OUTER JOIN orders o ON c.customer_id = o.customer_id
ORDER BY c.name, o.order_date;

-- Show employees with their managers
SELECT e1.name as employee_name. e1.job_title, e2.name as manager_name, e2.job_title as manager_title
from employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.employee_id
ORDER BY e2.name, e1.name;

-- Get order details with customer names and product names
SELECT c.name as customer_name, o.order_date, p.product_name, oi.order_quantity, oi.unit_price, (oi.quantity * oi.unit_price) as line_total
FROM customers c
JOIN orders o on c.customer_id = o.customer_id
JOIN order_items oi on o.order_id = oi.order_id
JOIN products p on oi.product_id = p.product_id
ORDER BY o.order_date, c.name;

-- Show employee names, departments, and manager names
SELECT e.name as employee_name, d.department_name, m.name as manager_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
LEFT JOIN employees m ON e.manager_id = m.employee_id
ORDER BY d.department_name, e.name;


-- =============================================================================
-- SUBQUERIES SOLUTIONS
-- =============================================================================

-- Find employees earning more than the average salary
SELECT name, salary, job_title, salary - (SELECT AVG(salary) FROM employees) as above_avg_by
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)
ORDER BY salary DESC;

-- Get products more expensive than the average electronics price
SELECT products_name, category, price
FROM products
where price > (SELECT AVG(PRICE) FROM products WHERE category = 'Electronics')
ORDER BY price DESC;

-- Find customers who have placed orders
SELECT c.name, c.email, c.registration_date
FROM customers c
WHERE c.customer_id IN (SELECT DISTINCT customer_id FROM orders)
ORDER BY c.name;

-- Alternative with EXISTS
SELECT c.name, c.email, c.registration_date
FROM customers c
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id)
ORDER BY c.name;

-- Get products that have never been ordered
SELECT p.product_name, p.category, p.price
from products p
WHERE p.product_id NOT IN (SELECT DISTINCT product_id, FROM order_items WHERE product_id IS NOT NULL)
ORDER BY p.product_name;

-- Find each department's highest paid employees
SELECT e1.name, e1.salary, d.department_name
FROM employees e1
JOIN departments d ON e1.department_id = d.department_id
WHERE e1.salary = (SELECT MAX(e2.salary) FROM employees e2 WHERE e2.department_id = e1.department_id)
ORDER BY d.department_name;

-- Get customers with above average order amounts for their country
SELECT c.name, c.country, o.total_amount,
    (SELECT AVG(o2.total_amount)
    FROM orders o2
    JOIN customers c2 ON o2.customer_id = c2.customer_id
    WHERE c2.country = c.country) as country_avg
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.total_amount > (
    SELECT AVG(o2.total_amount)
    FROM orders o2
    JOIN customers c2 ON o2.customer_id = c2.customer_id
    WHERE c2.country = c.country
)
ORDER BY c.country, o.total_amount DESC;

-- =============================================================================
-- WINDOW FUNCTIONS SOLUTIONS
-- =============================================================================

-- Rank employees by salary within each department
SELECT e.name, d.department, e.salary,
    RANK() OVER (PARTITION BY d.department_name ORDER BY e.salary DESC) as salary_rank,
    DENSE_RANK() OVER (PARTITION BY d.department_name ORDER BY e.salary DESC) as dense_rank,
    ROW_NUMBER() OVER (PARTITION BY d.department_name ORDER BY e.salary DESC) as row_num
FROM employees e
JOIN departments d ON e.department_id = d.department_id
ORDER BY d.department_name, e.salary DESC;

-- Number orders chronologically for each customer
SELECT c.name, o.order_date, o.total_amount,
    ROW_NUMBER() OVER (PARTITION BY c.customer_id ORDER BY o.order_date) as order_sequence
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
ORDER BY c.name, o.order_date;

-- Compare each employee's salary to the previous hire in their department
SELECT e.name, d.department, e.hire_date, e.salary,
    LAG(e.salary) OVER (PARTITION BY e.department_id ORDER BY e.hire_date) as prev_salary,
    e.salary - LAG(e.salary) OVER (PARTITION BY e.department_id ORDER BY e.hire_date) as salary_diff
FROM employees e
JOIN departments d ON e.department_id = d.department_id
ORDER BY d.department_name, e.hire_date;

-- Show order amount change from previous order for each customer
SELECT c.name, o.order_date, o.total_amount,
    LAG(o.total_amount) OVER (PARTITION BY o.customer_id ORDER BY o.order_date) as prev_amount,
    o.total_amount - LAG(o.total_amount) OVER (PARTITION BY o.customer_id ORDER BY o.order_date) as amount_change
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
ORDER BY c.name, o.order_date;

-- Show each employee's salary vs highest salary in their department
SELECT e.name, d.department_name, e.salary,
    FIRST_VALUE(e.salary) OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) as dept_max_salary,
    LAST_VALUE(e.salary) OVER (PARTITION BY e.department_id ORDER BY e.salary DESC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as dept_min_salary
FROM employees e
JOIN delartments d ON e.department_id = d.department_id
ORDER BY c.name, o.order_date;

-- Calculate 3-Order moving average of order amounts by customer
SELECT c.name, o.order_date, o.total_amount,
    AVG(o.total_amount) OVER (PARTITION BY o.customer_id ORDER BY o.order_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as moving_avg_3
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
ORDER BY c.name, o.order_date;

-- Running total of sales by month
SELECT DATE_FORMAT(o.order_date,'%Y-%m') as order_month,
    SUM(o.total_amount) as monthly_sales,
    SUM(SUM(o.total_amount)) OVER (ORDER BY DATE_FORMAT(o.order_date,'%Y-%m')) as running_total
FROM orders o
GROUP BY DATE_FORMAT(o.order_date, '%Y-%m')
ORDER BY order_month;

-- Divide employees into salary quartiles
SELECT e.name, d.department, e.salary, NTILE(4) OVER (ORDER BY e.salary) as salary_quartile
FROM employees e
JOIN departments d ON e.department_id = d.department_id
ORDER BY e.salary DESC;

-- Calculate salary percentiles by department
SELECT e.name, d.department_name, e.salary,
    PERCENT_RANK() OVER (PARTITION BY e.department_id ORDER BY e.salary) as salary_percentile,
    ROUND(PERCENT_RANK() OVER (PARTITION BY e.department_id ORDER BY e.salary) * 100, 1) as percentile_rank
FROM employees e
JOIN departments d ON e.department_id = d.department_id
ORDER BY d.department_name, e.salary DESC;


-- =============================================================================
-- CTE SOLUTIONS
-- =============================================================================
