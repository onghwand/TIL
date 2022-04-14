## Model Relationship

### 0. Foreign Key, 외래 키

> 관계형 데이터베이스에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키

- 외래 키 특징 (참조 무결성)
  - 키를 사용하여 부모 테이블의 유일한 값을 참조
  - 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만 유일한 값이어야 함

<br>

### 1. Article - Comment (1:N)

#### 1.1. comment(댓글) 모델 정의

> articles/models.py

```python
class Comment(models.Model):
    # 테이블에는 자동으로 article_id로 col 생성됨
    article = models.ForeignKey(Article, on_delete=models.CASCADE) 
    # content, created_at, updated_at ...
    # 꼭 makemigrations, migrate
```

- CASCADE : 부모 객체가 삭되 됐을 때 이를 참조하는 객체도 삭제

> articles/admin.py

```python
from .models import Comment

admin.site.register(Comment)
```

```bash
$ python manage.py createsuperuser
```

<br>

#### 1.2. 역참조

- 1:N 관계에서 1에 해당하는 테이블에서 반대로 참조하는 것
- comment_set manager가 생성되므로 이용하면된다  
  - `1에 해당하는 class`.`N에 해당하는 class`_set.all()

```python
comments = article.comment_set.all()
```

<br>

#### 1.3. `Comment` Form

1. `commentform` 작성하고
2. view > detail에서 불러와서 context로 넘긴후
3. detail.html에서 렌더링

> articles/forms.py

```python
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',) # 댓글 입력받을 창만 표시
        #fields = '__all__'
```

> articles/views.py

```python
from .forms import CommentForm

def detail(request, pk):
    pass
    comment_form = CommentForm()
    context = {
        'comment_form': comment_form
    }
    pass   
```

<br>

#### 1.4. Create `comment`

1. `url` 만들고 => path(`<int:pk>/comments/`, `views.comments_create`, name='comments_create')
2. detail.html 댓글 생성 form action에 `url` 입력하고
3. views.py에 `comments_create`함수 생성

> articles/views.py

```python
def comments_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False) # 생성만 하고 commit 아직안하게끔
        comment.article = article # article 지정해줘야 하니까
        comment.save() # commit
    return redirect('articles:detail', article.pk)
```

<br>

#### 1.5. READ `comment`

1. 특정 article에 있는 모든 댓글을 가져온 후 context로 넘겨주고
2. detail.html에서 렌더링

> views.py

```python
def detail(request,pk):
    pass
    comments = article.comment_set.all()
    context = {
        'comments': comments,
    }
    pass
```

> detail.html

```django
{% for comment in comments %}
	<li>{{ comment.content }}</li>
{% endfor %}
```

<br>

#### 1.6. DELETE `comment`

1. delete `url` 만들고 => path(`<int:article_pk>/comments/<int:comment_pk>/delete/`, `views.comment_delete`, name='comments_delete')
2. delete 버튼 만들고 => detail.html에서 post method로 각 댓글 옆에
3. views.py에서 `comments_delete` 함수 생성

> views.py

```python
def comments_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
```

<br>

#### 1.7. decorator

- 다 끝나면 데코레이터(`@require_`)와 로그인 조건(`is_authenticated`) 추가

<br>

### 2. Customizing authentication

[Custom User Model](https://docs.djangoproject.com/en/4.0/topics/auth/customizing/)

#### 2.1. User 모델 대체하기

- 커스텀 유저 모델을 설정하는 것을 강력하게 권장
  - 나중에 유저 모델을 변경하기가 매우 번거롭기 때문에 custom해놓고 시작

> accounts/models.py

```python
from django.contrib.auth.models import AbstarctUser

class User(AbstarctUser):
    pass
```

> settings.py

```python
AUTH_USER_MODEL = 'acoounts.User'
```

> accounts/admin.py

```python
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

<br>

##### 2.1.1. 만약에 중간에 모델을 수정하는 것이라면

- 데이터베이스를 초기화 한 후 마이그레이션 진행
- 초기화 방법
  - db.sqlite3 파일 삭제
  - migrations 파일 모두 삭제 (파일명에 숫자가 붙은 파일만 삭제 ex)0001~~)
  - 그 후 다시 makemigrations, migrate
- 또 custom해줘야 하는 것 `UserCreationForm`, `UserChangeForm` => 이것도 custom안하면 `model=auth.User`

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model() # 현재 active 상태인 user model을 가져옴
        fields = UserCreationForm.Meta.fields + ('custom_field',)
```

- 이 후에 view.py에 가서 다 수정해야함 `UserCreationForm` => `CustomUserCreationForm`

<br>

##### 2.1.2. User모델 참조

> django에서 내부적으로 불러오는 순서 때문에(INSTALLED_APP 다음으로 MODEL불러옴)

- settings.AUTH_USER_MODEL => str 반환
  - models.py에서 User 모델 참조할 때
- get_user_model() => object 반환
  - models.py가 아닌 곳에서 User 모델 참조할 때

<br>

### 3. User - Article (1:N)

> 위 Article - Comment 과정과 동일

```python
from django.conf import settings

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=model.CASCADE)
```

- `makemigrations`, `migrate`

#### 3.1. CREATE

- Create 새로고침 해보고 `User`인풋이 나오면 `forms->fields` 조정
- views.py 가서 `article.user = request.user` 누가 글 작성 한것인지 DB에 입력해주기

#### 3.2. DELETE / UPDATE

- `if request.user == article.user:` => 이 글을 작성한 사람만 삭제 가능

- update에서 만약에 글 작성한 사람이 아니면 index로 redirect

#### 3.3. READ

- index.html에서 `{{ article.user }}` 작성자도 출력
- detail.html에서 `{% if user == article.user %}` 이용하여 수정/삭제 버튼 출력하지 않도록 처리

<br>

### 4. User - Comment (1:N)

```python
from django.contf import settings

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=model.CASCADE)
```

1. `makemigrations`, `migrate`
2. 원치 않는 input이 출력될 시, fields 조정
3. Comment에 user가 추가 되었으므로 views.py에서도 댓글 작성 시, `comment.user = request.user`

4. 비로그인 유저에게는 댓글 form 출력 숨기기 => detail.html
5. 댓글 작성자 출력 => detail.html
6. 자신이 작성한 댓글만 삭제 버튼을 볼 수 있도록 수정 => detail.html
7. 자신이 작성한 댓글만 삭제 할 수 있도록 수정 => `if request.user == comment.user:` => views.py