# Django 완전 처음 시작 가이드
## 개발 환경 설정 단계
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

## 앱 생성 & 등록

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


## Migrations 순서

- 순서: `models.py에 class 생성 > 설계도 작성 > 설계도를 DB에 반영`
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
- 순서: `admin 계정 생성 > DB에 생성된 admin 계정 확인 > admin에 모델 클래스 등록 > 서버켜고 로그인 후 모델클래스 등록 확인 > 데이터 CRUD 테스트, 실제 DB 테이블 저장 확인`

#### admin 계정 생성
- createsuperuser

```bash
$ python manage.py createsuperuser
# email은 선택 사항(입력 안하고 진행 가능)
# 비밀 번호 생성시 보안상 터미널에 출력 안됨 무시하고 입력 하면 됨. 커서(?)안움직임
```

#### admin에 모델 클래스 등록
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