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

### 배달

```python
import heapq
import sys

def solution(N, road, K):
    INF = sys.maxsize
    answer = 0
    graph = [[] for _ in range(N+1)]
    for x,y,z in road:
        graph[x].append((y,z))
        graph[y].append((x,z))
        
    dist = [INF]*(N+1)
    dist[1] = 0
    q = []
    heapq.heappush(q, (0,1))
    while q:
        min_dist, min_idx = heapq.heappop(q)
        
        if dist[min_idx] != min_dist:
            continue
        
        for cur_idx, cur_dist in graph[min_idx]:
            if dist[cur_idx] > cur_dist + min_dist:
                dist[cur_idx] = cur_dist + min_dist
                heapq.heappush(q, (dist[cur_idx], cur_idx))
    cnt = 0
    for d in dist:
        if d <= K:
            cnt +=1

    return cnt
```

### H-Index

```python
def solution(citations):
    n = len(citations)
    H = -1
    
    for i in range(n+1):
        cnt = 0
        for j in range(n):
            if citations[j] >= i:
                cnt += 1
        if cnt >= i:
            H = i
    
    return H
```

### 삼각 달팽이

```python
def solution(n):
    answer = []
    for i in range(n):
        answer.append([0]*(i+1))
    
    N = n*(n+1)//2
    di = [1,0,-1]
    dj = [0,1,-1]
    si = sj = mode = 0
    for i in range(1, N+1):
        
        answer[si][sj] = i
        si, sj = si+di[mode], sj+dj[mode]
        if 0<=si<n and 0<=sj<=si and answer[si][sj] == 0 :
            continue
        
        si, sj = si-di[mode], sj-dj[mode]
        mode = (mode+1)%3
        si, sj = si+di[mode], sj+dj[mode]
        
    ans = []
    for a in answer:
        ans.extend(a)
    
    return ans
```

### 전력망을 둘로 나누기

```python
def solution(n, wires):
    minV = n
    for i in range(len(wires)):
        tmp = wires[:i] + wires[i+1:]
        
        graph = [[] for _ in range(n+1)]
        for x,y in tmp:
            graph[x].append(y)
            graph[y].append(x)
        
        v = [0]*(n+1)
        q = [1]
        while q:
            i = q.pop(0)
            for j in graph[i]:
                if v[j] == 0:
                    v[j] = 1
                    q.append(j)
        
        cnt = abs(v.count(1)-(v.count(0)-1))
        if cnt < minV:
            minV = cnt
        
    return minV
```

### 이진 변환 반복하기

```python
def solution(s):
    cnt = loop = 0
    while s != '1':
        loop += 1
        zeros, ones = s.count('0'), s.count('1')
        cnt += zeros
        s = bin(ones)[2:]
        
    return [loop, cnt]
```

### n^2 배열 자르기

```python
def solution(n, left, right):
    arr = []
    for i in range(left, right+1):
        q,r = divmod(i,n)
        arr.append(max(q,r)+1)
    return arr
```

### 숫자 블록

```python
def solution(begin, end):
    answer = []
    arr = []
    for i in range(begin, end+1):
        if i <=1:
            arr.append(0)
        else:
            for k in range(2, int(i**(1/2))+1):
                if i%k == 0:
                    if i//k > 10**7:
                        continue
                    arr.append(i//k)
                    break
            else:
                arr.append(1)
                    
    return arr
```

### N-Queen

```python
def can_go(i,j,qs):
    for qi,qj in qs:
        if abs(qi-i) == abs(qj-j):
            return False
    return True

cnt = 0
def f(i,n,v,qs):
    global cnt
    if i == n:
        cnt += 1
        return
    for j in range(n):
        if v[j] == 0 and can_go(i,j,qs):
            v[j] = 1
            qs.append((i,j))
            f(i+1,n,v,qs)
            qs.pop()
            v[j] = 0
    
    
def solution(n):
    v=[0]*n 
    f(0,n,v,[])
    return cnt
```

### 2 x n 타일링

```python
def solution(n):
    arr = [0]*(n+1)
    for i in range(1,n+1):
        if i == 1:
            arr[i] = 1
        elif i == 2:
            arr[i] = 2
        else:
            arr[i] = (arr[i-1]+arr[i-2])%1000000007
    
    return arr[n]
```

### 하노이의 탑

```python
def solution(n):
    arr = []
    def hanoi(n,start, mid, end):
        if n == 1:
            arr.append([start, end])
            return 
        hanoi(n-1,start, end, mid)
        arr.append([start,end])
        hanoi(n-1,mid,start,end)
    hanoi(n,1,2,3)
    
    return arr
```

### 쿼드압축 후 개수 세기

```python
def solution(arr):
    answer = [0,0]
    def compress(i,j,l):
        start = arr[i][j]
        for a in range(l):
            for b in range(l):
                if arr[i+a][j+b] != arr[i][j]:
                    l //= 2
                    compress(i+l,j+l,l)
                    compress(i,j+l,l)
                    compress(i+l,j,l)
                    compress(i,j,l)
                    return
        answer[start] += 1
    
    compress(0,0,len(arr))
        
    return answer
```

### 모음사전

```python
def solution(word):
    answer = 0
    words = []
    alps = ['A','E','I','O','U']
    s=''
    for a in alps:
        s += a
        words.append(s)
        for e in alps:
            s += e
            words.append(s)
            for i in alps:
                s += i
                words.append(s) 
                for o in alps:
                    s += o
                    words.append(s)
                    for u in alps:
                        s += u
                        words.append(s)
                        s = s[:4]
                    s=s[:3]
                s=s[:2]
            s=s[:1]
        s=''
 
    return words.index(word)+1
```

### 교점에 별 만들기

```python
def solution(line):
    p = []
    maxx = maxy = -1000
    minx = miny = 1000
    for i in range(len(line)):
        a,b,e = line[i]
        for j in range(i+1,len(line)):
            c,d,f = line[j]
            if a*d - b*c !=0:
                x = (b*f - e*d) / (a*d - b*c)
                y = (e*c - a*f) / (a*d - b*c)
                if x.is_integer() and y.is_integer():
                    x, y = int(x), int(y)
                    # if x > maxx:
                    #     maxx = x
                    # if y > maxy:
                    #     maxy = y
                    # if x < minx:
                    #     minx = x
                    # if y < miny:
                    #     miny = y
                    p.append((x,y))
    minx, maxx, miny, maxy = min(p)[0],max(p)[0],min(p,key = lambda x: x[1])[1],max(p,key = lambda x: x[1])[1]
    arr = [['.']*(maxx-minx+1) for _ in range(maxy-miny+1)]
    
    for x,y in p:
        arr[maxy-y][x-minx] = '*'
        
    lst = []
    for a in arr:
        lst.append(''.join(a))
    
    return lst
```

### 다리를 지나는 트럭

```python
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque(0 for _ in range(bridge_length))
    truck_weights.reverse()
    while bridge:
        answer += 1
        bridge.popleft()
        
        if truck_weights:
            if sum(bridge) + truck_weights[-1] <= weight:
                bridge.append(truck_weights.pop())
            else:
                bridge.append(0)
            
    return answer
```

### 무인도 여행

```python
from collections import deque
def bfs(i,j,v,maps,n,m):
    q = deque()
    q.append((i,j))
    v[i][j] = 1
    
    cnt = int(maps[i][j])
    while q:
        si,sj = q.popleft()
        for di,dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            ni,nj = si+di, sj+dj
            if 0<=ni<n and 0<=nj<m and maps[ni][nj] != 'X' and v[ni][nj] == 0:
                v[ni][nj] = 1
                q.append((ni,nj))
                cnt += int(maps[ni][nj])
    return cnt
    
    
    
def solution(maps):
    answer = []
    n, m = len(maps), len(maps[0])
    v = [[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not v[i][j]:
                answer.append(bfs(i,j,v,maps,n,m))
    
    answer.sort()
    
    return answer if answer else [-1]
```

### 호텔대실

```python
def get_minute(t):
    h,m = map(int, t.split(':'))
    return h*60 + m

def solution(book_time):
    L = 24*60
    arr = [0]*L
    for i in range(len(book_time)):
        start, end = get_minute(book_time[i][0]), get_minute(book_time[i][1])
        arr[start] += 1
        if end + 10 < L:
            arr[end+10] -= 1
    
    for i in range(1,L):
        arr[i] += arr[i-1] 
    
    return max(arr)
```

