# 프로젝트에서 새로 알게 된 내용 또는 후기

## 230427

- 작업 중인 브랜치(로컬)에서 다른 브랜치(원격)의 변경 된 코드를 받아서 반영한 뒤 현재 내 로컬 브랜치에서 이어서 작업하기
```bash
# 1. 원격 브랜치 목록을 가져오기(--prune 옵션은 로컬 저장소에서 원격 저장소에서 삭제된 브랜치와 태그 등을 자동으로 제거)
# "git fetch" 명령어는 원격 저장소의 최신 변경 내용을 로컬 저장소로 가져오는 명령어
$ git fetch --prune

# 2. 원격 브랜치 목록 확인
$ git branch -r

# 3. models라는 브랜치를 만들어 origin/models 브랜치 가져오기

$ git checkout -t origin/models 

# 4. 기존 브랜치로 돌아가기
$ git checkout [기존 로컬 브랜치명]

# 5. 현재 브랜치에 models  브랜치 merge
$ git merge models 
```

## 230428
```bash
vi plates/models.py
# 텍스트에디터 vim improved

python -Xutf8 manage.py loaddata posts.json reviews.json

git rebase --continue
```


## 230502
### 소셜 로그인 (카카오 api) 순서 대로

#### django-allauth 설치 및 기본 세팅
```bash
# 라이브러리 설치
pip install django-allauth
```

```python
# settings.py

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)



INSTALLED_APPS = [

    # 카카오톡 소셜 로그인 관련 부분
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.kakao',
    
]


SITE_ID = 1
LOGIN_REDIRECT_URL = '/'  # 로그인 후 리다이렉트 될 경로


# urls.py - 프로젝트 폴더 안에 urls.py

urlpatterns = [
	
    # 소셜로그인 관련 url
    path('accounts/', include('allauth.urls')),

]

```
#### 마이그래이션

```bash
# 마이그래이션
python manage.py makemigrations
python manage.py migrate

#서버 실생
python manage.py runserver
```

#### admin 페이지 접속
- 소셜 애플리케이션에 클라이언트 아이디와 비밀 키 등록 
- 또는(위아래 둘중 택 1)
- settings.py에 아래 코드 추가
```python
SOCIALACCOUNT_PROVIDERS = {
    'kakao': {
        'APP': {
            'client_id': 'ebf3ef3af88a14332db7d305424cc5f5',
            'secret': 'ph9pfWMBdkqx5Vijx0q9XY9ny4Civ6FC',
            'key': '',
        },
        'SCOPE': ['account_email', 'profile_image', 'profile_nickname'],# 권한
        'PROFILE_FIELDS': ['nickname', 'profileImageURL', 'email'], # 요청 정보 종류
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
    }
}
```

#### 템플릿 추가

```html
<!-- login.html -->
{% load socialaccount %}

<a href="{% provider_login_url 'kakao' method='oauth2' %}">
카카오톡 로그인
</a>
```
#### 참고
- 카카오 디벨로퍼 사이트에서 rest api key 와 secret 발급(다른 문서 참고)


## 230503
- 다중 이미지 추가 드디어 성공

## 230506
### 발표 목차
1. 프로젝트 개요
- 1-1 개발동기	
- 1-2 기획의도
2. 프로젝트 상세
- 2-1 구조도
- 인덱스.  맛집 페이지 . 리뷰 상세 페이지. 프로필페이지
- 2-2 ERD
- 2-3 기술설명
3. 프로젝트 시연
- 3-1 시연
4. 진행 프로세스
- 4-1 개발일정
- 4-2 개발환경
- 4-3 마치며
