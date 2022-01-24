## Python 기초6

### 여러가지 메소드

> find()

- 첫 번재 위치를 반환. 없으면, -1을 반환

```python
'banana'.find('a')
>>> 1
'banana'.fing('c')
>>> -1
```

> strip([chars])

- 문자, 공백 제거

```python
'  abc d  '.strip()
>>> 'abc d'
'  abc d  '.lstrip() #왼쪽만 제거
>>>'abc d  ' 
'  abc d  '.rstrip() #오른쪽만 제거
>>>'  abc d'
'abc da'.strip('a')
>>>'bc d'
```

> remove() , pop()

- remove() => 가장 왼쪽의 첫번째 항목 제거
- pop() => 가장 오른쪽의 항목 반환 후 제거

```python
# remove()
a = [1,2,3,4,1]
print(a.remove(1))
print(a)
>>> None
[2, 3, 4, 1]

# pop()
a = [1,2,3,4]
print(a.pop())
print(a)
>>> 4
[1, 2, 3]
```



### Shallow Copy & Deep Copy

```python
# Shallow Copy, 같은 객체를 참조함
original = [1, 2, 3]
copy = original
copy[0] = 'hi'
print(original, copy)
>>> ['hi', 2, 3] ['hi', 2, 3]

# Deep Copy, 다른 객체를 참조함
import copy
original = [1, 2, 3]
copy = copy.deepcopy(original)
copy[0] = 'hi'
print(original, copy)
>>> [1, 2, 3] ['hi', 2, 3]
```

