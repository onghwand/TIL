### 수 찾기

```python
N = int(input())
arr = sorted(list(map(int, input().split())))
M = int(input())
nums = list(map(int, input().split()))

for n in nums:
    start = 0
    end = N-1
    while start <= end:
        mid = (start+end)//2

        if arr[mid] == n:
            print(1)
            break
        elif arr[mid] < n:
            start = mid + 1
        else:
            end = mid - 1
    else:
        print(0)
```

### 나무 자르기

```python
from bisect import bisect_right
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

trees = list(map(int, input().split()))


# bisect_right(trees, k)
left = 0
right = max(trees)
while left <= right:
    mid = (left+right) // 2

    total = 0
    for tree in trees:
        if tree >= mid:
            total += tree-mid
    # print(left, right, mid, total)
    if total >= M:
        left = mid +1
    else:
        right = mid -1

print(right)
```

### 숫자 카드 2

```python
from bisect import bisect_left, bisect_right
N = int(input())
arr = sorted(list(map(int, input().split())))
M = int(input())
nums = list(map(int, input().split()))

ans = []
for n in nums:
    l,r = bisect_left(arr,n), bisect_right(arr,n)
    ans.append(r-l)
    
print(*ans)
```

### 랜선 자르기

```python
k, n = map(int, input().split())
lens = []
for _ in range(k):
    lens.append(int(input()))

left = 1
right = max(lens)
while left <= right:
    mid = (left+right)//2

    cnt = 0
    for len in lens:
        cnt += len//mid
    # print(left, right,mid,cnt)
    if cnt >= n: # 가능하면
        left = mid + 1 # 왼쪽을 올려
    else: # 불가능하면
        right = mid - 1 #오른쪽을 내려
print(right)
```

### 공유기 설치

```python
n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

left = 1
right = max(arr)
while left <= right:
    mid = (left+right)//2

    cnt = 1
    cur = arr[0]
    for i in range(1, len(arr)):
        if arr[i] >= cur + mid:
            cnt += 1
            cur = arr[i]

    if cnt >= c:
        left = mid + 1
    else:
        right = mid - 1

print(right)
```

### 예산

```python
n = int(input())
arr =list(map(int, input().split()))
m = int(input())

l = 1
r = max(arr)
while l<=r:
    mid = (l+r)//2

    cnt = 0
    for a in arr:
        if a>mid:
            cnt += mid
        else:
            cnt += a

    if cnt == m:
        print(mid)
        break
    elif cnt > m:
        r = mid - 1
    else:
        l = mid + 1
else:
    print(r)
```

### 두 용액

```python
import sys
INF = sys.maxsize

n = int(input())
arr =sorted(list(map(int, input().split())))

if arr[0] > 0:
    ans= [arr[0],arr[1]]
elif arr[-1] <0:
    ans=[arr[-2],arr[-1]]
else:
    l,r = 0,n-1
    v = INF
    while l<r:
        ll, rr =arr[l], arr[r]

        if abs(ll+rr)<v:
            v = abs(ll+rr)
            ans = [ll,rr]

        if ll+rr < 0:
            l+=1
        elif ll+rr > 0:
            r-=1
        else:
            break
print(*ans)
```

### K번째 수

```python
n,k = int(input()), int(input())

l,r =1,k

while l<=r:
    mid = (l+r)//2

    cnt = 0
    for i in range(1,n+1):
        cnt += min(mid//i, n)

    if cnt >= k:
        r = mid - 1
    else:
        l = mid + 1
print(l)
```

### 중량제한

```python
from collections import deque
import sys

input = sys.stdin.readline
def bfs(limit):
    v[s] = 1
    q = deque()
    q.append(s)
    while q:
        nxt = q.popleft()
        if nxt == e:
            return True
        for ni,nw in graph[nxt]:
            if v[ni] == 0 and nw >= limit:
                q.append(ni)
                v[ni] = 1
    return False


n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])


s,e = map(int, input().split())
l,r = 1, 1000000000
while l<=r:
    mid = (l+r)//2
    v = [0]*(n+1)
    if bfs(mid):
        l = mid + 1
    else:
        r = mid - 1

print(r)
```





