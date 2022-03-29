## 5203. 베이비진 게임

```python
T = int(input())
for tc in range(1,T+1):
    a = list(map(int, input().split()))
    p1 = a[0:11:2]
    p2 = a[1:12:2]
    cnt1 = [0]*14
    cnt2 = [0]*14
    i = 0
    ans = 0

    while i<6:
        k=p1[i]+2
        cnt1[k] += 1
        if i>1 and (cnt1[k] == 3 or 0 not in cnt1[k-2:k+1] or 0 not in cnt1[k-1:k+2] or 0 not in cnt1[k:k+3]):
            ans = 1
            break
        l=p2[i]+2
        cnt2[l] += 1
        if i>1 and (cnt2[l] == 3 or 0 not in cnt2[l-2:l+1] or 0 not in cnt2[l-1:l+2] or 0 not in cnt2[l:l+3]):
            ans = 2
            break
        i+=1

    print(f'#{tc} {ans}')
```

## 5202. 화물 도크

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0]*N
    for i in range(N):
        arr[i] = list(map(int,input().split()))

    arr.sort(key=lambda x:x[1])
    cnt = 1
    i = 0
    j = 1
    while j < N:
        if arr[i][1] <= arr[j][0]:
            cnt += 1
            i = j
            j = i+1
        else:
            j += 1

    print(f'#{tc} {cnt}')
```

## 5201. 컨테이너 운반

```python
T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    w = sorted(list(map(int, input().split())), reverse=True) # 화물
    t = sorted(list(map(int, input().split())), reverse=True) # 트럭

    # 트럭 - 화물 하나씩 매칭
    i=j=0
    cnt=0
    while i<len(w) and j<len(t):
        if w[i] <= t[j]:
            cnt += w[i]
            i+=1
            j+=1
        else:
            i+=1
    print(f'#{tc} {cnt}')

```

## 5189. 전자카트

```python
def f(i,N):
    global minV
    if i == N:
        lst = [0] + p
        cnt = 0
        for k in range(N):
            cnt += arr[lst[k]][lst[k+1]]
        cnt += arr[lst[N]][lst[0]]
        if cnt < minV:
            minV = cnt
    else:
        for j in range(i,N):
            p[i], p[j] = p[j], p[i]
            f(i+1,N)
            p[i], p[j] = p[j], p[i]
    return
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    minV = 100*N
    p=[x+1 for x in range(N-1)]
    f(0,N-1)
    print(f'#{tc} {minV}')

```

## 5188. 최소합

```python
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for k in range(1,2*N-1): #누적합
        for i in range(N):
            for j in range(N):
                if i+j == k:
                    if i==0:
                        arr[i][j] += arr[i][j-1]
                    elif j==0:
                        arr[i][j] += arr[i-1][j]
                    else:
                        arr[i][j] += min(arr[i-1][j], arr[i][j-1])

    print(f'#{tc} {arr[N-1][N-1]}')
```

