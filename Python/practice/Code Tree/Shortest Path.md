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

