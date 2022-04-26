# 자바스크립트 

> 아래의 문제를 자바스크립트로 풀이하세요.

## 문제 1. 

var, let, const의 차이점을 작성하시오.

```
스코프: 함수/블록/블록
재선언: o x x
재할당: o o x
```

## 문제 2.

주어진 학생 점수 score의 값에 따라 다른 결과를 출력하는 코드를 작성하세요.

* 90점이상 100점 이하 : 'A'
* 80점이상 90점 미만 : 'B'
* 70점이상 80점 미만 : 'C'
* 60점이상 70점 미만: 'D'
* 60점 미만 : '과락'

```javascript
let score = 100
```

```javascript
// 코드 작성
if (score >= 90 && score <= 100) {
    console.log('A')
} else if (score >= 80 && score < 90) {
    console.log('B')
} else if (score >= 70 && score < 80) {
    console.log('C')
} else if (score >= 60 && score < 70) {
    console.log('D')
} else {
    console.log('과락')
}
```

## 문제 3.

주어진 username인 경우 ''관리자입니다.'를 출력하고, 나머지 경우는 모두 username을 출력하는 코드를 작성하세요.

```javascript
let username = 'admin'
```

```javascript
// 코드 작성
if (username === 'admin') {
    console.log('관리자입니다')
} else {
    console.log(username)
}
```

## 문제 4.

numbers의 숫자의 합을 출력하는 코드를 작성하세요.

기본 for문과 for...of를 활용하여 각각 작성합니다.

```javascript
let numbers = [1, 2, 3]
```

```javascript
// 기본 for
let sumV = 0
for (i = 0; i < numbers.length; i++){
    sumV += numbers[i]
}
console.log(sumV)
```

```javascript
// for..of
let sumV = 0
for (let num of numbers) {
    sumV += num
}
console.log(sumV)
```
