### 나무박멸

```python
n, m, k, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def around(i,j,drug): # 성장할 때 주변개수 세기
    cnt = 0
    divider = 0
    for di,dj in [[0,1],[0,-1],[1,0],[-1,0]]:
        ni,nj=i+di,j+dj
        if 0<=ni<n and 0<=nj<n and arr[ni][nj] > 0:
            cnt += 1
        if 0<=ni<n and 0<= nj<n and arr[ni][nj] == 0 and drug[ni][nj] == 0:
            divider += 1
    return cnt, divider

def kill(i,j,k): # 제초제로 죽는 나무수
    killed = arr[i][j]
    for di,dj in [[-1,-1],[-1,1],[1,-1],[1,1]]:
        ni, nj = i+di, j+dj
        limit = k
        while 0<=ni<n and 0<=nj<n and limit > 0:
            if arr[ni][nj] <= 0:
                break
            killed += arr[ni][nj]
            ni += di
            nj += dj
            limit -= 1


    return killed

def scatter(i,j,c,drug,k):
    arr[i][j] = 0
    drug[i][j] = c
    for di, dj in [[-1, -1], [-1, 1], [1, -1], [1, 1]]:
        ni, nj = i + di, j + dj
        limit = k
        while 0 <= ni < n and 0 <= nj < n and limit > 0:
            if arr[ni][nj] == 0:
                drug[ni][nj] = c
                break
            if arr[ni][nj] == -1:
                break
            arr[ni][nj] = 0
            drug[ni][nj] = c
            ni += di
            nj += dj
            limit -= 1

total = 0
drug = [[0]*n for _ in range(n)]

for _ in range(m): # m년동안
    v = [[0] * n for _ in range(n)]


    origin = set()
    # 1. 성장
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                cnt, divider = around(i, j,drug)
                arr[i][j] += cnt
                origin.add((i,j,divider))
                v[i][j] = 1

    # print('성장')
    # for a in arr:
    #     print(*a)

    # 2. 번식
    for i,j,divider in origin:
        if divider == 0 :
            continue
        son = arr[i][j] // divider
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and v[ni][nj] == 0 and arr[ni][nj] != -1 and drug[ni][nj] == 0: # 제초제도 아니면
                arr[ni][nj] += son

    # print('번식')
    # for a in arr:
    #     print(*a)

    # 3. 제초제 위치 선정
    maxV = 0
    position = (0,0)
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0 :
                killed = kill(i, j, k)
                if maxV < killed:
                    maxV = killed
                    position = (i,j)

    # 0. 제초제 1년 경과
    for i in range(n):
        for j in range(n):
            if drug[i][j] != 0 and arr[i][j] != -1:
                drug[i][j] -= 1

    # 4. 제초제 뿌리기 arr => 0 세팅 and drug => c 세팅
    scatter(position[0],position[1],c,drug,k)


    # print('제초제 작업후 나무')
    # for a in arr:
    #     print(*a)
    # print('제초제 작업후 제초제')
    # for d in drug:
    #     print(*d)

    # 5. 죽은 나무 세기
    total += maxV

    # print('죽은나무수')
    # print(total)

print(total)
```

### 꼬리잡기놀이

```python
n,m,k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def make_team(i,j,arr,v,team): # 시계방향으로 길을 구하기위해 dfs
    for di,dj in [[0,1],[0,-1],[1,0],[-1,0]]:
        ni,nj = i+di,j+dj
        if 0<=ni<n and 0<=nj<n and v[ni][nj]==0 and arr[ni][nj] > 0:
            v[ni][nj] = 1
            team.append([ni,nj])
            make_team(ni,nj,arr,v,team)


def get_direction(teams,arr): # 현재 움직이는 방향 구하기
    direction = []
    for team in teams:
        partial = []
        for i,j in team:
            partial.append(arr[i][j])
        direction.append(partial)

    return direction

def move(direction,arr,teams,clock): # 움직이기
    # 시계/반시계 체크하고 움직여야함
    for t in range(len(direction)):
        team = direction[t]
        clockwise = False
        idx = team.index(1)
        if idx == len(team)-1 and team[0] in [3,4]:
            clockwise = True
        elif idx != len(team)-1 and team[idx+1] in [3,4]:
            clockwise = True

        clock[t] = clockwise

        if clockwise: # 시계
            last = team[-1]
            for i in range(len(team)-2,-1,-1): # 시계
                team[i+1] = team[i]
            team[0] = last
        else: # 반시계
            first = team[0]
            for i in range(1,len(team)):
                team[i-1] = team[i]
            team[-1] = first

    for i in range(len(teams)):
        for j in range(len(teams[i])):
            si,sj = teams[i][j]
            arr[si][sj] = direction[i][j]

def find_team(teams, position, direction,clock):
    for i in range(len(teams)):
        for j in range(len(teams[i])):
            if position == teams[i][j]:
                idx = direction[i].index(1)
                # print(teams[i], idx, j, direction[i], position, clock[i])
                if clock[i]: # 시계방향이면
                    if idx > j:
                        num = idx - j + 1
                    elif idx == j:
                        num = 1
                    else:
                        num = len(direction[i]) - (j - idx -1) # 2, 4
                    return i, num
                else:
                    if idx > j:
                        num = len(direction[i]) - (idx - j - 1)
                    elif idx == j:
                        num = 1
                    else:
                        num = j - idx + 1
                    return i, num
    return -1, -1

def change_direction(idx,direction,arr, teams):
    for i in range(len(direction[idx])):
        if direction[idx][i] == 1:
            direction[idx][i] = 3
            si,sj = teams[idx][i]
            arr[si][sj] = 3
        elif direction[idx][i] == 3:
            direction[idx][i] = 1
            si, sj = teams[idx][i]
            arr[si][sj] = 1

def throw(arr, mode, sub, direction, teams):
    if mode == 0: # 서쪽에서 날라옴
        for j in range(n):
            if arr[sub][j] in [1,2,3]:
                idx, num = find_team(teams,[sub,j], direction,clock)
                if idx == -1:
                    return
                score[idx] += num**2
                change_direction(idx,direction,arr, teams)
                return
    elif mode == 1:
        for j in range(n):
            if arr[n-j-1][sub] in [1,2,3]:
                idx, num = find_team(teams,[n-j-1,sub], direction,clock)
                # print(num)
                if idx == -1:
                    return
                score[idx] += num**2
                change_direction(idx,direction,arr, teams)
                return
    elif mode == 2:
        for j in range(n):
            if arr[n-sub-1][n-j-1] in [1,2,3]:
                idx, num = find_team(teams,[n-sub-1,n-j-1], direction,clock)
                if idx == -1:
                    return
                score[idx] += num**2
                change_direction(idx,direction,arr, teams)
                return
    elif mode == 3:
        for j in range(n):
            if arr[j][n-sub-1] in [1,2,3]:
                idx, num = find_team(teams,[j,n-sub-1], direction,clock)
                if idx == -1:
                    return
                score[idx] += num**2
                change_direction(idx,direction,arr, teams)
                return

teams = [] # 팀의 이동 선
score = [0]*m # 각 팀의 점수
clock = [0]*m # 각 팀의 방향 => True:시계 False:반시계 xxxxx

v = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if v[i][j] == 0 and arr[i][j] != 0:
            team = [[i,j]]
            v[i][j] = 1
            make_team(i, j, arr, v, team)
            teams.append(team)

# print(teams)

direction = get_direction(teams,arr) # 1 뒤에 4가 있다면 시계방향 + 1이 마지막에 있다면 0번째꺼 확인
# print(direction)
# for a in arr:
    # print(*a)

for rounds in range(k):
    # print('---------',rounds,'--------')
    move(direction,arr,teams,clock)
    # print(direction)
    # for a in arr:
    #     print(*a)
    # print(clock)

    # sub = rounds % n**2
    mode, sub = divmod(rounds ,n)
    mode = mode % 4
    # print(mode,sub)
    throw(arr, mode, sub, direction, teams)
    # print(direction)
    # print(score)
    # for a in arr:
    #     print(*a)
print(sum(score))
```

