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

### 텀 프로젝트

```python
import sys
input = sys.stdin.readline

t=int(input())
for tc in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))

    v = [0]*(n+1)
    cnt = 0
    for i in range(1,n+1):
        if i == arr[i]:
            v[i] = 1

    for x in range(1,n+1):
        group = []
        if not v[x]:
            c = 1
            while v[x] == 0:
                group.append(x)
                v[x] = c
                c += 1
                x = arr[x]

            if x in group: # 부분 사이클이 있다면
                cnt += v[x]-1
            else: 
                cnt += c-1

    print(cnt)
```

### 앱

```python
import sys
input = sys.stdin.readline

n,m= map(int, input().split())
byte = list(map(int, input().split()))
cost = list(map(int, input().split()))

res = sum(cost)
dp = [[0]*(res+1) for _ in range(n)]

# dp[i][j] = i번째까지 앱으로 j코스트 조합을 만들었을 때 최대메모리
for i in range(n):
    for j in range(len(dp[0])):
        if cost[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], byte[i] + dp[i-1][j-cost[i]])

        if dp[i][j] >= m:
            res = min(res, j)

print(res)
```

