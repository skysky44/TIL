# 나만의 Workbench 활용 가이드

## Workbench 활용 MySQL 접속 방법

1. Workbench 실행
2. MySQL Connections +
3. Connection Name 입력, Connection Method 입력(표준TCP/IP?)
4. Hostname 입력(기본값:'127.0.0.1' or 'localhost' )
5. Test Connection 클릭해서 test
6. 완료

## 실습 데이터베이스에 대한 쿼리(Query)문 작성 및 쿼리문 실행 방법

1. 원하는 DB 선택(SCHEMAS안에서)
2. +SQL 아이콘 클릭(DB 선택)
3. SQL 쿼리문 작성(Query창) 또는 마우스 우클릭도 가능(?)
4. Query창 번개 아이콘 클릭
5. result grid창과 output창 확인

## 쿼리(Query)문

### SELECT

```
SELECT [열이름]
    FROM [테이블이름]
```

- SELECT \* FROM [테이블이름]
  - 테이블 안의 모든 행과 열 추출

### USE

- USE [데이터베이스 이름]
  - 사용하고 싶은 데이터베이스 지정

### SHOW

- SHOW DATABASES;
  - 현재 서버 DB 목록 확인
- SHOW TABLE STATUS;
  - 테이블 목록+상태 확인하기
- SHOW TABLES;
  - 테이블 목록만 확인하기
