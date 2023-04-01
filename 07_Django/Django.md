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


## Django 3일차
### Template system
- 데이터 `표현`을 제어하면서, `표현`과 관련된 로직을 담당

### Django Template Language(DTL)
- Template에서 조건, 반복, 변수, 필터 등의 프로그래밍적 기능을 제공하는 시스템

#### Variable
- {{ variable }}
- view 함수에서 render 함수의 세번째 인자. 딕셔너리 타입으로 넘겨받음
- 딕셔너리 key 해당 문자열이 template에서 사용 가능하나 변수명
- dot(.) 사용해서 변수 속성에 접근

#### Filters
- 표시할 변수를 수정 할 때 사용
- chained가 가능. 일부 필터는 인자를 받기도 함 {{name|truncatewords:30}}
- 약 60 개의 built-in template filters 제공
- {{ variable|filter }}

#### Tags
- 반복 또는 논리 수행하여 제어흐름을 만드는 등 변수보다 복잡한 일들을 수행
- 일부 태그는 시작과 종료 태그가 필요 {% if %} {% endif %}
- 약 24개의 built-in template tags를 제공
- {% tag %}

#### Comments
- DTL에서의 주석 표현
- {# name #}
- {% comment %} {% endcomment %}

### 템플릿 상속(Template inheritance)
- 페이지 공통요소 포함. 하위 템플릿이 재정의 할 수 있는 공간을 정의하는 'skeleton' 템플릿을 작성하여 상속 구조를 구축

- skeleton 템플릿
- block 태그: 하위 템플릿에서 재정의(overridden)할 수 있는 블록을 정의(하위 템플릿이 작성할 수 있는 공간을 지정)

```html
<!-- articles/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  {% block content %}
  <!-- block 지정 -->
  {% endblock content %}
</body>
</html>
```
- 상속 받을 html
- extends 태그 사용. 반드시 최상단 작성
```html
{% extends 'base.html' %}

{% block content %}
<!-- 작성 -->
{% endblock content %}
```

### 요청과 응답 with HTML form
- 데이터를 보내고 가져오기
- HTML form은 HTTP요청을 서버에 보내는 가장 편리한 방법

#### 'form' element
- 사용자로부터 할당된 데이터를 서버로 전송
- 웹에서 사용자 정보를 입력하는 여러방식(text, password 등)을 제공

#### action & method
- 데이터를 어디(action)로 어떤 방식(method)으로 보낼지
- action
  - 입력 데이터가 전송될 URL을 지정(목적지)
  - 이 속성 지정 안하면 데이터는 현재 form이 있는 페이지의 URL로 보내짐
- method
  - 데이터를 어떤 방식으로 보낼 것인지 정의
  - 데이터의 HTTP request methods (GET, POST)를 지정

#### 'input' element
- 사용자의 데이터를 입력 받을 수 있는 요소
- type 속성 값에 따라 다양한 유형의 입력 데이터를 받음
- 'name': input의 핵심 속성. 데이터를 제출했을 때 서버는 name 속서에 설정된 값을 통해 사용자가 입력한 데이터에 접근할 수 있음
- 검색창에 입력했지만 실제로 서버랑 url을 써서 소통한 것. 그래서 name 속성이 있어야 함.
- 서버는 name 속성에 설정된 값을 통해 사용자 입력 데이터에 접근

```html
{% extends 'base.html' %}

{% block content %}
<form action="/catch/" method="GET">
    <input type="text" name="message" class="form-control" placeholder="내용 입력">
    <button type="submit" class="mx-2 btn btn-primary">Throw</button>
</form>

{% endblock content %}
```

#### Query String Parameters
- 사용자의 입력 데이터를 URL 주소에 파라미터를 통해 넘기는 방법
- 문자열은 앰퍼샌드(&)로 연결된 key=value 쌍으로 구성
- 기본 URL과 물음표(?)로 구분됨
- ex.http://host:port/path?key=value&key=value


### 요청과 응답 활용

```python
# urls.py
urlpatterns = [
    path('throw/', views.throw),
    path('catch/', views.catch),]

# view.py
def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    data = request.GET.get('message')
    # 딕셔너리 .get 메서드로 키 값 조회
    content = {
        'data': data
    }
    return render(request, 'articles/catch.html', content)
```

```html
<!-- throw.html -->
{% extends 'base.html' %}

{% block content %}
<form action="/catch/" method="GET">
    <input type="text" name="message">
    <button type="submit">Throw</button>
</form>
{% endblock content %}

<!-- catch.html -->
{% extends 'base.html' %}

{% block content %}
  <h1> {{ data }} </h1>
{% endblock content %}

```

- 모든 요청 데이터는 HTTP request 객체에 들어있음(view 함수의 첫번째 인자)

### 추가 템플릿 경로 지정
```python
# settings.py
# 경로지정을 편하게 하기 위해 최상단 지점을 지정해 놓은 변수
BASE_DIR = Path(__file__).resolve().parent.parent

# 템플릿 경로 지정
TEMPLATES = [
    { 'DIRS': [BASE_DIR / 'templates',],
    }]
```
- 객체 형태 주소 쓰는 이유: unix는 /로
윈도우는 \라서 운영체제에 따라 문제가 발생하지 않도록 하기 위해


### DTL 주의사항
- python처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만 명칭을 그렇게 설계한 것 뿐.
- python 코드로 실행되는 것이 아니며 python과 관련 없음
- 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것임
- 프로그래밍적 로직은 되도록 view 함수에서 작성 및 처리

### Django 공식 문서 보는 법
- 오른쪽 하단에 언어와 버전 변경 가능
장고 검색 창 잘 안됨. 구글 검색이용 
1. 오른쪽 목차를 본다. 내가 들어온 곳이 적합한지 보고, 찾을 주제로 이동
2. 만약 필터의 세부적인 내용 보고 싶다면 포함된 링크로 이동


## Django 4일차

### Django URLs
- URL dispatcher(운항 관리자, 분배기): URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view 함수를 연결(매핑)
- Variable Routing: URL 일부에 변수를 포함시키는 것(변수는 `view 함수의 인자`로 전달 할 수 있음)
- Path converters: URL 변수의 타입을 지정(str, int 등 5가지 타입 지원)
- urls.py의 num(변수)과 view.py의 num(변수)랑 변수명이 맞아야 함.

```python
# urls.py
# <path_converter:variable_name>
path('articles/<int:num>/', views.detail)

# view.py
# 변수는 `view 함수의 인자`로 전달 할 수 있음
def detail(request, num):
    context = {
        'num': num
    }
    return render(request, 'articles/detail.html', context)

# detail.html
<h3>여기는 {{ num }}번 글 입니다.</h3>

```

### App URL mapping
- 각 앱에 URL을 정의하는 것
- 프로젝트와 각 앱의 URL을 나누어 관리

### mapping 순서
```python
# firstpjt/urls.py
# 1. include 추가
from django.urls import path, include

urlpatterns = [

    path('articles/', include('articles.urls')),
    # 2. aricles/로 입력된 url을 articles 앱의 urls.py 파일로 연결(매핑) 

]


# articles/urls.py

# 3. 상위 경로 import
from django.urls import path
from . import views # 명시적 상대경로 (. 현재위치 django 권장사항)

# 4. 기존처럼 작성(실제 URL은 articles/index/가 되는 것)
urlpatterns = [
    path('index/', views.index),
]
```

### URL 이름 지정
- URL 이름 + app 이름표 붙이기
- name='throw'
- {% url 'articles:throw' arg1 arg2 %}
- 주의: app 이름표 지정후에는 app_name:url_name 형태로만 사용 가능

```python
# articles/urls.py

app_name = 'articles'
urlpatterns = [
    path('throw/', views.throw, name='throw'),
]
```

```html
<!-- throw.html -->
<a href="{% url 'articles:throw' arg1 arg2 %}"></a>
<!-- throw/arg1/arg2/인 URL로 연결 -->
```

### 참고
- Trailing Slashes: 장고는 URL 끝에 '/'없으면 자동으로 붙임
- url 뒤에 / 붙고 안 붙고는 기술적으로는 다른 건데 네이버나 구글은 각자 서버에서 내부적으로 처리 하는 것
- NoReverseMatch 에러나오면 무조건 URL관련 문제!
- 루트 페이지(?, 첫페이지)을 위해서 프로젝트에 프로젝트폴더에 views.py를 생성하고
index를 만들어 주는 방법. path('',)빈 문자열로 지정
- 서버 켜진지 확인하는 법: 윈도우 포트 확인 검색(cmd 명령어:nestat ~~~)

## Django 5일차

### Django Model
- 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공
- 테이블 구조 설계하는 청사진(blueprint)

### model class 작성
- models.py 작성
- class 상속을 이용
- 테이블의 필드 이름(클래스 변수명) / 테이블 필드의 데이터 타입 / 테이블 필드의 제약조건

```python
# articles/models.py
from django.db import models

class Article(model.Model):

  # id필드는 자동생성
  # Model이라는 부모 클래스 상속 받음
    title = models.CharField(max_length=10)
    # 필드 이름(변수명) title / 데이터 타입(모델 필드 클래스) CharField / 제약조건(모델 필드 클래스의 키워드 인자) max_length=10
    content = models.TextField()

```
- CharField(): 길이 제한이 있는 문자열을 넣을 때 사용(필드 최대 길이 결정 max_length 필수 인자)
- TextField(): 글자의 수가 많을 때 사용
- 위의 문자열 필드의 경우 null=True 대신 blank=True 권장
- Date TimeField(): 날짜와 시간 넣을 때
- Date TimeField의 선택 인자 auto_now, auto_now_add
- auto_now: 데이터가 저장될 때마다 자동으로 현재 날짜시간 저장(수정한 시간)
- auto_now_add: 데이터가 `처음`생성 될때만 자동으로 현재 날짜 시간 저장

### Migrations
- 순서: `models.py에 class 생성 > 설계도 작성 > 설계도를 DB에 반영`

- model 클래스의 변경사항(필드 생성, 추가 수정 등)을 DB에 최종 반영하는 방법
- Migrations 과정 model class ---(`makemigrations`)---> migrations파일(설계도) ---(`migrate`)--->db.sqlite3

![image](https://user-images.githubusercontent.com/110805149/227451788-65828a8f-4a1b-414b-8edb-b2f842e18068.png)

### Migrations 핵심 명령어
```bash
# 1. 설계도(migration) 작성
$ python manage.py makemigrations

# 2. 설계도를 DB에 전달하여 반영
$ python manage.py migrate

```

#### 기존 테이블에 필드를 추가해야 할 때
- models.py에 `클래스 변수를 추가` > (makemigrations `옵션 선택`)---> migrations파일(설계도) ---(migrate)--->db.sqlite3


```python
# articles/models.py

class Article(model.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 이후에 두개의 필드를 추가

```
- 필드 추가 후 기존 순서대로 재진행
- makeigrations하면 기본 값 설정이 필요.
- 1번은 직접 기본값 입력하는 방법
- 2번은 현재 대화에서 나간후 models.py에서 관련 설정하는 법
- 1번 2번 읽어보고 상황에 맞게 진행 하면 됨

```bash
# 1. 설계도(migration) 작성
$ python manage.py makemigrations


# 2. 설계도를 DB에 전달하여 반영
$ python manage.py migrate

```

### Admin Site
- django는 추가 설치 및 설정 없이 자동으로 관리자 인터페이스를 제공
- 데이터 관련 테스트 및 확인 하기 매우 유용

- 순서: `admin 계정 생성 > DB에 생성된 admin 계정 확인 > admin 페이지에 모델 클래스 등록 > 서버켜고 로그인 후 모델클래스 등록 확인 > 데이터 CRUD 테스트, 실제 DB 테이블 저장 확인`

#### admin 계정 생성
- createsuperuser

```bash
$ python manage.py createsuperuser
# email은 선택 사항(입력 안하고 진행 가능)
# 비밀 번호 생성시 보안상 터미널에 출력 안됨 무시하고 입력 하면 됨. 커서(?)안움직임
```

#### admin 페이지에 모델 클래스 등록
```python
# articles/admin.py

from django.contrib import admin
# 명시적 상대경로 .
# from . import models 이거 보다는 아래가 편함(models를 반복해야하니까)
from .models import Article

# 만든 Article 클래스를 등록
admin.site.register(Article)

# 암기 꿀팁: admin site 에 등록(register) 하겠다
```

### Migrations 기타 명령어

```bash
$ python manage.py showmigrations
# migrations 파일의 migrate 여부 확인 용도
# [X] 표시가 있으면 migrate 완료되었음 의미

$ python manage.py sqlmigrate articles 0001
# 해당 migraions 파일이 sql 문으로 어떻게 해석 되어 DB에 전달되는지 확인 용도
# articles는 앱이름 0001은 migrations 파일 번호

```

## Django 6일차
### ORM(Object-Relational-Mapping)
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 시스템 간에 데이터를 변환하는 프로그래밍 기술

### QuerySet API
```python
Article.objects.all()
# Model class . Manager . QuerySet API
```
![image](https://user-images.githubusercontent.com/110805149/228266213-357727e5-f976-4738-a1c3-c3390e5211ca.png)

#### Query
- 데이터베이스에 특정한 데이터를 보여 달라는 요청
- 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 DB에 전달
- DB의 응답 데이터를 ORM이 QuerySet 자료형태로 변환하여 전달

#### QuerySet
- 데이터베이스에게서 전달 받은 객체 목록(데이터 모음, 순회 가능)
- Django ORM을 통해 만들어진 자료형
- 단, 데이터베이스가 단일한 객체 반환 할 때(get)는 QuerySet 아닌 모델(Class)의 인스턴스로 반환

### ORM CREATE
- 외부 라이브러리 설치 및 설정
```bash
# 설치
$ pip install ipython
$ pip install django-extensions # - 하이픈 

# setting.py Installed apps 추가
INSTALLED_APPS = [
  'articles',
  'django_extensions', 
  # 이거 - 하이픈 아니고 _ 언더바
]
# requirements.txt에 추가
$ pip freeze > requirements.txt
```
#### Django shell
- django 환경 안에서 실행되는 python shell
- 입력하는 QuerySet API 구문이 django 프로젝트에 영향을 미침

#### 데이터 객체를 만드는 (생성하는) 3가지 방법
- 방법 1
```python
# Article 클래스의 인스턴스 생성
article = Article()

# article 인스턴스에 title과 content 인스턴스 변수에 값을 저장
article.title = '제목A'
article.content = '내용A'

# 테이블에 레코드 하나 생성을 위해 저장(인스턴스 메서드 save 호출)
article.save()
```

- 방법 2
```python
article = Article(title='제목A', content='내용A')
article.save()
```

- 방법 3(자동 save)
```python 
# QuerySet api의 create 메서드를 활용
Article.objects.create(title='제목A', content='내용A')
```

### ORM READ
#### 전체 데이터 조회
```python
Article.objects.all()
# .all() 기억!!
```

#### 단일 데이터 조회
- get() 사용
- 객체를 찾을 수 없으면 DoesNotExist 예외 발생
- 둘 이상의 객체 찾으면 MultipleObjectsReturned 예외 발생

```python
Article.objects.get(pk=1)

Article.objects.get(pk=100)
# pk 100이 없을 때 DoesNotExist 예외 발생

Article.objects.get(content='django!')
# content가 'django!'인 데이터가 2개 이상이면 리턴 안됨(단일 데이터 조회)
# MultipleObjectsReturned 예외 발생
```

#### 특정 조건 데이터 조회(단일 데이터 아닌 경우)
- filter() 사용
```python
Article.objects.filter(content='django!')
```


#### Field lookups
- 특정 레코드에 대한 조건 설정 방법
- QuerySet 메서드 filter(), exclude() 및 get()에 대한 키워드 인자로 지정
- Field lookup 문서: https://docs.djangoproject.com/en/3.2/ref/models/querysets/#field-lookups

#### ORM, QuerySet API 사용 이유
- 데이터베이스 쿼리를 추상화하여 django 개발자가 데이터베이스와 직접 상호 작용하지 않아도 되도록 함
- 데이터베이스와의 결합도를 낮추고 개발자가 더욱 직관적이고 생산적으로 개발할 수 있도록 도움


### 참고 
- QuerySet API 문서 : https://docs.djangoproject.com/en/3.2/topics/db/queries/
- print(Article.objects.all().query) 입력하면 sql문으로 확인 가능
- django_extensions 설치 후 등록 해야함(그래야 shell_plus도 실행됨)
- 결과물 출력 안될 때 models.py도 확인

## Django 7일차

### ORM UPDATE
```python
# 수정할 인스턴스 조회
article = Article.objects.get(pk=1)

# 인스턴스 변수를 변경
article.title = 'bye'

# 저장
article.save()

# 변경 내용 확인 'bye'
article.title
```

### ORM DELETE
- 삭제하면 리턴 값이 있다.
- '몇 번 글이 삭제되었습니다' 출력가능

```python
# 삭제할 인스턴스 조회
article = Article.objects.get(pk=1)

# delete 메서드 호출(삭제 된 객체가 반환)
article.delete()
(1, {'articles.Article' : 1})

# 삭제한 데이터느 더 이상 조회 안 됨
Article.objects.get(pk=1)
DoesNotExist
```

### ORM with view
#### 사전준비
```python
# app URLs 분할 및 연결
# crud/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('articles/', include('articles.urls')),
]

# articles/urls.py
from django.urls import path
from . import views
app_name = 'articles'
urlpatterns = [
  path('', view.index, name='index'),
]
```

#### READ
##### 전체게시글 조회
```python
# articles/urls.py
app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
]

#articles/views.py

def index(request):
    # DB에 전체 게시글 조회를 요청
    articles = Article.objects.all()  # 전체 조회니까 복수형 articles로 변수
    # print(articles)
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)
```
```html
<!-- articles/index.html -->

<body>
  <h1>Articles</h1>
  <a href="{% url 'articles:new' %}">[NEW]</a>
  {% for article in articles  %}
    {% comment %} <p>글번호: {{ article.pk }}</p> {% endcomment %}
    <p>제목: <a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a></p>
    <p>내용: {{ article.content }}</p>
    <hr>
  {% endfor %}
</body>
```

##### 단일게시글 조회
```python
# articles/urls.py
app_name = 'articles'
urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
]

# articles/view.py

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    # print(article)
    context = {
        'article': article,  # 단일객체 조회라서 단수형으로
    }
    return render(request, 'articles/detail.html', context)
```
```html
<!-- articles/detail.html -->
<body>
  <h1>Detail</h1>
  <p>글 번호: {{ article.pk }}</p>
  <p>제목: {{ article.title }}</p>
  <p>내용: {{ article.content }}</p>
  <p>작성일: {{ article.created_at }}</p>
  <p>수정일: {{ article.updated_at }}</p>
  <a href="{% url 'articles:index' %}">[BACK]</a>
</body>
```

#### CREATE
- create 로직 구현하기위해 필요한 view 함수
  - new: 사용자의 입력을 받는 페이지를 렌더링
  - create: 사용자가 입력한 데이터를 받아 DB에 저장

##### new 로직 구성
```python
# articles/urls.py
app_name = 'articles'
urlpatterns = [
    path('new/', views.new, name='new'),
]

# articles/view.py

def new(request):
    return render(request, 'articles/new.html')
```
```html
<!-- articles/new.html -->
<body>
  <h1>New</h1>
  <form action="{% url 'articles:create' %}" method="GET">
    <div>
      <label for="title">제목: </label>
      <input type="text" name="title" id="title">
    </div>
    <div>
      <label for="conent">내용: </label>
      <textarea name="content" id="content" cols="30" rows="10"></textarea>
      {% comment %} textarea 우측하단에 늘릴 수 있는 손잡이 있음 {% endcomment %}
    </div>
    <input type="submit">
  </form>
  <a href="{% url 'articles:index' %}">[BACK]</a>
</body>
```

##### create 로직 구성
```python
# articles/urls.py
app_name = 'articles'
urlpatterns = [
    path('create/', views.create, name='create'),
]

# articles/view.py

def create(request):
    # new에서 보낸 사용자 데이터를 받아서 변수에 할당
    title = request.GET.get('title')
    content = request.GET.get('content')
    # request.GET 데이터 dictionary다

    # # 받은 데이터를 DB에 저장
    # # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2 (2번을 사용하기로)
    article = Article(title=title, content=content)
    # 저장 전에 유효성 검사와 같은 추가 작업을 위해 2번 방법 택함(현재는 models.py에 있는 max_length 동작 안하고 있음..)
    article.save()

    # 3
    # Article.objects.create(title=title, content=content)

    # 결과 페이지 반환
    return render(request, 'articles/create.html')
```
```html
<!-- articles/create.html -->
<body>
  <h1>작성이 완료되었습니다.</h1>
  <a href="{% url 'articles:index' %}">[BACK]</a>
</body>
```


### 참고
- 한국 시간 설정 하기
```python
# settings.py
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
```
- 프로젝트 연습 방법
  - 새로운 프로젝트 생성부터 배운 곳 까지. 옆에 자료를 먼저 띄워 두기 보다 안 본 상태로 해보고 막히면 막힌 부분을 별도로 기록(왜 막혔는지 채워가기)하고 완성까지


## Django 8일차
### HTTP request methods
- 게시글 작성 후 작성 완료 페이지 렌더링 하는 것은 적절한 응답 아님
- 데이터 저장 후 유저를 어디론가 다시보내야 함
#### redirect()
- 인자에 작성된 주소로 다시 요청을 보냄

```python
# views.py
from django.shortcuts import render, redirect
# redirect import 하기

def create(request):
    # 생략...
    return redirect('todos:detail', todos.pk)
    # pk 다시 보낼때 , 로 구분
```

### HTTP
- 네트워크 상에서 데이터를 주고 받기위한 약속

#### HTTP request methods
- 데이터(리소스)에 어떤 요청(행동)을 원하는지 나타내는 것
- GET & POST

##### GET Method
- 특정 리소스를 조회하는 요청
- Query String 형식으로 보내짐
- 데이터를 가져올 때(조회)만 사용

##### POST Method
- 특정 리소스에 변경 사항을 만드는 요청
- HTTP Body에 담겨 보내짐
- 게시글 작성후 403 응답 확인(CSRF 토큰 필요)
```html
<!-- new.html -->
<form action="{% url 'articles:create' %}" method="POST">
  {% csrf_token %}
<!-- csrf 토큰 없으면 403 응답 -->
```
```python
# views.py
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title=title, content=content)
    article.save()
    # 생성한 글의 주소 이동 응답
    # 새로 생성한 글의 pk를 활용
    # 템플릿과 비교 했을 때 띄어쓰기 대신 쉼표 사용한다고 생각하면 됨
    return redirect("articles:detail", article.pk)
```
##### CSRF(Cross-Site-Request-Forgery)
- 사이트 간 요청 위조
- 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법
- Security Token(CSRF Token): 대표적인 CSRF 방어 방법
  - 서버는 사용자의 입력데이터에 임의의 난수 값(token) 부여
  - 매 요청 마다 해당 token  포함시켜 전송 시킴
  - 이후 서버 요청 받을 때마다 전달된 token 유효한지 검증
- 토큰 사용해 최소한의 신원 확인 하는 것
- 개발자도구보면 form 태그 안에 input hidden으로 숨겨져 있음
- {% csrf_token %} form 아래 추가
- settings.py 보면 중간 연결다리. csrf가 있음

```html
<!-- new.html -->
<form  method="POST">
  {% csrf_token %}
<!-- csrf 토큰 없으면 403 응답 -->
```

#### DELETE
##### delete 로직
```python
# urls.py
urlpatterns = [
    path('<int:pk>/delete/', views.delete, name="delete"),
]

# view.py
def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('todos:index')
```
```html
<!-- detail.html -->
<form action="{% url 'todos:delete' todo.pk %}" method="POST">
  {% csrf_token %}
  <input type="submit" value="삭제">
</form>
```

#### UPDATE
- Update 로직 위해 필요한 view 함수: edit, update
- edit: 사용자의 입력을 받는 페이지(수정페이지)를 렌더링
- update: 사용자가 입력한 데이터를 받아 DB에 저장

##### edit 로직
```python
# urls.py
urlpatterns = [
    path('<int:pk>/edit/', views.edit, name="edit"),
]

# view.py
def edit(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/edit.html', context)
```
```html
<!-- edit.html -->
{% extends 'todos/base.html' %}

{% block content %}
<h3>할 일 수정</h3>
<form action="{% url 'todos:update' todo.pk %}" method="POST" >
  {% csrf_token %}
  <div>
    <label for="title">제목</label><br>
    <input type="text" id="title" name="title" value={{ todo.title }}>
    <!-- value 입력이 중요 -->
  </div>
  <div>
    <label for="content">내용</label><br>
    <textarea name="content" id="content" cols="30" rows="10">{{ todo.content }}</textarea>
    <!-- textarea는 value 입력이 안됨. 태그에 직접 입력 -->
  </div>
  <div>
    <label for="priority">우선순위</label><br>
    <input type="number" id="priority" name="priority" value={{ todo.priority }}>
    <!-- value 입력이 중요 -->
  </div>
  <div>
    <label for="deadline">마감기한</label><br>
    <input type="date" id="deadline" name="deadline" value={{ todo.deadline|date:"Y-m-d" }}>
    <!-- 날짜 형식을 맞춰는 방법 {{ value|date: }}-->
  </div>
  <div>
    <br>
    <input type="submit">
  </div>

</form>

{% endblock content %}

<!-- detail.html -->
<!-- edit 버튼 -->
<a href="{% url 'todos:edit' todo.pk %}">[수정]</a>
```

##### Update 로직
```python
# urls.py
urlpatterns = [
    path('<int:pk>/update/', views.update, name="update"),
]

# view.py
def update(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.title = request.POST.get('title')
    todo.content = request.POST.get('content')
    todo.priority = request.POST.get('priority')
    todo.deadline = request.POST.get('deadline')
    todo.save()
    return redirect('todos:index')
```
```html
<!-- edit.html -->
{% block content %}
<h3>할 일 수정</h3>
<!-- {% url 'todos:update' todo.pk %} 중요 -->
<form action="{% url 'todos:update' todo.pk %}" method="POST" >
  {% csrf_token %}
```

## 참고
- a태그는 get만 가능
- 추후 REST API에서 효율적인 URL 구조 다룰 예정