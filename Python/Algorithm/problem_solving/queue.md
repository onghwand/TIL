## 1226. 미로1

```python
def bfs(sti,stj):
    queue = []
    queue.append((sti,stj))
    v[sti][stj] = 1
    while queue :
        i, j = queue.pop(0)
        if arr[i][j] == '3':
            return 1
        else:
            for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
                ni, nj = i+di, j+dj
                if arr[ni][nj] in '03' and v[ni][nj] == 0:
                    queue.append((ni,nj))
                    v[ni][nj] = 1
    return 0
for _ in range(10):
    tc = int(input())
    arr = [input() for _ in range(16)]

    sti, stj = 1, 1
    v = [[0]*16 for _ in range(16)]
    ans = bfs(sti,stj)

    print(f'#{tc} {ans}')
```

## 1225. 암호 생성기

```python
for tc in range(1,11):
    a=input()
    queue = list(map(int,input().split()))
    i=0
    arr=[1,2,3,4,5]
    while True:
        p = queue.pop(0)
        if p == 1 or p-arr[i%5] <= 0:
            queue.append(0)
            break
        queue.append(p-arr[i%5])
        i += 1

    print(f'#{tc}', *queue)
```

