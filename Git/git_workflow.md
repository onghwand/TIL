## Git workflow

### 1. Feature Branch Workflow

> 저장소의 소유권이 있는 경우

1. clone을 통해 저장소를 로컬에 복제

   ```shell
   $git clone <주소>
   ```

2. 기능 추가를 위해 branch 생성 및 기능 구현

   ```shell
   $git switch -c <브랜치 이름>
   ```

3. 기능 구현 후 원격 저장소에 브랜치 반영 - Pull Request

4. 병합 완료 된 브랜치 삭제(github에서)

5. master 브랜치로 switch

6. 병합된 master의 내용을 pull

7. 원격 저장소에서 병합 완료 된 로컬 브랜치 삭제(로컬에서)

8. 1-7이 1사이클 계속 반복

<br>

### 2. Forking Workflow

1. 소유권이 없는 원격 저장소를 fork를 통해 본인 계정으로 복제

2. fork된 본인 계정에서 clone으로 받음

3. 추후 로컬 저장소를 원본 원격 저장소와 동기화하기 위해 url연결

   ```shell
   $ git remote add upstream [원본 URL]
   ```

4. 기능 추가를 위해 branch 생성 및 기능 구현

5. 기능 구현 후 원격 저장소에 브랜치 반영

6. 원본 저장소에 Pull Request

7. 병합 완료 된 브랜치 삭제

8. master 브랜치로 switch

9. 병합된 master의 내용을 pull

   ```shell
   $ git pull upstream master
   ```

10.  원격 저장소에서 병합 완료 된 로컬 브랜치 삭제

11.  1-10의 1사이클 반복
