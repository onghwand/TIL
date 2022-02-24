## stack2 

### 4874. Forth

```python
def cal(postfix):
    ans = []
    for n in postfix:
        if n in '*+-/' and len(ans) < 2:
            return 'error'
        elif n == '*':
            post = int(ans.pop())
            pre = int(ans.pop())
            ans.append(pre * post)
        elif n == '+':
            post = int(ans.pop())
            pre = int(ans.pop())
            ans.append(pre + post)
        elif n == '-':
            post = int(ans.pop())
            pre = int(ans.pop())
            ans.append(pre - post)
        elif n == '/':
            post = int(ans.pop())
            pre = int(ans.pop())
            ans.append(int(pre / post))
        elif n == '.':
            break
        else:
            ans.append(n)

    if len(ans) != 1:
        return 'error'
    return ans[0]


T = int(input())
for tc in range(1, T + 1):
    postfix = list(input().split())
    sol = cal(postfix)

    print(f'#{tc} {sol}')
```

### 4875. 미로

```python
def fstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
def dfs(i,j,N):
    stack = []
    visited =[[0]*N for _ in range(N)]
    while 1:
        # i, j 칸 방문
        visited[i][j] = 1
        if maze[i][j] == 3: #목적지면
            return 1
        # 현재 위치 i, j에서 갈 수 있는 곳 탐색
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i + di, j+dj
            # 미로 내부, 벽이 아니면(통로 or 도착칸), 방문하지 않은 칸
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                stack.append((i,j))
                i, j = ni, nj
                break
        else: # 갈수있는 칸이 없으면
            if stack:
                i, j = stack.pop()
            else:
                break
    return 0

def dfs2(i, j, N):
    visited[i][j] = 1
    if maze[i][j] == 3:
        return 1
    else:
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                if dfs2(ni, nj, N):
                    return 1
        return 0
T= int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    sti, stj = fstart(N)
    #ans = dfs(sti, stj, N)
    #print(f'#{tc} {ans}')
    visited = [[0]*N for _ in range(N)] # dfs2
    print(f'#{tc} {dfs2(sti, stj, N)}')
```

### 4880. 토너먼트 카드게임

```python
def f(i,j):
    if i==j:
        return i
    else:
        left = f(i, (i+j)//2)
        right = f((i+j)//2+1, j)

        return win(left,right)

def win(left, right):
    RSP = {1:3, 2:1, 3:2}
    if arr[right] == RSP[arr[left]]:
        return left
    elif arr[left] == arr[right]:
        return min(left, right)
    else:
        return right

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))

    print(f'#{tc} {f(1, len(arr)-1)}')
```

### 4881. 배열 최소 합

> 순열구해서 전부 다

```python
def f(i, N):
    if i == N:
        cnt = 0
        for i,j in zip([x for x in range(N)],p):
            cnt += arr[i][j]
            if sums and min(sums) < cnt:
                break
        sums.append(cnt)
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i + 1, N)
            p[i], p[j] = p[j], p[i]
 
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    p = [x for x in range(N)]
    sums=[]
    f(0, N)
 
    print(f'#{tc} {min(sums)}')
```

> 가지치기

```python
def f(row):
    global minV, partial
    if partial > minV:
        return
    elif row == N:
        if partial < minV:
            minV = partial
    for i in range(N):
        if not col[i]:
            col[i] = True
            partial += arr[row][i]
            f(row+1)
            col[i] = False
            partial -= arr[row][i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    col = [False]*N

    minV = 0
    for i in range(N):
        minV += arr[i][i]
    partial = 0
    f(0)
    print(f'#{tc} {minV}')
```

```python
def ff(i,N,s):
    global minV
    if i == N and minV > s:
        minV = s
    elif minV <= s:
        return
    else:
        for j in range(N):
            if not col[j]:
                col[j] = True
                ff(i+1, N, s+arr[i][j])
                col[j] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    col = [False]*N

    minV = 1000
    ff(0,N,0)
    print(f'#{tc} {minV}')
```

