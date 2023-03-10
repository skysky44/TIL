# DB 1일차

## 관계형 데이터베이스 용어 정리

1. Table (aka Relation)

- 데이터를 기록하는 곳
- 스프레드시트​(?)

2. Field (aka Column, Attribute(속성))​

- 각 필드는 고유한 데이터 형식(타입)이 지정됨
- Column(열): ex. id, 이름, 청구지, 주소지

3. Record (aka Row, Tuple)​

- 구체적인 데이터 값
- Row(행): 1(id), 김민준(이름), 서울(청구지), 강원(주소지)

4. Database (aka Schema)

- table이 여러개 모인 것(테이블이 데이터베이스가 아니라 많은 테이블을 가진 것이 데이터베이스)
- 테이블의 집합(Set of tables)

5. Primary Key(기본 키, PK)

- 각 레코드의 고유한 값
- 레코드의 식별자

6. Foreign Key(외래 키, FK)

- 테이블 필드중 `다른 테이블의 레코드`를 `식별`할 수 있는 키
- 각 레코드에서 서로 다른 테이블 간의 관계를 만드는데 사용

## RDBMS(Relational Database Management System)

- 관계형 데이터 베이스 관리하는 프로그램
- 데이터 저장 및 관리를 용이하게 함
- 데이터베이스와 사용자 간 인터페이스
- ex. MySQL, Oracle
- MySQL 구조 : Table < Database < Database Server(MySQL)
- RDBMS는 온오프 서버(Database Server)로 된 경우도 있고 파일로 된 경우 있음
- `테이블로 구조화` 되어 있음
- `외래키를 이용`해서 `테이블 간 관계를 형성`함

## SQL(Structured Query Language)

- 구조화된 질의 언어 : 단순하게 질의만을 수행하는 것이 아니라 데이터베이스의 모든 작업을 통제하는 비절차적(Non-procedural) 언어

## 참고

![image](https://user-images.githubusercontent.com/110805149/217444963-4bee77e2-b337-4ae0-9b36-7ccf88e2fe13.png)

# DB 2일차

## SQL(Structure Query Language)

- 테이블의 형태로 구조화된 관계형 데이터베이스에게 요청을 질의(요청)
- 컴퓨터와의 대화: 프로그래밍 언어 / 관계형데이터베이스와의 대화: SQL
- 데이터베이스 이미지는 디스크드라이브 모양
- SQL Syntax
  - 키워드는 대문자로 작성(권장, 명시적 구분)
  - 끝나면 세미콜론 필요

## SQL Statements(SQL문)

```sql
SELECT column_name FROM table_name;
```

- 해당 예시 코드는 SELECT Statement라 부름
- select, from 2개의 키워드로 구성

- SQL Statements 유형
  - DDL: 데이터 정의(구조)
    - 데이터의 기본 구조 및 형식 변경
    - CREATE, DROP, ALTER
  - DQL: 데이터 검색(R)
    - SELECT
  - DML: 데이터 조작(CUD)
    - 추가,수정, 삭제
    - INSERT, UPDATE, DELETE
  - DCL: 데이터 제어(컨트롤, 권한, 계정)
    - COMMIT, ROLLBACK, GRANT, REVOKE
  - DQL(데이터 검색)이 가장 중요
    - 어떻게 원하는 데이터를 가공해서 검색할 것인가 중요

## 용어 정리

- Query
  - 일반적으로 SQL로 작성하는 코드를 쿼리문(SQL문)이라 함
- SQL 표준
  - 미국 국립 표준협회(ANSI)와 국제 표준화 기구(ISO)의해 표준이 채택
  - 다만 RDBMS별 독자적인 기능에 따라 표준 벗어나는 문법도 존재

## Single Table Queries

### Querying data

```sql
SELECT
    column_name
FROM
    table_name;
```

- SELECT문 테이블의 데이터를 조회 및 반환
- SELECT \*(asterisk) 사용 모든 필드 선택

### Sorting data

```sql
SELECT
    column_name1 AS '별칭'
    column_name2 * column_name3
FROM
    table_name;
ORDER BY
    column1[ASC|DESC]
```

- ASC: 오름차순(기본값)
- DESC: 내림차순
- 두번 정렬하면 일단 첫번째 기준 정렬하고 중복되는 항목에 한해 두번째 기준으로 정렬
- AS: 별칭을 붙이는 것, result에 필드명으로 보여줌
- 사칙 연산도 가능
  - 덧셈: +
  - 뺄셈: -
  - 곱셈: \*
  - 나눗셈: /
  - 나머지: %

## 참고

- NULL 데이터 없음
- --: 주석 처리
- '' 문자열 표시 해야 함(정확하게)
- 워크벤치 탭 설정
  - General Editors
  - Tab key inserts spaces instead of tabs
- Beautify Query: 워크벤치에서 Ctrl + B -> 정렬(들여쓰기 등)

# DB 3일차

## Filtering data

- Clause(절)

  - DISTINCT: 조회 결과에서 중복된 레코드 제거, SELECT 바로 뒤에 씀

  ```sql
  SELECT DISTINCT
  ```

  - WHERE: 조회 시 특정 검색 조건 지정

  ```sql
  SELECT
    lastName, firstName, officeCode
  FROM
      employees
  WHERE
      officeCode BETWEEN 1 AND 4;

  SELECT
    lastName, firstName, officeCode
  FROM
      employees
  WHERE
    officeCode IN (1,3,4);
  --     officeCode = 1
  --     OR officeCode = 3
  --     OR officeCode = 4 ;
  ```

  - LIMIT: 조회하는 레코드 수를 제한

  ```sql
  SELECT
      firstName, officeCode
  FROM
      employees
  ORDER BY officeCode DESC

  LIMIT 3 , 5;
  -- offset3, 이면 3 건너뛰고 4번째부터 5개
  -- LIMIT [offset,] row_count;
  -- LIMIT 5 OFFSET 3;도 가능
  ```

- Operator(연산자)
  - BETWEEN: 숫자 범위에 해당하는지 확인
  - IN: 값이 특정 목록 안에 있는지 확인
  - LIKE: 값이 특정 패턴에 일치하는지 확인 - ildcard Characters
    % 0개 이상의 문자열과 일치하는지 확인
    \_ 단일 문자와 일치하는지 확인
  - Comparison(비교 연산자)
  - Logical(논리 연산자)

## Grouping data

- GROUP BY: 레코드를 그룹화하여 요약본 생성 with 집계 함수(Aggregation Functions)
- Aggregation Functions: 값에 대한 계산을 수행하고 단일한 값을 반환하는 함수
  - ex. SUM, AVG, MAX, MIN, COUNT
- GROUP BY후 조건이 있다면 HAVING(WHERE 아닌) 사용
- HAVING: GROUP BY 없으면 WHERE처럼 동작

```sql
SELECT
    country, AVG(creditLimit)
FROM
    customers
-- WHERE 안됨
--     AVG(creditLimit) > 80000
GROUP BY
    country
HAVING
    AVG(creditLimit) > 80000;


```

## SELECT statement 실행 순서

- FROM -> WHERE -> GROUP BY -> HAVING -> SELECT ->ORDER BY -> LIMIT

1. 테이블에서(FROM)
2. 특정 조건에 맞춰(WHERE)
3. 그룹화하고(GROUP BY)
4. 만약 그룹중에 조건이 있다면 맞추고(HAVING)
5. 조회하여(SELECT)
6. 정렬하고(ORDER BY)
7. 특정 위치의 값을 가져온다(LIMIT)

## 참고

- MyWQL 오름차순 정렬 시 NULL이 NULL 아닌 값보다 먼저 나옴
- 코드가 복잡해지면 AS로 별칭 많이 사용함
- 연도별 그룹화하는 법
  ```sql
  SELECT
     YEAR(orderDate) AS 'year', COUNT(orderNumber)
  FROM
      orders
  GROUP BY
      YEAR(orderDate);
  ```

# DB 4일차

## Managing Tables

- 데이터가 들어가는 테이블 구조에 대한 정의 변경
- SQL Statements 유형
  - DDL(Data Definition Language): 데이터의 기본 구조 및 형식 변경
  - CREATE, DROP, ALTER
- 하나의 필드에 여러가지 데이터 타입 안됨
- 필드이름과 데이터 타입 간에 공백 구분
- 숫자, 문자, 날짜 3가지 타입이 대표적
- CHAR(50): 무조건 50자를 채움. 나머지를 공백으로 채움
- VARCHAR(50): (가변길이) 들어온 길이만큼만 채움
- TEXT: 길이 정하지 않는 타입

### Create a table

```sql
CREATE TABLE examples (
    examId INT AUTO_INCREMENT,
    lastname VARCHAR(50) NOT NULL,
    firstname VARCHAR(50) NOT NULL,
    PRIMARY KEY (examId) -- primary key  편의상 최하단에 쓰는 것
);
-- 테이블 구조 확인
SHOW COLUMNS FROM examples;
```

- 각 필드 데이터 타입 작성
- 테이블 및 필드 제약조건(constraints) 작성
  - NOT NULL: 해당 필드 NULL 저장 못하도록 지정
  - PRIMARY KEY 해당 필드를 기본 키로 지정
- 속성
  - AUTO_INCREMENT
    - 기본 키 필드에 사용(고유 숫자 부여)
    - 시작 값 1, 값 생략시 자동 1씩 증가
    - 이미 사용한 값 재사용하지 않음(1,2,3에서 2 지우고 새로 입력하면 4부터 입력)
    - 기본적으로 NOT NULL 제약 조건 포함

### Delete a table

```sql
DROP TABLE examples; -- (DELETE 아니고 DROP)
```

### Modifying table fields

- ALTER TABLE: 하나로 (필드) 생성, 수정, 삭제 가능

- ALTER TABLE ADD : 필드 추가
- ALTER TABLE MODIFY : 필드 속성 변경
- ALTER TABLE CHANGE COLUMN : 필드 이름 변경(change column은 modify 기능도 포함)
- ALTER TABLE DROP COLUMN : 필드 삭제

```sql
ALTER TABLE examples
ADD age INT NOT NULL,
ADD address VARCHAR(100) NOT NULL;

ALTER TABLE examples
MODIFY address VARCHAR(50) NOT NULL;

ALTER TABLE examples
MODIFY lastname VARCHAR(10) NOT NULL,
MODIFY firstname VARCHAR(10) NOT NULL;

ALTER TABLE examples
CHANGE COLUMN state2 state VARCHAR(100) NOT NULL;

ALTER TABLE examples
DROP COLUMN address;

ALTER TABLE examples
DROP COLUMN state,
DROP COLUMN age;
```

## Modifying Data

- SQL Statement 유형
  - DML(Data Manipulation Language)
  - 데이터 조작(추가, 수정, 삭제)
  - INSERT, UPDATE, DELETE

### Insert data into table

- INSERT INTO
  - INSERT INTO 절 다음에 테이블 이름과 괄호 안에 필드 목록 작성
  - VALUES 키워드 다음 괄호 안에 삽입할 값 목록을 작성
  - 싱크 맞아야 함(괄호안)

```sql
INSERT INTO
    articles (title, content, createdAt)
VALUES
    ('hello', 'world', '2000-01-01');

INSERT INTO
    articles (title, content, createdAt)
VALUES
    ('title1','content1','1900-01-01'),
    ('title2','content2','1800-01-01'),
    ('title3','content3','1700-01-01');

INSERT INTO
    articles (title, content, createdAt)
VALUES
    ('mytitle', 'mycontent', CURDATE());
```

- UPDATE
  - SET 절 다음에 수정할 필드와 새 값을 지정
  - WHERE절 수정할 레코드를 지정하는 조건 작성

```sql
UPDATE
    articles
SET
    title = 'newTitle'
WHERE
    id = 1;

UPDATE
    articles
SET
    title = 'newTitle2',
    content = 'newContent2'
WHERE
    id = 2;

UPDATE
    articles
SET
    content = replace(content, 'content', 'TEST');

SET SQL_SAFE_UPDATES = 0; -- 안전모드해제
```

- DELETE
  - DELETE FROM 절 다음에 테이블 이름 작성
  - WHERE 절에서 삭제할 레코드 지정(지정 안하면 모든 레코드 삭제)

```sql
DELETE FROM articles
WHERE
    id = 1;

SELECT * FROM articles
ORDER BY createdAt DESC;

DELETE FROM articles
ORDER BY createdAt DESC
LIMIT 2;
```

## 참고

- not null 사용 해야 할까?
  - 별말 없으면 NOT null 그냥 써 둠
  - 파이썬 등 다른 언어와 연동을 위해 0이나 빈문자열로 대체(null쓰면 타입을 또 바꿔야 해서)
- 안전모드 해제
  ```sql
  set sql_safe_updates=0;
  ```
- 정리
  - CREATE TABLE
  - DROP TABLE
  - ALTER TABLE
    - ADD
    - MODIFY
    - CHANGE
    - DROP
  - INSERT INTO VALUES
  - UPDATE SET
  - DELETE FROM

# DB 5일차

## Multi Table Queries

## Joining tables

### JOIN 종류

- INNER JOIN
- OUTER JOIN
  - LEFT JOIN
  - RIGHT JOIN

### INNER JOIN

- 두 테이블에서 `값이 일치하는 레코드만` 결과로 반환
- FROM 절 뒤 메인테이블 지정(LEFT)
- INNE JOIN 절 뒤 조인할 테이블 지정(RIGHT)
- ON 키워드 이후 조인 조건 작성
  - 필드가 양쪽 모두 존재할 경우 USING(필드명) 사용

```SQL
SELECT articles.id , content, name -- 겹칠 때 테이블명.id
FROM articles
INNER JOIN users
    ON articles.userId = users.id;
```

### LEFT JOIN

- 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블 모든 레코드 반환
- 왼쪽 테이블 한 개 레코드에 여러 개 오른쪽 테이블 레코드가 일치하면 해당 왼쪽 레코드 여러번 표시

```SQL
SELECT
    contactFirstName, orderNumber, status
FROM
    customers
LEFT JOIN orders
    ON customers.customerNumber = orders.customerNumber
WHERE orderNumber IS NULL;
```

### RIGHT JOIN

- 왼쪽 테이블의 일치하는 레코드와 함께 오른쪽 테이블 모든 레코드 반환
- 오른쪽 테이블 한 개의 레코드에 여러개의 왼쪽 레코드가 일치할 경우 해당 오른쪽 레코드 여러 번 표시

```SQL
SELECT
    employeeNumber, firstName, customerNumber, contactFirstName
FROM
    customers
RIGHT JOIN employees
    ON  employees.employeeNumber = customers. salesRepEmployeeNumber
WHERE customerNumber IS NULL;
```

## JOIN 정리

![image](https://user-images.githubusercontent.com/110805149/219874544-52e329a7-b6da-491f-893d-6acf51f55480.png)

- 합집합 왼쪽 UNION 오른쪽 (중복 삭제)
- 중복 유지하고 싶으면 UNION ALL

## 참고

- 관계형 데이터베이스 : JOIN 중요함
- JOIN 할 때 길면 복잡해서 AS를 많이 사용함

# DB 6일차

## Nested queries(중첩 쿼리)

### Subquery: 단일 쿼리문에 여러 테이블 데이터 결합

- 조건에 따라 하나 이상의 테이블에서 데이터 검색하는 경우 사용
- `FROM 절` 에서 사용하는 `subquery`는 별도의 파생된 테이블로 간주 되기 때문에 MYSQL에서는 반드시 `별칭 지정` 필요

```sql
SELECT customerNumber, amount, contactFirstName
FROM (
    SELECT contactFirstName, amount, customerNumber
    FROM payments
    INNER JOIN customers
    USING (customerNumber)
) AS findName -- 별칭 지정
WHERE amount = (
    SELECT MAX(amount)
    FROM payments
);
```

### EXISTS operator

- 쿼리문에서 반환되 레코드 존재 여부 확인
- subquery가 하나 이상의 행을 반환 하면 EXISTS 연산자는 TRUE 반환 그렇지 않으면 FALSE 반환
- 주로 WHERE 절에서 subquery 반환 값 존재 여부 확인에 사용

```sql
SELECT customerNumber, customerName
FROM customers
WHERE
    EXISTS(
        SELECT *
        FROM orders
        WHERE customers.customerNumber = orders.customerNumber
);
```

### CASE statement

- SQL 문에서 조건문 구성

```sql
CASE case_value
  WHEN when_value1 THEN statements
  WHEN when_value2 THEN statements
  ...
  [ElSE else_statements]
END CASE;
```

- case_value와 when_value1가 동일한 것을 찾을 때까지 순차적 비교 -> 찾으면 THEN 절 코드 실행
- 동일 값 못찾으면 ELSE 절 코드 실행(ELSE절 없을때 동일 값 못 찾으면 오류 발생)

```SQL
SELECT contactFirstName, creditLimit,
    CASE
        WHEN creditLimit > 100000 THEN 'VIP'
        WHEN creditLimit > 70000 THEN 'Platinum'
        ELSE 'Bronze'
    END AS grade
FROM customers;
```

## 참고

- 한 개의 글에 여러개의 댓글 가능, 댓글에 여러 개 게시글 가능

  - 글 여러 개 : 유저 1, 댓글 여러 개 : 글 1
  - N:1관계
  - FK(외래키)는 N쪽에 성립한다

- 일반적 정렬은 힘든 작업 따라서 서브쿼리 쓰는게 더 단순하게 이용 가능
- SQL 사용법
  - DATEDIFF('2023-03-01', '2023-03-28') / TIMESTAMPDIFF(DAY , '2023-03-01', '2023-03-28');
  - HOUR(DATETIME)하면 시간만 꺼낼 수 있다
  - DATE_FORMAT(DATETIME, '%Y-%m-%d')
  - IFNULL( Column명, 'Null일 경우 대체 값')

# DB 7일차

## Transactions

- 여러 쿼리문을 묶어서 하나의 작업처럼 처리하는 방식(다성공 또는 다 실패)
- ex. 계좌이체(인출&입금)
- 쪼개질 수 없는 업무처리 단위
- ALL or NOTHING

```SQL
START TRANSACTION; -- 시작을 알림
state_ments;
...
[ROLLBACK|COMMIT] -- 정상적으로 완료되면 COMMIT 아니면 ROLLBACK
```

- 커밋이나 롤백 전 임시 데이터 영역에 머무름
- 기본적으로 MySQL은 자동 변겨 사항 COMMIT 함

```SQL
SET autocommit = 0; -- 비활성화


START TRANSACTION;

INSERT INTO users (name)
VALUES ('harry'), ('test');

SELECT * FROM users;

-- ROLLBACK;

COMMIT;
```

## Triggers

- 특정 이벤트(INSERT, UPDATE, DELETE)에 대한 응답으로 자동 실행되는 것(SELECT는 안됨)

```SQL
DELIMITER //
CREATE TRIGGER trigger_name
  {BEFORE|AFTER} {INSERT|UPDATE|DELETE}
  ON table_name FOR EACH ROW
BEGIN
  trigger_body;
END//
DELIMITER ;
```

- 각 레코드의 어느 시점에 트리거가 실행될지 결정(삽입, 수정, 삭제 전/후): 커밋 (최종수정) 전이냐 후냐 생각
- ON 키워드 뒤에 트리거가 속한 테이블의 이름을 지정
- 트리거가 활성화될 때 실행할 코드를 trigger_body에 지정
- 여러 명령문을 실행하려면 BEGIN END 키워드로 묶어서 사용
- DELIMITER : 하나하나 완성된 구문은 ; 으로 종료해야되는데 임시로 종료표시를 바꿔줌

```SQL
DELIMITER // -- 여기서부터 종료 조건은 이제'//'
CREATE TRIGGER myTrigger
-- 언제?
    BEFORE UPDATE
    ON articles FOR EACH ROW
BEGIN  -- 여러개 일 때
    SET NEW.updatedAt = current_time(); -- 여기 때문에 ;를 // 로
END//
DELIMITER; -- 여기서부터 다시 ;로 복구
```

## 참고

- 추가 명령문 참고

```SQL
-- 트리거 목록 확인
SHOW TRIGGERS;

-- 트리거 삭제
DROP TRIGGER trigger_name;
```

- 트리거 생성 시 에러

```SQL
-- 실행중인 프로세스 목록 확인
SELECT *FROM information_schema.INNODB_TRX;
-- 특정 프로세스의 trx_mysql_thread_id 삭제
KILL [trx_mysql_thread_id1];
```

- 워크벤치 왼쪽 파란점: 구문 표시
- A-B : A에만 해당되고 B에는 속하지 않는 레코드(?)

```SQL
SELECT ANIMAL_ID, O.NAME
FROM ANIMAL_INS AS I
RIGHT JOIN ANIMAL_OUTS AS O
    USING(ANIMAL_ID)
WHERE
    I.ANIMAL_ID IS NULL -- 여기 참고
ORDER BY
    ANIMAL_ID;
```

# DB 8일차

## Normalization(정규화)

- RDB 설계 단계에서 `중복을 최소화`하여 데이터를 `구조화`하는 과정
  - 구조화: 크고, 제대로 조직되지 않은 테이블의 관계를 작고 잘 조직된 테이블과 관계들로 나누는 것
- 기본적으로는 3정규화까지 진행. 4,5정규화도 있음

- 제1정규화

  - 각 필드에 하나의 값만 저장
  - 유사 정보 저장하는 두개 필드 안 됨

- 제2정규화

  - 키 값을 이용해 데이터를 특정 지을수 있는 것(함수 종속성)을 찾아 테이블 분할

- 제3정규화

  - 기본 키 이외의 부분에서 중복이 없는지를 조사하여 테이블을 분할

- 정규화 목적
  - 하나의 데이터는 한 곳에만 위치
  - 테이블 간 관계는 키로 형성
  - 데이터 변경해도 한 곳만 변경하는 구조

## Data Modeling

- 데이터베이스 시스템을 `시각적`으로 표현하는 프로세스

### ER(Entity-Relationship) Diagram

- 구성요소

  - Entity : Table
  - Attribute : Field
  - Relation : PK,FK

- Relationship 표현 방법

  - Cardinality: 1:1, N:1, N:M
  - Optionality(선택가능성): 필수&선택

- 데이터 모델링 중요성
  - 개발 오류 감소
  - 설계 및 생성 속도와 효율성 촉진
  - 문서화 및 시스템 설계 일관성 조성
  - 엔지니어와 비즈니스 팀 간 커뮤니케이션 촉진

# 참고

- ERD 작성 툴
  - draw.io
  - http://aquerytool.com
  - https://www.erdcloud.com : 실시간 공동 작업 가능
- 우아콘2020 배달의민족 마이크로서비스 여행기
  - https://www.youtube.com/watch?v=BnS6343GTkY
