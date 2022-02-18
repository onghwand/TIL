## string 문제풀이

출처 : https://swexpertacademy.com/main/main.do

> 3일차 - 회문2

```python
for tc in range(1,11):
    tc = input()
    arr = [list(input()) for _ in range(100)]
 
    maxV = 1
 
    # 행
    for i in range(100): # 행위치
        for L in range(100, maxV, -1): #회문의 길이
            for j in range(101-L):
                lst = arr[i][j:j+L]
                if lst == lst[::-1]:
                    maxV = L
                    break
            if L < maxV:
                break
 
    # 열
    arr = list(map(list,zip(*arr))) # transpose
    for i in range(100):  # 행위치
        for L in range(100, maxV, -1):  # 회문의 길이
            for j in range(101 - L):
                lst = arr[i][j:j + L]
                if lst == lst[::-1]:
                    maxV = L
                    break
            if L < maxV:
                break
    print(f'#{tc} {maxV}')
```

> 쇠막대기 자르기

```python
T = int(input())
for tc in range(1, T+1):
    lst = input()
    sol = cnt = 0
    for i in range(len(lst)):
        if lst[i] == '(':
            cnt += 1
        else:
            if lst[i-1] == '(':
                cnt -= 1
                sol += cnt
            else:
                cnt -= 1
                sol += 1
    print(f'#{tc} {sol}')
```

> 의석이의 세로로 말해요

```python
T = int(input())
for tc in range(1, T+1):
    arr = [['']*15 for _ in range(5)]
 
    for i in range(5):
        lst = input()
        L = len(lst)
        for j in range(L):
            arr[i][j] = lst[j]
 
    print(f'#{tc}', end=' ')
    for i in range(15):
        for j in range(5):
            print(arr[j][i], end='')
    print()
```

> 자기 방으로 돌아가기

```python
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [0]*200 #두개씩 마주보고 있으므로 통로가 200개의 칸
 
    # 통로 칸마다 겹치는 횟수 세기
    for i in range(N):
        A, B = map(int, input().split())
        if A < B:
            for n in range(A, B+1):
                if n % 2 == 0:
                    arr[int(n//2 - 1)] += 1
            if B % 2: # B가 홀수면
                arr[int(B//2)] += 1
        else:
            for n in range(B, A+1):
                if n % 2 == 0:
                    arr[int(n // 2 - 1)] += 1
            if A % 2:  # A가 홀수면
                arr[int(A // 2)] += 1
 
    print(f'#{tc} {max(arr)}')
```

