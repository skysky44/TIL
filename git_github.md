# Git & GitHub

## CLI
 - Command Line Interface
 - 명령 기반의 인터페이스

## GUI
  - Graphical User Interface
  - 그래픽 기반의 인터페이스

  `인터페이스란 내가 무언가를 조작하는 하나의 접면`

## CLI 명령어 정리
  - ls : 목록
  - mkdir 폴더명 : 디렉토리 생성
  - cd : 이동
  - cd .. : 상위 디렉토리
  - cd . : 현재 디렉토리
  - touch 파일명 : 새로운 파일을 생성
  - rm 파일명 : 파일삭제
  - rm -r 폴더명 : 폴더 삭제 가능(포함한 모든 폴더와 파일 같이 삭제)
  - ~ : 홈 디렉토리
  - pwd : 현재 디렉토리 출력

## 버전관리
### Git
  - 분산 버전 관리 시스템
  - 로컬에서도 버전 기록 관리

  - Working directory : 파일의 변경사항
  - Staging area : 버전으로 기록하기 위한 파일 변경사항의 목록
  - Repository : 커밋(버전)들이 기록 되는 곳
  
  ### Git 명령어
  - git init : git 폴더 생성
  - git add : staging area로
  - git commit -m '메시지' : repository로
  - git status : 현재 상태(?)
  - git log : 커밋 상태
  - :q 나올때

  ### 궁금한 점
  - HEAD -> master 의미
  - git reset 사용법
  > [reset_명확히_알고_가기] (https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-Reset-%EB%AA%85%ED%99%95%ED%9E%88-%EC%95%8C%EA%B3%A0-%EA%B0%80%EA%B8%B0)

    
      git reset --soft : HEAD만 이동
      git reset --mixed : add 전 상태로
      git reset --hard : 다 지워짐
      
      git reset --hard [깃 커밋 해시]
      git reset --hard HEAD^ : ^ 개수만큼 커밋 지워짐
    