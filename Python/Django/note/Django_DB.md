## Model Relationship

### 1. Foreign Key, 외래 키

> 관계형 데이터베이스에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키

- 외래 키 특징 (참조 무결성)
  - 키를 사용하여 부모 테이블의 유일한 값을 참조
  - 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만 유일한 값이어야 함

<br>

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
def comments_create(request.pk):
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