## Dijkstra

> 각 정점까지의 최단 경로3

```python
n , m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    i,j,d = map(int, input().split())
    graph[i][j] = d

INF = 100000000
dist = [INF]*(n+1)
dist[1] = 0
v = [0]*(n+1)
for i in range(n):

    # idx 뽑기
    minidx = -1
    for j in range(1,n+1):
        if v[j]:
            continue
        if minidx == -1 or dist[minidx] > dist[j]:
            minidx = j
    
    v[minidx] = 1

    for k in range(1,n+1):
        if graph[minidx][k]:
            dist[k] = min(dist[k], dist[minidx]+graph[minidx][k])

for i in range(2,n+1):
    if dist[i] ==INF:
        print(-1)
    else:
        print(dist[i])

```

> 각 정점까지의 최단 경로

```python
import heapq
import sys
INF = sys.maxsize

n,m = map(int, input().split())
k = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    i, j, d = map(int, input().split())
    graph[i].append((j,d))
    graph[j].append((i,d))

dist = [INF]*(n+1)
dist[k] = 0
pq = []
heapq.heappush(pq, (0,k))

while pq:
    min_dist, min_idx = heapq.heappop(pq)

    if dist[min_idx] != min_dist:
        continue
    
    for target_index, target_dist in graph[min_idx]:
        new_dist = target_dist + dist[min_idx]
        if dist[target_index] > new_dist:
            dist[target_index] = new_dist
            heapq.heappush(pq, (new_dist, target_index))

for i in range(1, n+1):
    if dist[i] == INF:
        print(-1)
    else:
        print(dist[i])
```

> 가장 오래 걸리는 학생2

```python
import heapq
import sys
INF = sys.maxsize

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    i, j, d = map(int, input().split())
    graph[j].append((i,d))
# print(graph)
dist = [INF]*(N+1)
pq = []
dist[N] = 0
heapq.heappush(pq, (0,N))
while pq:
    min_dist, min_idx = heapq.heappop(pq)

    if dist[min_idx] != min_dist:
        continue
    
    for idx,dis in graph[min_idx]:
        nxt_dist = dist[min_idx] + dis
        if dist[idx] > nxt_dist:
            dist[idx] = nxt_dist
            heapq.heappush(pq, (nxt_dist, idx))
print(max(dist[1:]))
```

> 최단거리 경로

```python
import heapq
import sys
INF = sys.maxsize

n,m=map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    i,j,d = map(int, input().split())
    graph[i].append((j,d))
    graph[j].append((i,d))
A,B=map(int,input().split())

dist = [INF]*(n+1)
dist[A] = 0

path = [0]*(n+1)
pq = []
heapq.heappush(pq,(0,A))
while pq:
    min_dist, min_idx = heapq.heappop(pq)

    if dist[min_idx] != min_dist:
        continue
    
    for target_idx, target_dist in graph[min_idx]:
        new_dist = dist[min_idx] + target_dist
        if new_dist < dist[target_idx]:
            dist[target_idx] = new_dist
            heapq.heappush(pq, (new_dist, target_idx))
            path[target_idx] = min_idx
            
x = B
vertices = []
vertices.append(x)

while x != A:
    x = path[x]
    vertices.append(x)

print(dist[B])
print(*vertices[::-1])
```

> 사전순으로 가장 앞선 최단거리 경로

```python
import heapq
import sys

INF = sys.maxsize
n,m=map(int, input().split())
q = []
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))
    graph[y].append((x,z))

A,B=map(int, input().split())

dist = [INF]*(n+1)
dist[A] = 0
heapq.heappush(q, (0,A))
path = [0]*(n+1)
while q:
    min_dist, min_idx = heapq.heappop(q)

    if min_dist != dist[min_idx]:
        continue

    for cur_idx, cur_dist in graph[min_idx]:
        nxt_dist = dist[min_idx] + cur_dist
        if dist[cur_idx] >= nxt_dist:
            dist[cur_idx] = nxt_dist
            heapq.heappush(q, (nxt_dist, cur_idx))
            if path[cur_idx] < min_idx:
                path[cur_idx] = min_idx

x = B
vertices=[]
vertices.append(B)

while x!=A:
    x = path[x]
    vertices.append(x)
print(dist[B])
print(*vertices[::-1])
```

