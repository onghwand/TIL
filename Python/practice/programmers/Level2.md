## Level2

### 행렬 테두리 회전하기

```python
from copy import deepcopy
def rotate(ax,ay,bx,by,arr):
    minV = len(arr)*len(arr[0])
    tmp = arr[ax][ay]
    minV = min(minV,tmp)
    for i in range(ax,bx):
        test = arr[i+1][ay]
        arr[i][ay]= test
        minV = min(minV,test)
    for i in range(ay,by):
        test = arr[bx][i+1]
        arr[bx][i] = test
        minV = min(minV,test)
    for i in range(bx,ax,-1):
        test=arr[i-1][by]
        arr[i][by]=test
        minV = min(minV,test)
    for i in range(by,ay,-1):
        test = arr[ax][i-1]
        arr[ax][i] = test
        minV = min(minV,test)
    arr[ax][ay+1] = tmp
        
    return arr, minV
    
def solution(rows, columns, queries):
    answer = []
    arr = [[y*columns+x for x in range(1,columns+1)] for y in range(rows)]

    for a,b,c,d in queries:
        arr, minV = rotate(a-1,b-1,c-1,d-1,arr)
        answer.append(minV)
    
    return answer
```

### 게입 맵 최단거리

> dfs, 효율성 실패

```python
minV = 10000
def solution(maps):
    answer = 0
    n,m = len(maps), len(maps[0])
    
    def f(i,j,n,m,cnt,maps,v):
        global minV
        if (i,j) == (n-1,m-1):
            if minV > cnt:
                minV = cnt
            return
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<n and 0<=nj<m and maps[ni][nj]==1 and v[ni][nj]==0:
                v[ni][nj] = 1
                f(ni,nj,n,m,cnt+1,maps,v)
                v[ni][nj] = 0
            
    v = [[0]*m for _ in range(n)]
    f(0,0,n,m,1,maps,v)
    if minV == 10000:
        return -1
    return minV
```

> bfs

```python
from collections import deque
def solution(maps):
    answer = 0
    n,m = len(maps), len(maps[0])
    
    def f(i,j,n,m,maps,v):
        q=deque()
        q.append((i,j))
        v[i][j] = 1
        while q:
            si,sj = q.popleft()
            if (si,sj) == (n-1,m-1):
                return v[si][sj]
            
            for di,dj in [[0,1],[0,-1],[1,0],[-1,0]]:
                ni,nj = si+di, sj+dj
                if 0<=ni<n and 0<=nj<m and v[ni][nj]==0 and maps[ni][nj]==1:
                    v[ni][nj] = v[si][sj] + 1
                    q.append((ni,nj))
        return -1
    
    v = [[0]*m for _ in range(n)]
    return f(0,0,n,m,maps,v)
```

