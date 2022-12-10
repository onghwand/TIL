### 최단경로

```python
import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
s = int(input())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append([w,v])

dist = [INF]*(V+1)
dist[s] = 0
q = []
heapq.heappush(q, [0,s])

while q:
    min_dist, min_point = heapq.heappop(q)

    if dist[min_point] != min_dist:
        continue

    for cur_dist, cur_point in graph[min_point]:
        tmp = cur_dist + min_dist
        if tmp < dist[cur_point]:
            dist[cur_point] = tmp
            heapq.heappush(q, [tmp, cur_point])

for i in range(1, V+1):
    print("INF" if dist[i] == INF else dist[i])
```

### 최소비용 구하기

```python
import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    i,j,v=map(int, input().split())
    graph[i].append([v,j])

A, B = map(int,input().split())

dist = [INF] * (N+1)
dist[A] = 0
q = []
heapq.heappush(q, [0,A])
while q:
    min_dist, min_idx = heapq.heappop(q)

    if min_dist != dist[min_idx]:
        continue

    for cur_dist, cur_idx  in graph[min_idx]:
        nxt = cur_dist + min_dist
        if nxt < dist[cur_idx]:
            dist[cur_idx] = nxt
            heapq.heappush(q, [nxt, cur_idx])

print(dist[B])
```

### 파티

```python
import sys, heapq
INF = sys.maxsize
input = sys.stdin.readline

n,m,x = map(int, input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    i,j,v = map(int, input().split())
    graph[i].append((v,j))

def di(s):
    dist = [INF]*(n+1)
    dist[s] = 0
    q = []
    heapq.heappush(q, (0,s))

    while q:
        min_dist, min_idx = heapq.heappop(q)

        if min_dist != dist[min_idx]:
            continue

        for cur_dist, cur_idx in graph[min_idx]:
            nxt = cur_dist + min_dist
            if nxt < dist[cur_idx]:
                dist[cur_idx] = nxt
                heapq.heappush(q, (nxt, cur_idx))

    return dist


dist_x = di(x)
maxV = 0
for i in range(1,n+1):
    if maxV < di(i)[x]+dist_x[i]:
        maxV = di(i)[x]+dist_x[i]
print(maxV)
```

### 특정한 최단 경로

```python
import heapq, sys
INF = sys.maxsize
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    u,v,w=map(int, input().split())
    graph[u].append((w,v))
    graph[v].append((w,u))
a, b = map(int, input().split())

def di(s):
    dist = [INF]*(N+1)
    dist[s] = 0
    q = []
    heapq.heappush(q, (0,s))

    while q:
        min_dist, min_idx = heapq.heappop(q)

        if dist[min_idx] != min_dist:
            continue

        for cur_dist, cur_idx in graph[min_idx]:
            nxt = cur_dist + min_dist
            if nxt < dist[cur_idx]:
                dist[cur_idx] = nxt
                heapq.heappush(q, (nxt, cur_idx))
    return dist

if INF in [di(1)[a],di(a)[b],di(b)[N],di(1)[b],di(b)[a],di(a)[N]]:
    print(-1)
else:
    print(min(di(1)[a]+di(a)[b]+di(b)[N],di(1)[b]+di(b)[a]+di(a)[N]))
```

### 알고스팟

```python
from collections import deque
di=[0,0,1,-1]
dj=[1,-1,0,0]

m,n = map(int, input().split())
arr = [list(map(int,list(input()))) for _ in range(n)]
dist = [[-1]*m for _ in range(n)]

dist[0][0] = 0
q = deque()
q.append((0,0))
while q:
    i,j = q.popleft()
    for k in range(4):
        ni, nj =i+di[k], j+dj[k]
        if 0<=ni<n and 0<=nj<m and dist[ni][nj] == -1:
            if arr[ni][nj] == 0:
                dist[ni][nj] = dist[i][j]
                q.appendleft((ni,nj))
            else:
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni,nj))
print(dist[n-1][m-1])
```

### 미확인 도착지

> 각 지점마다 바로 전 지점 저장해놓고 dfs => 시간초과

```python
import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline
def dijkstra(k):
    dist = [INF]*(n+1)
    dist[k] = 0

    q = []
    heapq.heappush(q,[0,k])

    trace = [0]*(n+1)
    trace[k] = k
    while q:
        min_dist, min_idx = heapq.heappop(q)
        if dist[min_idx] != min_dist:
            continue

        for cur_dist, cur_idx in graph[min_idx]:
            dst = cur_dist + min_dist
            if dst < dist[cur_idx]:
                dist[cur_idx] = dst
                heapq.heappush(q, [dst,cur_idx])
                trace[cur_idx] = min_idx
    return trace, dist

def is_target(target, g, h, trace): # dfs로 g-h 경로 지나가는지 체크
    passed = set()
    while target != 2:
        target = trace[target]
        if target in [g,h]:
            passed.add(target)

        if passed == {g,h}:
            return True
    return False



T = int(input())
for tc in range(T):
    n,m,t = map(int,input().split())
    s,g,h = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,d = map(int,input().split())
        graph[a].append([d,b])
        graph[b].append([d,a])

    trace, dist = dijkstra(s)
    # print(trace, dist)

    real_target = []
    for _ in range(t):
        target = int(input())
        if is_target(target, g, h, trace):
            real_target.append(target)

    print(*sorted(real_target))
```

> 다익 3번, g-h 거친것과 거리같으면 ok

```python
import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline
def dijkstra(k):
    dist = [INF]*(n+1)
    dist[k] = 0

    q = []
    heapq.heappush(q,[0,k])

    while q:
        min_dist, min_idx = heapq.heappop(q)
        if dist[min_idx] != min_dist:
            continue

        for cur_dist, cur_idx in graph[min_idx]:
            dst = cur_dist + min_dist
            if dst < dist[cur_idx]:
                dist[cur_idx] = dst
                heapq.heappush(q, [dst,cur_idx])
             
    return dist


T = int(input())
for tc in range(T):
    n,m,t = map(int,input().split())
    s,g,h = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,d = map(int,input().split())
        graph[a].append([d,b])
        graph[b].append([d,a])

    start = dijkstra(s)
    g_ = dijkstra(g)
    h_ = dijkstra(h)

    real_target = []
    for _ in range(t):
        target = int(input())
        if start[g]+g_[h]+h_[target] == start[target] or start[h]+h_[g]+g_[target] == start[target]:
            real_target.append(target)

    print(*sorted(real_target))
```

