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
# 로그인 버튼
```html
{% load socialaccount %}
<a class='' href="{% provider_login_url 'kakao' process="login" method='oauth2'%}">
  <i class=""></i>
</a>
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


## 230508
### 1차 프로젝트 회고
1. KEEP : 어떤 방식들을 다음 프로젝트에도 유지했으면 하나요? 
- 조원들 간 편안한 분위기 및 서로 배려 해주는 것들이 가장 유지 되었으면 합니다.
- 매일 마무리 할 때 아쉬운 부분이나 좋았던 부분 회고 할 때 솔직하게 말해주던 부분들 이 좋았습니다.
후반부에 시간이 적다 보니 정말 필요한 것들 부터 우선 순위를 정해서 작업한 부분이 완성도나 작업속도 둘 다에 좋은 영향을 준 것 같아서 유지 되었으면 합니다.
- 2.  PROBLEM : 어떤 방식이 문제였나요? 개선할 수 있는 것들 
- 프론트와 백의 개발 순서 조절을 잘하면 좋을 것 같아요. 프론트도 백도 기본적인 코드나 템플릿부터 깔아 두고 만들어 나가면 속도를 맞춰서 같이 나가기에 좀 더 수월 할 듯해요.
- 문제 상황이나 에러가 발생 했을 때 혼자 오래 잡고 있는 것도 좋지만 조원들에게 또는 조원 외에 다른 분들에게 도움을 요청 해보는 것도 좋을 것 같아요. 혼자 계속 보면 힘들고 결과물이 없다는 생각에 부담감과 미안함만 늘더라고요. 
- 태스크 보드 작성이 익숙하지 않아요. 작업을 공유하고 진행 상황보기위해 적는 것이 아닌 단순 기록용으로 적는 느낌이 들어서 아쉬웠어요. 
- 모델의 변경이 잦아서 코드가 복잡해지고 같은 작업이 반복 되는 것 같기도 합니다. 최초 ERD 작성을 조금 더 다 같이 공유해서 하고 이후에 작업하면서 필요할 때 조금만 수정 할 수 있도록 할 필요가 있을 것 같아요.
3.  TRY : 문제였던 방식들 개선하기 위해 다음 프로젝트때 어떤 방식을 해보고 싶나요? 
- 처음부터 우선 순위를 단계별로 잘 정하고 ERD 작성을 꼼꼼하게 해서 작업 해보고 싶어요. 지라 사용 해서 조금 더 과정을 눈으로 보면서 작업 하고 싶어요. 조금 더 편하게 얘기도 해보고 싶어요. 더 친해지고 싶습니다.

-  기술적인 부분에서는 이번보다 조금 더 업그레이드 해서 처음부터 우선 순위를 단계별로 잘 정하고 ERD 작성을 꼼꼼하게 해서 작업 해보고 싶어요. 지라 사용 해서 조금 더 과정을 눈으로 보면서 작업 하고 싶어요. 사실 크게 문제를 느끼진 못했지만 생각해본 부분입니다.
-  조원들과 관계에서 처음엔 어색했는데 프로젝트가 끝나가니까 내적 친밀감이 생긴 느낌입니다. 처음 하는 프로젝트이고 조장도 처음 한 건데 아무래도 미흡한 부분들이 많았을 텐데 다들 이해 해 주셔서 감사했어요. 그리고 조 안에서 서로 도움 주면서 해결해 나갈 때 도움도 많이 받고 저도 소소하게 알려 드렸던 것 같습니다. 처음엔 조용한 분위기라서 살짝 걱정도 되었지만 다들 각자 맡은 부분 엄청 열심히 하셔서 제가 더 열심히 해야겠다라는 생각이 많이 들었어요.
