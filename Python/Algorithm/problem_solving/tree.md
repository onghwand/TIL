## 5177. 이진 힙

```python
def push(n):
    global last
    last += 1
    arr[last] = n
    c = last
    p = c // 2
    while p >= 1 and arr[p] > arr[c]:
        arr[p], arr[c] = arr[c], arr[p]
        c = p
        p = c // 2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    arr = [0]*(N+1)
    last = 0

    for n in nums:
        push(n)

    total = 0
    while last >= 1:
        total += arr[last//2]
        last = last//2

    print(f'#{tc} {total}')
```

## 5176. 이진탐색

```python
def inorder(v,n):
    global cnt
    if v <= n:
        inorder(v*2,n)
        arr[v] = cnt
        cnt += 1
        inorder(v*2+1,n)

T = int(input())
for tc in range(1, T+1):
    n = int(input())

    arr = [0]*(n+1)
    cnt = 1
    inorder(1,n)

    print(f'#{tc} {arr[1]} {arr[int(n/2)]}')
```

## 5178. 노드의 합

```python
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [0]*(N+1)
    for i in range(M):
        node, n = map(int, input().split())
        arr[node] = n

    for i in range(N-M, 0,-1):
        if arr[i] == 0 :
            if i*2+1 <= N :
                arr[i] = arr[i*2] + arr[i*2+1]
            else:
                arr[i] = arr[i*2]

    print(f'#{tc} {arr[L]}')
```

## 5174. subtree 

```python
T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    c1 = [0]*(E+2)
    c2 = [0]*(E+2)
    for i in range(E):
        p, c = arr[i*2] , arr[i*2+1]
        if c1[p] == 0:
            c1[p] = c
        else:
            c2[p] = c

    cnt = 1
    queue = []
    queue.append(N)
    while queue:
        p = queue.pop(0)
        if c1[p] :
            queue.append(c1[p])
            cnt += 1
        if c2[p] :
            queue.append(c2[p])
            cnt += 1

    print(f'#{tc} {cnt}')
```

