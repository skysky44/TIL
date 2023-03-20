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