### 트리 순회

```python
n = int(input())
dc = {}
for _ in range(n):
    a,b,c = input().split()
    dc[a] = [b,c]
pre=''
ino=''
post=''

def preorder(root):
    global pre
    pre+=root
    if dc[root][0] != '.':
        preorder(dc[root][0])
    if dc[root][1] != '.':
        preorder(dc[root][1])

def inorder(root):
    global ino
    if dc[root][0] != '.':
        inorder(dc[root][0])
    ino += root
    if dc[root][1] != '.':
        inorder(dc[root][1])

def postorder(root):
    global post
    if dc[root][0] != '.':
        postorder(dc[root][0])
    if dc[root][1] != '.':
        postorder(dc[root][1])
    post += root

preorder('A')
inorder('A')
postorder('A')
print(pre)
print(ino)
print(post)
```

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

### 트리의 지름

```python
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

def bfs(s,w):
    q = deque()
    q.append((s,w))
    maxV = maxI = 0
    while q:
        cs,cw = q.popleft()
        for ns,nw in graph[cs]:
            if dist[ns] == -1:
                dist[ns] = cw+nw
                if dist[ns] > maxV:
                    maxV = dist[ns]
                    maxI = ns
                q.append((ns,cw+nw))
    return maxV,maxI


dist = [-1]*(n+1)
dist[1]=0
maxV,maxI = bfs(1,0)
dist = [-1]*(n+1)
dist[maxI]=0
maxV,maxI = bfs(maxI,0)
print(maxV)
```

### 트리

```python
N = int(input())
arr = list(map(int, input().split()))
k = int(input())

def dfs(k):
    arr[k] = -2
    for i in range(len(arr)):
        if arr[i] == k:
            dfs(i)
dfs(k)
cnt = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        cnt += 1
print(cnt)

```

### 이진 검색 트리

```python
import sys
sys.setrecursionlimit(10**6)
preorder = []
def postorder(start,end):
    if start >= end:
        return

    root = preorder[start]
    if root >= preorder[end-1]:
        postorder(start+1,end)
        print(root)
        return
    idx = 0
    for i in range(start+1, end):
        if preorder[i] > root:
            idx = i
            break

    postorder(start+1,idx)
    postorder(idx,end)
    print(root)


while 1:
    try:
        preorder.append(int(input()))
    except:
        break
print(preorder)
postorder(0,len(preorder))
```



