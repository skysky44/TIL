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
