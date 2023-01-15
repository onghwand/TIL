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

### 개미굴

```python
N = int(input())
arr = []
maxV = 0
for _ in range(N):
    info = list(input().split())
    if int(info[0]) > maxV:
        maxV = int(info[0])
    arr.append(info[1:])

arr.sort()
# print(arr)

dash = '--'
answer = []
for i in range(N):
    if i == 0:
        for j in range(len(arr[i])):
            answer.append(dash*j + arr[i][j])
    else:
        idx = 0
        for j in range(len(arr[i])):
            if arr[i-1][j] != arr[i][j] or len(arr[i-1]) <= j:
                break
            else:
                idx = j + 1
        for j in range(idx, len(arr[i])):
            answer.append(dash*j + arr[i][j])

for ans in answer:
    print(ans)
```

### 노드사이의 거리

```python
import sys, heapq
INF = sys.maxsize

N, M =map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,c = map(int, input().split())
    graph[a].append([c,b])
    graph[b].append([c,a])

arr = []
for _ in range(M):
    arr.append(list(map(int,input().split())))

def dijkstra(x,y):
    dist = [INF]*(N+1)
    dist[x] = 0

    q = []
    heapq.heappush(q, [0,x])
    while q:
        min_dist, min_idx = heapq.heappop(q)
        if dist[min_idx] != min_dist:
            continue

        for cur_dist, cur_idx in graph[min_idx]:
            tmp = cur_dist + min_dist
            if dist[cur_idx] > tmp:
                dist[cur_idx] = tmp
                heapq.heappush(q, [tmp, cur_idx])

    return dist[y]

for x,y in arr:
    print(dijkstra(x,y))
```

### 양 구출 작전

> 문제를 잘못고른것같다.. 메모리 초과가 계속나는데 구글에 올라와있는 다른 해답들도 똑같이 메모리 초과가난다. 예제는 통과

```python
import sys

sys.setrecursionlimit(1000000)
N = int(input())

tree = [0]*(N+1)
group = [0]*(N+1)
cnt = [0]*(N+1)
tree[1] = 1
for i in range(2,N+1):
    t,a,p = input().split()
    a,p = int(a), int(p)
    tree[i] = p
    group[i] = t
    cnt[i] = a


def move(k, residue):
    if group[k] == 'W':
        tmp = residue
        residue -= cnt[k]
        cnt[k] = max(cnt[k]-tmp, 0)
        if residue <= 0:
            return 0
    elif k == 1:
        return residue

    return move(tree[k], residue)

answer = 0
for i in range(2,N+1):
    if group[i] == 'S':
        count = move(i, cnt[i])
        answer += count
    # print(cnt,i,count)
print(answer)
```

### [13325 이진트리](https://t-anb.tistory.com/29)

```python
k = int(input())
tree = [0,0]+list(map(int, input().split()))

cumul = [x for x in tree]

for i in range(len(tree)-1,1,-2):
    cumul[i//2] = cumul[i//2] + max(cumul[i],cumul[i-1])

for i in range(1,len(cumul)):
    if i*2+1 <= len(cumul):
        tree[i*2] += (cumul[i]-tree[i])-cumul[i*2]
        tree[i*2+1] += (cumul[i]-tree[i])-cumul[i*2+1]
        cumul[i * 2] += (cumul[i] - tree[i]) - cumul[i * 2]
        cumul[i * 2 + 1] += (cumul[i] - tree[i]) - cumul[i * 2 + 1]

print(sum(tree))
```

### 1949 우수마을

```python
import sys
sys.setrecursionlimit(10**6)

N = int(input())
tree = [0]+list(map(int, input().split()))
v = [0]*(N+1)
def dfs(i):
    v[i] = 1
    for city in graph[i]:
        if v[city] == 0:
            dfs(city)
            dp[i][1] += dp[city][0]
            dp[i][0] += max(dp[city][0], dp[city][1])

dp = [[0,tree[i]] for i in range(N+1)]
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(max(dp[1]))
```

### 19542 전단지돌리기

```python
import sys
from collections import deque
import sys
sys.setrecursionlimit(10**6)
n,s,d = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(cur,pre):
    v[cur] = 1
    tree[cur] = pre
    for nxt in graph[cur]:
        if v[nxt] == 0:
            dfs(nxt,cur)
            deep[cur] = max(deep[nxt]+1, deep[cur])

tree = [0]*(n+1)
deep = [0]*(n+1)
v = [0]*(n+1)
dfs(s,0)
tree[s]=s

total = 0
vi = [0]*(n+1)
for i in range(1,n+1):
    cnt = 0
    if deep[i] == d:
        nxt = i
        while tree[nxt] != nxt:
            if vi[nxt] == 0:
                vi[nxt] = 1
                cnt += 1
            else:
                break
            nxt = tree[nxt]
        total += cnt*2
print(total)
```

### 20364 부동산 다툼

```python
import sys
input = sys.stdin.readline
N, Q = map(int,input().split())
sections = [0]*(N+1)
for _ in range(Q):
    x = int(input())
    origin = x
    last = 0

    while x != 0:
        if sections[x] == 1:
            last = x
        x //= 2
    if last == 0:
        sections[origin] = 1
    print(last)
```

### 3584 가장 가까운 공통 조상

```python
T = int(input())

def get_level(k):
    lv = 0
    while tree[k] != 0:
        k = tree[k]
        lv += 1
    return lv


for tc in range(T):
    N = int(input())
    tree = [0]*(N+1)
    for _ in range(N-1):
        a,b = map(int, input().split())
        tree[b] = a

    a,b = map(int,input().split())
    lv_a, lv_b = get_level(a), get_level(b)

    diff = abs(lv_a - lv_b)
    if lv_a > lv_b:
        for i in range(diff):
            a = tree[a]
            lv_a -= 1
    elif lv_a < lv_b:
        for i in range(diff):
            b = tree[b]
            lv_b -= 1
    
    while a != b:
        a, b = tree[a], tree[b]

    print(a)
```

### 사촌

```python
import sys
input = sys.stdin.readline

while True:
    n,k = map(int,input().rstrip().split())
    if n==0 and k == 0:
        break
    answer = 0
    arr = [-1] + list(map(int, input().split()))
    lst = [-1] + [0]*n
    cnt = -1
    for i in range(1,len(arr)):
        if arr[i] == k:
            check = i
        if arr[i-1]+1 != arr[i]:
            cnt += 1
        lst[i] = cnt

    for i in range(1,len(arr)):
        if lst[i] != lst[check] and lst[lst[i]] == lst[lst[check]]:
            answer+=1
    print(answer)
```

### 22856 트리 순회

> 종료조건 0 not in visited[1:] 로 하니까 시간초과 => root == arr[-1]

```python
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
left = [0] * (n + 1)
right = [0] * (n + 1)
parent = [0] * (n + 1)

for _ in range(n):
    a, b, c = map(int, input().split())
    left[a] = b
    right[a] = c
    if b != -1:
        parent[b] = a
    if c != -1:
        parent[c] = a

cnt = 0
arr=[]
def in_order(root):
    if left[root] != -1:
        in_order(left[root])
    arr.append(root)
    if right[root] != -1:
        in_order(right[root])

def traverse(root):
    global cnt
    visited[root] = 1
    if left[root] != -1 and visited[left[root]] == 0:
        cnt += 1
        return traverse(left[root])
    elif right[root] != -1 and visited[right[root]]==0:
        cnt += 1
        return traverse(right[root])
    elif root == arr[-1]:
        return
    else:
        cnt += 1
        return traverse(parent[root])

visited = [0]*(n+1)
in_order(1)
traverse(1)
print(cnt)
```

