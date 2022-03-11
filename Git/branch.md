## Git 브랜치

[Git 공식 문서](https://git-scm.com/book/en/v2)

> 브랜치 왜 이용하나
>
> 현재 사용하고 있는 네이버 서비스를 수정할 수 없음. 네이버는 브랜치를 생성해서 수정한 다음 merge해주는 게 맞음.

1. 브랜치를 생성한다(새로운 파일을 만들었다면 add => commit까지 하고)
2. master 브랜치로 가서 merge 한다
3. 브랜치를 다 사용했으므로 삭제한다

<br>

### 0. 기본 명령어

- git config --global -l

- git status : add 된 목록 확인

- git log (--oneline) (--all) (--graph)
  - --oneline 옵션 : 세부사항 생략하고 한 줄로
  - --all 옵션 : 해당 브랜치의 log 이외의 모든 log
  - --graph 옵션 : 그래프 형식으로 보여줌(분기 , merge )

<br>

### 1. branch

- git branch : 브랜치 목록 확인

- git branch 브랜치이름: 새로운 브랜치 생성
- git branch -d 브랜치이름: 특정 브랜치 삭제 (병합된 브랜치만 삭제)
  - git branch -D 브랜치이름: (강제 삭제)
- git switch 브랜치이름: 다른 브랜치로 이동
  - git switch -c 브랜치 이름: 브랜치를 새로 생성과 동시에 이동

<br>

### 2. merge(병합)

- git merge 병합할 브랜치 이름 : 브랜치를 병합시킴
  - merge하기 전에 메인이 될 브랜치로 switch해야함(흡수 할 브랜치로 이동)
    - A와 B중에 A에서 merge하면 A로 흡수되고 A만 남음
- merge이후에는 branch의 역할이 끝난 것이므로 삭제한다.

<br>

### 3. 병합할 때 생길 수 있는 상황들 3가지

#### 1. fast-forword

- 브랜치가 생긴 이후에 마스터는 아무런 변화가 없었던 상황
- 그냥 브랜치 마지막으로 head를 옮긴다

#### 2. 3-way merge(merge commit)

- 브랜치가 생긴 이후에 마스터도 커밋을 쌓은 상황(분기가 생김)
- 마스터의 마지막 커밋 & 브랜치의 마지막 커밋 & 분기점 => 3-way => 3개를 다 합침

#### 3. merge conflict

- merge하는 두 브랜치에서 같은 파일의 같은 부분을 동시에 수정하고 merge하면 git은 해당 부분을 자동으로 merge 해주지 못함
- 반면 동일 파일이더라도 서로 다른 부분을 수정했다면 conflict 없이 자동으로 merge commit 된다.

> conflict 해결 방법

conflict난 부분을 수정 한 뒤, git commit만 입력 (-m 커밋메세지 입력 X)

=> vim 창에서 `esc`=>`:wq`=>`enter`