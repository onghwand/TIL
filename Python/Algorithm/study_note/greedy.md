## 완전검색 & 그리디

### 1. 반복 또는 재귀

- 재귀는 문제해결을 위한 알고리즘 설계가 간단하고 자연스럽다
- 일반적으로 재귀는 반복보다 더 많은 메모리와 연산을 필요로한다
- 입력 값이 커질수록 재귀는 반복에 비해 비효율적일 가능성이 높다

> 완전 검색
>
> 많은 종류의 문제들이 특정 조건을 만족하는 경우나 요소를 찾는 것
>
> 완전 검색은 조합적 문제에 대한 brute-force 방법이다

### 2. 순열

> 사용한 숫자들을 지우면서 새로운 순열을 만드는 방법

```python
def p(i,N):
    if i == N:
        print(b)
    else:
        for j in range(N):
            if not used[j]:
                used[j]=1
                b[i] = a[j]
                p(i+1,N)
                used[j]=0

a=[1,2,3]
used=[0]*3
b=[0]*3
p(0,3)

'''
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
'''
```

> 주어진 숫자들 중에서 정해진 개수의 순열

```python
def p(i,N,m):
    if i == N:
        print(b)
    else:
        for j in range(m):
            if not used[j]:
                used[j]=1
                b[i] = a[j]
                p(i+1,N,m)
                used[j]=0

a=[1,2,3,4,5]
used=[0]*5
b=[0]*3
p(0,3,5) # 5개의 주어진 숫자중 3개만 이용한 순열 
```

> 조합

```python
N=5
for i in range(1,N-1):
    for j in range(i+1,N):
        for k in range(j+1,N+1):
            print(i,j,k)
'''
1 2 3
1 2 4
1 2 5
1 3 4
1 3 5
1 4 5
2 3 4
2 3 5
2 4 5
3 4 5
'''

def ncr(n,r,s):
    if r==0:
        print(comb)
    else:
        for i in range(s, n-r+1):
            comb[3-r] = A[i]
            ncr(n,r-1,i+1)
n=5
r=3
comb=[0]*3
A=[1,2,3,4,5]
ncr(n,r,0)
'''
[1, 2, 3]
[1, 2, 4]
[1, 2, 5]
[1, 3, 4]
[1, 3, 5]
[1, 4, 5]
[2, 3, 4]
[2, 3, 5]
[2, 4, 5]
[3, 4, 5]
'''


```

