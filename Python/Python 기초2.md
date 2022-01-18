## 파이썬 기초 2

- 리스트 원소 개수 세기

```python
numbers = [1, 1, 2, 2, 3, 4]
numbers.count(1)
```



- 상수는 대문자로 작성

```python
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

FIND_NUM = 5

count_num = 0
for i in numbers:
    if i == FIND_NUM:
        count_num += 1
print(count_num)
```



- join 메서드 (리스트 원소들을 str로 연결, 리스트 원소는 무조건 str type)

```python
numbers = ['1', '2', '3']
print(''.join(numbers))
print('!!'.join(numbers))
```

```
123
1!!2!!3
```



- isdecimal(), isnumeric(), isdigit() (str이 숫자형태인지 bool로 반환)

> isdigit() (중간)

해당 문자열이 '숫자'로 이루어져 있는지 검사

> isdecimal() (가장 보수적)

int로 바로 변활할 수 있는 수인지 검사

> isnumeric() (특수문자도 숫자면 다 인정)

숫자처럼 생기면 다 True

