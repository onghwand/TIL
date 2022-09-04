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

