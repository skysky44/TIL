## Django 1일차
### Framework
- Frame + work
- 웹 애플리케이션의을 빠르게 개발하도록 도와주는 도구
- 개발에 필요한 기본 구조, 규칙, 라이브러리 등 제공
- 필수적 개발에만 집중 가능, 개발 속도 높임, 유지보수 용이

### Django
- 대규모 서비스에도 안정적 서비스 제공
- django 사용해서 서버 구현

### 클라이언트와 서버(Client & Server)
- Client: 서비스 요청하는 주체
- Server: 클라이언트의 요청에 응답하는 주체

### 개발 환경 설정 단계(가상환경 vevn)
  1. 기본 폴더 생성
  2. 폴더 안에서 git bash 실행
  3. 파이썬으로 venv(virtual environments) 생성
    - 폴더명은 venv로(권장.강제)

  ```bash
  python -m venv venv
  ```
  4. venv 실행(스위치 ON)
    - tab키 활용 - 자동입력 사용(오타방지), pip list로 확인

  ```bash
  source venv/Scripts/activate
  ```
  
  5. Django 설치
    - 3.2.18(LTS버전)
  ```bash
  pip install Django==3.2.18
  ```
  6. 의존성 파일 생성(패키지 설치시 마다 진행)
    - requirements s 복수형!!
  ```bash
  pip freeze > requirements.txt
  ```

  7. gitignore 추가
    - 여기부터는 vscode에서 하는 게 편한것 같기도(아니면 처음부터) ctrl + shift+ p interpreter python
    - venv 폴더 추가!!!
    - 이전 단계에서해도 무방
    - gitignore.io 활용

  8. git init 
  ```bash
  git init
  ```

  9. Django 프로젝트 시작
    - 주의: . 안쓰면 manage.py 다른폴더에 생김(. 현재위치 의미)
  ```bash
  Django-admin startproject [프로젝트파일명] .
  ```

  10. 서버 실행하기
    - manage.py 위치에서 실행
    - 주소클릭 로켓화면 확인
    - 서버종료: ctrl + c
  
  ```bash
  python manage.py runserver
  ```

## 가상환경 사용 이유
- 의존성 관리: 프로젝트마다 라이브러리 및 패키지를 독립적 사용
- 팀 프로젝트 협업: 버전간 충돌 방지
- 우리가 사용하는 일반적 환경은 글로벌 환경

## LTS(Long-Term Support)
- 장기간 지원되는 안정적 버전
- Django의 경우 현재 3.2.xx

## 참고
- 가상환경에 들어간다고 생각하기보단 가상환경 on/off 개념으로 생각
- Django projectstart 할 때 마지막 . 잊지않도록 해야함
- deactivate 입력하면 가상환경 꺼짐
- 파이썬에서는 안되는데 장고에서는 trailing comma 허용(마지막 ,)
- 프레임워크 공부할 때 내부코드나 왜이렇게 되는지 너무 깊게 파고 들면 힘들어짐. 규칙으로 받아들여야 함.
- Django는 상대적으로 규칙이 많고 어려운 프레임워크는 아님
- Django mvc

## Django 2일차
- Django project: 애플리케이션의 집합(DB 설정, URL 연결, 전체 앱 설정 등 처리)
- Django application: 독립적으로 작동하는 기능 단위 모듈(각자 특정 기능 담당, 다른 앱들과 하나의 프로젝트 구성, MTV 패턴 해당하는 파일 및 폴더 담당)
- 블로그를 만든다면 프로젝트: 블로그(전체설정 담당) / 앱: 게시글, 댓글, 카테고리 회원 관리 등 (DB, 로직, 화면)

### 앱 생성 & 등록

1. 앱 생성
  - 앱 이름 `복수형` 권장
```bash
python manage.py startapp articles
# articles: 앱이름
```

2. 앱 등록
  - settings.py 파일에서 'articles'(앱이름) 추가
```python
# Application definition
INSTALLED_APPS = [
    # 앱 등록 권장 순서

    # 1. local app
    'articles',
    
    # 2. 3rd party app(설치를 통해 추가하는앱)
    
    # 3. 기본 django app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
  - 반드시 생성후 등록. 그렇지 않으면 앱 생성 안 됨.


### 디자인 패턴
- 소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책
- 공통적 문제를 해결하는 형식화 된 관행

#### MVC 디자인 패턴
- Model - View - Controller
- 애플리케이션 구조화하는 대표적 패턴
- 데이터, 사용자 인터페이스, 비즈니스 로직을 분리
- 시각적 요소와 뒤에서 실행 되는 로직을 서로 영향 없이, `독립적이고 쉽게 유지보수` 가능

  ![image](https://user-images.githubusercontent.com/110805149/226540868-ed5798cf-5a59-4384-8f2c-2a9bdb2ea7bd.png)

### MTV 디자인 패턴
- Model - Template - View
- django에서 애플리케이션을 구조화 하는 패턴
- 기존 MVC 패턴과 동일하지만 명칭은 다르게 정의

- MVC : Model - View - Controller
- MTV : Model - Template - View

### 프로젝트 구조
- settings. py: 프로젝트의 모든 설정 관리
- urls.py: url과 view 연결

- 아래는 우선 참고만(현재 단계 별도수정 안함)
- _init_.py: 해당폴더를 패키지로 인식하도록 설정
- asgi.py: 비동기식 웹서버와의 연결 관련설정
- wsgi.py: 웹서버와의 연결 관련설정
- manage.py: django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티

### 앱 구조
- admin.py: 관리자용 페이지 설정
- models.py: DB와 관련된 Model 정의, MTV 패턴의 M
- views.py: HTTP 요청을 처리하고 해당 요청에 대한 응답 반환, MTV 패턴의 V

- 아래는 우선 참고만(현재 단계 별도수정 안함)
- apps.py: 앱의 정보가 작성된 곳
- tests.py: 프로젝트 테스트 코드를 작성하는 곳

### 요청과 응답
- 요청 > urls.py > view.py > templates > 응답

#### URLs
```python
from articles import views
# 1. articles 앱에서 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', views.index),
# 2. path에 url 추가하기, 마지막 / 필수
# views.py 안에 index 함수

]
```

#### Views
```python
from django.shortcuts import render
# render 페이지를 만들어주는 함수


# Create your views here.
# 특정 기능을 수행하는 view 함수를 만듦
def index(request):
    return render(request, 'articles/index.html')
# return 응답(메인페이지)
#  'index.html'안에는 경로가 문자열로 들어가야함 'articles/index.html'
```

#### Templates
- articles 폴더 안에 `templates 폴더 생성`
- templates 폴더안에 템플릿 페이지(html 등) 작성

  ![image](https://user-images.githubusercontent.com/110805149/226558374-5b803e38-e985-4456-857e-177c69886645.png)


## 참고
- Django(프레임워크, 백엔드)는 json을 만들고 그 json을 프론트엔드 프레임워크가 받아서 사용
- 그래서 templates가 자동생성 안되는 것



