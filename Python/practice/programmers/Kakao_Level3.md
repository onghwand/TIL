### 불량 사용자

> 제일 싫어하는 상황이 나왔다. 거의 디버깅 불가능이다 이건
>
> | 테스트 1 〉  | 통과 (0.01ms, 10.2MB) |
> | ------------ | --------------------- |
> | 테스트 2 〉  | 통과 (0.06ms, 10.3MB) |
> | 테스트 3 〉  | 통과 (0.08ms, 10.3MB) |
> | 테스트 4 〉  | 통과 (0.03ms, 10.4MB) |
> | 테스트 5 〉  | 실패 (시간 초과)      |
> | 테스트 6 〉  | 통과 (4.05ms, 10.2MB) |
> | 테스트 7 〉  | 통과 (0.03ms, 10.2MB) |
> | 테스트 8 〉  | 통과 (0.06ms, 10.4MB) |
> | 테스트 9 〉  | 통과 (0.06ms, 10.3MB) |
> | 테스트 10 〉 | 통과 (0.03ms, 10.4MB) |
> | 테스트 11 〉 | 통과 (0.08ms, 10.3MB) |

```python
def same(user, ban):
    if len(user) == len(ban):
        for i in range(len(ban)):
            if ban[i] == user[i] or ban[i] =='*':
                continue
            else:
                return False
        else:
            return True
    else:
        return False
    
whole = []
def solution(user_id, banned_id):
    answer = 0
    possible = []
    for ban in banned_id:
        tmp = []
        for user in user_id:
            if same(user, ban):
                tmp.append(user)
        possible.append(tmp)
    # print(possible)
    N = len(possible)
    def f(i, N, arr):
        global whole
        if i == N:
            if set(arr) not in whole and len(set(arr)) == len(arr):
                whole.append(set(arr))
            return
        else:
            for j in range(len(possible[i])):
                f(i+1, N, arr+[possible[i][j]])
                
    f(0, N, [])
    # print(whole)
    return len(whole)
```



> 혹시나 하고 and로 연결되어 있는 조건문 앞 뒤 순서만 바꿨는데 해결됐다..
>
> | 테스트 1 〉  | 통과 (0.02ms, 10.3MB)    |
> | ------------ | ------------------------ |
> | 테스트 2 〉  | 통과 (0.06ms, 10.2MB)    |
> | 테스트 3 〉  | 통과 (0.06ms, 10.2MB)    |
> | 테스트 4 〉  | 통과 (0.05ms, 10.2MB)    |
> | 테스트 5 〉  | 통과 (8781.74ms, 10.1MB) |
> | 테스트 6 〉  | 통과 (5.14ms, 10.3MB)    |
> | 테스트 7 〉  | 통과 (0.04ms, 10.2MB)    |
> | 테스트 8 〉  | 통과 (0.07ms, 10.2MB)    |
> | 테스트 9 〉  | 통과 (0.08ms, 10.3MB)    |
> | 테스트 10 〉 | 통과 (0.03ms, 10.1MB)    |
> | 테스트 11 〉 | 통과 (0.08ms, 10.4MB)    |

```python
def same(user, ban):
    if len(user) == len(ban):
        for i in range(len(ban)):
            if ban[i] == user[i] or ban[i] =='*':
                continue
            else:
                return False
        else:
            return True
    else:
        return False
    
whole = []
def solution(user_id, banned_id):
    answer = 0
    possible = []
    for ban in banned_id:
        tmp = []
        for user in user_id:
            if same(user, ban):
                tmp.append(user)
        possible.append(tmp)
 
    N = len(possible)
    def f(i, N, arr):
        global whole
        if i == N:
            if len(set(arr)) == len(arr) and set(arr) not in whole :
                whole.append(set(arr))
            return
        else:
            for j in range(len(possible[i])):
                f(i+1, N, arr+[possible[i][j]])
                
    f(0, N, [])
    return len(whole)
```

<br>

### [다시풀기]보석쇼핑

> 1차시도, 시간초과
>
> | 테스트 1 〉  | 통과 (0.21ms, 10.2MB)    |
> | ------------ | ------------------------ |
> | 테스트 2 〉  | 통과 (5.36ms, 10.8MB)    |
> | 테스트 3 〉  | 통과 (30.66ms, 16.9MB)   |
> | 테스트 4 〉  | 통과 (655.02ms, 30.4MB)  |
> | 테스트 5 〉  | 통과 (69.49ms, 30.1MB)   |
> | 테스트 6 〉  | 통과 (0.04ms, 10.4MB)    |
> | 테스트 7 〉  | 통과 (0.06ms, 10.3MB)    |
> | 테스트 8 〉  | 통과 (1253.92ms, 63.7MB) |
> | 테스트 9 〉  | 통과 (487.88ms, 78.9MB)  |
> | 테스트 10 〉 | 통과 (5023.56ms, 96MB)   |
> | 테스트 11 〉 | 실패 (시간 초과)         |
> | 테스트 12 〉 | 통과 (1028.67ms, 205MB)  |
> | 테스트 13 〉 | 통과 (1777.15ms, 366MB)  |
> | 테스트 14 〉 | 실패 (시간 초과)         |
> | 테스트 15 〉 | 통과 (6665.49ms, 1.43GB) |

```python
from itertools import combinations
def solution(gems):
    every = set(gems)
    combi = list(combinations(range(len(gems)+1),2))
    combi = sorted(combi, key=lambda x: (x[1]-x[0], x[0]))
    
    for com in combi:
        if set(gems[com[0]:com[1]]) == every:
            return [com[0]+1, com[1]]
            
```

> 2차 시도, 최소 보석 수 이상부터 탐색을 해도 된다라고 생각했지만 또 시간초과
>
> | 테스트 1 〉  | 통과 (0.09ms, 10MB)      |
> | ------------ | ------------------------ |
> | 테스트 2 〉  | 통과 (2.68ms, 10.5MB)    |
> | 테스트 3 〉  | 통과 (41.30ms, 16MB)     |
> | 테스트 4 〉  | 통과 (28.49ms, 18.7MB)   |
> | 테스트 5 〉  | 통과 (79.79ms, 29MB)     |
> | 테스트 6 〉  | 통과 (0.02ms, 10.3MB)    |
> | 테스트 7 〉  | 통과 (0.05ms, 10.1MB)    |
> | 테스트 8 〉  | 통과 (960.44ms, 50.1MB)  |
> | 테스트 9 〉  | 통과 (426.15ms, 69.4MB)  |
> | 테스트 10 〉 | 통과 (2986.14ms, 45.8MB) |
> | 테스트 11 〉 | 실패 (시간 초과)         |
> | 테스트 12 〉 | 통과 (1320.06ms, 186MB)  |
> | 테스트 13 〉 | 통과 (1938.98ms, 336MB)  |
> | 테스트 14 〉 | 실패 (시간 초과)         |
> | 테스트 15 〉 | 통과 (7824.78ms, 1.34GB) |

```python
from itertools import combinations
def solution(gems):
    every = set(gems)
    L = len(every)
    combi = filter(lambda x: x[1]-x[0] >= L,list(combinations(range(len(gems)+1),2)))
    combi = sorted(combi, key=lambda x: (x[1]-x[0], x[0]))
    
    for com in combi:
        if set(gems[com[0]:com[1]]) == every:
            return [com[0]+1, com[1]]
```

> 3차 시도, 애초에 조합을 다 만드는데 시간이 소요되는거같아서 while로 방법을 바꾸니 시간이 줄었다 근데도 시간초과, 백트래킹처럼 가지치기를 안하면 안되는가보다.
>
> | 테스트 1 〉  | 통과 (0.02ms, 10.2MB)    |
> | ------------ | ------------------------ |
> | 테스트 2 〉  | 통과 (0.31ms, 9.98MB)    |
> | 테스트 3 〉  | 통과 (0.39ms, 10.1MB)    |
> | 테스트 4 〉  | 통과 (0.10ms, 10.2MB)    |
> | 테스트 5 〉  | 통과 (0.02ms, 9.94MB)    |
> | 테스트 6 〉  | 통과 (0.01ms, 9.94MB)    |
> | 테스트 7 〉  | 통과 (0.01ms, 10.1MB)    |
> | 테스트 8 〉  | 통과 (831.47ms, 10MB)    |
> | 테스트 9 〉  | 통과 (175.01ms, 10.2MB)  |
> | 테스트 10 〉 | 통과 (2562.53ms, 10.2MB) |
> | 테스트 11 〉 | 실패 (시간 초과)         |
> | 테스트 12 〉 | 통과 (309.42ms, 10.1MB)  |
> | 테스트 13 〉 | 통과 (241.88ms, 10.2MB)  |
> | 테스트 14 〉 | 실패 (시간 초과)         |
> | 테스트 15 〉 | 통과 (393.33ms, 10.3MB)  |

```python
from itertools import combinations
def solution(gems):
    every = set(gems)
    L = len(every)
    i = 0
    while 1:
        if set(gems[i:i+L]) == every:
            return [i+1, i+L]
        if i+L == len(gems):
            i = -1
            L += 1
        i += 1
```

> 결국 [참고](https://dev-note-97.tistory.com/70)
>
> 투포인터 알고리즘이라고 한다. 나처럼 다 순회하는게 아니라 지렁이가 움직이는거처럼 앞 뒤를 조절하며 확인한다.
>
> 시간 차이가 말도 안된다..
>
> | 테스트 1 〉  | 통과 (0.02ms, 10.1MB) |
> | ------------ | --------------------- |
> | 테스트 2 〉  | 통과 (0.06ms, 10.1MB) |
> | 테스트 3 〉  | 통과 (0.29ms, 10.2MB) |
> | 테스트 4 〉  | 통과 (0.30ms, 10.1MB) |
> | 테스트 5 〉  | 통과 (0.61ms, 9.98MB) |
> | 테스트 6 〉  | 통과 (0.01ms, 10.1MB) |
> | 테스트 7 〉  | 통과 (0.01ms, 10.1MB) |
> | 테스트 8 〉  | 통과 (0.35ms, 10.2MB) |
> | 테스트 9 〉  | 통과 (0.87ms, 10.1MB) |
> | 테스트 10 〉 | 통과 (0.57ms, 10.1MB) |
> | 테스트 11 〉 | 통과 (0.81ms, 10.3MB) |
> | 테스트 12 〉 | 통과 (1.57ms, 10.1MB) |
> | 테스트 13 〉 | 통과 (1.29ms, 10.3MB) |
> | 테스트 14 〉 | 통과 (1.72ms, 10.2MB) |
> | 테스트 15 〉 | 통과 (4.51ms, 10.4MB) |

```python
def solution(gems):
    answer = [] 
    shortest = len(gems)+1 # 현재 최단 구간 길이

    start_p = 0 # 구간의 시작점
    end_p = 0 # 구간의 끝 점 (보석을 체크하는 기준점)

    check_len = len(set(gems)) # 보석의 총 종류 수
    contained = {} # 현재 구간에 포함된 보석들(종류: 갯수)

    while end_p < len(gems): # 구간의 끝 점이 gems의 길이보다 작을 동안

        if gems[end_p] not in contained: # 현재 끝 점의 보석이 contained에 없다면(이 종류가 처음 발견되었다면)
            contained[gems[end_p]] = 1 # dictionary에 추가
        else:
            contained[gems[end_p]] += 1 # 이미 있으면 dictionary에 +1
            
        end_p += 1 # 끝 점 증가

        if len(contained) == check_len: # 현재 구간 내 보석의 종류의 갯수가 전체 종류의 갯수와 같다면 (현재 구간내 모든 종류가 다 있다면)
            while start_p < end_p: # start_p 가 end_p 보다 같을 때까지 증가
                if contained[gems[start_p]] > 1: # start_p에 해당하는 보석이 구간 내에 하나 이상 있다면
                    contained[gems[start_p]] -= 1 # 구간 내 보석 하나 감소(start_p 의 보석 뺄거니까)
                    start_p += 1 # start_p 증가
                    
                elif shortest > end_p - start_p: # 기존의 구간 최단거리보다 현재의 구간거리가 더 짧다면
                    shortest = end_p - start_p
                    answer = [start_p+1, end_p] # answer와 최단거리 갱신
                    break
                    
                else:
                    break

    return answer
```

<br>

### [다시풀기]징검다리 건너기

> 역시나 효율성
>
> ```
> 테스트 1 〉통과 (0.01ms, 10.3MB)
> 테스트 2 〉통과 (0.02ms, 10MB)
> 테스트 3 〉통과 (0.07ms, 10MB)
> 테스트 4 〉통과 (0.28ms, 10.1MB)
> 테스트 5 〉통과 (0.27ms, 10.1MB)
> 테스트 6 〉통과 (108.09ms, 10.2MB)
> 테스트 7 〉통과 (374.66ms, 10.2MB)
> 테스트 8 〉통과 (512.34ms, 10.3MB)
> 테스트 9 〉통과 (792.17ms, 10.1MB)
> 테스트 10 〉통과 (0.59ms, 10.1MB)
> 테스트 11 〉통과 (0.10ms, 10.1MB)
> 테스트 12 〉통과 (0.58ms, 10.2MB)
> 테스트 13 〉통과 (3.30ms, 10.4MB)
> 테스트 14 〉통과 (111.41ms, 10.1MB)
> 테스트 15 〉통과 (347.70ms, 10.2MB)
> 테스트 16 〉통과 (481.34ms, 10.2MB)
> 테스트 17 〉통과 (813.48ms, 10.2MB)
> 테스트 18 〉통과 (0.25ms, 10MB)
> 테스트 19 〉통과 (2.26ms, 10.2MB)
> 테스트 20 〉통과 (6.99ms, 10.1MB)
> 테스트 21 〉통과 (96.60ms, 10.1MB)
> 테스트 22 〉통과 (265.24ms, 10.2MB)
> 테스트 23 〉통과 (502.82ms, 10.1MB)
> 테스트 24 〉통과 (763.99ms, 10.2MB)
> 테스트 25 〉통과 (0.04ms, 9.95MB)
> 테스트 1 〉실패 (시간 초과)
> 테스트 2 〉실패 (시간 초과)
> 테스트 3 〉실패 (시간 초과)
> 테스트 4 〉실패 (시간 초과)
> 테스트 5 〉실패 (시간 초과)
> 테스트 6 〉실패 (시간 초과)
> 테스트 7 〉실패 (시간 초과)
> 테스트 8 〉실패 (시간 초과)
> 테스트 9 〉실패 (시간 초과)
> 테스트 10 〉실패 (시간 초과)
> 테스트 11 〉실패 (시간 초과)
> 테스트 12 〉실패 (시간 초과)
> 테스트 13 〉실패 (시간 초과)
> 테스트 14 〉실패 (시간 초과)
> ```

```python
def solution(stones, k):
    answer = 0
    
    while 1 :
        for i in range(len(stones)):
            if stones[i:i+k] == [0]*k:
                return answer
        else:
            stones = list(map(lambda x: max(x-1,0), stones))
            answer += 1   
```

> 2차 시도 나름 빨라졌지만 효율성 실패
>
> ```
> 테스트 1 〉통과 (0.00ms, 10MB)
> 테스트 2 〉통과 (0.01ms, 10.2MB)
> 테스트 3 〉통과 (0.01ms, 10.1MB)
> 테스트 4 〉통과 (0.02ms, 10MB)
> 테스트 5 〉통과 (0.03ms, 10.2MB)
> 테스트 6 〉통과 (0.19ms, 10MB)
> 테스트 7 〉통과 (0.56ms, 10.1MB)
> 테스트 8 〉통과 (1.48ms, 10.3MB)
> 테스트 9 〉통과 (1.72ms, 10.1MB)
> 테스트 10 〉통과 (0.03ms, 10.1MB)
> 테스트 11 〉통과 (0.01ms, 10.2MB)
> 테스트 12 〉통과 (0.02ms, 10.1MB)
> 테스트 13 〉통과 (0.03ms, 9.96MB)
> 테스트 14 〉통과 (0.24ms, 10.2MB)
> 테스트 15 〉통과 (0.53ms, 10.3MB)
> 테스트 16 〉통과 (0.93ms, 10.1MB)
> 테스트 17 〉통과 (1.56ms, 10.2MB)
> 테스트 18 〉통과 (0.01ms, 10.1MB)
> 테스트 19 〉통과 (0.03ms, 10.3MB)
> 테스트 20 〉통과 (0.03ms, 10.3MB)
> 테스트 21 〉통과 (0.19ms, 10.1MB)
> 테스트 22 〉통과 (0.53ms, 10.3MB)
> 테스트 23 〉통과 (0.91ms, 10.1MB)
> 테스트 24 〉통과 (1.58ms, 10.3MB)
> 테스트 25 〉통과 (0.01ms, 10.3MB)
> 테스트 1 〉실패 (시간 초과)
> 테스트 2 〉실패 (시간 초과)
> 테스트 3 〉실패 (시간 초과)
> 테스트 4 〉실패 (시간 초과)
> 테스트 5 〉실패 (시간 초과)
> 테스트 6 〉
> 테스트 7 〉실패 (시간 초과)
> 테스트 8 〉실패 (시간 초과)
> 테스트 9 〉실패 (시간 초과)
> 테스트 10 〉실패 (시간 초과)
> 테스트 11 〉실패 (시간 초과)
> 테스트 12 〉실패 (시간 초과)
> 테스트 13 〉실패 (시간 초과)
> 테스트 14 〉실패 (시간 초과)
> ```

```python
def solution(stones, k):
    minV = 2000000000
    
    for i in range(len(stones)-k+1):
        if max(stones[i:i+k]) < minV:
            minV = max(stones[i:i+k])
            
    return minV
```

> 슬슬 완전탐색으로는 문제가 하나도 안풀리는거같다
>
> [이진 탐색](https://whwl.tistory.com/269) 
>
> 위에 내풀이는 리스트 한번만 돌면되고 이진 탐색은 mid계속 바꿔가면서 순회하는데 왜 내 풀이 효율성이 더 안좋은지 모르겠다. 
>
> ```
> 테스트 1 〉통과 (0.01ms, 10.3MB)
> 테스트 2 〉통과 (0.01ms, 10.1MB)
> 테스트 3 〉통과 (0.04ms, 10.3MB)
> 테스트 4 〉통과 (0.04ms, 10MB)
> 테스트 5 〉통과 (0.03ms, 10MB)
> 테스트 6 〉통과 (0.63ms, 10.1MB)
> 테스트 7 〉통과 (0.50ms, 10.3MB)
> 테스트 8 〉통과 (0.66ms, 10.3MB)
> 테스트 9 〉통과 (1.19ms, 10.1MB)
> 테스트 10 〉통과 (0.02ms, 10.3MB)
> 테스트 11 〉통과 (0.02ms, 10.3MB)
> 테스트 12 〉통과 (0.03ms, 10.1MB)
> 테스트 13 〉통과 (0.04ms, 10.1MB)
> 테스트 14 〉통과 (0.33ms, 10.3MB)
> 테스트 15 〉통과 (0.50ms, 10.1MB)
> 테스트 16 〉통과 (0.41ms, 10.1MB)
> 테스트 17 〉통과 (0.67ms, 10.3MB)
> 테스트 18 〉통과 (0.02ms, 10.3MB)
> 테스트 19 〉통과 (0.03ms, 10.3MB)
> 테스트 20 〉통과 (0.06ms, 10.1MB)
> 테스트 21 〉통과 (0.30ms, 10.2MB)
> 테스트 22 〉통과 (0.56ms, 10MB)
> 테스트 23 〉통과 (0.49ms, 10.2MB)
> 테스트 24 〉통과 (1.35ms, 10.2MB)
> 테스트 25 〉통과 (0.03ms, 10.1MB)
> 테스트 1 〉통과 (236.66ms, 18.6MB)
> 테스트 2 〉통과 (320.14ms, 18.6MB)
> 테스트 3 〉통과 (384.57ms, 18.4MB)
> 테스트 4 〉통과 (161.11ms, 18.6MB)
> 테스트 5 〉통과 (206.12ms, 18.5MB)
> 테스트 6 〉통과 (194.81ms, 18.6MB)
> 테스트 7 〉통과 (369.26ms, 18.5MB)
> 테스트 8 〉통과 (408.27ms, 18.5MB)
> 테스트 9 〉통과 (361.63ms, 18.6MB)
> 테스트 10 〉통과 (413.99ms, 18.6MB)
> 테스트 11 〉통과 (384.24ms, 18.6MB)
> 테스트 12 〉통과 (363.22ms, 18.6MB)
> 테스트 13 〉통과 (242.25ms, 18.6MB)
> 테스트 14 〉통과 (216.54ms, 18.5MB)
> ```

```python
def solution(stones, k):
    start = 1
    end = 200000000
    mid = (start + end) // 2
    
    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        for stone in stones:
            if stone - mid <= 0:
                cnt += 1
                if cnt >= k:
                    end = mid - 1
                    break
            else:
                cnt = 0
        else:
            start = mid + 1
    return start   
```

<br>

### [1차] 추석 트래픽

> 어려운 문제가 아니었는데 괜히 쫄아서 구글링했다. level3와서는 왜 구글없이는 못풀지
>
> [참고](https://velog.io/@mrbartrns/%ED%8C%8C%EC%9D%B4%EC%8D%AC-1%EC%B0%A8%EC%B6%94%EC%84%9D-%ED%8A%B8%EB%9E%98%ED%94%BD-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%A0%88%EB%B2%A83)

```python
def get_time(time):
    hour, minute, sec = time.split(':')
    sec, mili = map(int, sec.split('.'))
    return (int(hour)*3600 + int(minute)*60 + sec)*1000 + mili
    
def start_time(time, duration):
    duration = int(float(duration[:-1])*1000)
    return get_time(time) - duration

def solution(lines):
    answer = 0
    ends = []
    starts =[]
    for line in lines:
        t = line.split()
        ends.append(get_time(t[1])) 
        starts.append(start_time(t[1], t[2]))
    
    for i in range(len(lines)):
        cnt = 1
        
        for j in range(i+1, len(lines)):
            if ends[i] > starts[j]-999:
                cnt += 1
                
        answer = max(cnt, answer)
        
    return answer
```

<br>

### [1차] 셔틀버스

> 생각보다 고려해야할 경우의 수가 많아서 문제풀면서 처음으로 직접 테스트케이스 추가하면서 디버깅했다.
>
> 추가한 TC
>
> ```
> 테스트 7
> 입력값 〉2, 10, 2, ["08:59", "08:59", "08:59", "09:00", "23:59"]
> 기댓값 〉"08:59"
> 실행 결과 〉테스트를 통과하였습니다.
> 테스트 8
> 입력값 〉1, 1, 1, ["09:00", "23:59"]
> 기댓값 〉"08:59"
> 실행 결과 〉테스트를 통과하였습니다.
> ```

```python
def get_time(t):
    q, r = divmod(t,60)  
    if q < 10:
        q = f'0{q}'
    else:
        q = str(q)
    if r < 10:
        r = f'0{r}'
    else:
        r = str(r)
    return f'{q}:{r}'
    
    
def solution(n, t, m, timetable):
    answer = ''
    cnt = 0
    timetable = sorted(list(map(lambda x: int(x.split(':')[0])*60 + int(x.split(':')[1]), timetable)))
    
    i = 0
    s = 540
    
    for j in range(n):
        res = m
        if j == n-1 and res == 1:
            return min(get_time(timetable[i]-1), get_time(s))
        for k in range(i, min(i+m,len(timetable))):
            if timetable[k] > s:
                i = k
                break
            res -= 1
            if j == n-1 and res == 1:
                if k+1 < len(timetable):
                    return min(get_time(timetable[k+1]-1),get_time(s))
                return get_time(s)  
        else:
            i = k+1
        s += t
    
    return get_time(s-t)                 
```

<br>

### 표 편집

> [Linked List](https://kjhoon0330.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%91%9C-%ED%8E%B8%EC%A7%91-Python)

```python
def solution(n,k,cmd):
    cur = k
    table = { i:[i-1,i+1] for i in range(n)}
    table[0] = [None, 1]
    table[n-1] = [n-2, None]
    
    answer = ['O'] * n
    stack = []
    for c in cmd:
        if c == 'C':
            answer[cur] = 'X'
            prev, nxt = table[cur]
            stack.append([prev,cur,nxt])
            if nxt == None:
                cur = table[cur][0]
            else:
                cur = table[cur][1]
            if prev == None:
                table[nxt][0] = None
            elif nxt == None:
                table[prev][1] = None
            else:
                table[prev][1] = nxt
                table[nxt][0] = prev
                
        elif c == 'Z':
            prev, now, nxt = stack.pop()
            answer[now] = 'O'
            if prev == None:
                table[nxt][0] = now
            elif nxt == None:
                table[prev][1] = now
            else:
                table[prev][1] = now
                table[nxt][0] = now
                
        else:
            c1, c2 = c.split()
            c2 = int(c2)
            if c1 == 'D':
                for _ in range(c2):
                    cur = table[cur][1]
            else:
                for _ in range(c2):
                    cur = table[cur][0]
 
    return ''.join(answer)
```

<br>

### 광고삽입

> 1차 시도, 시간초과

```python
def sec(time):
    hour, minute, sec = map(int,time.split(':'))
    return hour*3600+ minute*60 + sec

def clock(s):
    hour, r = divmod(s,3600)
    minute, sec = divmod(r,60)
    hour = f'0{hour}' if hour < 10 else str(hour)
    minute = f'0{minute}' if minute < 10 else str(minute)
    sec = f'0{sec}' if sec < 10 else str(sec)
    return f'{hour}:{minute}:{sec}'

def solution(play_time, adv_time, logs):
    answer = ''
    adv = sec(adv_time)
    play = sec(play_time)
    d = []
    for log in logs:
        start, end = map(lambda x : sec(x), log.split('-'))
        
        d.append([start, 1])
        d.append([end, -1])
    d=sorted(d)
    for i in range(len(d)):
        if i == 0:
            continue
        else:
            d[i][1] = d[i-1][1] + d[i][1]
    
    d = [[0,0]] + d
    # print(d)
    cumul = []
    s = 0
    for i in range(1,len(d)):
        s += (d[i][0]-d[i-1][0])*d[i-1][1]
        cumul.append(s)
    # print(cumul)
    max_p = 0
    max_t = 0
    for s in range(play-adv+1):
        e = s+adv
        for j in range(len(d)):
            if s < d[j][0]:
                ns = cumul[j-2] + (s-d[j-1][0])*d[j-1][1]
                break
        for j in range(len(d)):
            if e < d[j][0]:
                ne = cumul[j-2] + (e-d[j-1][0])*d[j-1][1]
                break
        else:
            ne = cumul[len(d)-2] + (e-d[len(d)-1][0])*d[len(d)-1][1]
                
        if max_p < ne-ns:
            max_p = ne-ns
            max_t = s
        
    return clock(max_t)
```

> [+1-1](https://dev-note-97.tistory.com/156)

```python
def sec(time):
    hour, minute, sec = map(int,time.split(':'))
    
    return hour*3600+ minute*60 + sec

def clock(s):
    hour, r = divmod(s,3600)
    minute, sec = divmod(r,60)
    hour = f'0{hour}' if hour < 10 else str(hour)
    minute = f'0{minute}' if minute < 10 else str(minute)
    sec = f'0{sec}' if sec < 10 else str(sec)
    return f'{hour}:{minute}:{sec}'

def solution(play_time, adv_time, logs):
    answer = ''
    adv = sec(adv_time)
    play = sec(play_time)
    times = [0 for _ in range(play+1)]
    for log in logs:
        start, end = map(lambda x : sec(x), log.split('-'))
        times[start] += 1
        times[end] -= 1
    
    # 초당 시청자수 누적합(두번해야지 누적합이 구해짐)
    for i in range(1, len(times)):
        times[i] = times[i] + times[i-1]
    for i in range(1, len(times)):
        times[i] = times[i] + times[i-1]
    
    max_t = 0
    max_p = 0
    for i in range(adv-1, len(times)):
        if i >= adv:
            if max_p < times[i] - times[i-adv]:
                max_p = times[i] - times[i-adv]
                max_t = i-adv+1
        else:
            if max_p < times[i] :
                max_p = times[i] 
                max_t = i-adv+1
        
    return clock(max_t)
```



<br>

### 매칭점수

> 1차 시도

```python
def solution(word, pages):
    urls = []
    for page in pages:
        url = ''
        for i in range(len(page)):
            if page[i:i+8] == 'content=':
                j = i+8
                while page[j] != '>':
                    url += page[j]
                    j += 1
                urls.append(url[:-1])
                break
 
    bases = []
    links = []
    for page in pages:
        page = page.lower()
        word = word.lower()
        cnt = 0
        for i in range(len(page)):
            if page[i:i+len(word)] == word and not page[i-1].isalpha() and not page[i+len(word)].isalpha():
                cnt += 1
        bases.append(cnt)    
        links.append(page.count('</a>'))
        
    scores = [x for x in bases]  
    for j in range(len(pages)):  
        for i in range(len(urls)):
            if i != j and urls[i] in pages[j]:
                scores[i] += bases[j] / links[j]
                
    idx = -1
    maxV = 0
    for k in range(len(scores)):
        if scores[k] > maxV:
            maxV = scores[k]
            idx = k
            
    return idx
```

