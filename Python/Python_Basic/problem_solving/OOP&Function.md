## Python 문제풀이

> `__str__`과 `__repr__` => 뚜렷한 용도의 차이는 잘 모르겠음

- `__str__` : 사용자 입장에서 보기 쉬운,  간소화된 호출 (informal)
- `__repr__` : 시스템이 인식하는대로, 객체의 모습 그대로를 호출 (official)

```python
# __str__과 __repr__ 동시에 존재한다면 __str__로 호출됨
a = 'hello'

print(repr(a)) # 'hello'
print(str(a)) # hello
```



> Faker()

- 가상의 데이터를 만들어주는 패키지

``` python
from faker import Faker
fake = Faker()
fake.name()
# => 'Mark Owen'
fake_ko=Faker('ko_KR')
fake_ko.name()
# => '손상철'
```



> ERROR

- ZeroDivisionError : 0으로 나누려고 할 때
- NameError : 변수명이 없을 때
- TypeError : 연산이나 함수가 부적절한 형의 객체에 적용될 때
- IndexError : 설정한 범위 밖의 인덱스가 사용되었을 때
- KeyError : 딕셔너리에서 없는 Key에 접근하려고 할 때
- ModuleNotFoundError : 모듈을 찾을 수 없을 때
- ImportError : 임포트 하려는 이름을 찾을 수 없을 때



> Animal, Bird, Dog

- Bird와 Dog는 Animal의 상속을 받는 class

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def walk(self):
        print(f'{self.name}! 걷는다!')
    def eat(self):
        print(f'{self.name}! 먹는다!')
        
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def walk(self):
        print(f'{self.name}! 달린다!')
        
    def bark(self):
        print(f'{self.name}! 짖는다!')
        
class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def fly(self):
        print(f'{self.name}! 푸드덕!')  
        
dog = Dog('멍멍이')
dog.walk() # 멍멍이! 달린다!
dog.bark() # 멍멍이! 짖는다!

bird = Bird('구구')
bird.walk() # 구구! 걷는다!
bird.eat() # 구구! 먹는다!
bird.fly() # 구구! 푸드덕!
```



> Point & Rectangle

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def get_area(self):
        return abs(self.p1.x - self.p2.x) * abs(self.p1.y - self.p2.y)
    
    def get_perimeter(self):
        return 2 * (abs(self.p1.x- self.p2.x) + abs(self.p1.y - self.p2.y))
    
    def is_square(self):
        return abs(self.p1.x - self.p2.x) == abs(self.p1.y - self.p2.y)
    
p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area()) # 4
print(r1.get_perimeter()) # 8
print(r1.is_square()) # True

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area()) # 9
print(r2.get_perimeter()) # 12
print(r2.is_square()) # True
```



> 딕셔너리 뒤집기

```python
# version1
def dict_invert(my_dict):
    # 새로 만들 빈 딕셔너리 
    inverted = {}
    # 중복을 없앤 value들을 key로 전환 후, value를 담을 빈 list 생성
    for value in set(my_dict.values()):
        inverted[value] = []
        # 입력 딕셔너리를 순회하며 value가 일치하면 key를 담는다
        for key in my_dict.keys():
            if my_dict[key] == value:
                inverted[value].append(key)
    return inverted

# version2
def dict_invert(my_dict):
    inverted = {}
    for key, value in my_dict.items():
        inverted[value] = inverted.get(value, []) + [key]
    return inverted

print(dict_invert({1: 10, 2: 20, 3: 30})) # {10: [1], 20: [2], 30: [3]}
print(dict_invert({1: 10, 2: 20, 3: 30, 4: 30})) # {10: [1], 20: [2], 30: [3, 4]}
print(dict_invert({1: True, 2: True, 3: True})) # {True: [1, 2, 3]}
```

