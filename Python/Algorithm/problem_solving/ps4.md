## 문제풀이4

### 5648. 원자 소멸 시뮬레이션

```python
def meet(a, b):  # 만나면 return 시간
    if abs(a[0] - b[0]) == abs(a[1] - b[1]):  # 대각선위치에서 내려와서 만날때
        t = abs(a[0] - b[0])
        if a[0] + t * mode[a[2]][0] == b[0] + t * mode[b[2]][0] and a[1] + t * mode[a[2]][1] == b[1] + t * mode[b[2]][1]:
            return t
    elif a[0] == b[0]:  # x좌표가 같고
        if a[1] < b[1] and a[2] == 0 and b[2] == 1:
            return (b[1] - a[1]) / 2
        elif a[1] > b[1] and a[2] == 1 and b[2] == 0:
            return (a[1] - b[1]) / 2
    elif a[1] == b[1]:  # y좌표가 같고
        if a[0] < b[0] and a[2] == 3 and b[2] == 2:
            return (b[0] - a[0]) / 2
        elif a[0] > b[0] and a[2] == 2 and b[2] == 3:
            return (a[0] - b[0]) / 2
    return 0  # 안만나면 0


mode = [[0,1], [0, -1], [-1, 0], [1, 0]]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    atoms = [0] * N  # 0:x좌표 1:y좌표 2:방향 3:에너지
    for i in range(N):
        atoms[i] = list(map(int, input().split()))
    times = []
    for i in range(N):
        for j in range(i + 1, N):
            time = meet(atoms[i][:3], atoms[j][:3])
            if time > 0:
                times.append([time, i, j])
    times = sorted(times) # 0:만나는 시간 1,2:만나는 원자 종류 
    cnt = 0
    v = [0] * N
    pre = -1
    # 만나는 원자들 시간순으로 하나씩 순회하며 에너지 합
    for m in times:
        if pre == m[0]:
            if v[m[1]] == 0:
                cnt += atoms[m[1]][3]
                v[m[1]] = 1
            if v[m[2]] == 0:
                cnt += atoms[m[2]][3]
                v[m[2]] = 1
            pre = m[0]
        elif v[m[1]] == 0 and v[m[2]] == 0 and pre != m[0]:
            cnt += atoms[m[1]][3] + atoms[m[2]][3]
            v[m[1]] = 1
            v[m[2]] = 1
            pre = m[0]

    print(f'#{tc} {cnt}')
```

### 2806. N-Queen

```python
def f(i,N,pre): # pre: 퀸 놓은 좌표들
    global cnt
    if i == N:
        cnt += 1
        # for a in arr:
        #     print(*a)
        return
    else:
        for j in range(N):
            if not v[j] and queen(pre,i,j):
                v[j] = 1
                # arr[i][j] = 1
                f(i+1,N,pre+[(i,j)])
                # arr[i][j] = 0
                v[j] = 0

def queen(pre,i,j): #대각선에 퀸 있으면 F 없으면 T
    for p in pre:
        if abs(p[0]-i) == abs(p[1]-j):
            return False
    return True

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    #arr = [[0]*N for _ in range(N)]
    v = [0]*N
    cnt = 0
    f(0,N,[])
    print(f'#{tc} {cnt}')
```

### 2115. 벌꿀채취

```python
def f(tmp,M,C):
    global maxV
    for i in range(1<<M):
        cnt = 0
        sq = 0
        for j in range(M):
            if i & (1<<j):
                cnt += tmp[j]
                sq += tmp[j]**2
        if cnt <= C:
            if maxV < sq:
                maxV = sq

T = int(input())
for tc in range(1,T+1):
    N,M,C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = [[0]*(N-M+1) for i in range(N)]
    # for a in arr:
    #     print(*a)

    for i in range(N):
        for j in range(N-M+1):
            tmp = arr[i][j:j+M]
            if sum(tmp) <= C:
                lst[i][j] = sum(map(lambda x:x**2, tmp))
                #print(arr[i][j:j+M])
            else:
                maxV = 0
                f(tmp,M,C)
                lst[i][j] = maxV
    # for l in lst:
    #     print(*l)

    ans = 0
    for i in range(N):
        for j in range(N-M+1):
            ttmp = lst[i][j]
            for k in range(N):
                for l in range(N-M+1):
                    if (i==k and abs(j-l) <=M-1) or (i,j) == (k,l) :
                        continue
                    ttmp += lst[k][l]
                    if ttmp > ans:
                        ans = ttmp
                    ttmp -= lst[k][l]

    print(f'#{tc} {ans}')
```

### 1249. 보급로

```python
def f(i,j):
    q = []
    q.append((i,j))
    while q:
        i,j=q.pop(0)
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            ni,nj=i+di,j+dj
            if 0<=ni<N and 0<=nj<N :
                if costs[ni][nj] > costs[i][j] + arr[ni][nj]:
                    costs[ni][nj] = costs[i][j] + arr[ni][nj]
                    q.append((ni,nj))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,list(input()))) for _ in range(N)]
    costs = [[100000000]*N for _ in range(N)]
    costs[0][0] = 0
    f(0,0)
    # for a in costs:
    #     print(*a)
    print(f'#{tc} {costs[N-1][N-1]}')
```

