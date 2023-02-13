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
