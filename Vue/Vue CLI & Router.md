## Vue CLI & Router

### 1. SFC (Single File Component)

- 하나의 컴포넌트는 `.vue` 확장자를 가진 하나의 파일 안에서 작성되는 코드의 결과물
  - `Vue 컴포넌트 === Vue 인스턴스 === .Vue 파일`

- 각 기능 별로 파일을 나눠서 개발
  - 처음 개발 준비 단계에서 시간 소요가 증가하지만 이후 유지보수 용이
- Vue 컴포넌트는 const app = new Vue({...})의 app을 의미하며 이는 Vue 인스턴스
  - 단일 html 파일 안에서도 여러 개의 컴포넌트를 만들어 개발 가능

<br>

### 2. Vue CLI

- Vue.js 개발을 위한 표준 도구

- Vue CLI Quick Start

  ```shell
  $ npm install -g @vue/cli
  $ vue --version # 버전확인
  $ vue create my-first-app # 프로젝트 생성
  	>Default([Vue 2] babel, eslint) 
  $ cd my-first-app # 위치 이동
  $ npm run serve # 서버 실행
  ```

> Node.js

- 자바스크립트를 브라우저가 아닌 환경에서도 구동할 수 있도록 하는 자바스크립트 런타임 환경

> NPM (Node Package Manage)

- 자바스크립트 언어를 위한 패키지 관리자
  - Python에 pip가 있다면 Node.js에는 NPM

<br>

### 3. Babel & Webpack

> Babel

- JavaScript compiler
- 자바스크립트의 ECMAScript 2015+ 코드를 이전 버전으로 번역/변환해주는 도구

> Webpack

- static module bundler
- 모듈 간의 의존성 문제를 해결하기 위한 도구
  - 여러 모둘을 하나로 묶어주고 묶인 파일은 하나로 합쳐짐 webpack 이외에도 다양한 모듈 번들러 존재
  - Vue CLI는 이러한 Babel, Webpack에 대한 초기 설정이 자동

<br>

### 4. Pass Props & Emit Events

- 컴포넌트는 트리(계층구조)로 구성됨
  - 컴포넌트간 부모-자식 관계가 구성되며 의사 소통이 필요함
- 부모는 자식에게 데이터를 전달(Pass props)하며, 자식은 자신에게 일어난 일을 부모에게 알림(Emit event)
  - props는 아래로, events는 위로
  - 부모는 props를 통해 자식에게 '데이터'를 전달하고, 자식은 events를 통해 부모에게 메시지를 보냄 

#### 4.1. 컴포넌트 구조

1. 템플릿(HTML) : HTML body부분 => 각 컴포넌트 작성
2. 스크립트(JS) : 컴포넌트 정보, 데이터, 메서드 
3. 스타일(CSS) : 컴포넌트 스타일

> 컴포넌트 등록 3단계

1. 불러오기 (import)
2. 등록하기 (register)
3. 보여주기 (print)

#### 4.2. Props

> static props

```vue
// App.vue
// 자식 컴포넌트에 보낼 prop 데이터 선언
<about my-message="This is prop data"></about> 

// About.vue
// 수신할 prop 데이터를 명시적으로 선언 후 사용

<template>
	<div>
    	<h2>{{ myMessage }}</h2> // script에서 불러와서 사용
    </div>
</template>

<script>
	export default {
        name: 'About',
        props: {
            myMessage: String, // Camel Case로 바꿔줘야함
        }
    }
</script>
```

> dynamic props

- bind로 동적으로 묶음
- 컴포넌트의 data는 반드시 함수여야함

```vue
<template>
	<div>
    	<about
         :parent-data="parentData"
        >
    	</about>
    </div>
</template>

<script>
	export default {
        name: 'App',
        components: {
            About
        },
        data: function () {
            return {
                parentData:"This is parent Data"
            }
        },
    }
</script>
```

#### 4.3. Emit event

- Listening to Child Components Events
- $emit( `eventName` )
  - 현재 인스턴스에서 이벤트를 트리거
  - 추가 인자는 리스너의 콜백 함수로 전달
- 부모는 자식이 보낸 이벤트를 v-on(@)를 이용해서 청취

> 순서 예시

1. 자식 컴포넌트에 input태그 생성(`v-model`로 동기화된 변수 생성, `@keyup.enter`로 엔터 눌렀을 때 변수 값 변경 함수 실행)
2. data(), methods에 자식컴포넌트에 부여할 함수와 변수 생성
3. 부모 컴포넌트에 `@child-input-change` 로 자식에서 emit으로 보내온 event에 반응, 과 동시에 반응할 함수부여
4. 부모 컴포넌트에 emit으로 날라온 변수받아서 할 동작 `parentGetChange`함수 생성

> App.vue

```vue
<template>
  <div id="app">
    <FirstVue @child-input-change="parentGetChange"/>
  </div>
</template>

<script>
import FirstVue from './components/FirstVue.vue'
export default {
  name: 'App',
  components: {
    FirstVue
  },
  methods: {
    parentGetChange(data) {
      console.log('부모', data)
    }
  }
}
</script>
```

> FirstVue.vue

```vue
<template>
  <div>
    <h2>First Vue!</h2>
    <input
    type="text"
    @keyup.enter="childInputChange"
    v-model="childInputData">
  </div>
</template>

<script>
export default {
  name: 'FirstVue',
  data(){
    return {
      childInputData:'',
    }
  },
  methods: {
    childInputChange() {
      this.$emit('child-input-change', this.childInputData)
    }
  }
}
</script>
```

<br>

### 5. Vue Router

- Vue.js 공식 라우터
- 라우트에 컴포넌트를 매핑한 후, 어떤 주소에서 렌더링할 지 알려줌
  - django처럼 html 템플릿이 여러개 있는것이 아니기 때문에

> Vue Router 시작

```shell
$ vue create my-router-app # 프로젝트 생성
$ cd my-router-app # 프로젝트 이동
$ vue add router # plug in 설치, commit 여부 Yes, History mode 사용여부 Yes
```

> index.js

- 라우트에 관련된 정보 및 설정이 작성 되는 곳

> <router-link>

- 사용자 네비게이션을 가능하게 하는 컴포넌트
- 목표 경로는 `to`  prop으로 지정
- HTML5 히스토리 모드에서 router-link는 클릭 이벤트를 차단하여 브라우저가 페이지를 리로드하지 않도록 함(새로고침 X)

> <router-view>

- 주어진 라우트에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트
- 실제 component가 DOM에 부착되어 보이는 자리를 의미
  - 장고에서 <block content>랑 비슷한 느낌

> History mode

- 브라우저의 히스토리는 남기지만 실제 페이지는 이동하지 않는 기능을 지원