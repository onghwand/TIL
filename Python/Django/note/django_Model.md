## Django Model

### 1. Model

- 저장된 데이터 베이스의 구조
- Django는 model을 통해 데이터에 접속하고 관리
- 일반적으로 각각의 model은 하나의 데이터베이스 테이블에 매핑

> 데이터베이스 (DB)

- 체계화된 데이터의 모임

> 쿼리

- 데이터를 조회하기 위한 명령어
- "Query를 날린다" => DB를 조작한다

> 스키마

- 데이터베이스에서 자료구조, 표현방법, 관계등을 정의한 구죠

> 기본기 Primary Key

- 반드시 설정해야 하며, 각 행의 고유값이다.



### 2. ORM, Object-Relational-Mapping

- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에(Django-SQL) 데이터를 변환하는 프로그래밍 기술
- Django는 내장 Django ORM을 사용

> 장점

- SQL을 잘 알지 못해도 DB 조작이 가능
- SQL의 절차적 접근이 아닌 객체 지향적 접근 => 높은 생산성

> 단점

- ORM 만으로 완전한 서비스를 구현하기 어려움

> models.py 작성

```python
# articles/models.py

class Article(models.Model): # 이미 만들어진 기능을 이용하기 위해 상속
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 처음 추가되는 시점에만
    updated_at = models.DateTimeField(auto_now=True)  # 변경되면 계속 갱신

# 다 만들거나 변경했으면 bash창에서
# $ python manage.py makemigrations => 마이그레이션 파일 생성
# $ python manage.py migrate => DB 반영
```

- 각 모델은 django.models.Model 클래스의 서브 클래스로 표현됨
  - Article이라는 모델은 models.Model을 상속받았으므로 서브클래스가 된다.
- models 모듈을 통해 어떠한 타입의 DB 컬럼을 정의할 것인지 정의
  - title과 content는 모델의 필드를 나타냄
  - 각 필드는 클래스 속성으로 지정되어 있으며, 각 속성은 각 데이터베이스의 열에 매핑



### 3. Migrations

- Django가 model에 생긴 변화를 반영하는 방법

> Migrations Commands

- makemigrations	
  -  model을 변경한 것에 기반한 새로운 마이그레이션을 만들 때 사용

```bash
$ python manage.py makemigrations

Migrations for 'articles':
  articles\migrations\0001_initial.py
    - Create model Article
```

- migrate
  - 마이그레이션을 DB에 반영하기 위해 사용
  - 설계도를 실제 DB에 반영하는 과정
  - 모델에서의 변경 사항들과 DB의 스키마가 동기화를 이룸

```bash
$ python manage.py migrate

Operations to perform:
  Apply all migrations: admin, articles, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
-이하 생략-
```

> 위 두개 명령어 입력 뒤에 `SQLite`  vscode확장 프로그램 깔고 
>
> db.sqlite3 우클릭 =>`Open database`
>
> 하면 탐색기 아래쪽에 `SQLITE EXPLORER`생김 => 열어서 테이블 만들어졌는지 확인

- sqlmigrate
  - 마이그레이션에 대한 sql구문을 보기 위해 사용
  - 마이그레이션이 SQL 문으로 어떻게 해석되어서 동작할지 미리 확인 할 수 있음
- showmigrations
  - 프로젝트 전체의 마이그레이션 상태를 확인하기 위해 사용
  - 마이그레이션 파일들이 migrate 됐는지 안됐는지 여부를 확인



> DB에 값에 빈 값은 존재할 수 없다.

```bash
$ python manage.py makemigrations

# 새로운 필드가 추가되었는데 기본 값이 없다.
It is impossible to add the field 'created_at' with 'auto_now_add=True' to article without providing a default. This is because the database needs something to populate existing rows.

# 옵션
# 1. 직접 디폴트값을 설정할게
# 2. 종료하고 models.py에서 직접 설정
 1) Provide a one-off default now which will be set on all existing rows
 2) Quit and manually define a default value in models.py.
Select an option: 1
# 디폴트 값을 파이썬 문법으로 유효한 것을 입력해.
Please enter the default value as valid Python.
Accept the default 'timezone.now' by pressing 'Enter' or provide another value.
The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
Type 'exit' to exit this prompt
[default: timezone.now] >>> #enter 누르면 timezone.now로 설정됨
Migrations for 'articles':
  articles\migrations\0002_article_created_at_article_updated_at.py
    - Add field created_at to article
    - Add field updated_at to article
```



### 4. 데이터조작 ORM / DB API

- DB를 조작하기 위한 도구

> 사전 준비

```bash
$ pip install ipython django-extensions
```

- settings.py 가서 앱 등록

```python
# settings.py
INSTALLED_APPS = [
    'articles',
    'django_extensions', # <= 이거 추가, _ underscore 주의 하이픈 아님   
]
```

- 시작

```bash
$ python manage.py shell_plus
```



> CREATE

```bash
In [1]: Article.objects.all() # 전체 데이터 조회하는 법 READ
Out[1]: <QuerySet []>

In [2]: article = Article()

In [3]: article.title = '제목'

In [4]: article.content = '내용입니다.'

In [5]: article
Out[5]: <Article: Article object (None)>

In [6]: article.save() # 저장을 해야 반영됨

In [7]: article
Out[7]: <Article: Article object (1)>

In [8]: Article.objects.all()
Out[8]: <QuerySet [<Article: Article object (1)>]>

# 2번째 객체(데이터) 생성
In [9]: a2 = Article(title='2번글', content='2번 내용')        

In [10]: a2.save()

In [11]: Article.objects.all()
Out[11]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>

# 3번째 객체 생성 => save()할 필요없는 방법
In [13]: Article.objects.create(title='3번글', content='3번내용')
Out[13]: <Article: Article object (3)>

In [14]: Article.objects.all()
Out[14]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
```

> READ

```bash
# 전체 데이터 조회
In [1]: Article.objects.all() 
Out[1]: <QuerySet []>

# 단일 데이터 조회 (pk == id)
In [15]: Article.objects.get(pk=1)
Out[15]: <Article: Article object (1)>

In [16]: Article.objects.get(id=1)
Out[16]: <Article: Article object (1)>

# 없는 데이터 조회
In [17]: Article.objects.get(id=100)
DoesNotExist: Article matching query does not exist. #에러

# 같은 값을 2개이상 가지는 데이터를 get(무조건 하나 return)으로 조회하면 error
In [18]: Article.objects.create(title='제목', content='4번내용')
Out[18]: <Article: Article object (4)>

In [19]: Article.objects.get(title='제목')
MultipleObjectsReturned: get() returned more than one Article -- it returned 2!

# 여러 데이터를 조회 => filter()
In [23]: Article.objects.filter(title='제목')
Out[23]: <QuerySet [<Article: Article object (1)>, <Article: Article object (4)>]>

In [24]: Article.objects.filter(title='제목')[0].content
Out[24]: '내용입니다.'
```

> UPDATE

```bash
In [26]: a2 = Article.objects.get(pk=2)

In [27]: a2.pk
Out[27]: 2

In [28]: a2.title = '제목' # 수정하고
 
In [29]: a2.save() # 저장
```

> DELETE

```bash
In [30]: a3 = Article.objects.get(pk=3)

In [31]: a3.delete()
Out[31]: (1, {'articles.Article': 1})

In [32]: exit() # 빠져나오기
```

> 마지막으로 저장된 결과 항목

| id   | title | content     | created_at                 | updated_at                 |
| ---- | ----- | ----------- | -------------------------- | -------------------------- |
| 1    | 제목  | 내용입니다. | 2022-03-08 04:58:48.749412 | 2022-03-08 04:58:48.749412 |
| 2    | 제목  | 2번 내용    | 2022-03-08 05:03:48.654551 | 2022-03-08 05:43:13.989528 |
| 4    | 제목  | 4번내용     | 2022-03-08 05:16:33.889441 | 2022-03-08 05:16:33.889441 |



### 5. 웹페이지에 DB 반영

> models.py

```python
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
```

> views.py

```python
from django.shortcuts import render
from .models import Article # models.py에서 Article 클래스를 가져옴

def index(request):
    articles = Article.objects.all() # 모든 데이터를 가져와서 context로 넘겨줌
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)
```

> index.html

```django
{% extends 'base.html' %}

{% block content %}

{% for article in articles %}
<p>{{article.title}}</p>
<p>{{article.content}}</p>
<p>{{article.created_at}}</p>
<hr />
{% endfor %} 

{% endblock content %}
```



### 6. 입력받아서 DB에 저장 후 웹페이지에 반영 CREATE & READ

- 동작순서

1. new.html에서 `title`과 `content`를 입력받는다

2. create함수의 request로 정보를 받아와서 DB에 저장한 순간, index함수는 동작해서 index.html의 게시글 업데이트가 일어남

3. create.html은 새로 만들어진 내용을 보여주며 잘 게시되었는지 확인시켜줌

> views.py

```python
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 입력으로 받은 정보 땡겨와서
    title=request.GET.get('title')
    content=request.GET.get('content')
    
    # DB에 저장한 후
    article = Article()
    article.title = title
    article.content = content
    article.save()
    
    # context로 html에 넘겨주기
    context={
        'article': article,
    }
    return render(request, 'articles/create.html', context)
```

> new.html

```django
{% extends 'base.html' %}

{% block content %}
<h1>게시글 작성</h1>
<form action="{% url 'articles:create' %}" method="GET">
  <p>
    <label for="title">title:</label>
    <input type="text" id='title' name='title'>
  </p>
  <p>
    <label for="content">content:</label>
  </p>
  <textarea name="content" id="content" cols="30" rows="10"></textarea>
  <p>
    <input type="submit" value="submit">
  </p>
</form>
{% endblock content %}
```

> create.html

```django
{% extends 'base.html' %}

{% block content %}
<p>{{article.id}}번 글이 작성되었습니다</p>
<p>{{article.title}}</p>
<p>{{article.content}}</p>
{% endblock content %}
```



### 7. 게시글 제목을 누르면 상세보기 페이지로 이동(Variable Routing)

> urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    -생략-
    path('<int:id>/', views.detail, name='detail'), # http://127.0.0.1:8000/articles/1/
]
```

> views.py

- redirect를 이용하면 페이지 이동을 제어할 수 있음, import 해야함

```python
from django.shortcuts import redirect, render
from .models import Article

def create(request):
    -생략-
    # return render(request, 'articles/create.html', context)
    # return redirect('articles:index') 
    return redirect('articles:detail', article.pk)

def detail(request, id):
    article = Article.objects.get(id=id)
    
    context={
        'article': article
    }
    return render(request, 'articles/detail.html', context)
```

> index.html

- url이름이 detail이고 라우팅 변수는 밖에다 article.pk라고 써줘야함

```django
-생략-
<a href="{% url 'articles:detail' article.pk %}">{{article.title}}</a>
```

> detail.html

```django
{% extends 'base.html' %} 
{% block content %}
<h1>{{article.id}}번 글</h1>
<h2>제목: {{article.title}}</h2>
<h2>내용: {{article.content}}</h2>
<h2>생성시간: {{article.created_at}} | 업데이트 시간:{{article.updated_at}} </h2>

{% endblock content %}
```



### 8. 게시글 삭제 DELETE

1. 글 삭제 버튼을 만든다.
2. 삭제할 url을 생성한다.
3. delete 함수를 만든다.

> detail.html

```django
-생략-
<a href="{% url 'articles:delete' article.pk %}">글 삭제</a>
```

> urls.py

```python
urlpatterns = [
    path('<int:id>/delete', views.delete, name='delete'),
]

```

> views.py

- request인자를 안써도 `passing the HttpRequest as the first argument to the view function. ` 때문에 써야함

```python
def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    
    return redirect('articles:index')
```



### 9. 게시글 수정 UPDATE

1. `detail.html` 글 수정 버튼을 만든다. => 누르면 수정 페이지로 이동
2. `urls.py` 글 수정 정보를 받을 path & 받아서 DB 업데이트를 해줄 path 등록
3. `edit.html` 수정페이지를 만든다. => `views.py : def edit`기존 내용이 담겨있어야함
4. `views.py : def update`수정해서 `제출`버튼을 누르면 update되어 index.html로 redirect

> detail.html

```django
-생략-
<a href="{% url 'articles:edit' article.id %}">글 수정</a>
```

> urls.py 

- 글 수정 정보를 받을 path & 받아서 DB 업데이트를 해줄 path

```python
urlpatterns = [
    -생략-
    path('<int:id>/edit', views.edit, name='edit' ),
    path('<int:id>/update', views.update, name='update'),
]
```

> edit.html

- 기존에 입력되어있었던 정보를 그대로 표시해야하므로 
  - title에는 value로 기존 정보 입력
  - content에는 태그 사이에 입력

```django
{% extends 'base.html' %}

{% block content %}
<h1>게시글 수정</h1>
<form action="{% url 'articles:update' article.id%}" method="GET">
  <p>
    <label for="title">title:</label>
    <input type="text" id='title' name='title' value={{article.title}}>
  </p>
  <p>
    <label for="content">content:</label>
  </p>
  <textarea name="content" id="content" cols="30" rows="10">{{article.content}}</textarea>
  <p>
    <input type="submit" value="submit">
  </p>
</form>
{% endblock content %}
```

> views.py

```python
def edit(request, id):
    article = Article.objects.get(id=id)
    
    context={
        'article': article
    }
    return render(request, 'articles/edit.html', context)

def update(request, id):
    # 수정한 정보 땡겨와서
    title=request.GET.get('title')
    content=request.GET.get('content')
    
    # DB에 update한 후
    article = Article.objects.get(id=id)
    article.title = title
    article.content = content
    article.save()
    
    # 홈 화면으로 연결
    return redirect('articles:index')
```



## 10. POST & CSRF

- GET은 정보를 받아올 때, POST는 정보를 입력해서 전송할 때
- method="POST" 하고 해킹방지를 위해 {% csrf_token %} 입력해야함

```django
<form action="{% url 'articles:update' article.id %}" method="POST">
  {% csrf_token %}
```



## 11. 관리자 계정 ADMIN

- app을 관리할 수 있음

> articles/admin.py

```python
from django.contrib import admin
from .models import Article
# Register your models here.

# admin site에 register하겠다.
admin.site.register(Article)
```

> bash

```bash
$ python manage.py createsuperuser
사용자 이름 (leave blank to use '82102'): admin
이메일 주소: 
Password: #1234
Password (again): #1234
비밀번호가 너무 짧습니다. 최소 8 문자를 포함해야 합니다.
비밀번호가 너무 일상적인 단어입니다.
비밀번호가 전부 숫자로 되어 있습니다.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

