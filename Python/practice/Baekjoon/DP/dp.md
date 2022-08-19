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

