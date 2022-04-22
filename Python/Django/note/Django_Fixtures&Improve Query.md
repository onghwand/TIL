## Fixtures & Improve Query

### 0. REST API 문서화

#### 0.1. drf-yasg

- 'Yet another Swagger genertor'
- API를 설계하고 문서화 하는데 도움을 주는 라이브러리

#### 0.2. 설치 

- [설치 가이드](https://drf-yasg.readthedocs.io/en/stable/readme.html?highlight=install#installation)

```shell
$ pip install drf-yasg
```

> settings.py

```python
INSTALLED_APPS =[
    'drf_yasg',
]
```

> articles/urls.py

```python
# from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
       # 아래는 선택 인자
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('swagger/', schema_view.with_ui('swagger')),
]
```

<br>

### 1. Fixtures

> 데이터베이스의 serialized 된 내용을 포함하는 파일 모음

- 앱을 처음 설정할 때 미리 준비된 데이터로 데이터베이스를 미리 채우는 것이필요한 상황이 있음
- 마이그레이션 또는 fixtures와 함께 초기 데이터를 제공

- django가 fixtures 파일을 찾는 경로 : app/fixtures/

#### 1.0. 폴더

- 앱 안에 fixtures 폴더 만들기 => 필요하면 articles/fixtures/articles/user.json

#### 1.1. dumpdata

```shell
# --indent 옵션을 주지 않으면 한 줄로 작성됨
# auth앱의 user 모델 데이터를 indent 4칸의 user.json 파일로 출력
$ python manage.py dumpdata --indent 4 auth.user > user.json
```

#### 1.2. loaddata

```shell
# app/fixtures/user.json 파일을 데이터베이스로 로드
$ python manage.py loaddata user.json
```

#### 1.3. 사용 예시

> 데이터 생성

```shell
$ python manage.py seed articles --number=10
```

> 각 모델 별 dumpdata 실행

```shell
$ python manage.py dumpdata --indent 4 articles.article > article.json
$ python manage.py dumpdata --indent 4 articles.comment > comments.json
$ python manage.py dumpdata --indent 4 accounts.user > users.json
```

> loaddata 실행

```shell
$ python manage.py loaddata articles/articles.json articles/comment.json accounts/user.json
```

<br>

### 2. Improve query

#### 2.1. QuerySets are lazy

- 쿼리셋을 만드는 작업에는 데이터베이스 작업이 포함되지 않음
- django는 쿼리셋이 `평가`될 대까지 실제로 쿼리를 실행하지 않음
  - DB에 쿼리를 전달하는 일이 웹 애플리케이션을 느려지게 하는 주범 중 하나이기 때문

> 평가
>
> 쿼리셋에 해당하는 DB의 레코드들을 실제로 가져오는 것

- 평가된 모델들은 쿼리셋의 내장 캐시에 저장되며, 덕분에 우리가 쿼리셋을 다시 순회하더라도 똑같은 쿼리를 DB에 다시 전달하지 않음

> 캐시
>
> 데이터나 값을 미리 복사해 놓는 임시 장소

- 값을 다시 계산하는 시간을 절약하고 싶은 경우에 사용

#### 2.2. 쿼리셋이 평가되는 시점

1. Iteration

   ```python
   for article in Article.objects.all():
       print(article.title)
   ```

2. bool()

   ```python
   if Article.objects.filter(title='Test'):
       print('hello')
   ```

3. 이외 Pickling/Caching, Slicing, repr, len, list에서 평가됨

#### 2.3. 캐시와 쿼리셋

- 각 쿼리셋에는 데이터베이스 액세스를 최소화하는 캐시가 포함
  - 쿼리셋이 처음으로 평가되면 쿼리 결과를 쿼리셋의 캐시에 저장하고 결과 반환
    - 이후 쿼리셋 평가는 캐시 된 결과를 재사용

```python
# 나쁜 예
print([article.title for article in Article.objects.all()]) # 평가
print([article.content for article in Article.objects.all()]) # 평가

# 좋은 예
queryset = Article.objects.all()
print([article.title for article in queryset]) # 평가
print([article.content for article in queryset]) # 캐시 재사용
```

> 쿼리셋이 캐시되지 않는 경우

1. 쿼리셋 객체에서 특정 인덱스를 반복적으로 가져오면 매번 데이터베이스를 쿼리

   ```python
   queryset = Article.objects.all()
   print(queryset[5]) # DB
   print(queryset[5]) # DB
   ```

2. 쿼리셋 전체가 이미 평가된 경우 캐시에서 확인

   ```python
   [article for article in queryset]
   print(queryset[5]) # 캐시
   print(queryset[5]) # 캐시
   ```

#### 2.4. 필요하지 않은 것을 검색하지 않기

- len(queryset) 대신 QuerySet.count() 사용
- if queryset 대신 QuerySet.exists() 사용

```python
like_set = article.like_users.filter(pk=request.user.pk)
# if 문은 쿼리셋을 평가 => 캐시가 생김
if like_set:
    # 반복할때 캐시된 쿼리셋이 사용됨 => 만약 쿼리셋이 엄청 크면 캐시 자체가 문제될 수 있음 => iterator
    for user in like_set:
        print(user.username)
```

> exist()

```python
like_set = article.like_users.filter(pk=request.user.pk)
# exists()는 쿼리셋 캐시를 만들지 않으면서 레코드가 존재하는지 검사
if like_set.exist():
    # 트래픽과 메모리 절약
    article.like_users.remove(request.user)
```

> iterator()

- 몇 천 개 단위의 레코드를 다뤄야 할 경우, 이 데이터를 한번에 가져와 메모리에 올리는 행위는 매우 비효율적이기 때문에 데이터를 작은 덩어리로 쪼개서 가져오고, 이미 사용한 레코드는 메모리에서 지움

```python
like_set = article.like_users.filter(pk=request.user.pk)

if like_set.exist():
    for user in like_set.iterator():
        print(user.username)
```

#### 2.5. Annotate

```python
articles = Article.objects.order_by('-pk') # 전
articles = Article.objects.annotate(Count('comment')).order_by('-pk') # 후
```

```django
댓글개수 : {{article.comment_set.count}} 전
댓글개수 : {{article.comment__count}} 후
```

#### 2.6. 한번에 모든 것을  검색하기

1. select_related() - 1:1 or 1:N 참조 관계에서 사용
2. prefetch_related() - M:N or 1:N 역참조 관계에서 사용 

> selected_related()

- SQL의 INNER JOIN을 실행하여 테이블의 일부를 가져오고, SELECT FROM에서 관련된 필드들을 가져옴

```python
# 게시글의 사용자 이름까지 출력
articles = Article.objects.order_by('-pk') # 전
articles = Article.objects.select_related('user').order_by('-pk') # 후
```

> prefetch_related()

- SQL의 JOIN을 실행하지 않고 python에서 joining을 실행

```python
# 댓글 목록을 모두 출력 
articles = Article.objects.order_by('-pk') # 전
articles = Article.objects.prefetch_related('comment_set').order_by('-pk') # 후
```

> selected_related() & prefetch_related()

```python
# 댓글에 더해서 해당 댓글을 작성한 사용자 이름까지 출력 해보기
from django.db.models import Prefetch

articles = Article.objects.order_by('-pk') # 전
articles = Article.objects.prefetch_related(Prefetch('comment_set', queryset=Comment.objects.select_related('user'))).order_by('-pk') # 후
```

