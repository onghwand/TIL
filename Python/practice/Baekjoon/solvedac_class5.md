### 최소 스패닝 트리

```python
def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

def union(a,b):
    parent[find(b)] = find(a)


v,e = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(e)]
graph.sort(key=lambda x:x[2])

parent = [x for x in range(v+1)]
total = 0
for a,b,c in graph:
    if find(a) != find(b):
        union(a,b)
        total += c

print(total)
```

### 줄 세우기

```python
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, input().split())
    indegree[y] += 1
    graph[x].append(y)

res = []

q = deque()
for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)
while q:
    x = q.popleft()
    res.append(x)

    for y in graph[x]:
        indegree[y] -= 1
        if indegree[y] == 0:
            q.append(y)

print(*res)
```

### 부분합

```python
import sys
input = sys.stdin.readline

n,s = map(int ,input().split())
arr = list(map(int, input().split()))

if sum(arr) < s:
    print(0)
else:
    minV = len(arr)
    i=j=0
    part = arr[0]
    while 1:
        if part < s and j < len(arr)-1:
            j += 1
            part += arr[j]
        else:
            if part >= s:
                minV = min(minV, j - i + 1)

            i += 1
            if i == len(arr):
                break
            part -= arr[i-1]

    print(minV)
```

