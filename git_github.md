# Git & GitHub 1일차

## CLI
 - Command Line Interface
 - 명령 기반의 인터페이스

## GUI
  - Graphical User Interface
  - 그래픽 기반의 인터페이스

  `인터페이스란 내가 무언가를 조작하는 하나의 접면`

## CLI 명령어 정리
```bash
 ls : 목록
 mkdir 폴더명 : 디렉토리 생성
 cd : 이동
 cd .. : 상위 디렉토리
 cd . : 현재 디렉토리
 touch 파일명 : 새로운 파일을 생성
 rm 파일명 : 파일삭제
 rm -r 폴더명 : 폴더 삭제 가능(포함한 모든 폴더와 파일 같이 삭제)
 ~ : 홈 디렉토리
 pwd : 현재 디렉토리 출력
```
## 버전관리
### Git
  - 분산 버전 관리 시스템
  - 로컬에서도 버전 기록 관리

  - Working directory : 파일의 변경사항
  - Staging area : 버전으로 기록하기 위한 파일 변경사항의 목록
  - Repository : 커밋(버전)들이 기록 되는 곳
  
### Git 명령어
  ```bash
  $ git init # git 폴더 생성
  $ git add # staging area로
  $ git commit -m <메시지> # repository로
  $ git status # 현재 상태(?)
  $ git log # 커밋 상태
  $ :q # 나올때
  ```

### 궁금한 점
  - HEAD -> master 의미
  - git reset 사용법
  > [reset_명확히_알고_가기](https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-Reset-%EB%AA%85%ED%99%95%ED%9E%88-%EC%95%8C%EA%B3%A0-%EA%B0%80%EA%B8%B0)

  ```bash
  $  git reset --soft # HEAD만 이동
  $  git reset --mixed # add 전 상태로
  $  git reset --hard # 다 지워짐
  
  $  git reset --hard [깃 커밋 해시]
  $  git reset --hard HEAD^ # ^ 개수만큼 커밋 지워짐
  ```


# Git & GitHub 2일차
## 학습목표
- 원격저장소 활용 명령어를 이해하고 설명할 수 있다.
- 분산버전관리 시스템을 이해하고 설명할 수 있다.
- GitHub 원격 저장소에 로컬 저장소를 올려 관리할 수 있다.
- 원격저장소 활용 명령어를 이해하고 설명할 수 있다.

## 원격저장소(Remote Repository)
- GitHub, GitLab, Bitbucket 등
- Git도 버전관리, Github도 버전관리

## 원격저장소 활용

### Pull, Push 하기
1. Repository 생성(GitHub)

2. 로컬저장소에 원격저장소 정보 설정
```bash
$ git remote add origin <url> 
  # 원격저장소 추가해 오리진으로~
```
3. 로컬 저장소 버전을 원격저장소로 Push 하기
- Push: 로컬저장소 버전 -> 원격저장소
```bash
$ git push origin master 
```
4. 원격 저장소 버전을 로컬 저장소로 Pull 하기
- Pull : 원격저장소 버전 -> 로컬저장소
```bash
$ git pull oigin master
```

> origin: 원격저장소 기본이름이다. 마스터처럼

### Clone 하기
- 협업 프로젝트 등에 사용

```bash
$ git clone <url>
```
> 클론한 경우 git init 불필요. 폴더 안에 .git 이미 있기 때문

### 관련 명령어 정리
```bash
$ git clone <url> #원격저장소 복제
$ git remote -v #원격저장소 정보확인, v=verbose 상세하게 출력한다
$ git remote add <원격저장소> <url> #원격저장소 추가
$ git remote rm <원격저장소> #원격 저장소 삭제
$ git push <원격저장소> <브랜치> #원격 저장소에 push
$ git pull <원격저장소> <브랜치> #원격저장소로부터 pull
```

### gitignore
- 버전관리랑 상관없는 파일이나 비밀정보를 따로 관

1. .gitignore 생성

2. .gitignore 내에 작성
- secret.xlsx : 파일
- user/       : 디렉토리 
- *.pptx      : 모든 pptx
- !b.exe      : 예외처리

3. 주의사항
- 이미 커밋 된 것은 무시가 안된다!
- 미리 .gitignore 하자. 처음부터 잘.


4. 참고사항
- [gitignore.io](https://gitignore.io/) : 버전관리와 상관없는 파일제외하는 코드 검색 가능. 복붙 사용.
- 일반적으로 상위 폴더에 만듦

### 기타
- git add 하고 push 하면 안올라감. 깃헙은 커밋을 올리는 것!!!
- git 관리되는 폴더 내에 또 git 폴더 만들면 안됨. 서브모듈 배우면 되지만. 그냥은 안 됨.
- $ git status 까먹지마라!
- $ git commit 에서 바로 엔터치면 메시지 뜨는데, 커밋메시지 쓰고 :wq 하면 됨
- $ ​git config --global core.editor "code --wait" : 커밋 메시지 vim 창 안 뜨고 vscode 창이 뜨게 함

### 참고자료
- [Git초심자설명](https://backlog.com/git-tutorial/kr/)
- [Git완벽책](https://git-scm.com/book/en/v2)