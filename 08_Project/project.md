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

# 5. 현재 브랜치에 models 브랜치 merge
$ git merge models
