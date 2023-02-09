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
