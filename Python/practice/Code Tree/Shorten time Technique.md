## Preprocessing

> 괄호 쌍 만들어주기

```python
arr = list(input())
right = [0]*len(arr)

cnt = 0
for i in range(len(arr)-2, -1, -1):
    if arr[i] == ')' and arr[i+1] == ')':
        cnt += 1
    right[i] = cnt

answer = 0
for i in range(1, len(arr)):
    if arr[i-1] == '(' and arr[i] == '(':
        answer += right[i+1]
print(answer)
```

## Two Pointer

> 가장 짧은 부분합

```python
n, s = map(int, input().split())
arr = [0] + list(map(int, input().split()))
j = 0
sumV = 0
ans = n
for i in range(1,n+1):
    while  j+1 <= n and sumV < s :
        sumV += arr[j+1]
        j += 1
    if sumV < s:
        break
    ans = min(ans, j-i+1)
    sumV -= arr[i]
print(ans) if ans != n else print(-1)
```

