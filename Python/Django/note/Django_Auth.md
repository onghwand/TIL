## Auth

### Django Authentication System

- Django 인증 시스템은 django.contrib.auth에서 모듈로 제공
  - 필수 구성은 settings에 이미 포함되어 있음

### 1. App accounts 생성

> 만든 후에 INSTALLED_APPS에 꼭 등록 + urls.py 생성

```bash
$ python manage.py startapp accounts
```

- app 이름이 반드시 accounts일 필요는 없지만 장고 내부적으로 사용되는 이름이므로 권장



### 2. 쿠키와 세션

> HTTP 특징

- connectionless : 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
- stateless : 연결을 끊는 순간 통신이 끝나며 상태 정보가 유지되지 않음

=> **클라이언트와 서버의 지속적인 관계(로그인 상태)를 유지하기 위해 쿠키와 세션이 존재**

> 쿠키
>
> 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각

- HTTP 쿠키는 상태가 있는 세션을 만들어 줌
- 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용
  - 요청마다 같은 쿠키가 왔다갔다 하며 판단근거가 됨 => 상태가 유지되는 것 처럼 보이지만 stateless임 

> 세션
>
> 사이트와 특정 브라우저 사이의 상태를 유지시키는 것

- 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고, 클라이언트는 쿠키에 저장



### 3. 로그인

```python
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        from = AuthenticationForm()
    context = {
        'from': form
    }
    return render(request, 'accounts/login.html', context)
```

- base.html `로그인 링크` 만들기
- 로그인한 사용자가 user에 저장되므로 아래와 같이 사용 가능

```django
Hello, {{ user }}
```



### 4. 로그아웃

```python
from django.contrib.auth import logout as auth_logout
def logout(request):
    if request.user.is_authenticated:
    	auth_logout(request)
    ...
```



### 5. is_authenticated

- `request.user.is_authenticated`를 이용해서 
  - base.html 
    - 조건부 렌더링
  - view 
    - 로그인 중이면 로그인 못하게
    - 로그인 중일 때만 로그아웃 가능
  - index
    - 인증된 사용자만 게시글 작성 가능



### 6. login_required

- **delete 함수에 쓰면 next에 의해 get요청으로 변경되고 `@require_POST`랑 충돌남 => 쓰지말것**

```python
from django.contrib.auth.decorators import login_required

@login_required
def login(request):
    ...
    return redirect(request.GET.get('next') or 'articles:index')
	# 데코레이터에 의해 로그인 창이 연결되고 로그인 되면 next에 의해 원래 가려던 페이지로 연결
    # 반드시 login.html의 form의 action값을 비워줘야함
```



### 7. 회원가입

```python
from django.contrib.auth.forms import AuthenticationFrom, UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # auth_login(request, user) 회원가입후 자동으로 로그인 해주고 싶으면 user는 save에서 받아오기
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
```

- 회원가입 링크 base에 생성



### 8. 회원탈퇴

``` python
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request) # 유저 삭제해도 세션이 남아있으므로 세션정보지우기
    return redirect('articles:index')
```



### 9. 회원정보 수정

> accounts/forms.py

```python
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeFrom(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')
```

> views.py

```python
from .forms import CustomUserChangeForm

def update(request):
    #포스트면
    form = CustomUserChangeFrom(request.POST, instance=request.user)
    ...
```



### 10. 비밀번호 변경

```python
from django.contrib.auth.forms import PasswordChangeForm

def change_password(request):
    # 포스트면
    form = PasswordChangeFrom(request.user, request.POST)
    ...
```

#### 	10.1 비밀번호 변경 후 세션 무효화 방지

- 비밀번호를 변경하면 로그인이 풀림 => 선택적으로 사용

```python
from django.contrib.auth import update_session_auth_hash

def change_password(request):
    ...
    form.save()
    update_session_auth_hash(request, form.user)
    ...
```

