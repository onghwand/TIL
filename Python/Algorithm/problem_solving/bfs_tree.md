## 5688. 세제곱근을 찾아라

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = int(N**(1/3)+0.1)
    if ans**3 != N:
        ans = -1
    print(f'#{tc} {ans}')
```

## 4012. 요리사

```python
def f(i,N,cnt):
    global A,B
    if cnt == N//2:
        a=[]
        b=[]
        for i in range(N):
            if visited[i] == 1:
                a.append(i)
            else:
                b.append(i)

        for i in range(N//2):
            for j in range(i+1, N//2):
                A += arr[a[i]][a[j]] + arr[a[j]][a[i]]
                B += arr[b[i]][b[j]] + arr[b[j]][b[i]]
        ans.append(abs(A-B))
        A=B=0
        return
    else:
        for j in range(i, N):
            if not visited[j]:
                visited[j] = 1
                f(j+1,N,cnt+1)
                visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    ans=[]
    A=B=0
    f(0,N,0)
    print(f'#{tc} {min(ans)}')
```

## 1953. 탈주범 검거

```python
def bfs(i, j, L):
    global cnt

    queue = []
    queue.append((i,j))
    v[i][j] = 1
    cnt += 1

    while queue :
        i, j = queue.pop(0)
        if v[i][j] == L:
            break
        if arr[i][j] != 0:
            di, dj = tunnel[arr[i][j]]
            for k in range(len(di)):
                ni, nj = i+di[k], j+dj[k]
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 0 and v[ni][nj] == 0 and (-di[k],-dj[k]) in zip(*tunnel[arr[ni][nj]]): #다시 돌아올수도 있어야함
                    queue.append((ni,nj))
                    v[ni][nj] = v[i][j] + 1
                    cnt += 1

    return cnt

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    tunnel = {1:[[0,0,1,-1],[1,-1,0,0]],
              2:[[1,-1],[0,0]],
              3:[[0,0],[1,-1]],
              4:[[-1,0],[0,1]],
              5:[[1,0],[0,1]],
              6:[[1,0],[0,-1]],
              7:[[0,-1],[-1,0]]}

    sti, stj = R, C
    cnt = 0
    v = [[0]*M for _ in range(N)]
    bfs(sti, stj, L)


    print(f'#{tc} {cnt}')
```

## 1861. 정사각형 방

```python
def bfs(i,j,N):
    queue = []
    queue.append((i,j))
    cnt = 1

    while queue:
        i, j = queue.pop(0)
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni, nj = i+di, j+dj

            if 0<=ni<N and 0<=nj<N and arr[ni][nj]==arr[i][j]+1:
                queue.append((ni,nj))
                cnt += 1

    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    minV = N*N
    for i in range(N):
        for j in range(N):
            cnt = bfs(i,j,N)

            if cnt > maxV:
                maxV = cnt
                minV = arr[i][j]
            elif cnt == maxV and minV > arr[i][j]:
                minV = arr[i][j]

    print(f'#{tc} {minV} {maxV}')
```

## 1486. 장훈이의 높은 선반

```python
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    minV = sum(arr)
    for i in range(1<<N):
        cnt = 0
        for j in range(N):
            if i & (1<<j):
                cnt += arr[j]
        if cnt >= B and minV > cnt-B:
            minV = cnt - B

    print(f'#{tc} {minV}')
```

## 1238. Contact

```python
def bfs(S): # S는 시작점
    queue = []
    queue.append(S)
    v[S] = 1
    maxV = 1
    while queue:
        t = queue.pop(0)
        for k in range(101):
            if arr[t][k] == 1 and v[k] == 0:
                queue.append(k)
                v[k] = v[t] + 1
                if maxV < v[k]:
                    maxV = v[k]
    ans = []
    for i in range(101):
        if v[i] == maxV:
            ans.append(i)
    return ans

for tc in range(1, 11):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    arr = [[0]*101 for i in range(101)]
    v = [0]*101
    for i in range(N//2):
        f, t = lst[i*2], lst[i*2+1]
        arr[f][t] = 1

    ans = bfs(S)
    print(f'#{tc} {max(ans)}')
```

## 1232. 사칙연산

```python
def postorder(v):
    if v:
        if type(arr[v]) is str:
            a = postorder(c1[v])
            b = postorder(c2[v])
            return cal(a,b,arr[v])
        else:
            return arr[v]

def cal(pre,post,s):
    if s=='+':
        return pre+post
    elif s=='-':
        return pre-post
    elif s=='*':
        return pre*post
    else:
        return pre/post
for tc in range(1, 11):
    N = int(input())
    arr = [0]*(N+1)
    c1 = [0]*(N+1)
    c2 = [0]*(N+1)
    for i in range(1,N+1):
        n,b,*a= list(input().split())
        if len(a) == 0:
            arr[int(n)] = int(b)
        if len(a) == 2:
            arr[int(n)] = b
            c1[int(n)] = int(a[0])
            c2[int(n)] = int(a[1])

    print(f'#{tc} {int(postorder(1))}')
```

