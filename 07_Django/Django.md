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


## Django 9일차
### Form
#### HTML form
- 사용자로부터 form 요소를 통해 데이터를 받고 있으나 비정상적 혹은 악의적인 요청을 확인하지 않고 모두 수용중(유효성 검증 필요)
#### 유효성 검사
- 수집한 데이터가 정확하고 유효한지 확인하는 과정
- 입력 값, 형식, 중복, 범위, 보안 등 고려
- 이런 과정과 기능 제공 도구 필요

#### Django Form
- 사용자 입력 데이터를 수집하고, `처리 및 유효성 검증`을 수행하기 위한 도구
- 유효성 검사를 `단순화, 자동화` 할 수 있는 기능 제공

### Widgets
- HTML 'input' element의 표현을 담당
- Widget은 단순히 input 요소의 속성 및 출력 되는 부분을 변경하는 것
- Widget 공식문서: https://docs.djangoproject.com/ko/3.2/ref/forms/widgets/#built-in-widgets

```python
class ArticledForm(forms.ModelForm):
  # 위젯으로 input 디자인 변경. class 추가 하기.공식문서확인.
    content = forms.CharField(widget=forms.Textarea)
```

### ModelForm
- Form: 사용자 입력 데이터를 DB에 `저장하지 않을` 때(ex.로그인)
- ModelForm: 사용자 입력데이터를 DB에 `저장해야 할` 때(ex.회원가입)
- Meta에 model만 써도 되지만 표현(디자인) 하기 위해 widget 사용

```python
from django import forms
from .models import Article

# 일반 Form
# class ArticledForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

# ModelForm
class ArticledForm(forms.ModelForm):
    

    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('content',)
        # content만 출력
        # exclude = ('title',)
        # title 제외하고 출력

    # 클래스 안에 클래스? Inner class 파이썬 문법이랑 아무상관 없고
    # 그냥 django ModelForm의 구조가 이렇게 설계 되었을 뿐
    # 그냥 modelform에 대한 추가 정보를 클래스 meta에 쓸 뿐
    # form에 대한 추가 데이터(meta) 라고 생각하면 됨
    # ModelForm의 정보를 작성 하는 곳

```

#### Meta class
- ModelForm의 정보를 작성하는 곳
- fields: 포함 하는 필드
- exclude: 포함하지 않을 필드
```python
# articles/view.py
    class Meta:
        model = Article
        fields = '__all__' # 전체 필드 선택
        # fields = ('content',)
        # content 필드만 출력
        # exclude = ('title',)
        # title 필드 제외하고 출력
```

#### is_valid
- 여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를 boolean으로 반환
- 
```python 
# views.py 
def create(request):
    if request.method == 'POST':
        form = ArticledForm(request.POST)
        if form.is_valid():
          # is_valid()가 True가 아니면 왜 통과 못한 지 정보를 담아서 form으로 내려 줌(context form으로 감)
            article = form.save()
            return redirect("articles:detail", article.pk)

    else:
        form = ArticledForm()

    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```

#### save()
- 데이터베이스 객체를 만들고 저장
- 키워드 인자 instance 여부를 통해 생성할 지, 수정할 지를 결정
- instance가 객체를 명시함(어떤 객체를 수정할지 알려줌)
```python
# create
form = ArticledForm(request.POST)
form.save()

# update
form = ArticledForm(request.POST, instance=article)
# instance=article 차이
form.save()
```


### 오늘 배운 내용 요약
- Form과 ModelForm의 차이는 데이터 저장여부에 따라 사용
- 기존에 배운 new와 create를 create하나의 로직으로 합치기
- 기존에 배운 edit과 update를 update 하나의 로직으로 합치기
  - if문으로 request.method가 GET일때와 POST일 때 구분

```python
#view.py

# create
def create(request):
    # HTTP requests method POST라면
    if request.method == 'POST':
        form = ArticledForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect("articles:detail", article.pk)
    # POST가 아니라면
    else:
        form = ArticledForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

# create와 update 차이는 거의 instance=article 유무가 전부

# update
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticledForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("articles:detail", article.pk)
    else:
        form = ArticledForm(instance=article)

    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```
```html
<!-- create.html -->
<body>
  <h1>CREATE</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  <a href="{% url 'articles:index' %}">[BACK]</a>
</body>
```


### 참고
- 코드의 흐름에 따른 create 작성 순서
  - if 말고 else부터 작성 > 템플릿 작성 하고 폼 만들고 > 그리고 나서 if 문 작성
- {{ form.as_p }} :  form을 p태그로 나누어서 보여줌 


## Django 10일차
### Cookie & Session
#### HTTP
- HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 규약
- 웹(WWW)에서 이루어지는 모든 데이터 교환의 기초
##### HTTP 특징
- 비 연결 지향(connectionless): 서버는 요청에 대한 응답보낸 후 연결을 끊음
- 무상태(stateless): 연결을 끊는 순간 클라이언트와 서버간의 통신이 끝나며 상태 정보가 유지되지 않음
- 무상태라면 장바구니에 담은 상품 유지 되지 않음, 로그인 상태 유지되지 않음 등

#### 쿠키(Cookie)
- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
- 클라이언트 측에 저장되는 작은 데이터 파일
- 사용자 인증, 사용자 추적, 상태 유지 등에 사용 됨
##### 쿠키 사용 예시
1. 브라우저(클라이언트)는 쿠키를 로컬에 key-value 데이터 형식으로 저장
2. 이렇게 `쿠키 저장`했다가 동일한 서버에 `재요청`시 저장된 쿠키 함께 전송
- 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용됨
  - 로그인 상태 유지 가능
  - 상태가 없는(stateless) HTTP프로토콜에서 상태정보를 기억시켜 줌

- 장바구니 예시
  - 쿠팡 장바구니: 개발자도구 네트워크: set-cookie
  - ex.공지하루 안보기: 쿠키를 저장하고 서버에 보냄

##### 쿠키 사용 목적
1. 세션 관리(Session management)
- 로그인, 아이디 자동완성, 공지하루 안보기, 팝업체크, 장바구니 등 정보관리
2. 개인화(Personalization)
- 사용자 선호, 테마 등의 설정
3. 트래킹(Tracking)
- 사용자 행동을 기록 및 분석

#### 세션(Session)
- 서버 측에서 생성되어 클라이언트와 서버 간의 상태를 유지
- 상태 정보를 저장하는 데이터 저장방식
- 쿠키에 세션 데이터를 저장하여 `매 요청시마다`(로그인 유지) 세션 데이터를 함게 보냄
- 세션은 서버측에서 저장 됨
- 서버 측에서는 세션 ID를 생성하고, 이 ID를 클라이언트 측으로 전달하여, 클라이언트는 쿠키에 이 ID를 저장

##### 쿠키와 세션의 목적
- 클라이언트와 서버 간의 상태 유지

##### 쿠키와 세션의 차이
| HTTP | 쿠키 | 세션 |
|---|---|---|
| 위치 | 클라이언트 | 서버 |
| 상태 유지 위치 | 브라우저: 클라이언트 측에서 상태를 유지	| 서버: 세션 ID를 사용하여 클라이언트 상태를 유지 |
| 성능 | 클라이언트 측에서 자원 소모, 서버 부하 감소 | 서버 측에서 자원 소모, 클라이언트 부하 감소 |
| 특징 | 클라이언트가 여러 개일 때 각각의 브라우저에서 각자의 쿠키를 유지 | 다수의 클라이언트가 동시에 접속할 때 각각의 클라이언트에 대한 세션을 유지해야 함 |
| 목적 | 상태 유지, 사용자 식별, 개인화된 사용자 경험 제공 | 상태 유지, 사용자 식별, 보안 유지, 쇼핑 카트 등의 상태 유지 |

#### 쿠키 종류별 lifetime(수명)
- Session cookie: 현재 세션이 종료되면 삭제됨. 브라우저 종료와 함께 삭제
- Persistent cookies: Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제됨

#### 세션 in Django
- Django는 'database-backed sessions' 저장 방식을 기본값으로 사용
- session 정보는 DB의 `django_session` 테이블에 저장
- Django는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 session을 알아냄
- Django는 우리가 세션 메커니즘(복잡한 동작원리)예 대부분을 생각하지 않게끔 도움



### Authentication System 1
#### Django Authentication System(인증시스템)
- 사용자 인증고 관련된 기능을 모아 놓은 시스템
- 인증(신원확인)과 권한, 허가(권한 부여)를 함께 제공 및 처리

```python
# settings.py 
INSTALLED_APPS = [
    'django.contrib.auth',
    # 내장 되어 있음
]
```

#### 인증(로그인)하기 전 사전 설정 방법
- 새로운 app으로 accounts 생성 및 등록
  - urls 연결
- auth와 관련 경로나 키워드들이 django 내부적으로 accounts라는 이름으로 사용하기 있기 때문에 되도록 accounts 권장


#### Custom User model

##### Custom User model로 대체하기
- django가 기본적으로 제공하는 User model은 내장된 auth 모듈의 User 클래스 사용(별도의 설정 없어 간편, 직접 수정 불가)
- Django가 커스텀 User 모델 설정 `강력 권장`
- 이후 맞춤 설정 가능
- 모든 migrations 혹은 첫 migrate 실행전 이 작업을 마쳐야 함
- 공식문서: https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model

##### Custom User model 대체 방법
`[주의] 프로젝트 중간에 AUTH_USER_MODEL 변경 불가능`
- 이미 진행한 경우 데이터베이스 초기화 후 진행 필요 

1. AbstractUser 상속 받는 커스텀 User 클래스 작성
```python
# accounts/model.py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```
2. django 프로젝트가 사용하는 기본 User 모델을 우리가 작성한 User 모델로 지정(기본 값:auth.User)
```python
# settings.py

AUTH_USER_MODEL = 'accounts.User'
```
3. 기본 모델이 아니기 때문에 등록하지 않으면 admin site에 출력되지 않음
```python
# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# 공식 문서에 있음

admin.site.register(User, UserAdmin)
```

#### Login
- Session을 Create하는 과정
- AuthenticationForm(): 로그인 위한 built-in form 사용
- login(request, user): 인증된 사용자를 로그인 하는 함수
- get_user(): AuthenticationForm의 인스턴스 메서드 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환
- 로그인 후 세션 데이터 
  - db.sqlite3 > django_session 테이블에서 확인 가능
  - 브라우저:개발자도구 > Application > Cookies 확인가능


##### 로그인 로직 작성 방법
1. urls 작성
```python
# accounts/urls.py
app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
]
```
2. views 작성
```python
# accounts/views.py
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid:
            auth_login(request, form.get_user())
            # 함수명 login과 중복 되어서 auto_login
            return redirect('articles:index')
    else:
        form = AuthenticationForm
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
```
3. templates 작성
```html
<!-- accounts/login.html -->
<body>
  <h1>로그인</h1>
  <form action="{% url 'accounts:login' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
</body>
```

#### Logout
- Session을 Delete 하는 과정
- logout(request)
  - 현재 요청에 대한 session data를 DB에서 삭제
  - 클라이언트의 쿠키에서도 session id를 삭제


##### 로그아웃 로직 작성 방법
1. urls 작성
```python
# accounts/urls.py
app_name = 'accounts'
urlpatterns = [
    path('logout/', views.logout, name='logout'),
]
```
2. views 작성
```python
# accounts/views.py
# 로그아웃: 세션을 삭제함
def logout(request):
    auth_logout(request)
    # 함수명 logout과 중복 되어서 auto_logout
    return redirect('articles:index')

```
3. templates 작성
```html
<!-- articles/login.html -->
  <h1>Articles</h1>
  <form action="{% url 'accounts:logout'%}" method="POST">
    {% csrf_token %}
    <input type="submit" value="Logout">
  </form>
```

#### Template with Authentication data
- 템플릿에서 인증 관련 데이터 출력 방법: {{ user }} 
```html
<!-- articles/index.html -->
  <h3>안녕하세요, {{ user }} 님!</h3>
```
- context processors: 템플릿 렌더링 될 때 호출 가능한 컨텍스트 데이터 목록
```python
TEMPLATES = [
    {
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 미리 로드해 둠. 있다는 정도만 알자.
            ],
        },
    },
]
```

### Authentication System 2
- User 객체와 CUD
  - 회원가입, 회원탈퇴, 회원정보 수정, 비밀번호 변경

#### 회원가입
- User 객체를 Create 하는 것
- UserCreationForm(): 회원 가입 위한 built-in ModelForm



##### 회원가입 로직 작성 방법
1. urls 작성
```python
# accounts/urls.py
app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
```
2. views 작성
- CustomUserCreationForm() 사용

```python
# accounts/views.py
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        # User 객체를 대체 했기 때문에 UserCreationForm 사용하면 auth.User가 accounts.User로 바뀌었다는 에러 발생 >> CustomUserCreationForm 만들어서 교체
        # ModelForm은 첫번째인자로 데이터(기억하기 쉽게)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            # 회원가입후 로그인(login 함수와 중복 방지로auth_login)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```
    2.1 `forms.py에 CustomUserCreationForm` 만들고 accounts/views.py에 import 하기
    아래 간단 설명 있음

  ```python
  # accounts/forms.py
  from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# django User 객체에 대한 직접 참조 권장하지 않음!!!!

# from .models import User 하고  model = User 라고 할 수 있지만
# 중간에 수정될 수 있고 또는 순서상 User가 적절한 시기에 활성화되지 않을 수도 있어서 model = get_user_model() 사용
# get_user_model은 현재 프로젝트에 활성화 되어있는 User 객체를 반환해준다.
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):  # 상속 후 수정
        # 현재 우리가 사용하는 User class로 재정의
        model = get_user_model() # User 대신
  ```
3. templates 작성
```html
<!-- accounts/signup.html -->
<body>
  <h1>회원가입</h1>
  <form action="{% url 'accounts:signup' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
</body>
```

##### CustomUserCreationForm & CustomUserChangeForm
- [주의] User 객체를 대체 했기 때문에 UserCreationForm 사용하면 auth.User가 accounts.User로 바뀌었다는 에러 발생 >> `forms.py에 CustomUserCreationForm` 만들어서 교체

- (회원가입 함수 작성시)UserCreationForm은  CustomUserCreationForm으로
- (회원정보수정 함수 작성시) UserChangeForm은 CustomUserChangeForm으로 다시 작성

##### get_user_model()
- 현재 프로젝트에서 활성화된 사용자 모델(active user model)을 반환하는 함수

```python
# forms.py
from django.contrib.auth import get_user_model
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
```

#### 회원 탈퇴
- User 객체를 Delete 하는 것

##### 회원 탈퇴 로직 작성 방법
1. urls 작성
```python
# accounts/urls.py
app_name = 'accounts'
urlpatterns = [
    path('delete/', views.delete, name='delete'),
]
```
2. views 작성
```python
# accounts/views.py
def delete(request):
    request.user.delete()  # 유저정보 들어있음
    # auth_logout(request) # 세션id도 같이 삭제하고 싶은 경우
    return redirect('articles:index')

```
3. templates 작성
```html
<!-- articles/index.html -->
  <form action="{% url 'accounts:delete' %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="회원탈퇴">
  </form>
```

#### 회원 정보 수정
- User 객체를 Update 하는 것
- UserChangeForm(): 회원 정보 수정 위한 built-in ModelForm
- UserChangeForm()를 CustomUserChangeForm()으로 바꿔서 사용

##### 회원 정보 수정 로직
1. urls 작성
```python
# accounts/urls.py
app_name = 'accounts'
urlpatterns = [
    path('update/', views.update, name='update'),
]
```
2. views 작성
```python
# accounts/views.py
@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(
            request.POST, instance=request.user)  # 수정: instance
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)
```
3. templates 작성
```html
<!-- accounts/update.html -->
  <h1>회원 정보 수정</h1>
  <form action="{% url 'accounts:update' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
```

#### 비밀번호 변경
- django는 비밀번호 변경 페이지를 회원정보 수정 form에서 별도 주소로 안내
- /accounts/password/
- PasswordChangeForm(): 비밀번호 변경 위한 built-in Form
- 암호 변경 시 세션 무효화 > 로그인 상태 유지 안됨 > 로그인 위해 세션 무효화 방지 함수 사용
-  update_session_auth_hash(request, user): 암호가 변경 되어도 로그아웃 되지 않도록 새로운 pw의 세션데이터로 기존 세션을 업데이트

##### 비밀번호 변경 로직
1. urls 작성
```python
# accounts/urls.py
app_name = 'accounts'
urlpatterns = [
  # 추후에 중복될 수 있어서?? 왜인지는 불확실.. 
  # 여기만 change_password로 이름 정함
    path('password/', views.change_password, name='change_password'),
]
```
2. views 작성
```python
# accounts/views.py
from django.contrib.auth import update_session_auth_hash  # 비밀번호 변경 후 세션도 업데이트

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # 비밀번호 무효화 방지
            update_session_auth_hash(request, user)
            # 세션 업데이트로 로그인 유지
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
```
3. templates 작성
```html
<!-- accounts/change_password.html -->
  <h1>비밀번호 변경</h1>
  <form action="{% url 'accounts:change_password' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
```


#### 로그인 사용자에 대한 접근 제한
##### is_authenticated 속성
- 사용자 인증 여부를 알 수 있는 User model의 속성
- AnonymousUser에 대해 항상 False
- 권한, 활성화 상태, 유효한 세션 확인 안함

```python
# view.py
    if request.user.is_authenticated:
        return redirect('articles:index')
```
```html
<!-- index.html -->
  <!-- user.is_authenticated도 가능하지만 request 권장 -->
  {% if request.user.is_authenticated %} 
    <!-- 회원정보수정, 로그아웃 등 -->
  {% else %}
   <!-- 회원 가입, 로그인 등 -->
  {% endif %}
```
##### login_required 데코레이터
- 인증된 사용자에 대해서만 view 함수 실행 시키는 데코레이터
- 파이썬 문법 데코레이터

```python
from django.contrib.auth.decorators import login_required

@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```

## Django 12일차

### Static Files
- 서버 측에서 변경되지 않고 고정적으로 제공되는 파일(이미지, JS, CSS 파일 등)
- 정적 파일을 제공하기 위한 경로(URL)가 있어야 함

### Static files 제공하기
- 경로에 따른 Static file 제공하기
  - 기본 경로: app/static/
  - 추가 경로: STATICFILES_DIRS

#### 기본 경로에 static file 제공하기
```html
<!--1. articles/static/articles/ 경로에 이미지 파일 배치 -->

<!-- 2. static tag 사용 이미지 파일 url 제공 -->
<!-- articles/index.html -->
<!-- 2-1 static 로드 먼저 하기 -->
{% load static %}
<!-- 2-2 static에 경로 입력 -->
<img src="{% static 'articles/sample-1.png' %}" alt="img">
```

- STATIC_URL
  - URL + STATIC_URL + 정적파일 경로
```python
# settings.py
STATIC_URL = '/static/'
# 샘플이미지 제공하기 위해 만든 URL 주소 
```

#### 추가 경로 static file 제공하기
- 추가 경로에 이미지 파일 배치
1. 경로 설정하기(최상단아래 static)
```python
# settings.py

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```
2. 최상단 아래 static 폴더 안에 이미지 파일 저장

3. static tag 사용해 이미지 파일 url 제공
```html
<!-- articles/index.html -->
  <img src="{% static 'sample-2.png' %}" alt="img">
```

- STATICFILES_DIRS : 정적 파일의 기본 경로 외에 추가적인 경로 목록을 정의하는 리스트

### Media Files
- `사용자`가 웹에서 `업로드`하는 정적파일(user-uploaded)
- ImageField(): 이미지 업로드에 사용하는 모델 필드
- 이미지 객체가 직접 저장되는 것이 아닌 `이미지 파일의 경로 문자열`이 DB에 저장

#### 미디어 파일 제공하기 전 준비
1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정
- MEDIA_ROOT: 미디어 파일들이 위치하는 디렉토리의 절대 경로
- MEDIA_URL: MEDIA_ROOT에서 제공되는 미디어 파일에 대한 주소를 생성(STATIC_URL과 동일한 역할)
```python
#  settings.py
# 미디어 파일이 실제 어디로 저장되는지 결정(물리적 주소)
MEDIA_ROOT = BASE_DIR / 'media'
# 경로 여기까지만 가능하고 추가는 모델필드에서 추가 가능

# 사용자에 보여지는 주소(제공 하는 주소)
MEDIA_URL = '/media/'
```


2. 작성한 MEDIA_ROOT와 MEDIA_URL에 대한 url 지정
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 미디어 파일. 응답할 url 추가(실제 URL, 물리적 위치)
```

### 이미지 업로드 및 제공하기
#### 이미지 업로드
1. blank=True 속성 저장해 빈 문자열 저장되도록 설정(사진은 선택사항)
```python
# articles/models.py

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # MEDIA_ROOT 이후의 추가 경로를 설정 => upload_to='images/'
    # 날짜폴더로 넣고 싶을때 upload_to='%Y/%m/%d'
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
2. pillow 설치 > migration 진행 > requirements.txt 작성
```bash
$ pip install pillow 
# ImageField 사용위해 pillow 반드시 필요
$ python manage.py makemigrations
$ python manage.py migrate

$ pip freeze > requirements.txt
```
3. form 요소의 enctype 속성 추가 enctype="multipart/form-data"
```html
  <h1>Create</h1>
  <form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  ```

4. view 함수에서 업로드 파일에 대한 추가 코드 작성
```python
def create(request):
    if request.method == 'POST':
        print(request.FILES)
        form = ArticleForm(request.POST, request.FILES) #이미지 파일 여기 들어 있음
        # ...
```
5. 업로드 결과 DB 확인(파일 자체 아닌 `경로`가 저장 되는 것)

#### 이미지 제공 하기(업로드한 이미지를 보여줌)
1. url 속성을 통해 업로드 파일의 경로 값을 얻을 수 있음
```html
<!-- articles/detail.html -->
 <img src="{{ article.image.url }}" alt="img">
```
- article.image: 업로드 파일의 이름
- article.image.url : 업로드 파일의 경로

2. 출력 확인 및 MEDIA_URL 확인

3. 이미지 업로드하지 않은 게시물은 detail 템플릿을 출력할 수 없는 문제 발생
- 이미지 데이터 있는 경우만 출력 또는 대체 이미지 출력
```html
<!-- articles/detail.html -->
  {% if article.image %}
  <img src="{{ article.image.url }}" alt="img">
  {% else %}
  <img src="{% static 'articles/no-image.jpg' %}" alt="no_image">
  {% endif %}
```

#### 업로드 이미지 수정
1. 수정페이지 form 요소에 enctype 속성 추가
```html
<!-- articles/update.html -->
  <h1>Update</h1>
  <form action="{% url 'articles:update' article.pk %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="UPDATE">
  </form>
```
2. view 함수에서 업로드 파일에 대한 추가 코드 작성
```python
# articles/view.py
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        # ...
```

### 참고
- ImageField()의 upload_to 인자를 사용해 미디어 파일 추가 경로 설정
```python
  # 1. MEDIA_ROOT 이후의 추가 경로를 설정 => upload_to='images/'
  image = models.ImageField(blank=True, upload_to='images/')
  # 2. 날짜폴더로 넣고 싶을때 upload_to='%Y/%m/%d'
  image = models.ImageField(blank=True, upload_to='%Y/%m/%d')
  # 3. 
  def articles_image_path(instance, filename):
    return f'image/{instance.user.username}/{filename}'

  image = models.ImageField(blank=True, upload_to=articles_image_path)
```

- 사용자가 업로드하는 파일: 미디어 파일
- 스태틱 파일 : 미리 배치 되어있는 파일
- 스태틱 파일이 더 큰 개념

- 이미지 파일 원본 그대로 안하고 Django 이미지 리사이징도 가능. 라이브러리 사용
방법은 여러가지 다양


## Django 13일차

### Comment & Article
- many to one relationships (N:1 or 1:N): 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계
- Comment(N) - Article(1): 0개 이상의 댓글을 1개의 개시글에 작성될 수 있다.
- 두 모델의 관계
![image](https://user-images.githubusercontent.com/110805149/231139623-0f9fb757-2481-40fa-aab5-0c7aa1191de9.png)

- ForeignKey(): django에서 N:1 관계 설정 모델 필드

#### Comment 모델 정의
```python
# articles/models.py
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```
- ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자)으로 작성 권장
- ForeignKey 클래스를 작성하는 위치와 관계 없이 필드 마지막에 생성됨
- on_delete: 참조하던 상대방 대상이 없어지면? 폭포처럼 떨어져서 같이 삭제(on_delete=models.CASCADE)

#### 댓글 생성 연습

#### 역참조
- 나를 참조하는 테이블(나를 외래 키로 지정한)을 참조하는 것
- N:1 관계에서는 1이 N을 참조하는 상황
- 하지만 Article에는 Comment를 참조할 어떠한 필드도 없다.

- `article.comment_set.all()`: 모델인스턴스.related manager.QuerySet API

- related manager : N:1 혹은 M:N 관계에서 역참조 시에 사용하는 manager(objects라는 매니저를 통해 queryset api를 사용 했던 것처럼 related manager를 통해 queryset api를 사용할 수 있게 됨)
- related manager가 필요한 이유
  - article.comment 형식으로는 댓글 참조 할 수 없음
  - 실제 Article 클래스에는 Comment와의 어떠한 관계도 작성되어 있지 않기 때문
  - 대신 Django가 역참조 할 수 있는 'comment_set' manager를 자동으로 생성해 article.comment_set 형태로  댁슬 객체를 참조할 수 있음
  - N:1 관계에서 생성되는 Related manager의 이름은 참조하는 `모델명_set`이름 규칙으로 만들어짐

  ```python
  comments = article.comment_set.all()

  for comment in comments:
    print(comment.content)
  ```

### 댓글 생성, 읽기, 삭제 등
#### Comment CREATE
1. 사용자로부터 댓글 데이터를 입력 받기 위한 CommentForm 작성

```python
# articles/forms.py
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__' # 수정 필요!! 아래!
```

2. detail 페이지에서  CommentForm 출력(템플릿)
```html
<!-- articles/detail.html -->
<form action="{% url 'articles:comment_create' article.pk %}" method = "POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
```
- 그냥 출력하면 Comment 클래스의  외래키 필드 article 또한 데이터 입력이 필요하기 때문에 출력되어 나옴
- 하지만 외래키 필드는 `사용자의 입력으로 받는 것이 아니라 view 함수 내에서 받아 별도로 처리되어 저장`되어야함.

3. detail 페이지에서 CommentForm 출력(템플릿)
```python
# articles/forms.py
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',) # 여기를 바꿔줌
```
- 출력에서 제외된 외래키는 detail 페이지의 url의 pk값에서 가져올 수 있음
- 댓글의 외래 키 데이터 =  게시글의 pk 값

4. url 설정
```python
# articles/urls.py
urlpatterns = [
    path('<int:article_pk>/comments/', views.comment_create, name='comment_create'),
]
```
5. view 설정
```python
# articles/views.py
def comment_create(request, article_pk):
    # 몇 번 게시글인지 조회
    article = Article.objects.get(pk=article_pk)
    # 댓글 데이터를 받아서
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        # 커밋 잠시 멈춤: 인스턴스는 만들어주는데 DB에 저장은 안함
        comment.article = article
        # 인스턴스 채우고 잠시 저장 미뤘다가 id 채우고 저장하기
        comment.save()
        # commit=True가 기본값
```
- save(commit=False) : DB에 저장하지 않고 인스턴스만 반환

6. templates 설정
```html
<!-- articles/detail.html -->
<form action="{% url 'articles:comment_create' article.pk %}" method = "POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
```

#### Comment READ
1. 전체 댓글 출력(view 함수)
```python
# articles/view.py
def detail(request, pk):
    comment_form = CommentForm()
    article = Article.objects.get(pk=pk)
    # 해당 게시글에 작성된 모든 댓글을 조회(역참조)
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)
```
2. 전체 댓글 출력(템플릿)
```html
<!--  articles/detail.html -->
  <h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}
    <li>
      {{ comment.content }}
    </li>
    {% empty %}
    <p>댓글이 없어요..</p>
    {% endfor %}
  </ul>
```

#### Comment DELETE
1. 댓글 삭제 url 작성
```python
#  articles?urls.py
app_name = 'articles'
urlpatterns = [path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
]
```
2. 댓글 삭제 view 함수 작성
```python
# articles/views.py
def comment_delete(request, article_pk, comment_pk):
    # 삭제할 댓글을 조회
    comment = Comment.objects.get(pk=comment_pk)
    # article_pk = comment.article.pk도 가능, 권장x
    comment.delete()
    return redirect('articles:detail', article_pk)
```

3. 댓글 삭제 버튼 작성
```html
<!-- articles/detail.html -->
  <h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}

    <li>
      {{ comment.content }}
      <!-- 댓글 삭제 버튼 -->
      <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="삭제">
      </form>
    </li>
      {% endfor %}
  </ul>
```

### 참고
- 댓글 개수 출력 하기
  - DTL Filter - length 사용
  ```html
  <!-- 둘 중 하나 선택 사용 -->
  {{ comments|length }}

  {{ article.comment_set.all|length}}
  ```
  - QuerysetAPI - count() 사용
    ```html
  {{ article.comment_set.count }}

  ```

- 댓글 없는 경우 대체 컨텐츠 출력
  - DTL tag-for empty 사용: for 문 안에 empty
```html
<!--  articles/detail.html -->
  <h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}

    <li>
      {{ comment.content }}
    </li>
    <!-- empty 사용하면 댓글 없을 때 대체 해줌 -->
    {% empty %}
    <p>댓글이 없어요..</p>
    {% endfor %}
  </ul>
```
- 댓글 수정 구현하지 않는 이유
    - 일반적으로 수정 페이지 이동 하지않고 댓글 작성 form 부분만 변경되어 수정함
    - 페이지 일부영역만 업데이트 하는 것은 JavaScript의 영역

- 새로 작성한 Comment 모델을 admin site에 등록
```python
# articles/admin.py
from .models import Comment

admin.site.register(Comment)
```


## Django 14일차
### Many to one relationships 2
- Article(N) - User(1) : 0개 이상의 게시글을 1개 회원에 의해 작성 될 수 있음
- Comment(N) - User(1) : 0개 이상의 댓글은 1개의 회원에 의해 작성 될 수 있음
- 외래키는 N쪽이 들고 있다.

### Article & User
- User 외래키 정의
```python
# from accounts.models import User 비추천: 직접 참조할 수 있지만. 장고에서 간접 참조 함수 제공 하고 권장
# ​get_user_model "현재 프로젝트에 활성화"된 "User 객체"를 반환해주는 함수
# 다른 이름으로 상속 받아서 custom 해서 재정의 부분만 덮어씌움 accounts forms 참고
# user model은 추가적으로 생각해야할 것 있음

# 이전에 배웠던 get_user_model 함수 사용(models.py에서는 사용하지 않음)
# from django.contrib.auth import get_user_model

# settings.py 에 AUTH_USER_MODEL = 'accounts.User' => settings.AUTH_USER_MODEL 이거 가져다 쓰는건데.. 이거는 문자열이다 객체 아니다

# Django 내부 실행 원리(순서).. 나중에 user가 만들어졌을 때 문자열로 참조하게 함.그래야 정상 순서. user객체 사용하면 에러가 발생함.

# 유저 모델 참조 방법 2가지 get_user_model() 과 settings.AUTH_USER_MODEL 2가지
# 반환 되는 타입이 다름. 
# get_user_model() vs settings.AUTH_USER_MODEL /객체 vs 문자열/ models.py가 아닌 모든 곳에서 참조할 때 사용 vs models.py 모델 필드에서 참조할 때 사용

# models.py에서 User를 참조할땨만 다음과 같이 참조한다.
from django.conf import settings

# 마이그레이션 하면.. user default 기본값 설정하라고 나옴

# Create your models here.
class Article(models.Model):
    # user 소문자 + 단수형
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # # Article 클래스의 출력을 객체가 아니라 타이틀로 바꿔줌
    # def __str__(self):
    #     return self.title
```

#### User 모델을 참조하는 2가지 방법
##### get_user_model()
- 반환값 'User Object'(객체)
- models.py가 아닌 다른 모든 곳에서 참조할 때 사용

##### settings.AUTH_USER_MODEL
- 반환값 'accounts.User'(문자열)
- models.py의 모델 필드에서 참조할 때 사용

##### Migrations 진행
- 모든 컬럼은 NOT NULL 제약조건이 있어서 데이터 없이 새로추가 되는 user_id가 생성 되지 않음
- 기본값을 어떻게 할 것인지 1을 입력하고 enter 진행
- user_id에 어떤 데이터 넣을 것인지 1을 입력(임의로 user_id 1 입력)
- DB 확인

#### Article CREATE
1. ArticleForm 출력 확인
- User를 입력 폼에서 임의로 입력 하게 출력 됨

2. ArticleForm 출력 필드 수정
```python
# articles/forms.py
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content',) # 여기를 '__all__'에서 수정(User_id가 안보이도록)
```
3. 게시글 작성 시 User_id 필드 데이터 누락되어 에러 발생
- IntegrityError ~~ NOT NULL

4. 게시글 작성 시 작성자 정보가 함께 저장 될 수 있도록 save의 commit 옵션 활용
```python
# articles/views.py
@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False) # 일시정지
            article.user = request.user
            # article의 user필드에 request의 user 저장
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```

5. 게시글 작성후 테이블 확인


#### Article READ
1. index 템플릿과 detail 템플릿 에서 각 게시글의 작성자 출력 및 확인

```html
{% for article in articles %}
  {% comment %} <p>작성자: {{ article.user.username }}</p> 둘 다 됨. AbstractUser에 username 출력하도록 정의 되어있기때문에. 원래대로면 user까지 썼을때 user object 나와야됨 {% endcomment %}
  <p>작성자: {{ article.user }}</p> 

  <p>제목: 
    <a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a>
  </p>
  <p>내용: {{ article.content }}</p>
  <hr>
{% endfor %}
```

2. index 템플릿과 detail 템플릿 에서 각 게시글의 작성자 출력 및 확인

#### Article UPDATE
1. 수정을 요청 하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 수정하기
```python
# articles/view.py
@login_required # 막는 것뿐 아니라 로그인 페이지로 리다이렉트
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user == article.user:
    # 현재 수정을 진행 하려는 유저 vs 글 작성자 비교
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    # 비교한 유저와 작성자가 다르면 index로 리다이렉트
    else:
        return redirect('articles:index')
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```

2. 해당 게시글 작성자가 아니라면, 수정/ 삭제 버튼 출력 안하기
```html
  {% if  request.user == article.user %}
  <form action="{% url 'articles:delete' article.pk  %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="삭제">
  </form>
  <a href="{% url 'articles:update' article.pk %}">[UPDATE]</a>
    
  {% endif %}
```

#### Article DELETE
- 삭제 요청하는 사람과 게시글 작성한 사람 비교하여 본인만 삭제 가능하도록 함
```python
# articles/view.py
@login_required
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user == article.user: #본인만 삭제 가능
        article.delete()

    return redirect('articles:index')
```

### Comment & User
- User 외래키 정의
```python
# articles/models.py
class Comment(models.Model):
    # 외래 키 필드
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

#### Migration 진행
1. 진행 위에서 Article과 User모델 한 내용 반복
2. DB 확인

#### Comment CREATE
1. 댓글 작성시 user_id 필드 데이터 누락 에러 발생
- IntegrityError~~NOT NULL ~ user_id

2. 댓글 작성 시 작성자 정보가 함께 저장 되도록 save의 commit 옵션 활용
```python
@login_required
def comment_create(request, article_pk):
    # 몇 번 게시글인지 조회
    article = Article.objects.get(pk=article_pk)
    # 댓글 데이터를 받아서
    comment_form = CommentForm(request.POST)
    # 유효성 검증
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user # 유저 추가
        comment.save()
```
3. DB 테이블 확인

#### Comment READ 
- detail 템플릿에서 각 댓글의 작성자 출력 및 확인
```html
<!-- articles/detail.html -->
    {% for comment in comments %}

    <li>
      {% comment %} 그냥 user까지만도 가능 {% endcomment %}
      {{ comment.user.username }} - {{ comment.content }}
      <!-- 위에 추가 -->
      {% if request.user == comment.user  %}
        <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="삭제">
        </form>
      {% endif %}
```

#### Comment DELETE
1. 삭제를 요청하는 사람과 댓글 작성자 비교하여 본인 댓글만 삭제 할 수 있도록
```python
@login_required
def comment_delete(request, article_pk, comment_pk):
    # 삭제할 댓글을 조회
    comment = Comment.objects.get(pk=comment_pk)
    # article_pk = comment.article.pk 도 가능
    
    # 댓글 삭제를 요청하는자 vs 댓글 작성자 
    if request.user == comment.user: 
        # 댓글 삭제
        comment.delete()
    return redirect('articles:detail', article_pk)
```

2. 해당 댓글 작성자가 아니라면, 댓글 삭제 버튼을 출력하지 않도록 함
```html
<!-- articles/detail.html -->
    <li>
      {{ comment.user.username }} - {{ comment.content }}
      {% if request.user == comment.user  %}
      <!-- if 문 작성 -->
        <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="삭제">
        </form>
      {% endif %}
```
### 참고
- 인증된 사용자인 경우만 댓글 작성 및 삭제: @login_required
```python
@login_required
def comment_create(request, article_pk):

@login_required
def comment_delete(request, article_pk, comment_pk):
```

## Django 15일차
### Many to many relationships1
#### M:N 관계 맛보기
- 병원진료 시스템 모델 관계 만들기(환자-의사)
  - N:1은 동일한 환자지만 다른 의사에계 예약하기 위해 객체를 하나더 만들어서 예약해야함. 새로운 객체 생성할 수 밖에 없음

#### 중개 모델
- 환자의 외래키 삭제하고 별도의 예약 모델(중개모델) 새로 작성
- 예약 모델은 의사와 환자에 가각 N:1 관계

```python
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)
    # 

    def __str__(self):
        return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'

```

##### through argument
- 중개 테이블을 수동으로 지정하는 경우 through 옵션을 사용하여 사용하려는 중개 테이블을 나타내는 Django 모델을 지정할 수 있음
- 가장 일반적 용도는 "중개테이블에 '추가데이터'를 사용해 다대다 관계와 연결하려는 경우

##### 정리
- M:N 관계로 맺어진 두 테이블에는 변화가 없음
- ManyToManyField는 중개 테이블을 자동으로 생성함
- ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관 없음
- 대신 필드 작성위치에 따라 참조와 역참조 방향을 주의할 것 
- N:1은 완전한 종속의 관계였지만 M:N 은 의사에게 진찰 받는 환자, 환자를 진찰하는 의사의 두가


##### ManyToManyField(to, **options)
- many-to-many 관계 설정 시 사용하는 모델 필드
- 모델 필드의 RelatedManager를 사용하여 관련 개체를 추가, 제거 또는 생성
  - add(), remove(), create(), clear()

##### ManyToManyField's Arguments
1. related_name
- 역참조시 사용하는 manager name을 변경
```python
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')

# 변경 전
user.like_users_set.all()
# 변경 후
user.like_articles.all()
```
2. through
- 중개 테이블을 직접 작성하는 경우, through 옵션을 사용하여 중개테이블을 나타내는 Django 모델을 지정
- 일반적으로 중개 테이블에 추가 데이터를 사용하는 다대다 관계와 연결하려는 경우(extra data with a many-to-may relationship)에 사용 됨

3. symmetrical
- True일 경우
  - _set 매니저를 추가하지 않음
  - source 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함(대칭)
  - 즉 개가 당신의 친구면 당신도 내 친구가 됨
- False일 경우: 대칭을 원하지 않는 경우
  - Follow 기능 구현에서 다시 확인할 예정

##### M:N에서의 methods
- add()
  - 지정된 객체를 관련 객체 집합에 추가
  - 이미 존재하는 관계에 사용하면 관계가 복제 되지 않음
- remove()
  - 관련 객체 집합에서 지정된 모델 개체를 제거

#### Many to many relationships(N:M or M:N)
- 한테이블의 0개이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
- 양쪽 모두에서 N:1 관계를 가짐

##### Article(M) - User(N)
- 게시글은 회원으로부터 0개 이상의 좋아요를 받을 수 있고, 회원은 0개 이상의 게시글에 좋아요를 누를 수 있다.

##### 모델 관계 설정
1. ManyToManyField 작성 (중간 단계)
```python
# articles/models.py
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
2. 모델 관계 설정
- migration 진행 후 에러 확인
- like_users 필드 생성 시 자동으로 역참조에는 .article_set 매니저가 생성됨
- 그러나 이전 N:1(Article-User)관계에서 이미 해당 매니저를 사용 중
  - user.article_set.all() -> 해당 유저가 작성한 모든 게시글 조회ㅏ
- user가 작성한 글들(user.article_set)과 user가 좋아요를 누른글(user.article_set)을 구분할 수 없게 됨
- user와 관계된 ForeignKey 혹은 ManyToManyField 중에 하나에 related_name을 작성해야 함

- user.article_set
  - N:1 : 유저가 작성한 게시글 vs M:N : 유저가 좋아요한 게시글  (related manager 충돌)

3. 모델 관계 설정(최종 단계)
- related_name 작성 후 Migration
```python
# articles/models.py
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles') #여기
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
4. 모델 관계 설정
- 생성된 중개 테이블 확인

##### User - Article간 사용 가능한 related manager 정리
- article.user
  - 게시글을 작성한 유저
- user.article_set
  - 유저가 작성한 게시글(역참조) - N:1
- article.like_users
  - 게시글을 좋아요한 유저 - M:N
- user.like_articles
  - 유저가 좋아요한 게시글(역참조) - M:N


#### 좋아요 구현
1. url 및 view 함수 작성
```python
# articles/urls.py
app_name = 'articles'
urlpatterns = [
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]

# articles/views.py
def likes(request, article_pk):
    # 좋아요를 누른 대상 게시글
    article = Article.objects.get(pk=article_pk)

    # 좋아요 관계를 추가 or 삭제
    # 현재 좋아요를 요청하는 유저가 해당 게시글의 좋아요를 누른 유저 목록에 있는지 없는지를 확인
    if request.user in article.like_users.all():

    # # 해당 게시글의 좋아요를 누른 유저에서 현재 요청하는 유저의 존재를 조회(조회해야하는 데이터가 너무 커지면 이걸 쓰는게 나음. 하나가 존재하는지 아닌지 알고 싶을 때)
    # if article.like_users.filter(pk=request.user.pk).exists():

        # 좋아요 취소
        article.like_users.remove(request.user)
        # request.user.like_articles.remove(article) # 역참조(위와 동일)
    else:
        # 좋아요 추가
        article.like_users.add(request.user)
        # request.user.like_articles.add(article) # 역참조
    return redirect('articles:index')
```

2. index 템플릿에서 각 게시글에 좋아요 버튼 출력
```html
<!-- articles/index.html -->
  {% for article in articles %}
    <p>작성자: {{ article.user }}</p>
    <p>제목: 
      <a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a>
    </p>
    <p>내용: {{ article.content }}</p>
    <form action="{% url 'articles:likes' article.pk %}" method="POST">
      {% csrf_token %}
      {% if request.user in article.like_users.all %}
        <input type="submit" value="좋아요 취소">
      {% else %}
        <input type="submit" value="좋아요">
      {% endif %}
    </form>
    <hr>
  {% endfor %}
```

3. 좋아요 버튼 출력 확인

4. 좋아요 버튼 클릭 후 DB 테이블 확인

### 참고
- .exists() : QuerySet에 결과가 포함되어 있으면 True를 반환하고 그렇지 않으면 False를 반환 특히 큰 QuerySet에 있는 특정 개체의 존재와 관련된 검색에 유용
- exists() 적용

```python
# articles/views.py
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    # if request.user in article.like_users.all():
    #  위에서 아래로 변경
    if article.like_users.filter(pk=request.user.pk).exists(): # 여기

        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:index')
```

## Django 16일차
### Many to many relationships 2
### Profile 구현
1. 자연스러운 follow 흐름을 위한 프로필 페이지 작성
```python
# accounts/urls.py
urlpatterns = [
    path('<username>/', views.profile, name = 'profile'),
        #str: 생략가능
        # username 밑에 다른 url은 작동 안함
        # 1. 맨아래에 두기 2. 'profile/<username>/로 섞어주기 두가지 방법
]

# account/views.py
from django.contrib.auth import get_user_model

def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person': person, 
    }
    return render(request, 'accounts/profile.html', context)
```

2. profile 템플릿 작성
```html
<!-- accounts/profile.html -->

  <h3>{{ person.username }}가 작성한 모든 게시글</h3>
  {% for article in person.article_set.all  %}
    <div>{{ article.title }}</div>
  {% endfor %}

  <h3>{{ person.username }}가 작성한 모든 댓글</h3>
  {% for comment in person.comment_set.all  %}
    <div>{{ comment.content }}</div>
  {% endfor %}

  <h3>{{ person.username }}가 좋아요를 누른 모든 게시글</h3>
  {% for article in person.like_articles.all  %}
    <div>{{ article.title }} </div>
  {% endfor %}
```
3. profile 템프릿으로 이동할 수 있는 하이퍼 링크 작성
```html
 <!-- articles/index.html -->
    <a href="{% url 'accounts:profile' user.username %}">내 프로필</a>

     <p>작성자:
      <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a>
    </p>
```
4. 출력 확인

### User & User - follow 구현
- 유저는 0이상의 다른 유저와 관련된다.
  - 유저는 다른 유저로부터 0개 이상의 팔로우를 받을 수 있고, 유저는 0명 이상의 다른 유저들에게 팔로잉 할 수 있다.

#### Follow 구현
1. ManyToManyField 작성 및 Migration 진행
```python
# accounts/models.py
class User(AbstractUser):
    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    # 정참조인데 자기자신 일때 역참조 이름 만들어야 함
    # symmetrical 기본값 True면 대칭이라서 변경 필요
```

2. 중개테이블 필드 확인
- accounts_user_followings
- id / from_user_id / to_user_id

3. url 및 view 함수 작성
```python
# accounts/urls.py
urlpatterns = [
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]

# accounts/views.py

login_required
def follow(request, user_pk):
    # 팔로우를 할 대상이 필요
    User = get_user_model()
    you = User.objects.get(pk=user_pk)
    me = request.user
    if you != me:
        # 팔로우 or 언팔로우
        if me in you.followers.all():
            # 언팔로우
            you.followers.remove(me)
            # me.followings.remove(you)
        else:
            # 팔로우
            you.followers.add(me)
            # me.followings.add(you)
    return redirect('accounts:profile', you.username) # 상대방 프로필 페이지이기 때문 you.username
```

4. 프로필 유저의 팔로잉, 팔로워 수 & 팔로우 , 언팔로우 버튼 작성
```html
<!-- accounts/profile.html -->
  <div>
    팔로잉 : {{ person.followings.all|length }} / 팔로워 {{ person.followers.all|length }}
  </div>

  {% if request.user != person %}
  <div>
    <form action="{% url 'accounts:follow' person.pk %}">
      {% csrf_token %}
      {% if request.user in person.followers.all %}
        <input type="submit" value="언팔로우">
      {% else %}
        <input type="submit" value="팔로우">
      {% endif %}
    </form>
  </div>
  {% endif %}
```

5. 팔로우 버튼 클릭 후 팔로우 버튼 변화 및 중개 테이블 데이터 확인


### Fixtures
- Django가 데이터베이스로 가져오는 방법을 알고 있는 데이터 모음
- Django가 직접 만들기 때문에 데이터 베이스 구조에 맞추어 작성 되어있음

- Django는 fixtures를 사용해 모델에 초기 데이터를 제공
#### 초기데이터의 필요성
- 협업 하는 a,b 유저가 프로젝트 처음 시작할 때 미리 DB를 채움
- Django에서는 fixtures를 사용해 앱에 초기 데이터(initial data)를 제공할 수 있다.

#### 초기 데이터 제공하기
- 사전준비
  - M:N까지 모두 작성된 프로젝트에서 유저, 게시글, 댓글, 좋아요 등 각 테이터 최소 2개 이상 생성해두기

- fixtures 명령어
  - dumpdata: 생성(데이터 추출)
  - loaddata: 로드(데이터 입력)

#### dumpdata
- 데이터베이스의 모든 데이터를 출력, 여러모델을 하나의 json 파일로 만들수 있음
```bash
# 작성 예시
$ python manage.py dumpdata [app_name[.ModelName]] [app_name[.ModelName]] ... > filename.json
```
#### fixtures 생성
1. 
```bash
$ python manage.py dumpdata --indent 4 articles.article > articles.json
```

2.
1. 
```bash
$ python manage.py dumpdata --indent 4 articles.user > users.json
$ python manage.py dumpdata --indent 4 articles.comment > comments.json
```

#### loaddata
- fixtures 데이터를 데이터베이스로 불러오기

##### fixtures 기본 경로
- app_name/fixtures
- django는 설치된 모든 app의 디렉토리에서 fixtures 폴더 이후의 경로로 fixtures 파일을 찾아 load 함

##### fixtures 불러오기
1.
```python
# 해당 위치로 fixture 파일 이동
articles/
  fixtures/
    articles.json
    users.json
    comments.json
```
- db.sqlite3 파일 삭제 후 migrate 진행

2.
```bash
$ python manage.py loaddata articles.json users.json cooments.json
``` 
- load 후 데이터가 잘 입력 되었는지 확인하기

#### loaddata 순서 주의사항
- loaddata를 한번에 실행하지 않고 하나씩 실행한다면 모델 관계에 따라 순서가 중요할 수 있음
  - comment는 article에 대한 key 및 user에 대한 key가 필요
  - article은 user에 대한 key가 필요
- 즉, 현재 모델 관계에서는 user -> article -> comment 순으로 data를 넣어야 오류 발생하지 않음
```bash
$ python manage.py loaddata users.json
$ python manage.py loaddata articles.json
$ python manage.py loaddata comments.json
``` 

### 참고
#### 모든 모델을 한번에 dump 하기
```bash
# 3개의 모델을 하나의 json 파일로
$ python manage.py dumpdata --indent 4 articles.article articles.comment accounts.user > data.json

# 모든 모델을 하나의 json 파일로
$ python manage.py dumpdata --indent 4 > data.json
``` 

- fixtures는 직접 만드는 것이 아니다
  - 반드시 dumpdata를 사용하여 생성하는 것

#### loaddata 시 encoding codec 관련 에러가 발생하는 경우
- 2가지 방법 중 택 1
##### dumpdata 시 추가 옵션 작성
```bash
$ python -Xutf8 manage.py dumpdata [생략]
``` 

##### 메모장 활용
  1. 메모장으로 json 파일열기
  2. 다른이름으로 저장 클릭
  3. 인코딩을 UTF8로 선택 후 저장


## Django 17일차


## Django 18일차

### Django rest framework

#### HTTP Request Methods
- 리소스(resource, 자원)에 대한 행위(수행하고자 하는 동작)를 정의 HTTP verbs 라고도 함

#### 대표 HTTP Request Methods
1. GET
- 서버에 리소스의 표현을 요청
- GET을 사용하는 요청은 데이터만 검색해야 함
2. POST
- 데이터를 지정된 리소스에 제출
- 서버의 상태를 변경
3. PUT
- 요청한 주소의 리소스를 수정
4. DELETE
- 지정된 리소스를 삭제

#### HTTP response status codes
- 특정 HTTP 요청이 성공적으로 완료 되었는지 여부를 나타냄
- 응답은 5개의 그룹으로 나뉨
  - informational responses: 100-199
  - Successful responses: 200-299
  - Redirection messages: 300-399
  - Client error responses: 400-499
  - Server error responses: 500-599


### REST API

#### API(application programming interface)
- 애플리케이션과 프로그래밍으로 소통하는 방법
- API는 복잡한 코드를 추상화하여 대신 사용할 수 있는 몇가지 더 쉬운 구문을 제공

#### Web API
- 웹서버 또는 웹브라우저를 위한 API
- 현재 웹 개발은 모든 것을 하나부터 열까지 직접 개발하기보다 여러 open API를 활용하는 추세
- 대표적인 Third Party Open API 서비스 목록
  - YoutubeAPI, Naver Papago Kakao Map API 등
- API는 다양한 타입의 데이터를 응답
  - html, json 등


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

### Response JSON
- 지금까지 Django로 작성한 서버는 사용자에게 페이지만 응답하고 있었음
- 하지만 사실 서버가 응답할 수 있는 것은 페이지(html) 뿐만 아니라 다양한 데이터 타입을 응답할 수 있음
- Django는 더이상 Template 부분에 대한 역할을 담당하지 않게 되면 Front-end와 Back-end가 분리되어 구성되게 됨

![image](https://user-images.githubusercontent.com/110805149/233928600-6b908ee5-5006-431c-aa44-b2696c083581.png)

### Django REST framework(DRF)
- Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리
- https://www.django-rest-framework.org/

#### python에서 json 응답 받아보기
```python
import requests
from pprint import pprint

response = requests.get('http://127.0.0.1:8000/api/v1/articles/')

# json을 python 타입으로 변환
result = response.json()

# print(type(result))
# pprint(result)
# pprint(result[0])
pprint(result[0].get('title'))
```

### Serialization(직렬화)
- 여러시스템에서 활용하기 위해 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정
- 즉, 어떠한 언어나 환경에서도 `나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정`
![image](https://user-images.githubusercontent.com/110805149/233929855-1fd97c04-0a45-4b76-a140-1b60e499c6f4.png)
- Serialization in DRF : Serialized data를 JSON으로 변환

### DRF - Single Model
- Postman 설치
- Postman : API 구축하고 사용하기 위한 플랫폼, API를 빠르게 만들 수 있는 여러 도구 및 기능을 제공

#### ModelSerializer 작성
- articles/serializer.py 생성
- serializer.py 위치나 파일명은 자유롭게 작성 가능

```python
from rest_framework import serializers
from .models import Article
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)
```
#### ModelSerializer
- 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만듦
1. Model 정보에 맞춰 자동으로 필드 생성
2. serializer에 대한 유효성 검사기를 자동으로 생성
3. .create() 및 .update()의 기본 구현 메서드가 포함됨

- URL과 HTTP requests methods 설계
![image](https://user-images.githubusercontent.com/110805149/233934407-8cda17d7-6773-4b35-ac9b-b95ae0650389.png)

#### GET, POST, PUT, DELETE
- 코드 한 번에 
```python
# articles/urls.py
urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
]


# articles/views.py
# from django.shortcuts import render (이제 필요 없음)
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer

# Create your views here.
# drf는 api view 데코레이터 필수임
# 4. 해당 view 함수가 어떤 http 요청 메서드를 허용하는지 결정하는 데코레이터 작성(drf의 view함수에서 필수)
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # 1. 제공할 게시글 목록 조회
        articles = Article.objects.all()

        # 2. 게시글 목록 데이터를 직렬화(serialization)
        serializer = ArticleListSerializer(articles, many=True) #many 앞의 데이터가 다중데이터(쿼리셋: 객체모음)일때 True로 단일일 때 false

        # 3. 직렬화된 데이터를 json 데이터로 응답
        return Response(serializer.data) 
            #.data 그냥 문법임

    elif request.method == 'POST':
        # 사용자 데이터를 받아서 serializer로 직렬화
        serializer = ArticleSerializer(data=request.data)
        # request.post였는데 drf에서는 request.data
        # 유효성 검사
        if serializer.is_valid():
            # drf가 장고개발자위해 똑같이 is_valid만들어둠
            serializer.save()
            # 생성 성공 시 201 응답
            # 원래는 성공 시 status 200이 기본값인데 정확히는 201이 맞음
            return Response(status=status.HTTP_201_CREATED)
        # 생성 실패 시 400 응답
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        # 단일데이터 many 없어도 됨
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        # 삭제 성공 204

    elif request.method == 'PUT':
        # 사용자 데이터를 받아서 serializer로 직렬화 + 기존 데이터
        serializer = ArticleSerializer(article, data=request.data)
        # 앞이 instance 뒤에 객체
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
            # 수정은 생성의 하나로 봐서 status 따로 없음. 규약에 맞춰 쓰는 것뿐
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) - 생략 가능(is_valid(raise_exception=True) 대체)
```

#### 'api_view' decorator
- DRF