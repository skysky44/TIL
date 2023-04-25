# Github flow Collaboration
- 깃허브로 협업 하기

## 순서 요약
1. 팀장이 깃헙 만들고 환경 세팅
2. 팀원 깃헙 클론해서 각자 브랜치 생성 후 로컬 작업 후 push
3. 원격(레포지토리)에서 PR 하기
4. 원격에서 merge 하기(팀원들과 공유 후) - merge 후 브랜치 삭제
5. 로컬에서 main 브랜치로 변경 후 작업 했던 브랜치 삭제 

## branch 관련 명령어(생각 안나는 것 위주)
```bash
# 브랜치 생성 & 전환
git checkout -b [브랜치명]

# 브랜치 전환
git checkout [브랜치명]

# 브랜치 목록 확인
git branch -v

# 브랜치 삭제
git branch -d [브랜치명]

# 브랜치명
git branch -m [기존 브랜치명] [변경할 브랜치명]
```


## 개발 환경 준비
1. (팀장) Github 원격 저장소 생성
2. (팀장) Collaborator 초대
- (팀장) Collaborators 메뉴
- (팀장) 초대 아이디 입력
- (팀원) 이메일 확인
- (팀원) Collaborators 요청 수락
3. (전체) Github 원격 저장소 clone
4. (팀장) git 프로젝트 폴더에 개발 환경 구축
- .gitignore
- 가상환경 생성 및 실행
- django 및 기타 패키지 설치
- requirements.txt 작성
5. (팀장) git add & commit & push
6. (팀원) git pull
7. (팀원) 가상환경 및 패키지 목록 설치

## 개발 루틴

1. [로컬 / 드라이버] 토픽 브랜치 생성 & 전환
```bash
# 브랜치 생성 & 전환
git checkout -b [브랜치명]

# 브랜치 전환
git checkout [브랜치명]

# 브랜치 목록 확인
git branch -v

# 브랜치 삭제
git branch -d [브랜치명]

# 브랜치명
git branch -m [기존 브랜치명] [변경할 브랜치명]
```

2. [로컬 / 드라이버] 토픽 개발

3. 원격 저장소 add & commit & push
```bash
git add .

git commit -m '토픽 개발 내용'

# 현재 로컬 토픽 브랜치와 동일한 브랜치명으로 push
git push origin [브랜치명]
```
4. [원격 / 드라이버] 깃허브 PR 생성(토픽 브랜치 -> 메인 브랜치)
5. [원격 / 드라이버] 병합(merge)
6. [원격 / 드라이버] 토픽 브랜치 삭제
7. [로컬 / 드라이버] 메인 브랜치 전환 후 pull

```bash
git checkout [메인 브랜치명]

git pull origin [메인 브랜치명]
```
8. [로컬 / 드라이버] 토픽 브랜치 삭제
```bash
git branch -d [브랜치명]
```

## 병합(merge) 충돌(conflict)
### 병합 충돌 발생 이유
- 두 개의 개별 브랜치가 한 파일에서 같은 줄을 편집한 경우
- 한 브랜치에서는 파일이 삭제되었지만 다른 브랜치에서는 편집한 경우
### 병합 출동 확인 & 해결
1. Pull Request 생성 페이지, Create pull request 클릭
2. Pull Request 조회 페이지, Resolve conflicts 클릭
3. 병합 해결
- 충돌 코드 확인
- 코드 정리
- 커밋
4. 병합(merge)