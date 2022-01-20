## 파이썬 기초4

> abs() 직접 구현

```python
'''
절댓값은 숫자형 자료(int, float)가 들어오면 절댓값을 반환하고, 복소수형 자료(complex)가 들어오면 해당하는 자료의 크기를 반환합니다.

파이썬 내장 함수 abs()를 직접 구현한 my_abs()를 작성하시오.
'''

def my_abs(x):
    if type(x) is int or type(x) is float:
        if x > 0:
            return x
        elif x < 0:
            return -x
        else:
            return x**2
    elif type(x) is complex:
        return (x.real**2 + x.imag**2)**0.5
    
print(my_abs(-3-4j))
print(my_abs(-0.0))
>>> 5.0
0.0
```



> all() 직접 구현

```python
'''
all()은 인자로 받는 iterable(range, list)의 모든 요소가 참이거나 비어있으면 True를 반환합니다.

파이썬 내장 함수 all()을 직접 구현한 my_all()을 작성하시오.
'''

def my_all(elements):
    for element in elements:
        if bool(element) == False:
            return False
    return True

print(my_all([]))
print(my_all([1, 2, 5, '6']))
print(my_all([[], 2, 5, '6']))
>>> True
True
False
```



> 달팽이 문제

```python
'''
달팽이가 기둥의 꼭대기에 도달하는 날까지 걸리는 시간을 반환하는 함수 snail()을 작성하시오

1. height : 기둥의 높이(미터)
2. day : 낮 시간 동안 달팽이가 올라가는 거리(미터)
3. night : 달팽이가 야간에 잠을 자는 동안 미끄러지는 거리(미터)
'''

def snail(height, day, night):
    cnt = 0
    while True:
        cnt += 1
        height -= day
        
        if height <= 0:
            return cnt
        
        height += night
        
print(snail(100, 5, 2))
>>> 33
```



> 자릿수 더하기

```python
'''
자연수 number를 입력 받아, 각 자릿수의 합을 계산하여 출력하시오.
'''

def sum_of_digit(number):
    total = 0
    
    while True:
        if number <= 0:
            return total
        
        number, residue = divmod(number, 10)
        total += residue
 
print(sum_of_digit(1234))
print(sum_of_digit(4321))
print(sum_of_digit(54321))
>>> 10
10
15
```

