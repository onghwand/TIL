## JSON&Dict 그리고 auth

> JSON과 Dictionary의 차이점

1. `json`은 `Data Format`이며, 순수 문자열들이어서 `dictionary`나 그외 형태로 해석 가능
   `dictionary`는 `Data Structure`임
2. `json`의 `KEY`는 항상 문자열이여야 함
   `dictionary`의 `KEY`는 특정 데이터 타입에 구애 안받음
3. `json`의 각 `KEY`는 `undefined`라는 기본값을 가짐
   `dictionary`는 기본값을 가지지 않음
4. `json`은 `true`, `false`, `null`
   `dictionary`는 `True`, `False`, `None`



> auth란?

- Authentication, 인증을 뜻하며 유저의 identification을 확인하는 절차
- API를 사용할 때, key토큰을 할당받아서 사용하기도 하지만, id와 password를 통해 인증을 하는 경우도 있다. 이때 auth 옵션을 사용한다.

```python
import requests

url = 'https://www.naver.com'
response = requests.post(url, auth=('id', 'pwd'))

print('status code:', response.status_code)
```

