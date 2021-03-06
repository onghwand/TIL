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

<br>

### [3차] 방금그곡

> 최종프로젝트를 하느라 알고리즘 문제를 안푼지 거의 2주가 된 것 같다. 그래도 주말에 계속 코테를 봐와서 어색하진 않았다. 
>
> 1차 시도 왜 틀리는지 모르겠다.

```python
def solution(m, musicinfos):
    answer = '(None)'
    max_min = -1
    for music in musicinfos:
        start, end, title, part = music.split(',')
        start_hour, start_min = map(int, start.split(':'))
        end_hour, end_min = map(int, end.split(':'))
        playing_min = (end_hour - start_hour)*60 - start_min + end_min 
        # print(playing_min)
        L = len(part)
        q, r = divmod(playing_min, L)
        played = part*q + part[:r]
        #print(played)
        M = len(m)
        for i in range(len(played)-M+1):
            if played[i:i+M] == m and played[i:i+M+1] != m+'#':
                #print(played[i:i+M],played[i:i+M+1])
                if max_min < playing_min:
                    answer = title
                    max_min = playing_min
        
    return answer
```

> 2차 시도
>
> 카카오 공식 해답보고 치환해서 풀었는데도 틀려서 보니까 계속 'C#' 같은 음을 'C', '#' 두 개의 음으로 처리하고 있었다. 최대한 위에서 치환 처리를 해놓고 푸니 풀렸다.

```python
def solution(m, musicinfos):
    sub = {'C#':'c', 'D#':'d', 'F#':'f', 'G#':'g', 'A#':'a'}
    answer = '(None)'
    max_min = -1
    for music in musicinfos:
        start, end, title, part = music.split(',')
        start_hour, start_min = map(int, start.split(':'))
        end_hour, end_min = map(int, end.split(':'))
        playing_min = (end_hour - start_hour)*60 - start_min + end_min 
        
        for k in sub.keys():
            m = m.replace(k, sub[k])
            part = part.replace(k, sub[k])
            
        L = len(part)
        q, r = divmod(playing_min, L)
        played = part*q + part[:r]
        M = len(m)
        
        if m in played:
            if max_min < playing_min:
                answer = title
                max_min = playing_min
        
    return answer
```

<br>

### [1차] 프렌즈4블록

> 1차 시도, 고등학교때부터 느꼈던 거지만 나는 생각이 진짜 짧다 테케를 다 통과해버리면 뭐가 틀렸는지 찾기가 너무 힘들다

```python
def solution(m, n, board):
    answer = 0
    for i in range(len(board)):
        board[i] = list(board[i])
    
    # 겹쳐도 깨지니까 일단 set에 터질 좌표 모았음
    while 1:
        points = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != ' ' and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    points.add((i,j))
                    points.add((i+1,j))
                    points.add((i,j+1))
                    points.add((i+1,j+1))
        
        # 만약에 터질 좌표가 없으면 그만
        if len(points) == 0:
            break
        
        # 터질 좌표가 있으면 개수 세
        answer += len(points)
        
        # 터질 좌표 없애야 하니까 0으로 바꿔놔
        for i,j in points:
            board[i][j] = 0
        
        # for b in board:
        #     print(*b)
        
        # 열을 순회하면서 0으로 바꿔놨던거 위에꺼로 메꿔주면서 빈공간으로 바꿔 
        for j in range(n):
            zeros = 0  
            start = -1
            for i in range(m):
                if board[i][j] == ' ':
                    start = i
                if board[i][j] == 0:
                    board[i][j] = board[i-1][j]
                    zeros += 1
            
            for l in range(start+1, start+1+zeros):
                board[l][j] = ' '
        
#         for b in board:
#             print(*b)
        
#         print(answer)
                    
              
    return answer
```

> 2차 시도, 친구가 뭐가 틀렸는지 찾아줬다. 0일때 위에거 하나만 내리면 안되고, 다내려야한다.	

```python
def solution(m, n, board):
    answer = 0
    for i in range(len(board)):
        board[i] = list(board[i])
    
    while 1:
        points = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != ' ' and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    points.add((i,j))
                    points.add((i+1,j))
                    points.add((i,j+1))
                    points.add((i+1,j+1))
                    
        if len(points) == 0:
            break
            
        answer += len(points)
        
        for i,j in points:
            board[i][j] = 0
        
        for j in range(n):
            zeros = 0  
            start = -1
            for i in range(m):
                if board[i][j] == ' ':
                    start = i
                if board[i][j] == 0:
                    for k in range(i,0,-1):
                        board[k][j] = board[k-1][j]
                    zeros += 1
            
            for l in range(start+1, start+1+zeros):
                board[l][j] = ' '
               
    return answer
```

<br>

### [3차] 파일명 정렬

> EASY

```python
def solution(files):
    answer = []
    filtered = []
    for k in range(len(files)):
        front, *tail = files[k].split('.')
        head = ''
        number = ''
        for i in range(len(front)):
            if front[i].isdigit():
                number += front[i]
            else:
                if len(number) != 0:
                    break
                head += front[i].lower()
        filtered.append([head,number,k])
    
    filtered = sorted(filtered, key=lambda x: (x[0],int(x[1]),int(x[2])))
    
    for item in filtered:
        answer.append(files[item[2]])
    
    return answer
```

<br>

### [3차] 압축

> 문자열 끝에 도달했을때가 살짝 헷갈렸다.

```python
def solution(msg):
    dic = [0]
    answer = []
    for i in range(65, 91):
        dic.append(chr(i))

    i = 0
    while 1:
        j = 2
        while msg[i:i + j] in dic:
            if i + j >= len(msg):
                break
            j += 1
        if i+j >= len(msg):
            final = msg[i:i + j]
            last = msg[i:i + j - 1]
            break
        dic.append(msg[i:i+j])
        answer.append(dic.index(msg[i:i+j-1]))
        
        i = i+j-1

    if final not in dic:
        dic.append(last)
        answer.append(dic.index(last))
        answer.append(dic.index(msg[-1]))
    else:
        answer.append(dic.index(final))
        
    return answer
```

<br>

### [다시풀기]후보키

> [참고](https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-%ED%9B%84%EB%B3%B4%ED%82%A4-Python)
>
> issubset 메서드를 처음 알았다. 부분집합이 있는지 없는지 확인할때 유용할것같다.

```python
from itertools import combinations
def solution(relation):
    answer=0
    rows = len(relation)
    cols = len(relation[0])
    
    comb = []
    for i in range(1, cols+1):
        comb.extend(combinations(range(cols),i))
    
    unique = []
    for com in comb:
        tmp = [tuple(item[key] for key in com) for item in relation]
        
        if len(set(tmp)) == rows:
            put = True
            
            for x in unique:
                if set(x).issubset(set(com)):
                    put = False
                    break
            if put:
                unique.append(com)
                
    return len(unique)
```

<br>

### [다시풀기]순위 검색

> 효율성 테스트 통과 못함

```python
def solution(info, query):
    answer = []
    
    for q in query:
        cnt = 0 
        lang, job, level, food = map(lambda x: x.strip(), q.split('and'))
        food, score=food.split()
        for inf in info:
            lang1, job1, level1, food1, score1 = inf.split()

            if lang in (lang1, '-') and job in (job1, '-') and level in (level1, '-') and food in (food1, '-') and int(score1) >= int(score):
                cnt+=1
        answer.append(cnt)            
        
    return answer
```

> [참고](https://velog.io/@dogcu/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%9C%EC%9C%84-%EA%B2%80%EC%83%89)
>
> 라이브러리를 진짜 잘써야한다.

- bisect_left(a, x)
  - 정렬된 a에 x를 삽입할 위치를 리턴해준다. x가 a에 이미 있으면 기존 항목의 앞(왼쪽) 위치를 반환한다.
  - 이 문제에서는 query로 주어진 score 이상 개수를 구하는데 썼다.
- defaultdict
  - defaultdict(list) 라고하면 value값이 list로 설정된다.
  - dic['a'].append(1) 하면 'a':[1]이 바로 생성됨.

```python
from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    dic = defaultdict(list)
    
    for inf in info:
        inf = inf.split()
        condition = inf[:-1]
        score = int(inf[-1])
        for i in range(5):
            case = list(combinations([0,1,2,3], i))
            for c in case:
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = '-'
                
                key = ''.join(tmp)
                dic[key].append(score)
    # print(dic)         
    for v in dic.values():
        v.sort()
    # print(dic)
    
    for q in query:
        q = q.replace("and ", "").split()
        key = ''.join(q[:-1])
        score = int(q[-1])
        # print(key, score)
        cnt = 0
        if key in dic:
            target = dic[key]
            idx = bisect_left(target, score)
            # print(target, idx)
            cnt = len(target) - idx
        answer.append(cnt)
        
    return answer
```

<br>

### 오픈채팅방

> 생각보다 쉬운문제였는데 괜히 복잡하게 풀다가 오래걸렸다.

```python
def solution(record):
    answer = []
    names = {}
    for re in record:
        status, user_id, *username = re.split()
        if status == 'Enter' or status == 'Change':
            names[user_id] = username[0]
    
    for re in record:
        status, user_id, *username = re.split()
        if status == 'Enter':
            answer.append(f'{names[user_id]}님이 들어왔습니다.')
        elif status == 'Leave':
            answer.append(f'{names[user_id]}님이 나갔습니다.')
                
    return answer
```

<br>

### 괄호 변환

```python
def is_correct(p):
    stack = []
    for i in range(len(p)):
        if p[i] == '(':
            stack.append(p[i])
        else:
            if stack:
                stack.pop()
            else:
                return False
    else:
        return True
    
def f(p):
    cnt = 0
    if len(p) == 0:
        return p
    
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        elif p[i] == ')':
            cnt -= 1
        if cnt == 0:
            break
    u, v = p[:i+1], p[i+1:]
    
    if is_correct(u):
        return u + f(v)
    else:
        w = u[1:-1]
        x = ''
        for a in w:
            if a == '(':
                x += ')'
            else:
                x += '('      
        return '('+f(v)+')'+x
        
def solution(p):
    answer = ''
    
    if is_correct(p):
        return p
    else:
        answer = f(p)
    
    return answer
```

<br>

### 수식 최대화

```python
from itertools import permutations

def cal(pre, post, oper):
    if oper == '+':
        return pre+post
    elif oper == '-':
        return pre-post
    elif oper == '*':
        return pre*post
    
def solution(expression):
    num = ''
    arr = []
    op = set()
    for a in expression:
        if a.isdigit():
            num += a
        else:
            arr.append(int(num))
            num = ''
            arr.append(a)
            op.add(a)
    arr.append(int(num))
    permu = list(permutations(op))
    
    maxV = 0
    for p in permu:
        lst = [x for x in arr]
        for oper in p:
            i = 0
            while i < len(lst):
                if lst[i] == oper:
                    lst[i-1:i+2] = [cal(lst[i-1],lst[i+1],oper)]
                    i -= 1
                i += 1
        if maxV < abs(lst[0]):
            maxV = abs(lst[0])       
    
    return maxV
```

