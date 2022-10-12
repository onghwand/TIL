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

### 전화번호 목록

```python
t = int(input())
def check(arr,n):
    for i in range(n-1):
        if arr[i+1].startswith(arr[i]):
                return 'NO'
    return 'YES'

for _ in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input())
    
    arr.sort()
    print(check(arr,n))

```

### 트리의 순회

```python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

def find_root(inS, inE, postS, postE):
    # print(inS, inE, postS, postE)
    if (inS > inE) or (postS > postE):
        return

    root = postorder[postE]
    idx = inorder.index(root)
    print(root, end=' ')

    find_root(inS, idx-1, postS, postS+idx-inS-1)
    find_root(idx+1, inE, postS+idx-inS, postE-1)

find_root(0,n-1,0,n-1)

# testcase
# 12
# 7 3 8 1 9 4 10 0 11 5 2 6
# 7 8 3 9 10 4 1 11 5 6 2 0
```

### LCA

```python
from collections import deque
N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

tree = [0]*(N+1)
depth = [0]*(N+1)
q = deque()
q.append(1)
tree[1] = 1
depth[1] = 1
while q:
    k = q.popleft()
    for i in graph[k]:
        if tree[i] == 0:
            tree[i] = k
            depth[i] = depth[k] + 1
            q.append(i)
# print(tree)
# print(depth)

arr = []
M = int(input())
for _ in range(M):
    arr.append(list(map(int,input().split())))
# print(arr)

def find_common(x,y):
    if depth[x] == depth[y]:
        while x != y:
            x, y = tree[x], tree[y]
        return x
    elif depth[x] > depth[y]:
        while depth[x] != depth[y]:
            x = tree[x]
        return find_common(x,y)
    else:
        while depth[x] != depth[y]:
            y = tree[y]
        return find_common(x,y)

for x,y in arr:
    print(find_common(x,y))
```

### 트리

```python
def find(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x,y):
    p[find(y)] = x
    
case = 0
while 1:
    n, m = map(int, input().split())
    if (n,m) == (0,0):
        break

    # graph = [[] for _ in range(n+1)]
    p = [x for x in range(n + 1)]
    cycle = []
    for _ in range(m):
        x,y = map(int, input().split())
        p1 = find(x)
        p2 = find(y)
        if p1 != p2:
            union(x,y)
        else:
            cycle.append(x)

    group = set()
    for c in cycle:
        group.add(find(c))

    answer = 0
    for i in range(1,n+1):
        if find(i) in group:
            continue
        answer += 1
        group.add(find(i))

    case += 1
    if answer == 0:
        print(f"Case {case}: No trees." )
    elif answer == 1:
        print(f"Case {case}: There is one tree.")
    else:
        print(f"Case {case}: A forest of {answer} trees.")
```



