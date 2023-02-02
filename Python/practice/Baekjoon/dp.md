> dp를 정말 심각하게 못해서 연습시작

### 1로 만들기

```python
N = int(input())
dp = [0]*(N+1)
dp[1] = 0
for i in range(2,N+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
print(dp[N])
```

### 피보나치 함수

```python
T = int(input())
for _ in range(T):
    N = int(input())
    if N == 0:
        print('1 0')
        continue
    elif N == 1:
        print('0 1')
        continue
    dp0 = [0]*(N+1)
    dp1 = [0]*(N+1)
    dp0[0] = dp1[1] = 1
    dp0[1] = dp1[0] = 0

    for i in range(2,N+1):
        dp0[i] = dp0[i-1] + dp0[i-2]
        dp1[i] = dp1[i-1] + dp1[i-2]
    print(f'{dp0[N]} {dp1[N]}')
```

### 1,2,3 더하기

```python
T = int(input())
for _ in range(T):
    N = int(input())
    if N == 1:
        print(1)
        continue
    elif N == 2:
        print(2)
        continue
    elif N == 3:
        print(4)
        continue
    dp = [0]*(N+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4,N+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    print(dp[N])
```

### 2xn 타일링

```python
n = int(input())
dp = [0]*(n+1)
def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = (dp[i-2] + dp[i-1])%10007
    return dp[n]
print(f(n))
```

### RGB거리

```python
N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

for i in range(1,N):
    arr[i][0] = min(arr[i-1][1],arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i - 1][0], arr[i - 1][2]) + arr[i][1]
    arr[i][2] = min(arr[i - 1][0], arr[i - 1][1]) + arr[i][2]

print(min(arr[N-1]))
```

### 계단 오르기

```python
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

dp = [0]*N

for i in range(N):
    if i == 0:
        dp[i] = arr[i]
    elif i == 1:
        dp[i] = arr[i] + dp[i-1]
    elif i==2:
        dp[i] = max(arr[i]+arr[i-2], arr[i]+arr[i-1])
    else:
        dp[i] = max(arr[i] + dp[i-2],arr[i]+arr[i-1]+dp[i-3])
print(dp[N-1])
```

### 가장 긴 증가하는 부분 수열

```python
N = int(input())
arr = list(map(int, input().split()))

dp = [1]*N
for i in range(1,N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
```

### 정수 삼각형

```python
N = int(input())
arr = []
dp = [[0]*(i+1) for i in range(N)]
for i in range(N):
    arr.append(list(map(int, input().split())))

dp[0][0] = arr[0][0]

for i in range(N-1):
    for j in range(i+1):
        dp[i+1][j] = max(arr[i+1][j] + dp[i][j], dp[i+1][j])
        dp[i+1][j+1] = max(arr[i+1][j+1] + dp[i][j], dp[i+1][j+1])

print(max(dp[N-1]))
```

### 연속합

```python
N = int(input())
arr = list(map(int, input().split()))

dp =[0]*N
dp[0] = arr[0]

for i in range(1,N):
    dp[i] = max(dp[i-1]+arr[i], arr[i])

print(max(dp))
```

### 포도주 시식

```python
N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))

dp = [0]*N

for i in range(N):
    if i == 0:
        dp[i] = arr[i]
    elif i == 1:
        dp[i] = arr[i] + arr[i-1]
    elif i == 2:
        dp[i] = max(arr[i] + arr[i-1] , arr[i] + arr[i-2], dp[i-1])
    else:
        dp[i] = max(arr[i]+dp[i-2], arr[i]+arr[i-1]+dp[i-3], dp[i-1])

print(max(dp))
```

### 파도반 수열

```python
N = int(input())
for _ in range(N):
    n = int(input())
    dp = [0]*n
    for i in range(n):
        if i in [0,1,2]:
            dp[i] = 1
        else:
            dp[i] = dp[i-2]+dp[i-3]
    print(dp[n-1])
```

### 피보나치 수 2

```python
N = int(input())
fibo = [0]*(N+1)
for i in range(N+1):
    if i == 0:
        fibo[i] = 0
    elif i in [1,2]:
        fibo[i] = 1
    else:
        fibo[i] = fibo[i-1]+fibo[i-2]
print(fibo[N])
```

### 쉬운 계단 수

```python
N = int(input())

dp = [[0]*10 for _ in range(N+1)]
for i in range(1, 10):
    dp[1][i] = 1

MOD = 1000000000

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N]) % MOD)
```

### 2xn 타일링2

```python
n = int(input())

dp = [0]*(n+1)

for i in range(1,n+1):
    if i==1:
        dp[i] = 1
    elif i==2:
        dp[i] = 3
    else:
        dp[i] = dp[i-2]*2 + dp[i-1]

print(dp[n]%10007)
```

### 이친수

```python
n = int(input())

dp = [0]*(n+1)

for i in range(n+1):
    if i in [0,1,2]:
        dp[i] = 1
    else:
        for j in range(2,i+1):
            dp[i] += dp[i-j]

print(dp[n])
```

### 01타일

```python
N = int(input())

dp = [0]*(N+1)

for i in range(1,N+1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    else:
        dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[N])
```

### 카드 구매하기

```python
N = int(input())
dp = [0]*(N+1)
arr = list(map(int, input().split()))

for i in range(len(arr)):
    dp[i+1] = arr[i]

for i in range(1,N+1):
    for j in range(1,i):
        dp[i] = max(dp[i], dp[j]+dp[i-j])

print(dp[N])
```

### 스티커

```python
t = int(input())
for i in range(t):
  s = []
  n = int(input())
  for k in range(2):
    s.append(list(map(int, input().split())))
  for j in range(1, n):
    if j == 1:
      s[0][j] += s[1][j - 1]
      s[1][j] += s[0][j - 1]
    else:
      s[0][j] += max(s[1][j - 1], s[1][j - 2])
      s[1][j] += max(s[0][j - 1], s[0][j - 2])
  print(max(s[0][n - 1], s[1][n - 1]))
```

### 오르막 수

```python
N = int(input())

dp = [[0]*10 for _ in range(N)]

for i in range(N):
    for j in range(10):
        if i == 0 :
            dp[i][j] = 1
        else:
            for k in range(j,10):
                dp[i][j] += dp[i-1][k]

print(sum(dp[N-1])%10007)

```

### 가장 긴 바이토닉 부분 수열

```python
N = int(input())
arr =list(map(int, input().split()))

left = [0]*N
right = [0]*N

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            left[i] = max(left[i], left[j]+1)
        if arr[-j-1] < arr[-i-1]:
            right[-i-1] = max(right[-i-1], right[-j-1]+1)

maxV = 0
for k in range(N):
    if maxV < left[k] + right[k]+1:
        maxV = left[k]+right[k]+1
print(maxV)

```

### 합분해

```python
n, k = map(int, input().split())
dp = [[0]*201 for _ in range(201)]

for i in range(1,201):
    dp[1][i] += 1
    dp[i][1] = i

for i in range(2,201):
    for j in range(2,201):
        dp[i][j] = (dp[i][j-1]+dp[i-1][j])%(10**9)

print(dp[k][n])
```

### 전깃줄

```python
n = int(input())
arr = [[0]*n for _ in range(2)]
dc = {}
for i in range(n):
    x,y = map(int, input().split())
    arr[0][i] = x
    dc[x] = y
arr[0].sort()
for i in range(n):
    arr[1][i] = dc[arr[0][i]]

dp = [1]*n
for i in range(n):
    for j in range(i):
        if arr[1][i] > arr[1][j]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))
```

### 동전1

```python
n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [1]+[0]*k

for c in coin:
    for j in range(c,k+1):
        if j-c>=0:
            dp[j] += dp[j-c]

print(dp[k])
```

### 행렬 곱셈 순서

```python
n = int(input())
mtrx=[list(map(int, input().split())) for _ in range(n)]

arr = [[2**31]*n for _ in range(n)]
for i in range(n):
    arr[i][i] = 0

for diff in range(1,n):
    for i in range(n-diff):
        j = i+diff
        if diff == 1:
            arr[i][j] = mtrx[i][0]*mtrx[i][1]*mtrx[j][1]
        else:
            for k in range(i,j):
                arr[i][j] = min(arr[i][j],
                                arr[i][k]+mtrx[i][0]*mtrx[k][1]*mtrx[j][1]+arr[k+1][j])

print(arr[0][n-1])
```

### LCS2

```python
x = [0] + list(input())
y = [0] + list(input())
dp = [[0]*len(y) for _ in range(len(x))]

for i in range(1,len(x)):
    for j in range(1,len(y)):
        if x[i] == y[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
cnt = dp[-1][-1]
i,j = len(x)-1,len(y)-1
s = ''
while cnt>0:
    if cnt == dp[i-1][j]:
        i -= 1
    elif cnt == dp[i][j-1]:
        j -= 1
    else:
        s = x[i]+s
        cnt -= 1
        i -= 1
        j -= 1
print(len(s))
print(s)
```

### 외판원 순회

> 구글 해답을 봐도 어렵다..

```python
import sys
input = sys.stdin.readline

def solution(N,W,dp):
    for i in range(N):
        for j in range(N):
            if not W[i][j]:
                W[i][j] = float('inf')

    for i in range(1,N):
        dp[i][0] = W[i][0]

    for k in range(1, N-1): # k는 route 점의 개수
        for route in range(1, size):
            if count(route, N) == k: # route가 k개의 점으로 이루어져있는가
                for i in range(1,N):
                    if not isin(i,route): # i에서 출발하는데 i를 지나면 안됨
                        dp[i][route] = get_minimum(N,W,i,route,dp)

    dp[0][size-1] = get_minimum(N,W,0,size-1,dp)

    return dp[0][size-1]

def count(route,N):
    cnt = 0
    for n in range(1,N):
        if route & (1<<n-1) != 0:
            cnt += 1
    return cnt

def isin(i,route): # 점 i가 route에 있는지
    if route & (1 << i-1) != 0:
        return True
    return False

def get_minimum(N,W,i,route,dp):
    minimum_dist = float('inf')
    for j in range(1,N):
        if isin(j, route):
            before_route = route & ~(1<<j-1)
            dist = W[i][j] + dp[j][before_route]
            if minimum_dist > dist:
                minimum_dist = dist
    return minimum_dist


N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
size = 2**(N-1)
dp = [[float('inf')]*size for _ in range(N)]
print(solution(N,W,dp))
```

### 게임개발

```python
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
degree = [0]*(n+1)
times = [0]*(n+1)

for i in range(1,n+1):
    arr = list(map(int, input().split()))[:-1]
    times[i] = arr[0]
    for j in arr[1:]:
        degree[i] += 1
        graph[j].append(i)

result = [0]*(n+1)
q = deque()
for i in range(1,n+1):
    if not degree[i]:
        q.append(i)

while q:
    cur = q.popleft()
    result[cur] += times[cur]

    for building in graph[cur]:
        result[building] = max(result[building], result[cur])
        degree[building] -= 1
        if not degree[building]:
            q.append(building)

for i in range(1,n+1):
    print(result[i])
```

### 줄세우기

```python
n = int(input())
arr = [int(input()) for _ in range(n)]

dp = [1]*n
for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))
```

### 동전

```python
T = int(input())
for _ in range(T):
    n = int(input())
    coin = list(map(int, input().split()))
    money = int(input())

    dp = [0]*(money+1)
    dp[0] = 1
    for c in coin:
        for i in range(c,money+1):
            dp[i] += dp[i-c]

    print(dp[money])
```

### RGB거리2

```python
import sys
INF = sys.maxsize

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = INF
for i in range(3):
    dp = [INF]*3
    tmp = [INF]*3
    tmp[i] = arr[0][i]
    for j in range(1,n):
        dp[0] = arr[j][0] + min(tmp[1],tmp[2])
        dp[1] = arr[j][1] + min(tmp[0],tmp[2])
        dp[2] = arr[j][2] + min(tmp[0],tmp[1])

        tmp = [x for x in dp]

    for j in range(3):
        if i != j:
            ans = min(ans, dp[j])
print(ans)
```

### 작업

```python
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1) # 누적 차수
cost = [0]*(n+1) # 각 작업 소요시간

q = deque()

for i in range(1,n+1):
    arr = list(map(int, input().split()))
    cost[i] = arr[0]

    if not arr[1]:
        q.append(i)

    for v in arr[2:]:
        indegree[i] += 1
        graph[v].append(i)

end = [0]*(n+1) # 각 작업 끝나는 시간
maxV = 0
while q:
    c = q.popleft()
    end[c] += cost[c]

    if end[c] > maxV:
        maxV = end[c]

    for x in graph[c]:
        indegree[x] -= 1
        end[x] = max(end[x], end[c])

        if not indegree[x]:
            q.append(x)

print(maxV)
```

