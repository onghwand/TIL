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

