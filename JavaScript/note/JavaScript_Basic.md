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

<br>

### 4. 함수

> JavaScript의 함수는 `일급 객체`에 해당
>
> 일급 객체: 1. 변수에 할당 가능, 2. 함수의 매개변수로 전달 가능, 3. 함수의 반환 값으로 사용 가능

#### 4.1. 함수 선언식 (호이스팅 O, 권장 x => var과 같음)

- 함수의 이름과 함께 정의하는 방식

```javascript
function add(num1, num2) {
    return num1 + num2
}
```

#### 4.2. 함수 표현식 (권장)

- 함수를 표현식 내에서 정의하는 방식
  - 표현식: 어떤 하나의 값으로 결정되는 코드의 단위

```javascript
const add = function (num1, num2) {
    return num1 + num2
}
```

#### 4.3. 매개변수와 인자의 개수 불일치 허용

- 매개변수보다 인자의 개수가 많을 경우 => 잘림

```javascript
const twoArgs = function (arg1, arg2) {
    return [arg1, arg2]
}
twoArgs(1, 2, 3) // [1, 2]
```

- 매개변수보다 인자의 개수가 적을 경우 => undefined

```javascript
const threeArgs = function (arg1, arg2, arg3) {
    return [arg1, arg2, arg3]
}
threeArgs(1) // [1, undefined, undefined]
```

#### 4.4. Rest operator & Spread operator

> Rest operator

- rest operator로 처리한 매개변수에 인자가 넘어오지 않을 경우에는, 빈 배열로 처리

```javascript
const restOpr = function (arg1, arg2, ...restArgs) {
    return [arg1, arg2, restArgs]
}
restArgs(1,2,3,4,5) // [1,2,[3,4,5]]
restArgs(1,2) // [1,2,[]]
```

> Spread operator

- spread operator(...)를 사용하면 배열 인자를 전개하여 전달 가능

```javascript
const spreadOpr = function (arg1, arg2, arg3) {
    return arg1 + arg2 + arg3
}
const numbers = [1,2,3]
spreadOpr(...numbers) // 6
```

<br>

### 5. Arrow Function

- function 키워드 생략 가능
- 함수의 매개변수가 단 하나 뿐이라면, `()`도 생략 가능
- 함수 body가 표현식 하나라면 `{}` 과 `return`도 생략 가능

```javascript
const arrow1 = function (name) {
    return `hello, ${name}`
}

// 1. function 키워드 삭제
const arrow2 = (name) => {return `hello, ${name}`}

// 2. 매개변수가 1개일 경우에만 () 생략 가능
const arrow3 = name => {return `hello, ${name}`}

// 3. 바디가 표현식 1개(return 한문장)라면 {}과 return 생략 가능
const arrow4 = name => `hello, ${name}`
```

<br>

### 6. 문자열

[MDN-String Method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)

|  메서드  |                   설명                    |              비고              |
| :------: | :---------------------------------------: | :----------------------------: |
| includes | 특정 문자열의 존재여부를 참/거짓으로 반환 |                                |
|  split   |   문자열을 토큰 기준으로 나눈 배열 반환   | 인자가 없으면 기존 문자열 반환 |
| replace  | 해당 문자열을 대상 문자열로 교체하여 반환 |           replaceAll           |
|   trim   |      문자열의 좌우 공백 제거하여반환      |       trimStart, trimEnd       |

<br>

### 7. 배열

[MDN-Array Method](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array)

|     메서드      |                       설명                       |           비고           |
| :-------------: | :----------------------------------------------: | :----------------------: |
|     reverse     |      원본 배열 요소들의 순서를 반대로 정렬       |                          |
|    push&pop     |       배열의 가장 뒤 요소를 추가 또는 제거       |                          |
| unshift & shift |       배열의 가장 앞 요소를 추가 또는 제거       |                          |
|    includes     | 배열에 특정 값이 존재하는지 판별 후 참/거짓 반환 |                          |
|     indexOf     | 배열에 특정 값이 존재하는지 판별 후 인덱스 반환  | 요소가 없을 경우 -1 반환 |
|      join       |    배열의 모든 요소를 구분자를 이용하여 연결     | 구분자 생략 시 쉼표 기준 |

#### 7.1. Array Helper Methods

- 메서드 호출 시 인자로 callback 함수를 받는 것이 특징
  - callback 함수 : 어떤 함수의 내부에서 실행될 목적으로 인자로 넘겨받는 함수(파이썬의 lambda)

| 메서드  | 설명                                                         |
| ------- | ------------------------------------------------------------ |
| forEach | 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행               |
| map     | 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환           |
| filter  | 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환 |
| reduce  | 콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환        |
| find    | 콜백 함수의 반환 값이 참이면 해당 요소를 반환                |
| some    | 배열의 요소 중 하나라도 판별 함수를 통과하면 참을 반환       |
| every   | 배열의 모든 요소가 판별 함수를 통과하면 참을 반환            |

<br>

### 8. Objects

- 객체는 속성의 집합이며, 중괄호 내부에 key와 value의 쌍으로 표현
- key는 문자열 타입만 가능
  - key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현

#### 8.1. 객체와 메서드

- 객체.메서드() 로 호출 가능
- 메서드 내부에서 this 키워드가 객체(`me`)를 의미함

```javascript
const me ={
    firstName: 'John',
    lastName: 'Doe',
    fullName: this.firstName + this.lastName,
    getFullName: function () {
        return this.firstName + this.lastName
    }
}
```

#### 8.2. 객체 관련 ES6 문법

> 속성명 축약
>
> 객체를 정의할 때 key와 할당하는 변수의 이름이 같으면 축약 가능

```javascript
var bookShop = {
    books: books,
}

// ES6+
const bookShop = {
    books,
}
```

> 메서드명 축약
>
> 메서드 선선 시 function 키워드 생략 가능

```javascript
var obj ={
    greeting: function () {
        console.log('Hi!')
    }
}

// ES6+
const obj = {
    greeting() {
        console.log('Hi!')
    }
}
```

> 계산된 속성
>
> 객체를 정의할 때 key 이름을 표현식을 이용하여 동적으로 생성 가능

```javascript
const key = 'regions'

const ssafy = {
    [key]: value,
}
```

> 구조 분해 할당
>
> 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법

```javascript
const userInformations = {
    name: 'ssafy kim',
}

const name = userInformation.name

// ES6+
const {name} = userInformation
```

> Spread operator
>
> 객체 내부에서 객체 전개 가능 (얉은 복사)

```javascript
const obj = {b:2, c:3}
const newObj = {a:1, ...obj} // {a:1, b:2, c:3}
```

#### 8.3. JSON (JavaScript Object Notation)

> key-value쌍의 형태로 데이터를 표기하는 언어 독립적 표준 포맷

- 자바스크립트에서는 JSON을 조작하기 위한 두가지 내장 메서드를 제공
  - JSON.parse()
    - JSON =>자바스크립트 객체
  - JSON.stringify()
    - 자바스크립트 객체 => JSON

<br>

### 9. this

- JS의 this는 실행 문맥에 따라 다른 대상을 가리킴
- forEach의 콜백함수의 경우 메서드가 아님 => 메서드는 printArea: function()
  - 콜백함수 내부의 this는 window가 되어 this.PI 접근 불가 => bind(this) 사용해야함
  - bind과정을 없앤 것이 arrow function

```javascript
const obj = {
    PI: 3.14,
    radiuses: [1,2,3],
    printArea: function(){
        this.radiuses.forEach(function (r) {
            console.log(this.PI*r*r)
        }.bind(this))
    },
    //Arrow function
    //printArea: function(){
    //    this.radiuses.forEach((r) => {
    //        console.log(this.PI*r*r)
    //    })
    //},    
}
```

<br>

### 10. lodash

[lodash](https://lodash.com/)

- 모듈성, 성능 및 추가 기능을 제공하는 JavaScript 유틸리티 라이브러리
  - sample, reverse, range ...

```html
<body>
  <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
  _.sample([1,2,3,4]) // random 1 element
  
</body>
```

