### 최소 스패닝 트리

```python
def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

def union(a,b):
    parent[find(b)] = find(a)


v,e = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(e)]
graph.sort(key=lambda x:x[2])

parent = [x for x in range(v+1)]
total = 0
for a,b,c in graph:
    if find(a) != find(b):
        union(a,b)
        total += c

print(total)
```

