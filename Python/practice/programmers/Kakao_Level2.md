## LEVEL2

> [프로그래머스-카카오](https://programmers.co.kr/learn/challenges)

### 주차 요금 계산

> import 하기 싫었는데 결국 math.ceil 써버림
>
> 다 풀고 다른사람 풀이들 보는데 변수명이 너무 비슷해서 사람 생각하는게 다 똑같구나 느낌

```python
import math
def solution(fees, records):
    answer = []
    inout = {}
    status = {}
    charges = {}
    for record in records:
        time, car, mode = record.split()
        if mode == 'IN':
            status[car] = time
        else:
            hour_pre, minute_pre = map(int, status[car].split(':'))
            hour_post, minute_post = map(int,time.split(':'))
            elapsed = (hour_post-hour_pre)*60 + (minute_post-minute_pre)
            charges[car] = charges.get(car, 0) + elapsed
        inout[car] = mode
            
    for car in status.keys():
        if inout[car] == 'IN':
            hour_pre, minute_pre = map(int, status[car].split(':'))
            elapsed = (23-hour_pre)*60 + (59-minute_pre)
            charges[car] = charges.get(car, 0) + elapsed
            
    
    for key in charges.keys():
        if charges[key] <= fees[0]:
            charges[key] = fees[1]
        else:
            charges[key] = fees[1] + math.ceil((charges[key] - fees[0]) / fees[2]) * fees[3]
    
    
    for car in sorted(charges):
        answer.append(charges[car])
            
    return answer
```

<br>

### k진수에서 소수 개수 구하기

```python
def solution(n, k):
    s = ''
    while n > 0:
        s = str(n % k) + s
        n //= k

    nums = s.split('0')
    
    cnt = 0
    for num in nums:
        if len(num) > 0 and int(num) > 1:
            n = int(num)
            for i in range(2,int(n**(1/2))+1):
                if n % i == 0:
                    break
            else:
                cnt+=1
    return cnt
```

<br>

### 양궁대회

> 개망한 내 풀이
>
> | 테스트 1 〉  | 통과 (3.90ms, 10.2MB) |
> | ------------ | --------------------- |
> | 테스트 2 〉  | 통과 (4.51ms, 10.2MB) |
> | 테스트 3 〉  | 통과 (4.12ms, 10.2MB) |
> | 테스트 4 〉  | 실패 (런타임 에러)    |
> | 테스트 5 〉  | 통과 (4.37ms, 10.4MB) |
> | 테스트 6 〉  | 통과 (5.75ms, 10MB)   |
> | 테스트 7 〉  | 통과 (4.16ms, 10.1MB) |
> | 테스트 8 〉  | 통과 (3.91ms, 10.4MB) |
> | 테스트 9 〉  | 통과 (3.84ms, 10.3MB) |
> | 테스트 10 〉 | 통과 (4.24ms, 10.1MB) |
> | 테스트 11 〉 | 통과 (4.01ms, 10.1MB) |
> | 테스트 12 〉 | 통과 (4.02ms, 10.3MB) |
> | 테스트 13 〉 | 통과 (3.94ms, 10.4MB) |
> | 테스트 14 〉 | 통과 (4.15ms, 10.1MB) |
> | 테스트 15 〉 | 통과 (4.40ms, 10.2MB) |
> | 테스트 16 〉 | 통과 (4.16ms, 10.4MB) |
> | 테스트 17 〉 | 통과 (3.86ms, 10.2MB) |
> | 테스트 18 〉 | 통과 (3.65ms, 10.1MB) |
> | 테스트 19 〉 | 통과 (3.83ms, 10.2MB) |
> | 테스트 20 〉 | 통과 (4.38ms, 10.4MB) |
> | 테스트 21 〉 | 통과 (4.18ms, 10.3MB) |
> | 테스트 22 〉 | 통과 (4.26ms, 10.2MB) |
> | 테스트 23 〉 | 실패 (런타임 에러)    |
> | 테스트 24 〉 | 통과 (4.32ms, 10.2MB) |
> | 테스트 25 〉 | 통과 (4.02ms, 10.2MB) |

```python
def solution(n, info):
    answer = [-1]
    apeach = 0
    for i in range(11):
        if info[i]:
            apeach += 10-i
    
    need = [x+1 for x in info]
    
    maxV = 0
    for i in range(1<<11):
        #cnt = 0
        lion = 0
        lion_info = [0]*11
        apeach_tmp = apeach
        for j in range(11):
            if i & (1<<j):
                #cnt += need[j]
                lion += 10 - j
                lion_info[j] = need[j]
                if info[j]:
                    apeach_tmp -= 10-j
        if sum(lion_info) <= n:
            if sum(lion_info) < n:
                lion_info[10] = n-sum(lion_info)
            if  lion - apeach_tmp > maxV:
                maxV = lion - apeach_tmp
                answer = lion_info
            elif lion - apeach_tmp == maxV:
                for k in range(10, -1, -1):
                    if lion_info[k] > answer[k]:
                        answer = lion_info
                        break
                    elif lion_info[k] < answer[k]:
                        break

    return answer
```

> 다른사람 풀이
>
> 중복조합 함수가 있었다... 나중에도 유용하게 쓸 듯
>
> 안풀린다고 풀릴 때까지 하루종일 고민하는거보다 그냥 빨리 찾아서 습득하는게 더 나은 방법인 것 같다. 유용한 함수들도 알게 되고

```python
from itertools import combinations_with_replacement

def solution(n, info):
    answer = [0 for _ in range(11)]
    win = False
    max_num = 0   # 라이언이 이길때 가장큰 점수 차이
    # 1. 중복 조합을 이용해 라이언의 점수를 만든다.
    for res in list(combinations_with_replacement(range(0, 11), n)):
        now = [0 for _ in range(11)]
        for r in res:
             now[10 - r] += 1
        lion = 0
        peach = 0
        # 2. 라이언 점수와 어피치 점수 비교한다.
        for i, (l, p) in enumerate(zip(now, info)):
            if l == p == 0:
                continue
            if p >= l:
                peach += (10 - i)
            elif l > p:
                lion += (10 - i)
        # 3. 총 점수를 비교해 라이언이 큰 경우 결과를 업데이트 해준다.
        if lion > peach:
            win = True
            if (lion - peach) > max_num:
                max_num = lion - peach
                answer = now
    if not win:
        return [-1]
    return answer
```

> 조금 수정

```python
from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    maxV = 0
    for res in combinations_with_replacement(range(0,11),n):
        tmp = [0]*11
        for i in res:
            tmp[10-i] += 1
        
        apeach = lion = 0
        for i, (l,m) in enumerate(zip(tmp, info)):
            if l == m == 0:
                continue
            if l > m:
                lion += 10-i
            elif l <= m:
                apeach += 10-i
                
        if lion-apeach > maxV:
            answer = tmp
            maxV = lion-apeach
    
    return answer
```

<br>

### 거리두기 확인하기

```python
def isPerson(i,j,place):
    q = []
    q.append((i,j))
    v = [[0]*5 for _ in range(5)]
    v[i][j] = 1
    while q:
        ci,cj = q.pop(0)
        if (ci,cj) != (i,j) and place[ci][cj] == 'P':
            return 0
        else:
            for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
                ni,nj = ci+di, cj+dj
                if 0<=ni<5 and 0<=nj<5 and abs(ni-i)+abs(nj-j) <= 2 and v[ni][nj] == 0 and place[ni][nj] != 'X':
                    q.append((ni,nj))
                    v[ni][nj] = 1
    return 1
        

def solution(places):
    answer = []
    for place in places:
        flag = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    tmp = isPerson(i,j,place)
                    if tmp == 0 :
                        answer.append(0)
                        flag = 0
                        break
            if flag == 0:
                break
        else:
            answer.append(1)
                          
    return answer
```

<br>

### 튜플

> 오늘 카카오 인턴 코테에서 벽을 느꼈다. 연습으로 극복이 가능한건지 의문이다. 그냥 태생적으로 불가능한걸수도

```python
def solution(s):
    answer = []
    s=s[1:-1]
    stack = []
    tmp = []
    number = ''
    for n in s:
        if n == ',':
            if pre == '}':
                continue
            tmp.append(int(number))
            number = ''
        elif n == '}':
            tmp.append(int(number))
            stack.append(tmp)
            number = ''
            tmp = []
        elif n == '{':
            continue
        else:
            number += n
        pre = n
            
    stack.sort(key=lambda x: len(x))
    
    for arr in stack:
        for num in arr:
            if num not in answer:
                answer.append(num)
                break  
    
    return answer
```

<br>

### 캐시

```python
from collections import deque
def solution(cacheSize, cities):
    cache = deque()
    time = 0
    cities = list(map(lambda x: x.lower(), cities))  
    
    if cacheSize == 0:
        return 5*len(cities)
    
    for city in cities:
        if city not in cache:
            if len(cache) == cacheSize:
                cache.popleft()
            time += 5
        else:
            time += 1
            cache.remove(city)       
        cache.append(city) 
    return time
```

<br>

### n진수 게임

> 다른 풀이를 봐도 창의적인 풀이는 따로 없는 것 같다. 비슷비슷

```python
def solution(n, t, m, p):
    s = '0'
    L = p + m*t
    i = 1
    res = ''
    while len(s) <= L:
        tmp = ''
        q = i
        
        while q>0:
            q, r= divmod(q, n)
            if r<10:
                tmp = str(r) + tmp
            else:
                tmp = hex(r)[2:].upper() + tmp
    
        s += str(tmp)
        i += 1
        
    for i in range(p-1,t*m+p-1,m):
        res += s[i]
    
    return res
```

