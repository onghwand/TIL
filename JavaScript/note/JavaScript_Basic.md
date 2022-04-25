## JavaScript

- 브라우저 조작할 수 있는 유일한 언어

### 0. 세미콜론 & 코딩 스타일 가이드

- 자바스크립는 세미콜론을 선택적으로 사용 가능
  - 세미콜론이 없으면 ASI에 의해 자동으로 세미콜론이 삽입됨
    - ASI: 자동 세미콜론 삽입 규칙 (Automatic Semicolon Insertion)
- [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)

<br>

### 1. 변수와 식별자

- 식별자는 반드시 문자, 달러($) 또는 밑줄(_)로 시작
- 클래스명 외에는 모두 소문자로 시작

#### 1.1. let & const

> let

- 재할당 예정인 변수 선언 시 사용
- 변수 재선언 불가능
- 블록 스코프

> const

- 재할당 예정이 없는 변수 선언 시 사용
- 변수 재선언 불가능
- 블록 스코프

| 키워드 | 재선언 | 재할당 |   스코프    |     비고     |
| :----: | :----: | :----: | :---------: | :----------: |
|  let   |   x    |   o    | 블록 스코프 | ES6부터 도입 |
| const  |   x    |   x    | 블록 스코프 | ES6부터 도입 |
|  var   |   o    |   o    | 함수 스코프 |    사용 x    |

> 블록 스코프란?

- if, for, 함수 등의 중괄호 내부를 가리킴
  - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

<br>

### 2. 데이터 타입

#### 2.1. 원시타입 & 찹조 타입

- 원시 타입
  - 객체가 아닌 기본 타입
  - 변수에 해당 타입의 값이 담김
  - 다른 변수에 복사할 때 실제 값이 복사됨
- 참조 타입
  - 객체 타입의 자료형
  - 변수에 해당 객체의 참조 값이 담김
  - 다른 변수에 복사할 때 참조 값이 복사됨

> python과 다른 것들

- 숫자 타입

```javascript
const e = Infinity // 양의 무한대
const f = -Infinity // 음의 무한대
const g = NaN //산술 연산 불가
```

- 문자열 타입

```javascript
const fullName = `${firstName} ${lastName}` // 파이썬의 f스트링같은 개념
```

- undefined & null (개발자 의도 유무의 차이)

  - undefined : 변수의 값이 없음을 나타내는 데이터 타입

    - 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 undefined 

  - null : 변수의 값이 없음을 의도적으로 표현할 때 사용하는 데이터 타입

    ```javascript
    typeof null // object
    ```

#### 2.2. 자동 형변환 정리

| 데이터 타입 | 거짓       | 참               |
| ----------- | ---------- | ---------------- |
| Undefined   | 항상 거짓  | X                |
| Null        | 항상 거짓  | X                |
| Number      | 0, -0, NaN | 나머지 모든 경우 |
| String      | 빈 문자열  | 나머지 모든 경우 |
| Object      | X          | 항상 참          |

#### 2.3. `==` & `===`

- `==` : 비교할 때 암묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교
  - 예상치 못한 결과가 발생할 수 있으므로 특별한 경우를 제외하고 사용 X
- `===` : 엄격한 비교가 이뤄지며 암묵적 타입 변환이 발생하지 않음

#### 2.4. 연산자

- 논리 연산자

  - and : &&

  - or : ||

  - not : !

- 삼항 연산자 : 3 개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자

  - 가장 왼쪽의 조건식이 참이면 콜론 앞의 값을 사용하고 그렇지 않으면 콜론 뒤의 값을 사용

  ```javascript
  console.log(true ? 1 : 2) // 1
  ```

<br>

### 3. 반복문

#### 3.0 for (기본형)

````javascript
for (let i = 0; i < 6; i++){
    console.log(i) // 0 1 2 3 4 5
}
````

#### 3.1. for ... in

- 주로 객체의 속성들을 순회할 때 사용 (js에서 객체는 기본적으로 딕셔너리)
  - key값 반환

````javascript
const capitals = {
    korea: 'seoul',
    france: 'paris'
}

for (let capital in capitals) {
    console.log(capital) // korea, france
}

````

#### 3.2. for ... of

- 반복 가능한 객체를 순회하며 값을 꺼낼 때 사용
  - 반복 가능한 객체의 종류: Array, Map, Set, String 등

```javascript
const fruits = ['딸기', '바나나', '메론']

for (let fruit of fruits) {
    fruit = fruit + '!'
    console.log(fruit)
}

for (const fruit of fruits) {
    // fruits 재할당 불가
    console.log(fruit)
}
```



