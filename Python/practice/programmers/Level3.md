### N으로 표현

```python
def solution(N, number):
    answer = 0
    dp = [set() for _ in range(9)]
    dp[1].add(N)
    for i in range(1,9):
        for j in range(1,i):
            if j >= 1 and i-j >=1:
                for k in dp[j]:
                    for l in dp[i-j]:
                        dp[i].add(k+l)
                        dp[i].add(k-l)
                        if l != 0:
                            dp[i].add(k//l)
                        dp[i].add(k*l)
                for l in dp[j]:
                    for k in dp[i-j]:
                        dp[i].add(k+l)
                        dp[i].add(k-l)
                        if l != 0:
                            dp[i].add(k//l)
                        dp[i].add(k*l) 
                dp[i].add(int(str(N)*i))
        
        if number in dp[i]:
            return i 
        
    return -1
```

