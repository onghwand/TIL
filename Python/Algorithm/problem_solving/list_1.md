## List_1 문제풀이

- 출처 : https://swexpertacademy.com/main/main.do

### 삼성시의 버스 노선

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus = [0] * 5000 # 버스 노선

    # 버스 수 할당
    for i in range(N):
        A, B =map(int,input().split())
        for j in range(A-1, B):
            bus[j] += 1

    # 노선 순서대로 담기
    P = int(input())
    answer = []
    for i in range(P):
        c = int(input())
        answer.append(bus[c-1])

    print(f'#{tc}',*answer)

```



### 현주의 상자 바꾸기

```python
T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    boxes = [0] * N
    
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            boxes[j] = i
            
    print(f'#{tc}', *boxes)
```



### 간단한 소인수분해

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prime = {2: 0,
             3: 0,
             5: 0,
             7: 0,
             11: 0,
             }

    for key in prime.keys():
        while N % key == 0:
            prime[key] += 1
            N /= key

    print(f'#{tc}', end=' ')
    print(*list(prime.values()))
```



### 숫자카드

```python
T = int(input())
for tc in range(1, T+1):
    N = input()
    ai = list(map(int, input()))
    cnts = [0] * 10 # 0-9 각각의 개수

    for i in range(len(ai)):
        cnts[ai[i]] += 1

    maxV = 0 # 가장 많은 카드의 숫자
    cnt = cnts[maxV] # 가장 많은 숫자의 장 수
    for i in range(1, 10):
        if cnt <= cnts[i]:
            maxV = i
            cnt = cnts[i]

    print(f'#{tc} {maxV} {cnt}')
```



### 구간합

```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))

    # 초기값 설정
    minV = maxV = 0
    for i in range(M):
        minV += ai[i]
        maxV += ai[i]

    # min max 갱신
    for i in range(1, N-M+1):
        subtotal = 0 # M개씩 끊어서 합
        for j in range(M):
            subtotal += ai[i+j]

        if minV > subtotal:
            minV = subtotal
        if maxV < subtotal:
            maxV = subtotal

    print(f'#{tc} {maxV-minV}')

```



### 전기버스

```python
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    number = list(map(int, input().split()))
    charge = [0] * (N+1) # 충전소 위치 있으면 1 없으면 0
    diff = [] # 충전소 사이 거리 리스트

    diff.append(number[0] - 0) # 첫 충전소까지 거리
    for i in range(M-1):
        diff.append(number[i+1] - number[i])
    diff.append(N - number[M-1]) # 마지막 충전소부터 목표지점까지 거리

    # 주유소 위치 1로 표시한 리스트 charge
    for num in number:
        charge[num] += 1

    cnt = 0 # 충전수
    i = 0 # 갱신할 위치
    while True:
        i += K # 보폭만큼 가면서
        if i >= N: # 목표지점 넘어가면 break
            break

        if charge[i] == 1: # 보폭만큼 갔는데 충전소 있으면 충전
            cnt += 1
            #print(i)

        else: #보폭만큼 갔는데 충전소 없으면
            for j in range(i, i-K, -1): # 뒤로 돌아가면서 충전소 찾고 위치 갱신
                if charge[j] == 1:
                    i = j
                    cnt += 1
                    break

    for dif in diff: # 만약에 충전소 사이 거리가 보폭보다 큰 게 있다면 무효 cnt=0
        if dif > K:
            cnt = 0
            break

    print(f'#{tc} {cnt}')
```