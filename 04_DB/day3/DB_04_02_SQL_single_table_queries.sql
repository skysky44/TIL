-- 문제 1
SELECT DISTINCT
    country
FROM
    customers
ORDER BY
    country;

-- 문제 2
SELECT DISTINCT
    state
FROM
    customers
ORDER BY 
    state DESC;

-- 문제 3
SELECT 
    customerNumber, customerName, country
FROM
    customers
WHERE
    country != 'USA'
ORDER BY
    customerNumber DESC;
    
-- 문제 4
SELECT 
    *
FROM
    offices
WHERE
    city ='Paris';

-- 문제 5
SELECT 
    customerNumber, customerName, state
FROM
    customers
WHERE
    country = 'USA' AND state = 'CA'
ORDER BY
    customerName DESC;

-- 문제 6
SELECT 
    customerNumber, customerName, country, state
FROM
    customers
WHERE
    country = 'USA'
    AND state IN ('CA','NY')
ORDER BY
    customerNumber DESC;

-- 문제 7
SELECT 
    customerNumber, customerName, state
FROM
    customers
WHERE
    state IN ('CA','NY','CT','PA')
ORDER BY
    customerNumber DESC;

-- 문제 8
SELECT
    productCode, productName, quantityInStock
FROM
    products
ORDER BY
     quantityInStock;
     
-- 문제 9
SELECT
    productCode, productName, quantityInStock
FROM
    products
WHERE
    quantityInStock BETWEEN 2000 AND 3000
ORDER BY
     quantityInStock desc;
     
-- 문제 10
SELECT 
    customerNumber, customerName, phone
FROM
    customers
WHERE
    phone LIKE '%555';
    
-- 문제 11
SELECT
    productCode , quantityInStock
FROM
    products
ORDER BY
    quantityInStock
LIMIT 5;

-- 문제 12
SELECT
    jobTitle, COUNT(*) AS count_job
FROM
    employees
GROUP BY
    jobTitle
ORDER BY
    COUNT(*) DESC,
    jobTitle DESC;

-- 문제 13
SELECT 
    country, COUNT(*) AS count_country
FROM
    customers
GROUP BY
    country
ORDER BY
    count(*) DESC,
    country DESC;

-- 문제 14
SELECT
    orderNumber, SUM(quantityOrdered*priceEach) AS total
FROM
    orderdetails
GROUP BY
    orderNumber
ORDER BY
    total DESC;

-- 문제 15
SELECT 
   YEAR(orderDate) AS 'year', COUNT(orderNumber)
FROM
    orders
GROUP BY
    YEAR(orderDate);
    
-- 문제 16
SELECT 
    productLine, MAX(quantityInStock) AS max_stock
FROM
    products
GROUP BY productLine
HAVING
    MAX(quantityInStock) < 9000;

-- 문제 17
SELECT 
    ordernumber,
    SUM(quantityOrdered) AS itemsCount,
    SUM(priceEach * quantityOrdered) AS total
FROM
    orderdetails
GROUP BY orderNumber
HAVING
    SUM(quantityOrdered) >= 500
    AND SUM(priceEach * quantityOrdered) >= 50000;