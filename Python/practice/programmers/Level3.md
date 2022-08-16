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

### 기지국 설치

```python
def solution(n, stations, w):
    answer = 0
    cur = 1
    for st in stations:
        s, e = st-w, st+w
        diff = max(s - cur,0)
        q,r = divmod(diff,2*w+1)
        if r==0:
            answer += q
        else:
            answer += q+1   
        cur = e+1 
    diff = max(n+1-cur,0) 
    q,r = divmod(diff,2*w+1)
    if r==0:
        answer += q
    else:
        answer += q+1 
    return answer
```

### 디스크 컨트롤러

```python
import heapq
def solution(jobs):
    answer=now=i=0
    start= -1
    heap = []
    
    while i < len(jobs):
        for x,y in jobs:
            if start < x <= now:
                heapq.heappush(heap, (y,x))
        if heap:
            y,x = heapq.heappop(heap)
            start = now
            now += y
            answer += now - x
            i += 1
        else:
            now += 1
    
    return answer // len(jobs)
```

### 110 옮기기

```python
from collections import deque
def solution(s):
    answer = []
    
    for num in s:
        stack = []
        cnt = 0
        for n in num:
            if n == '0' and len(stack) > 1 and stack[-2:] == ['1','1']:
                cnt += 1
                stack.pop()
                stack.pop()
            else:
                stack.append(n)
        
        if cnt == 0:
            answer.append(num)
        else:
            new = deque()

            while stack:
                if stack[-1] == '1':
                    new.append(stack.pop())
                else:
                    break
            for i in range(cnt):
                new.appendleft('0')
                new.appendleft('1')
                new.appendleft('1')
            while stack:
                new.appendleft(stack.pop())
            answer.append(''.join(new))
                       
    return answer
```

### 합승 택시 요금

```python
import heapq
import sys
def solution(n, s, a, b, fares):
    answer = 0
    INF = sys.maxsize
    graph = [[] for _ in range(n+1)]
    for x,y,z in fares:
        graph[x].append((z,y))
        graph[y].append((z,x))
    
    def dijkstra(start):
        dist = [INF] * (n+1)
        dist[start] = 0
        heap = []
        heapq.heappush(heap,(0,start))
        while heap:
            min_dist, min_idx = heapq.heappop(heap)
            if dist[min_idx] != min_dist:
                continue
            for cur_dist, cur_idx in graph[min_idx]:
                val = cur_dist + min_dist
                if dist[cur_idx] > val:
                    dist[cur_idx] = val
                    heapq.heappush(heap, (val,cur_idx))
        return dist
    
    arr = [[]] + [dijkstra(i) for i in range(1,n+1)]
    minV = INF
    for i in range(1,n+1):
        minV = min(minV, arr[i][a]+arr[i][b]+arr[s][i])
    
    return minV
```

### 선입 선출 스케줄링

```python
def solution(n, cores):
    if n <= len(cores):
        return n
    n -= len(cores)
    left = 1
    right = max(cores)*n
    
    while left < right:
        mid = (left+right) // 2
        work = 0
        
        for core in cores:
            work += mid//core
        
        if work >= n:
            right = mid
        else:
            left = mid + 1
    
    for core in cores:
        n -= (right-1)//core
    
    
    for i in range(len(cores)):
        if right % cores[i] == 0:
            n -= 1
            if n == 0:
                return i+1
```

