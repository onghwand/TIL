## Graph, MST, Dijkstra

### 5250. 최소 비용

> v 초기값을 arr(0,0) 넣어놔서 혼자 한참 바보같은 고민했다..

```python
def f(i,j,N):
    q = []
    q.append((i,j))
    while q:
        i,j = q.pop(0)
        for di,dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            ni,nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] > v[i][j] + max(arr[ni][nj]-arr[i][j],0) + 1:
                v[ni][nj] = v[i][j] + max(arr[ni][nj] - arr[i][j], 0) + 1
                q.append((ni,nj))

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    v=[[10000000]*N for _ in range(N)]
    v[0][0] = 0
    f(0,0,N)
    print(f'#{tc} {v[N-1][N-1]}')
```

### 5251. 최소 이동거리

```python
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    INF = 1000000
    adjM = [[INF]*(N+1) for _ in range(N+1)] # 인접행렬

    for i in range(N+1):
        adjM[i][i] = 0 # 자기 자신과의 거리 0
    for _ in range(E):
        s, e, w = map(int, input().split())
        adjM[s][e] = w # 방향성 그래프

    # 다익스트라
    d = [adjM[0][i] for i in range(N+1)] # 출발점에서의 최소거리. adjM[0]을 복사
    u = [0]*(N+1) # 비용결정표시
    u[0] = 1
    for _ in range(N): # N+1 정점중 출발 제외한 N개 비용결정
        minV = INF
        w = 0
        for i in range(N+1): # 비용이 결정전이고 최소인 정점 w 찾기
            if u[i] == 0 and INF > d[i]:
                minV = d[i]
                w = i
        u[w] = 1 # 남은 정점 중 비용이 가장 적은 w
        # w에 인접인 정점 v에 대해 출발에서의 d[v]도착비용갱신
        for v in range(N+1):
            if 0< adjM[w][v] <INF: # v가 w에 인접
                d[v] = min(d[v],d[w]+adjM[w][v])

    print(f'#{tc} {d[N]}')
```

### 5249. 최소 신장 트리

```python
def findset(n):
    if n == p[n]:
        return n
    else:
        return findset(p[n])

def union(a,b):
    p[findset(b)] = findset(a)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = []
    for _ in range(E):
        n1,n2,w = map(int, input().split())
        edge.append((w,n1,n2))
    # Kruskal
    edge.sort() # 가중치 기준 오름차순 정렬
    p = [i for i in range(V+1)] # 대표원소
    cnt = 0 # 선택한 간선 수
    s = 0 # 가중치합
    for w,n1,n2 in edge: # V개의 간선 선택
        if findset(n1) != findset(n2): # 사이클이 아니면
            s += w # 가중치 추가
            union(n1,n2)
            cnt += 1
            if cnt == V:
                break
    print(f'#{tc} {s}')
```

### 5248. 그룹나누기

```python
def findset(n):
    if n == arr[n]:
        return n
    else:
        return findset(arr[n])

def union(a,b):
    arr[findset(b)] = findset(a)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [x for x in range(N+1)]
    lst = list(map(int, input().split()))
    for i in range(M):
        a,b = lst[i*2], lst[i*2+1
        union(a,b)
    cnt = 0
    for i in range(1,N+1):
        if i == arr[i]:
            cnt += 1
    print(f'#{tc} {cnt}')
```

