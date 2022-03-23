## 문제풀이3

## 4615. 재미있는 오셀로 게임

```python
def f(sti,stj,c):
    for di, dj in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]:
        l = 1
        lst = []
        while 1:
            ni, nj = sti+l*di, stj+l*dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]==3-c:
                lst.append((ni,nj))
            elif 0<=ni<N and 0<=nj<N and arr[ni][nj]==c and lst:
                for a,b in lst:
                    arr[a][b] = c
                break
            else:
                break
            l += 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(N) for _ in range(N)]
    arr[N//2-1][N//2-1] = 2
    arr[N//2][N//2] = 2
    arr[N//2-1][N//2] = 1
    arr[N//2][N//2-1] = 1

    for _ in range(M):
        i, j, c = map(int, input().split())
        arr[i-1][j-1] = c
        f(i-1,j-1,c)

    b = 0
    w = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                b += 1
            elif arr[i][j] == 2:
                w += 1

    print(f'#{tc} {b} {w}')
```

## 4366. 정식이의 은행업무

```python
T = int(input())
for tc in range(1, T+1):
    b = list(input())
    t = list(input())

    bins=[]
    tris=[]

    for i in range(len(b)):
        b[i] = str(1-int(b[i]))
        bins.append(int(''.join(b),2))
        b[i] = str(1-int(b[i]))

    for i in range(len(t)):
        t[i] = str((int(t[i])+1)%3)
        tris.append(int(''.join(t),3))
        t[i] = str((int(t[i]) - 1) % 3)
        t[i] = str((int(t[i]) + 2) % 3)
        tris.append(int(''.join(t), 3))
        t[i] = str((int(t[i]) - 2) % 3)

    ans = set(bins).intersection(set(tris))
    print(f'#{tc}',*ans)
```

## 2819. 격자판의 숫자 이어 붙이기

```python
def dfs(i,N,sti,stj):

    if i == N:
        lst.append(''.join(s))
        return

    else:
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni, nj = sti + di, stj + dj
            if 0 <= ni < 4 and 0 <= nj < 4:
                s.append(arr[ni][nj])
                dfs(i+1,N,ni,nj)
                s.pop()

T = int(input())
for tc in range(1, T+1):
    arr = [input().split() for _ in range(4)]
    lst = []
    s = []

    for i in range(4):
        for j in range(4):
            s.append(arr[i][j])
            dfs(1,7,i,j)
            s = []

    print(f'#{tc} {len(set(lst))}')
```

## 2382. 미생물 격리

```python
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    arr = [[0]*N for _ in range(N)]
    mode = {1: [-1, 0],
            2: [1, 0],
            3: [0, -1],
            4: [0, 1]
            }

    for k in range(K):
        i,j,n,m = map(int, input().split())
        arr[i][j]=[n,m]

    for m in range(M): # 주어진 시간동안
        v = [[0]*N for _ in range(N)]
        # 좌표 이동
        for i in range(N):
            for j in range(N):
                if arr[i][j] != 0:
                    di, dj = mode[arr[i][j][1]]
                    ni, nj = i+di, j+dj
                    if v[ni][nj] == 0:
                        v[ni][nj] = arr[i][j]
                    else:
                        v[ni][nj] = v[ni][nj]+arr[i][j]

        for i in range(N):
            for j in range(N):
                # 약품
                if v[i][j] != 0 and (i==0 or i==N-1 or j==0 or j==N-1):
                    if v[i][j][0] == 1:
                        v[i][j] = 0
                    else:
                        v[i][j][0] = v[i][j][0]//2
                        v[i][j][1] += 1 if v[i][j][1]%2 else -1 #홀수면 1더해주고 짝수면 빼야함 => 반대방향
                # 합치기
                if v[i][j] != 0 and len(v[i][j]) > 2:
                    maxV = 0
                    cnt = 0
                    for l in range(len(v[i][j])):
                        if not l%2:
                            cnt += v[i][j][l]
                            if maxV < v[i][j][l]:
                                maxV = v[i][j][l]
                    v[i][j] = [cnt, v[i][j][v[i][j].index(maxV)+1]] # 합쳐진 개수, 방향
        arr = v # 갱신해주고

    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                ans += arr[i][j][0]

    print(f'#{tc} {ans}')
```

## 2117. 홈 방범 서비스

```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxH = 0
    for k in range(1, 2*N+1):
        maxV = 0
        for i in range(N):
            for j in range(N):
                cnt = 0
                for m in range(N):
                    for l in range(N):
                        if abs(m-i)+abs(l-j) < k and arr[m][l]:
                            cnt += 1
                if cnt > maxV:
                    maxV = cnt

        profit = maxV*M - k**2 - (k-1)**2
        if profit >= 0 and maxH < maxV:
            maxH = maxV

    print(f'#{tc} {maxH}')
```

## 2105. 디저트 카페

```python
def f(i,j,cnt,k):
    global maxV
    if cnt > 1 and start == [i,j]:
        if cnt > maxV:
            maxV = cnt
        return
    else:
        for m in range(k,min(k+2,4)):
            ni,nj = i+di[m],j+dj[m]
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0 and d[arr[ni][nj]] == 0:
                d[arr[ni][nj]] = 1
                v[ni][nj] = 1 # 방문했고
                f(ni,nj,cnt+1,m)
                d[arr[ni][nj]] = 0
                v[ni][nj] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di =[1,1,-1,-1]
    dj =[1,-1,-1,1]

    maxV = -1
    v = [[0]*N for _ in range(N)]
    d = [0]*101
    for i in range(N):
        for j in range(N):
            start = [i,j]
            f(i,j,0,0)

    print(f'#{tc} {maxV}')
```

## 1952. 수영장

```python
def f(i,N,cost):
    global minV
    if i==N:
        if minV > cost:
            minV =cost
        return
    elif cost > minV or i > N:
        return
    else:
        f(i+1, N, cost+nums[i]*costs[0]) #1일권
        f(i + 1, N, cost + costs[1])  # 1달권
        f(i + 3, N, cost + costs[2]) # 3달권

T = int(input())
for tc in range(1, T+1):
    costs = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    minV = min(sum(nums)*costs[0], costs[3]) #1일권만
    f(0,12,0)
    print(f'#{tc} {minV}')
```

