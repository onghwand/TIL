## OOP

> 절차 지향 vs 객체 지향

- 절차지향 (Procedural Oriented Programming)	
  - 순차적인 실행에 초점
  - 데이터를 중심으로 함수 구현
- 객체지향 (Object Oriented Programming)
  - 객체간의 관계/조직에 초점
  - 기능을 중심으로 메서드 구현



> 클래스/인스턴스/속성/메소드

- 클래스 : 특정 객체를 생성하기 위해 변수와 메소드를 정의하는 일종의 틀
- 인스턴스(객체) : 클래스로부터 만들어진 각각의 사물 또는 개념, 실제로 존재하는 것
- 속성 : 특성(사람 클래스 - 이름, 나이), 상태
- 메소드 : 객체에 대한 기능, 행동, 동사



> 인스턴스 메소드

- 첫번째 인자로 인스턴스 자기자신(self)이 전달되게 설계

```python
class Person:
    # 오류 TypeError: test() takes 0 positional arguments but 1 was given
    # def test():  
        # return 'hi'
    
    def test(self):
        return self

p1 = Person()        
print(p1.test(), p1)
print(Person.test(p1))#내부적으로는 이렇게 실행

# 결과 (다 같은 결과)
<__main__.Person object at 0x0000020BFAC73700> <__main__.Person object at 0x0000020BFAC73700>
<__main__.Person object at 0x0000020BFAC73700>
```



> 생성자 메소드  `__init__`

- 인스턴스 객체가 생성될 때 속성 초기값 설정

```python
class Person:
    def __init__(self, name, age): #초기값으로 이름과 나이를 설정
        self.name = name
        self.age = age        

kildong = Person('HongKilDong', 20) #이름:HongKilDong 나이:20인 인스턴스 생성
print(kildong.name, kildong.age) # HongKilDong 20
```



> 소멸자 메소드 `__del__`

- 객체 소멸에 이용되는 메소드

```python
class Person:
    def __init__(self):
        print('생성')
        
    def __del__(self):
        print('소멸')
        
p1 = Person() # 생성
del p1 # 소멸
```



> 매직 메소드

- `__str__`,  `__le__(less than or equal to)`, `__gt__(greater than)` ... 내부적으로 정의된 메소드

```python
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        
    def __str__(self): # 객체 자체를 print하면 __str__에 정의된 형식으로 출력됨
        return f'{self.name}: {self.age}세'
    
    def __gt__(self, other): #__gt__로 정의하고 >로 쓸 수 있음
        return self.age > other.age

p1 = Person('재영', 20, 170)
p2 = Person('지선', 10, 160)

# __str__
print(p1) # 재영: 20세 
# __gt__
print(p1 > p2) # True 
```



> dir() 

- 사용 가능한 메서드 출력

```python
print(dir('hi'))

# 결과
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```



> 클래스 변수

- 한 클래스의 모든 인스턴스가 똑같은 값을 가지고 있는 속성

```python
class Korean: 
    # Korean이란 class의 객체들은 Korea라는 국적을 가질 수 밖에 없음
    nationality = 'Korea' 
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = Korean('길동', 20)
print(p1.nationality, Korean.nationality) # Korea Korea
```



> 클래스 메소드

- 클래스가 사용할 메소드, `@classmethod` 데코레이터를 사용하여 정의
  - 데코레이터 : 함수를 어떤 함수로 꾸며서 새로운 기능을 부여
- 첫 번째 인자로 클래스 자체(cls)를 받음

```python
class MyClass:
    
    @classmethod
    def class_method(cls):
        return cls

print(MyClass.class_method(), MyClass) 
# <class '__main__.MyClass'> <class '__main__.MyClass'>
```



> 스태틱 메소드

- 클래스가 사용할 메소드, `@staticmethod` 데코레이터를 사용하여 정의
- 호출시, 어떠한 인자도 전달되지 않음(클래스 정보에 접근/수정 불가)

```python
class MyClass:
    
    # TypeError: static_method() missing 1 required positional argument: 'static'
    # @staticmethod #self, cls와 다르게 자동으로 넘어가는 인자가 없다
    # def static_method(static):
        # return static
    
    @staticmethod 
    def static_method():
        return 'static'
    
print(MyClass.static_method()) # static
```



> 데코레이터

- 함수 안의 함수, 함수 안에 반복적인 작업을 하고 싶을 때 사용함
- 데코레이터 입력에 함수를 입력할 때는 괄호()를 빼고 이름만, 괄호()는 호출의 의미

```python
def hello(f):
    def wrapper():
        print('hello')
        print(f()) 
    return wrapper

@hello
def foo():
    return 'foo'

foo() # hello \n foo
```



Q. 클래스 변수나 인스턴스 조작을 할 수 없는데 스태틱 메소드를 굳이 클래스 내부에 정의할 필요가 있나



> 상속

- 클래스 사이에 부모-자식 관계를 형성. 부모클래스의 변수, 메소드를 쓸 수 있음(재사용)

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
 
class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
        
stud = Student('길동', 20, 4)

#Student 클래스에는 talk()가 없지만 Person을 상속받았으므로 쓸 수 있다.
stud.talk()  # 반갑습니다. 길동입니다.
```

- super() : 부모 메소드 재사용

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
 
class Student(Person):
    def __init__(self, name, age, gpa):
        super().__init__(name, age) #부모 클래스 __init__을 super()을 이용하여 재사용
        self.gpa = gpa # 부모 클래스에 없는 새로운 속성은 추가
```



> mro() (Method Resolution Order)

- 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메소드
-  기존 인스턴스 => 부모 클래스 방향으로 확장

```python
Student.mro() # [__main__.Student, __main__.Person, object]
```



> 다형성 (Polymorphism)

- 동일한 메소드가 클래스에 따라 다르게 행동할 수 있음을 의미
  - 메소드 오버라이딩: 부모 클래스에서 정의한 메소드를 자식 클래스에서 변경

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
 
class Student(Person):
    def __init__(self, name, age, gpa):
        super().__init__(name, age) 
        self.gpa = gpa 
        
    def talk(self):
        print(f'충성충성. 학생 {self.name}입니다.')

pers = Person('순신', 33)
stud = Student('길동', 20, 4)

# 결과 : 같은 talk() 메소드가 다르게 작동함 => 다형성, 메소드 오버라이딩
pers.talk() # 반갑습니다. 순신입니다.
stud.talk() # 충성충성. 학생 길동입니다.
```



> 캡슐화 (Encapsulation)

- 객체 일부 구현 내용에 대해 외부로부터 직접적인 접근을 차단

  - Public : 어디서나 호출 가능

  - _Protected : 부모 클래스 내부와 자식 클래스에서만 호출 가능 => 외부에서 호출 불가능

  - __Private : 본 클래스 내부에서만 사용 가능 => 하위클래스 or 외부에서 호출 불가능
    - getter(캡슐화된 변수에 접근) / setter(캡슐화된 변수 변경) => 함수이름도 변수명으로 해야함
      - getter : @property
      - setter : @변수명.setter

```python
class Person:
    def __init__(self, name, age, height):
        self.name = name # public
        self._age = age # protected => _ 언더바 1개
        self.__height = height # private => __ 언더바 2개
    
    # 함수이다 => p1.get_height()
    def get_height(self):
        return self.__height
    
    @property # 데코레이션에 의해 속성값으로 변환됨 => p1.height
    def height(self):
        return self.__height
    
    @height.setter # p1.hieght(170) X => p1.height = 170 
    def height(self, new_height):
        self.__height = new_height
        
p1 = Person('길동', 20, 160)
print(p1.get_height()) # 160
print(p1.height) # 160
p1.height = 170
print(p1.height) # 170
```



