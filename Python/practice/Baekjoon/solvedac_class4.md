### 14502 연구소

```python
import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def spread(r,c, tmp):
    q = deque()
    q.append((r,c))

    while q:
        ci,cj = q.popleft()

        for di,dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            ni,nj = ci+di,cj+dj
            if 0<=ni<n and 0<=nj<m and not tmp[ni][nj]:
                tmp[ni][nj] = 1
                q.append((ni,nj))

def get_zeros():
    zeros = []
    for i in range(n):
        for j in range(m):
            if not arr[i][j]:
                zeros.append((i,j))
    return zeros, len(zeros)

zeros, L = get_zeros()
maxV = 0
for i in range(L):
    for j in range(i+1, L):
        for k in range(j+1, L):
            # 원본 복제
            tmp = deepcopy(arr)

            # 벽세우기
            a,b = zeros[i]
            c,d = zeros[j]
            e,f = zeros[k]
            tmp[a][b] = 1
            tmp[c][d] = 1
            tmp[e][f] = 1

            for r in range(n):
                for c in range(m):
                    if tmp[r][c] == 2:
                        spread(r,c,tmp)

            cnt = 0
            for r in range(n):
                for c in range(m):
                    if not tmp[r][c]:
                        cnt += 1

            if maxV < cnt:
                maxV = cnt

print(maxV)
```

### N-Queen

```python
n = int(input())

def dfs(n, r):
    global cnt
    if n == r :
        cnt += 1
        return

    for j in range(n):
        if v[j] == -1 and meet(r,j,n):
            v[j] = r
            dfs(n,r+1)
            v[j] = -1

def meet(r,j,n):
    for k in range(n):
        if v[k] != -1 and abs(k-j) == abs(v[k]-r):
            return False
    return True


v = [-1] * n
cnt = 0
for i in range(n):
    v[i] = 0
    dfs(n,1)
    v[i] = -1

print(cnt)
```

