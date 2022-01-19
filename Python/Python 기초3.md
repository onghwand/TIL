# Python 기초3

## 함수

- 함수(Function)과 메소드(Method) 차이
  - 둘 다 함수이지만 메소드는 Class내에서 정의된 함수로 Class에서 생성된 객체에 종속적이다. 즉 다른 클래스(상속 제외)에서 만들어진 객체에 쓸 수 없다. 반면 함수(Function)은 객체로부터 독립적이다



- Keyword Arguments, Positional Arguments
  - Keyword Arguments : 순서 대신에 parameter 이름으로 값을 전달
  - Positional Arguments : 함수에서 정의한 위치대로 대입하는 parameter(순서를 지켜줘야함)
    - 두 가지를 혼용해서 함수 정의할 때, 무조건 Positional Arguments가 앞에 위치해야함

```python
def add(x, y):
    return x + y

# Keyword Arguments
print(add(y=2, x=1)) #parameter 이름으로 값을 전달하기 때문에 parameter 순서 상관없음

# Positional Arguments
print(add(1, 2)) #함수에서 정의된 인자 순서대로 x=1, y=2 정해짐

# 함수 정의 시 Keyword Arguments 보다 Positional Arguments가 앞에 위치
#1 틀림 (SyntaxError: non-default argument follows default argument)
def add(x=1, y):
    return x + y
#2 맞음
def add(x, y=2):
    return x + y

print(add(0)) # 이 때 1번과 같은 경우에는 x=0인지 y=0인지 알 수 없음
```



- 함수 내에서 print와 return
  - print : return 값이 없으므로 출력하면 None이 출력됨
  - return :  return값이 있으므로 출력하면 함수에서 연산된 값이 출력됨

```python
# print (void - 리턴 값이 없음)
def add1(x, y):
    print(x + y)
# return
def add2(x, y):
    return x + y

print(add1(1, 2))
>>>3
>>>None

print(add2(1, 2))
>>>3
```



- *args (arguments, tuple) 와 **kwargs (keyword arguments, dictionary)

```python
def add(*args):
    total = 0
    for i in args:
        total += i
    return total

add(1,2,3,4,5)
>>>15

def name_age(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

# key = value 형태로 입력하면 {key : value} 딕셔너리 형태로 보내짐
name_age(홍길동 = 22, 이순신 = 18)
>>>홍길동 22
   이순신 18
```



- mutable 과 immutable 의 구분 기준은 id

```python
# append와 같은 작업을 했는데 id가 변했다 -> immutable = 변화가 일어나면 id 바뀜(새로운 객체 생성)
a = '123'
print(f'a:{a}, id:{id(a)}')
a += '12'
print(f'a:{a}, id:{id(a)}')

>>> a:123, id:1676231332912
    a:12312, id:1676264196208


# append와 같은 작업을 했는데 id가 변하지 않았다 -> mutable = id를 유지하면서 변화가 일어남
b={1.2}
print(b, id(b))
b.add(3)
print(b, id(b))

>>> b:{1, 2}, id:1676263832928
    b:{1, 2, 3}, id:1676263832928
            
# 주의 - 튜플 자체는 immutable이지만 튜플 안에 리스트가 있다면 리스트에 대해서는 가능 
t = ('hi', [1,2,3])
print(f't:{t}, id:{id(t)}')
t[1][0] = 2
print(f't:{t}, id:{id(t)}')

>>> t:('hi', [1, 2, 3]), id:1676264561152
	t:('hi', [2, 2, 3]), id:1676264561152
```



####  Q. O(2n) 과 O(n)은 lim을 취했을 때 분명히 2배만큼 차이가 나는데 왜 둘 다 O(n)인가 

