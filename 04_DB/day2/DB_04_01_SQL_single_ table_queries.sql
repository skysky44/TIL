-- 문제 1
SELECT
    *
FROM
    employees;

-- 문제 2
SELECT
    customerNumber, customerName, phone
FROM
    customers;

-- 문제 3
SELECT
    firstName, lastName, email
FROM
    employees
ORDER BY
    firstName;

-- 문제 4
SELECT
    firstName AS '이름', lastName AS '성', email AS '이메일'
FROM
    employees
ORDER BY
    이름;

-- 문제 5
SELECT
    employeeNumber , lastName , firstName , officeCode , jobTitle 
FROM
    employees
ORDER BY
    jobTitle DESC,
    officeCode DESC;

-- 문제 6
SELECT
    *
FROM
    orderdetails
ORDER BY
    quantityOrdered,
    priceEach;
    
-- 문제 7
SELECT 
    customerNumber, country, contactFirstName
FROM
    customers
ORDER BY
    country , contactFirstName DESC;
    
-- 문제 8
SELECT 
    productCode,
    quantityInStock,
    buyPrice,
    quantityInStock * buyPrice
FROM
    products
ORDER BY quantityInStock * buyPrice DESC; 
    
	