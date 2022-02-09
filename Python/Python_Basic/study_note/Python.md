# Python

## 1. 자료구조
### 1-1. tuple(immutable), list(mutable)

> 시퀀스 데이터, 차이점은 값을 변경할 수 있는가 없는가

```python
# 점심 메뉴 리스트 생성
lunch_menu = ['pizza', 'beef', 'rice']

# 메뉴 출력
print(lunch_menu[0])
```

### 1-2. dictionary

> key, value로 이루어진 자료구조

```python
# 연락처 딕셔너리를 만들어주세요
phone_book = {'피자헛': '111-2222', '서브웨이': '222-3333'}

# 원하는 내용을 출력해주세요
print('피자헛:', phone_book['피자헛'])
```




## 2. 조건문
### 2-1 if/elif/else

```python
dust = 100

# 조건문 작성
if dust > 150:
    print('매우나쁨')
elif dust > 80 and dust <= 150:
    print('나쁨')
elif dust > 30 and dust <= 80:
    print('보통')
else:
    print('좋음')
```



## 3. 반복문
### 3-1. while

> 끝날 조건을 지정해주고 조건이 만족될 때까지 반복

```python
greeting = 'Guten Tag'

i = 0
while i < 10:  # 해당 조건이 False가 되면, 종료!
    print(greeting)
    i += 1
```

### 3-2. for

> 자료 안에서 마지막 순서까지 반복

```python
# for문?
for i in range(10):
    print(f'{i} : {greeting}')
```


## 4. random

> 난수 생성 및 무작위 표본 추출

#### 4-1. 점심 메뉴 추천

```python
# 1. 모듈 불러오기
import random

# 2. 점심 메뉴 리스트를 만들고 (최소 3개 이상)
lunch_menu = ['pizza', 'beef', 'rice']

# 3. today_menu에 무작위 메뉴 할당
today_menu = random.choice(lunch_menu)

# 4. 출력
print(today_menu)
```

#### 4-2. 로또 번호 

```python
# 1. 모듈 불러오기
import random

# 2. 숫자 통 (1~45)
num_box = list(range(1, 46))
# print(num_box)

# 3. 숫자 통에서 6개를 sample
result = random.sample(num_box, 6)

# 4. 결과 출력
print(result)
```

