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

### 입국심사

```python
def solution(n, times):
    left, right = 1, max(times)*n
    while left <= right:
        mid = (left+right)//2
        people = 0
        for time in times:
            people += mid//time
            if people > n :
                break
            
        if people >= n:
            answer = mid
            right = mid-1 
        else:
            left = mid + 1
    
    
    return answer
```

### 가장 먼 노드

```python
from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    dist = [0]*(n+1)
    
    for x,y in edge:
        graph[x].append(y)
        graph[y].append(x)
    
    q = deque([1])
    v = [0]*(n+1)
    v[1] = 1
    while q:
        k = q.popleft()
        for a in graph[k]:
            if v[a] == 0:
                q.append(a)
                v[a] = 1
                dist[a] = dist[k] + 1
                
    cnt = 0
    for a in dist:
        if a == max(dist):
            cnt += 1
    return cnt
```

