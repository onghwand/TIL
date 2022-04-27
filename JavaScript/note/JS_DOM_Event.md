## DOM, EVENT

### 1. DOM - Document Object Model

#### 1.1. 브라우저에서 할 수 있는 일

- DOM 조작
  - 문서(HTML) 조작
- BOM(Browser Object Model) 조작
  - navigator, screen, location, frames ...
- JavaScript Core
  - Data Structure, Conditional Expression, Iteration

#### 1.2. DOM 선택

- document.querySelector(selector)
  - 제공한 선택자와 일치하는 element **하나** 선택
  - 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환(없다면 null)
- document.querySelectorAll(selector)
  - 제공한 선택자와 일치하는 **여러** element 선택
  - 매칭 할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
  - 지정된 셀렉터에 일치하는 NodeList를 반환

> querySelector(), querySelectorAll()을 사용하는 이유

- id, class 그리고 tag 선택자 등을 모두 사용가능하므로, 더 구체적이고 유연하게 선택 가능

- getElementBy- 안씀

#### 1.3. DOM 변경

- document.createElement()
  - 작성한 태그 명의 HTML 요소를 생성하여 반환
- Element.append()
  - 특정 부모 Node의 자식 NodeList 중 마지막 자식 다음에 Node 객체나 DOMString을 삽입
  - **여러 개**의 Node 객체, DOMString을 추가 할 수 있음
  - 반환 값이 없음
- Node.appendChild()
  - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입(Node만 추가 가능)
  - 한번에 **오직 하나**의 Node만 추가 가능
  - 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 새로운 위치로 이동
  - 추가된 Node 객체 반환

- Node.innerText
  - Node 객체와 그 자손의 텍스트 컨텐츠를 표현   
- Element.innerHTML
  - 요소 내에 포함된 HTML 마크업을 반환
  - XSS 공격에 취약하므로 사용 시 주의
    - XSS : 악성 자바스크립트 코드를 삽입해 민감한 정보를 탈취

#### 1.4. DOM 삭제

-  ChildNode.remove()
  - Node가 속한 트리에서 해당 Node를 제거
- Node.removeChild()
  - DOM에서 자식 Node를 제거하고 제거된 Node를 반환
  - Node는 인자로 들어가는 자식 Node의 부모 Node

#### 1.5. DOM 속성

- Element.setAttribute(name, value)
  - 지정된 요소의 값을 설정
  - 속성이 이미 존재하면 값을 갱신
- Element.getAttribute(attributeName)
  - 해당 요소의 지정된 값을 반환
  - 인자는 값을 얻고자 하는 속성의 이름

<br>

### 2. Event

- 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체

#### 2.1. Event handler

- EventTraget.addEventListener()
  - 지정한 이벤트가 대상에 전달될 때마다 호출할 함수를 설정
  - 이벤트를 지원하는 모든 객체를 대상으로 지정 가능

- target.addEventListener(type, listener[, options])
  - type : 반응할 이벤트 유형
  - listener : 지정된 타입의 이벤트가 발생했을 때 알림을 받는 객체
    - EventListener 인터페이스 혹은 JS function 객체(콜백 함수)여야 함

```javascript
// 생략..
// 기본 형태
myTextInput.addEventListener('input', function (event) {
    const myPtag = document.querySelector('#my-paragraph')
    myPtag.innerText = event.target.value
})
```

#### 2.2. Event 취소

- event.preventDefault()
  - 현재 이벤트의 기본 동작을 중단('scroll'같은 경우는 없음, event.cancelable로 확인가능)

````javascript
checkBox.addEventListener('click', function (event) {
    event.preventDefault()
})
````

