### 트리의 부모 찾기

```python
from collections import deque
n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n-1):
    graph[i].sort()

q = deque()
q.append(1)

v = [0]*(n+1)
v[1] = 1
while q:
    t = q.popleft()
    for i in graph[t]:
        if v[i] == 0:
            v[i] = t
            q.append(i)

for k in range(2,n+1):
    print(v[k])
```

