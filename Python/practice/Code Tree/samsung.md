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

