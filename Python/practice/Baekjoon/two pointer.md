### 1644. 소수의 연속합

```python
arr = [True for x in range(4000000)]
arr[0] = False
arr[1] = False

for i in range(2,4000000):
    if arr[i]:
        j = 2
        while i*j < 4000000:
            arr[i*j] = False
            j += 1

primes = []
for i in range(2,4000000):
    if arr[i]:
        primes.append(i)

N = int(input())
count = start = end = 0

while start <= end and end <= len(primes):
    total = sum(primes[start:end])
    if total == N:
        count += 1
        end += 1
    elif total < N:
        end += 1
    else:
        start += 1

print(count)
```

