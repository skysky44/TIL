
-- 문제 1
SHOW COLUMNS FROM employees;
SHOW COLUMNS FROM offices;
SELECT * from employees;
SELECT * from offices;

SELECT 
    employeeNumber, lastName, firstName, city
FROM
    employees AS t1
INNER JOIN offices AS t2
    ON t1.officeCode = t2.officeCode
ORDER BY
    employeeNumber;

-- 문제 2
SELECT 
    customerNumber, officeCode, customers.city, offices.city
FROM
    customers
LEFT JOIN offices
    ON customers.city = offices.city
ORDER BY customerNumber DESC;

-- 문제 3
SELECT
    customerNumber , officeCode , customers.city , offices.city
FROM
    customers 
RIGHT JOIN offices
    ON customers.city = offices.city
ORDER BY customerNumber DESC;

-- 문제 4
SELECT
    customerNumber , officeCode , customers.city , offices.city
FROM
    customers 
INNER JOIN offices
    ON customers.city = offices.city
ORDER BY customerNumber DESC;

-- 문제 5
-- 문제 2, 문제 3, 문제 4 의 조회 결과가 다른 이유를 작성하시오.
/*세 문제 모두 테이블 customers 와 테이블 offices 를 city 기준으로 JOIN했다.
문제 2번은 테이블 customers의 모든 레코드와 테이블 offices에서 join 된 데이터를 출력했다.
그래서 offices의 city에 NULL이 포함 되어있다.
문제 3번은 테이블 offices의 레코드를 기준으로 연결된 테이블 customers의 데이터만 출력했다.
그래서 customerNumber와 테이블 customer의 city에 NULL이 존재한다.
문제 4번은 INNER JOIN을 사용했기 때문에 city 기준으로 JOIN 했을 때
테이블 customers와 테이블 offices 양쪽 모두 존재하는 레코드만 출력되었다. */

-- 문제 6
SELECT
    customerNumber , officeCode , customers.city , offices.city
FROM
    customers 
LEFT JOIN offices
    ON customers.city = offices.city
UNION
SELECT
    customerNumber , officeCode , customers.city , offices.city
FROM
    customers 
RIGHT JOIN offices
    ON customers.city = offices.city
ORDER BY customerNumber DESC;

-- 문제 7
SHOW COLUMNS FROM orderdetails;
SHOW COLUMNS FROM orders;
SELECT * from orderdetails;
SELECT * from orders;

SELECT
    t1.orderNumber , orderDate
FROM
    orderdetails AS t1
INNER JOIN orders AS t2
    ON t1.orderNumber = t2.orderNumber
ORDER BY
    orderNumber;

-- 문제 8
SELECT
    orderNumber , orderdetails.productCode , productName
FROM orderdetails
INNER JOIN products
    ON orderdetails.productCode = products.productCode
ORDER BY
    orderNumber;

-- 문제 9
SHOW COLUMNS FROM orderdetails;
SHOW COLUMNS FROM orders;
SHOW COLUMNS FROM products;

SELECT
    orderdetails.orderNumber , orderdetails.productCode , orderDate, productName
FROM orderdetails
INNER JOIN orders
    ON orderdetails.orderNumber = orders.orderNumber
INNER JOIN products
    ON orderdetails.productCode = products.productCode
ORDER BY
    orderNumber;

    
    




