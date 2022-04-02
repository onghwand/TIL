## BFS

### 5247. 연산

> deque
>
> 128,964 kb / 433ms

```python
from collections import deque
 
def f(N,M):
    q = deque([N])
    v = [0]*1000001
    while q:
        n = q.popleft()
        if n == M:
            return v[n]
        for t in [n+1,n-1,n-10,2*n]:
            if 0<t<1000001 and v[t] == 0:
                q.append(t)
                v[t] = v[n] + 1
    return
T =int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    c=f(N,M)
    print(f'#{tc} {c}')
```

> index 연산
>
> 155,740 kb / 417 ms

```python
def ff(N,M):
    q = [0]*1000001
    v = [0]*1000001
    cur=-1
    next=0
    q[next] = N
    while cur != next:
        cur += 1
        n = q[cur]
        if n == M:
            return v[n]
        for t in [n+1,n-1,n-10,2*n]:
            if 0<t<1000001 and v[t] == 0:
                next += 1
                q[next] = t
                v[t] = v[n] + 1
 
 
 
T =int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    c = ff(N, M)
    print(f'#{tc} {c}')
```

