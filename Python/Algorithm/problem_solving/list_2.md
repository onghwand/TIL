## list_2 문제풀이

- 출처 : https://swexpertacademy.com/main/main.do

### List2_연습2

```python
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    n = len(arr) # 배열 길이
    
    for i in range(1, 1<<n): # 공집합을 제외한 부분 집합의 개수만큼
        total = 0 # 부분집합의 합
        for j in range(n): # 원소의 수만큼 비트를 비교함
            if i & (1<<j): # i의 j번 비트가 1인 경우
                total += arr[j]

        if total == 0:
            print(f'#{tc} 1')
            break
            
    else: # 다 돌았는데 없으면
        print(f'#{tc} 0')
```

### List2_연습1

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input()) #행렬 크기
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 좌 우 상 하
    di = [0,0,-1,1]
    dj = [-1,1,0,0]

    total = 0 # 전체 합
    for i in range(N):
        for j in range(N):
            subtotal = 0 # (i,j) 주변 요소와 차이들의 절댓값 합
            for k in range(4):
                if 0 <= i+di[k] < N and 0 <= j+dj[k] < N:
                    diff = arr[i + di[k]][j + dj[k]] - arr[i][j] #인접한 요소와 차이
                    if diff < 0:
                        subtotal -= diff
                    else:
                        subtotal += diff

            total += subtotal

    print(f'#{tc} {total}')
```

### 달팽이 숫자

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 행렬 크기
    arr =[[0]*N for _ in range(N)]
    
    # 우 하 좌 상 => 달팽이 방향
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    mode = 0 # 방향 전환 인덱스
    i = j = 0 # 초기 위치

    arr[0][0] = 1
    for n in range(2, N*N+1):
        i += di[mode]
        j += dj[mode]
        arr[i][j] = n
        
        # 행렬 안에 위치하고 아직 할당된 값이 없으면
        if 0 <= i+di[mode] < N and 0 <= j+dj[mode] < N and not arr[i+di[mode]][j+dj[mode]]:
            continue

        if mode != 3:
            mode += 1
        else:
            mode = 0

    print(f'#{tc}')
    for row in arr:
        print(*row)
```

### [S/W 문제해결 기본] 2일차 - Sum

```python
for tc in range(1, 11):
    tc = int(input()) # tc번호
    N = 100
    arr = [0]*N
    for row in range(N):
        arr[row] = list(map(int, input().split()))

    maxV = 0

    # 행, 열 순회하며 max 갱신
    for i in range(N):
        row = 0 # 각 행 합
        col = 0 # 각 열 합
        for j in range(N):
            row += arr[i][j]
            col += arr[j][i]
        if row > maxV and row > col:
            maxV = row
        elif col > maxV and col > row:
            maxV =col

    # 대각선 2개 확인
    up = 0 # 우상향 대각선 합
    down = 0 # 우하향 대각선 합
    for k in range(N):
        up += arr[k][N-1-k]
        down += arr[k][k]
    if up > maxV and up > down:
        maxV = up
    elif down > maxV and down > up:
        maxV = down

    print(f'#{tc} {maxV}')
```

### [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬

```python
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    ai = list(map(int, input().split()))

    arr = [] # 정렬된 배열

    for i in range(5):
        max_idx = 0
        min_idx = 0
        for j in range(len(ai)):
            if ai[max_idx] < ai[j]:
                max_idx = j
        maxV = ai.pop(max_idx)
        for k in range(len(ai)):
            if ai[min_idx] > ai[k]:
                min_idx = k
        minV = ai.pop(min_idx)
        arr.append(maxV)
        arr.append(minV)
    print(f'#{tc}', *arr)
```

### 이진탐색

```python
T = int(input())
for tc in range(1, T+1):
    l = 1 # 시작 위치
    r, A, B = map(int, input().split())
    lA = lB = l
    rA = rB = r
    while True:
        cA = int((lA+rA)/2) # A의 중간
        cB = int((lB+rB)/2) # B의 중간
        if cA == A and cB != B: # A가 이김
            print(f'#{tc} A')
            break
        elif cA != A and cB == B : # B가 이김
            print(f'#{tc} B')
            break
        elif cA == A and cB == B: # 비김
            print(f'#{tc} 0')
            break
        else: # 중간 페이지와 찾는 쪽 관계에 따라 l,r 조정
            if A > cA and B > cB:
                lA = cA
                lB = cB
            elif A > cA and B < cB:
                lA = cA
                rB = cB
            elif A < cA and B > cB:
                rA = cA
                lB = cB
            else:
                rA = cA
                rB = cB 
```

### [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합

```python
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) # 부분집합의 원소 수 N, 합 K
    A = [1,2,3,4,5,6,7,8,9,10,11,12] # 집합A
    n = len(A) # 12
    cnt = 0 # 문제 조건을 만족하는 부분집합의 개수
    
    for i in range(1<<n):
        total = 0 # 부분집합의 합
        elements = 0 # 부분집합 원소 개수
        for j in range(n):
            if i & (1<<j):
                total += A[j]
                elements += 1
        if total == K and elements == N: # 합과 원소개수가 동시에 만족하면
            cnt +=1
            
    print(f'#{tc} {cnt}')
```

### 색칠하기

```python
T= int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [['']*10 for _ in range(10)] # 10*10 행렬
    cnt = 0 #보라색 칸 개수

    colors = [0]*N # 색칠 정보
    for i in range(N):
        colors[i] = list(map(int, input().split()))

    # 행렬에 사각형 영역만큼 색상을 문자열로 이어붙임. '1211' 이런식 => 1과 2가 들어가있기만 하면 보라색
    for color in colors:
        a = min(color[0], color[2]) # 가로 시작
        b = max(color[0], color[2]) # 가로 끝
        c = min(color[1], color[3]) # 세로 시작
        d = max(color[1], color[3]) # 세로 끝
        for i in range(a, b+1): # 사각형 가로
            for j in range(c, d+1): # 사각형 세로
                arr[i][j] += str(color[4])

    # 보라색 칸 개수 세기
    for i in range(10):
        for j in range(10):
            if '1' in arr[i][j] and '2' in arr[i][j]:
                cnt += 1

    print(f'#{tc} {cnt}')
```

