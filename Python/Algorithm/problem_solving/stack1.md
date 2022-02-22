## 4873. 반복문자 지우기

```python
T = int(input())
for tc in range(1, T+1):
    S = input()
    stack = []
    cnt = 0

    for s in S:
        if cnt != 0 and stack[-1] == s:
            stack.pop()
            cnt -= 1
        else:
            stack.append(s)
            cnt += 1

    print(f'#{tc} {cnt}')
```

## 4866. 괄호검사

```python
T = int(input())
for tc in range(1, T+1):
    S = input()
    stack = [0]*1000
    L = -1
    ans = 1
    for s in S:
        if s == '(' or s == '{':
            L += 1
            stack[L] = s
        elif s == ')' :
            if stack[L] == '(':
                L -= 1
            elif stack[L] != '(' or L == -1:
                ans = 0
                break
        elif s == '}' :
            if stack[L] == '{':
                L -= 1
            elif stack[L] != '{' or L == -1:
                ans = 0
                break
    if L != -1:
        ans = 0

    print(f'#{tc} {ans}')


```

## 4869. 종이붙이기

```python
def f(n):
    arr = [0]*1000
    if n == 0:
        return 1
    for i in range(1, n+1):
        if i == 1:
            arr[i-1] = 1
        else:
            arr[i-1] = i * arr[i-2]
    return arr[n-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())//10
    end = N//2
    cnt = 0
    '''
    ex) 50 = 20 20 10/ 20 10 10 10 / 10 10 10 10 10
           => 3C1*2^2 + 4C1*2^1+ 5C0*2^0 
           = 12 + 8 + 1
           = 21 
    '''
    for i in range(end+1):
        cnt += f(N-i) / (f(N-2*i)*f(i)) * (2**(i))

    print(f'#{tc} {int(cnt)}')
```

