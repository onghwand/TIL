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

