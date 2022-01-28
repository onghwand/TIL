# 파이썬 기초

## 1. 변수

> type()

변수에 할당된 값의 타입

```python
x = 'apple'
type(x)
# str
```

> id()

변수에 할당된 값의 고유한 메모리주소

```python
id(x)
# 4645387184
```

> 식별자

파이썬 객체를 식별하는데 사용하는 이름(변수 이름)

- 예약어는 사용할 수 없음 

```python
# 예약어 보는 법
import keyword
print(keyword.kwlist)
# ['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

## 2. 자료형

- Boolean/Numeric(int, float, complex)/String/None

### Boolean

```python
# False <- 0 , (), [], {}, None 등
# True <- False로 취급되는 것 이외 나머지
bool([]) # False
```

### Numeric

``` python
3.14 - 3.02 == 0.12
-> 0.12000000000001
-> False

# 같은지 판단하기 위해서는
# 1.
abs(a - b) <= 1e-10
# 2.
import math
math.isclose(a, b)
```

### String

- 문자열은 immutable

```python
a = 'apple'
a[-1] = 'd'
# TypeError: 'str' object does not support item assignment
```

- Escape sequence
  -  \n 줄바꿈, \t 탭 

- string interpolation

```python
name = 'kim'
height = 175
print(f'Hello, {name}! 키는 {height}')
# Hello, kim! 키는 175
```

## 3. 연산자 

### 3-1. 논리연산자

```python
print(2 or 3)
#처음에 True인게 확정이므로 값은 2
print(2 and 3)
#끝까지 가야 참/거짓 판별이 가능하므로 값은 3
```

### 3-2. 슬라이싱

```python
# -1 이 마지막 인덱스
word = 'abcdefghi'
word[2:5] # 2번째부터 4번째
# 'cde'
word[-6:-2] # -6번째부터 -3번째
# 'defg'
```



## 4. 프로그램 구성 단위

- 함수 -> 모듈 -> 패키지 ->라이브러리



## 5. 조건표현식

- 조건문을 한줄로 표현

```python
i=1
print(i if i%2 == 0 else i-1)
# 0
```



### 6. 반복문

- 딕셔너리 순회

```python
grades = {'a': 80, 'b': 70}
print(grades.keys())
print(grades.values())
print(grades.items())

'''
dict_keys(['a', 'b'])
dict_values([80, 70])
dict_items([('a', 80), ('b', 70)])
'''
```

- enumerate(iterable, start=0)  => 인덱스를 부여함

```python
alphabet = ['a', 'b', 'c']
list(enumerate(alphabet))
# [(0, 'a'), (1, 'b'), (2, 'c')]
```

- List/Dictionary Comprehension

```python
[num**2 for num in range(1,4)]
# [1, 4, 9]

{num:num**2 for num in range(1,4)}
# {1: 1, 2: 4, 3: 9}
```



## 7. 반복문 제어

- continue => continue 이후의 코드는 수행하지 않고 다음 반복 수행
- for-else => 끝까지 반복문을 실행한 이후 else문 실행
  - break를 통해 중간에 종료되는 경우 else 문은 실행되지 않음

















