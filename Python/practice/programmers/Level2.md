## Level2

> 행렬 테두리 회전하기

```python
from copy import deepcopy
def rotate(ax,ay,bx,by,arr):
    minV = len(arr)*len(arr[0])
    tmp = arr[ax][ay]
    minV = min(minV,tmp)
    for i in range(ax,bx):
        test = arr[i+1][ay]
        arr[i][ay]= test
        minV = min(minV,test)
    for i in range(ay,by):
        test = arr[bx][i+1]
        arr[bx][i] = test
        minV = min(minV,test)
    for i in range(bx,ax,-1):
        test=arr[i-1][by]
        arr[i][by]=test
        minV = min(minV,test)
    for i in range(by,ay,-1):
        test = arr[ax][i-1]
        arr[ax][i] = test
        minV = min(minV,test)
    arr[ax][ay+1] = tmp
        
    return arr, minV
    
def solution(rows, columns, queries):
    answer = []
    arr = [[y*columns+x for x in range(1,columns+1)] for y in range(rows)]

    for a,b,c,d in queries:
        arr, minV = rotate(a-1,b-1,c-1,d-1,arr)
        answer.append(minV)
    
    return answer
```

