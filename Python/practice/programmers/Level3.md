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

### 정수 삼각형

```python
def solution(triangle):
    L = len(triangle)
    arr = [[0]*(i+1) for i in range(L)]
    arr[0][0] = triangle[0][0]
        
    for i in range(L-1):
        for j in range(len(triangle[i])):
            arr[i+1][j] = max(arr[i+1][j], arr[i][j]+triangle[i+1][j])
            arr[i+1][j+1] = max(arr[i+1][j+1], arr[i][j]+triangle[i+1][j+1])
        
    return max(arr[-1])
```

### 네트워크

```python
def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i==j:
                continue
            else:
                if computers[i][j] == 1:
                    graph[i].append(j)
    
    v = [0]*n
    cnt = 0
    for i in range(n):
        if v[i] != 0:
            continue
        else:
            cnt += 1
            q = [i]
            while q:
                p = q.pop(0)
                for x in graph[p]:
                    if v[x] == 0:
                        v[x] = 1
                        q.append(x)
        
    return cnt
```

### 이중우선순위큐

```python
import heapq
def solution(operations):
    answer = [0,0]
    minheap = [] 
    maxheap = []
    for op in operations:
        o, n = op.split()
        if o == 'I':
            heapq.heappush(minheap, int(n))
            heapq.heappush(maxheap, -int(n))
        else:
            if maxheap:
                if n == '1':
                    maxV = heapq.heappop(maxheap)
                    minheap.remove(-maxV)
                else:
                    minV = heapq.heappop(minheap)
                    maxheap.remove(-minV)
   
    if len(maxheap)==0:
        return [0,0]
    else:
        return [-heapq.heappop(maxheap),heapq.heappop(minheap)]
```

### 베스트앨범

```python
def solution(genres, plays):
    answer = []
    dic = {}
    total = {}
    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], []) + [(plays[i],i)]
        total[genres[i]] = total.get(genres[i], 0 ) + plays[i]
    
    for k in dic.keys():
        dic[k] = sorted(dic[k],key=lambda x: (-x[0],x[1]))
    
    totals = []
    for k,v in total.items():
        totals.append((v,k))
    totals = sorted(totals, reverse=True)

    for num, genre in totals:
        for n, song in dic[genre][:2]:
            answer.append(song)
            
    return answer
```

### 단어변환

```python
def dif(word, new):
    cnt = 0
    for i in range(len(word)):
        if word[i] != new[i]:
            cnt += 1
    return cnt

def solution(begin, target, words):
    minV = len(words)+1
    v = [0]*len(words)
    
    def dfs(begin, target, cnt):
        nonlocal minV
        if begin == target:
            if minV > cnt:
                minV = cnt
            return 
        for i in range(len(words)):
            if v[i] == 0 and dif(words[i], begin) == 1:
                v[i] = 1
                dfs(words[i], target, cnt+1)
                v[i] = 0
    dfs(begin, target, 0)
   
    if minV == len(words) + 1:
        return 0
    return minV
```

### 단속카메라

```python
def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x: x[1])
    v = [0]*len(routes)
    i = 0
    camera = -30001
    while i < len(routes):
        inn, out = routes[i]
        if inn <= camera <= out :
            i+=1
            continue
        camera = out
        answer +=1
        i+=1
        
    return answer
```

