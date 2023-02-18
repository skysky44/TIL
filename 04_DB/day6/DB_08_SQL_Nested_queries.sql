-- 문제 1
SELECT productCode , productName , MSRP
FROM products
WHERE MSRP > (
    SELECT AVG(MSRP)
    FROM products
)
ORDER BY MSRP;

-- 문제 2
SELECT customerNumber, customerName
FROM customers
WHERE customerNumber IN (
    SELECT customerNumber
    FROM orders
    WHERE orderDate BETWEEN '2003-01-06' AND '2003-03-26'
)
ORDER BY customerNumber;

-- 문제 3
SELECT productCode , productName , productLine , MSRP
FROM products
WHERE MSRP = (
    SELECT MAX(MSRP)
    FROM products
)
AND productLine = 'Classic cars';

-- 문제 4
SELECT customerNumber, customerName, country
FROM customers
WHERE country = (
    SELECT country
    FROM customers
    GROUP BY country
    ORDER BY COUNT(*) DESC
    LIMIT 1 
)
ORDER BY customerNumber;
-- subqery에서 IN/ALL/ANY/SOME이랑 LIMIT 동시 사용 불가

-- 문제 5

SELECT customerNumber, customerName, COUNT(*) AS order_count
FROM (
    SELECT *
    FROM orders
    INNER JOIN customers USING(customerNumber)
      ) AS t1
GROUP BY customerNumber
ORDER BY order_count DESC
LIMIT 1;
    
-- 문제 6
SELECT DISTINCT productCode , productName
FROM orderdetails
INNER JOIN orders
    USING(orderNumber)
INNER JOIN products
    USING(productCode)
WHERE  DATE_FORMAT(orderDate,'%Y') = '2004'
ORDER BY productCode DESC;


