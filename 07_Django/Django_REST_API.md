# REST API 정리

## REST(Representational State Transfer)
- API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
  - 2000년 로이 필딩의 박사학위 논문에서 처음 소개후 네트워킹 문화에 널리퍼짐
- `소프트웨어 아키텍쳐 디자인 제약 모음`(a group of software architecture design constraints)
- REST 원리를 따르는 시스템을 `RESTful` 하다고 부름
- `자원을 정의`하고 `자원에 대한 주소를 지정`하는 전반적인 방법을 서술

## REST에서 자원을 정의하고 주소 지정하는 방법
1. 자원의 식별 : URL
2. 자원의 행위 : HTTP Methods
3. 자원의 표현: 궁극적으로 표현되는 결과물, JSON으로 표현된 데이터를 제공

## REST API
- REST라는 API 디자인 아키텍처를 지켜 구현한 API

## REST framework
- Django를 기반으로 한 웹 API 개발을 쉽게 할 수 있는 프레임워크
- REST 아키텍처 스타일을 따르며, API 뷰, 시리얼라이저, 라우터 등을 제공
- JSON 포맷을 기본으로 지원
- 인증, 권한, 캐싱 등의 고급 기능도 제공
- Django ORM을 이용하여 데이터베이스와 상호작용하고, Django 템플릿 시스템을 사용하여 API 디자인을 쉽게 관리 가능
- 개발자가 보다 효율적으로 웹 API를 개발할 수 있도록 도움