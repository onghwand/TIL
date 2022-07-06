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

