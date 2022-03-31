## 분할정복_백트래킹 문풀

### 5205. 퀵 정렬

```python
def hoare(arr,l,r):
    p = l
    i,j=l+1,r
    while i<=j:
        while i<=j and arr[i]<=arr[p]:
            i+=1
        while i<=j and arr[j]>arr[p]:
            j-=1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[p] = arr[p], arr[j]
    return j

def qs(arr,l,r):
    if l<r:
        p = hoare(arr,l,r)
        qs(arr,l,p-1)
        qs(arr,p+1,r)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    qs(arr,0,N-1)
    print(f'#{tc} {arr[N//2]}')
```

### 5208. 전기버스2

```python
def f(i,n,s,bat): # s:충전수, bat:배터리용량
    global minV
    if s > minV:
        return
    else:
        for j in range(1,bat+1):
            if i+j>=n:
                if s < minV:
                    minV = s
            else:
                f(i+j,n,s+1,bus[i+j])

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N, bus = arr[0], arr[1:]
    minV = N
    f(0,N-1,0,bus[0])
    print(f'#{tc} {minV}')
```

### 5209. 최소생산비용

```python
def f(i,N,s):
    global minV
    if i == N:
        if s < minV:
            minV = s
    elif s > minV:
        return
    else:
        for j in range(N):
            if not v[j]:
                v[j] = 1
                f(i+1,N,s+arr[i][j])
                v[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0]*N
    minV = 99*N
    f(0,N,0)
    print(f'#{tc} {minV}')
```

### 5207. 이진 탐색

```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    m = (N-1)//2
    cnt = 0
    for b in B:
        pre = 0
        l = 0
        r = N - 1
        while l <= r:
            m = (l+r)//2
            if b == A[m]:
                cnt += 1
                #print(b)
                break
            elif b > A[m]:
                if pre == 'r':
                    break
                l = m+1
                pre = 'r'
            else:
                if pre == 'l':
                    break
                r = m-1
                pre = 'l'

    print(f'#{tc} {cnt}')
```

### 1865. 동철이의 일분배

```python
def f(i,N,p):
    global maxV
    if i==N:
        if p > maxV:
            maxV = p
    elif p<=maxV:
        return
    else:
        for j in range(N):
            if not v[j]:
                v[j] = 1
                f(i+1,N,p*arr[i][j]/100)
                v[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    v=[0]*N
    maxV = 0
    f(0,N,1)
    print(f'#{tc} {maxV*100:6f}')
```

