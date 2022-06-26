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

