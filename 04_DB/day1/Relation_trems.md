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
