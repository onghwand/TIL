## REST API

### 1. HTTP

#### 1.1. URL, URN, URI

- URL(Uniform Resource Locator)
  - 통합 자원 위치
  - 네트위크 상에 자원이 어디 있는지 알려주기 위한 약속
- URN(Uniform Resource Name)
  - 통합 자원 이름
  - URL과 달리 자원의 위치에 영향을 받지않는 유일한 이름 역할을 함

- URI(Uniform Resource Identifier)
  - 통합 자원 식별자
  - 인터넷의 자원을 식별하는 유일한 주소

#### 1.2. URI의 구조

> https://www.example.com:80/path/to/myfile.html/?key=value#quick-start

- Scheme(protocol) `https://`
  - 브라우저가 사용해야 하는 프로토콜
  - http, data, file, ftp, mailto
- Host(Domain name) `www.example.com`
  - 요청을 받는 웹 서버의 이름
- Port `:80`
  - 웹 서버 상의 리소스에 접근하는데 사용되는 기술적인 '문'

- Path `/path/to/myfile.html`
  - 웹 서버 상의 리소스 경로
- Query(Identifier) `?key=value`
  - 웹 서버에 제공되는 추가적인 매개 변수
- Fragment `#quick-start`
  - 자원 안에서의 북마크의 한 종류를 나타냄

<br>

### 2. RESTful API

> 프로그래밍을 통해 클라이언트의 요청에 JSON을 응답하는 서버를 구성

#### 2.1. API

- Application Programming Interface
- 프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스
  - 애플리케이션과 프로그래밍으로 소통하는 방법

#### 2.2. REST

- `RE`presentational `S`tate `T`ransfer
- 네트워크 구조 원리의 모음
  - 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법
- REST 원리를 따르는 시스템을 RESTful이란 용어로 지칭함

> REST의 자원과 주소의 지정 방법

1. 자원: URI
2. 행위: HTTP Method
3. 표현: JSON

#### 2.3. JSON(JavaScript Object Notation)

- JavaScript의 표기법을 따른 단순 문자열

#### 2.4. REST의 핵심 규칙

1. '정보' URI로 표현
2. 자원에 대한 '행위'는 HTTP Method로 표현(GET, POST, PUT, DELETE)

<br>

### 3. Response

- 랜덤 데이터 생성법: django-seed라이브러리 install => python manage.py seed articles --number=20

- Content-Type

  - 데이터의 media type을 나타내기 위해 사용됨
  - 응답 내에 있는 컨텐츠의 컨텐츠 유형이 실제로 무엇인지 클라이언트에게 알려줌

- JsonResponse

  - JSON-encoded response를 만드는 HttpResponse의 서브 클래스

  - ''safe'' parameter

    - True(기본값)

    - dict 이외의 객체를 직렬화 하려면 False로 설정해야함

      ```python
      response =JsonResponse([1,2,3], safe=False)
      ```

#### 3.1. Serialization

- 직렬화 : 데이터 구조나 객체 상태를 동일하거나 다른 컴퓨터 환경에 저장하고 나중에 재구성할 수 있는 포맷으로 변환하는 과정

#### 3.2. Django REST Framework

- Django REST framework(DRF) 라이브러리를 사용한 JSON 응답

  ```shell
  $pip install djangorestframework
  ```

```python
INSTALLED_APPS = [
    'rest_frmework',
]
```

```python
urlpatterns = [
    path('json-3/', views.article_json_3),
]
```

> serializers.py

```python
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Aritcle
        fields = '__all__'
```

> views.py

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer

@api_view()
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True) # 단일 인스턴스가 아니면 many=True
    return Response(serializer.data)
```

|          |  Django   |    DRF     |
| :------: | :-------: | :--------: |
| Response |   HTML    |    JSON    |
|  Model   | ModelForm | Serializer |

<br>

### 4. Single Model

#### 4.0. Init Project

> my_api/urls.py

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('articles.urls')),
]
```



|             |     GET      |  POST   |     PUT     |   DELETE    |
| :---------: | :----------: | :-----: | :---------: | :---------: |
|  articles/  | 전체 글 조회 | 글 작성 |             |             |
| articles/1/ | 1번 글 조회  |         | 1번 글 수정 | 1번 글 삭제 |

#### 4.1. GET - Article List

> urls.py

```python
urlpatterns = [
    path('articles/', views.article_list), # 4.1.
    path('articles/<int:article_pk>/', views.article_detail), # 4.2.
]
```

>views.py

- `api_view` : 필수적으로 작성

```python
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer
from rest_framework import status

@api_view(['GET','POST'])
def article_list(request):
    #4.1. GET - Article List
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer =ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

	#4.3. POST - Create Article
    elif request.method == 'POST':
        serializer = AricleSerializer(data=request.data)
        if serializer.is_valid(raise_exeption=True): # 속성을 쓰면 else일때 400error가 뜸
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','DELETE','PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    #4.2. GET - Article Detail
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
	#4.4. DELETE - Delete Article
    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete': f'데이터 {article_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    #4.5. PUT - Update Article
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.saver()
            return Response(serializer.data)
```

#### 4.2. GET - Article Detail

- Article List와 Article Detail을 구분하기 위해 추가 Serializer 정의

> serializers.py

```python
from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', 'title')
        
class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = '__all__'
```

<br>

### 5. 1:N Relation

> models.py

```python
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

```shell
$python manage.py makemigrations
$python manage.py migrate
$python manage.py seed articles --number=20
```

> serializers.py

```python
class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',) # 유효성검사에서 빠짐=> 코드 구조상 유효성 검사후에 article을 정해줘야 하므로 유효성검사 통과되도록 해야함 # 5.3. POST - Create Comment
```

> urls.py

```python
urlpatterns = [
    path('comments/', views.comment_list) # 5.1. GET - Comment List
    path('comments/<int:comment_pk>/', views.comment_detail) # 5.2. GET - Comment Detail
    path('articles/<int:article_pk>/comments/', views.comment_create) # 5.3. POST - Create Comment
]
```

> views.py

```python
# 5.1. GET - Comment List
@api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET','DELETE','PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(pk=comment_pk)
    
    # 5.2. GET - Comment Detail
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    # 5.4. DELETE&PUT - delete, update Comment
    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'delete': f'댓글 {comment_pk}번이 삭제되었습니다.'
        }
        return Response(date, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# 5.3. POST - Create Comment
@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

#### 5.2. 댓글 목록 출력하기

```python
class ArticleSerializer(serializers.ModelSerializer):
    # 1번 방법 => 댓글의 pk만 출력
    comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # 2번 방법 => CommentSerializer fields에 정의되어 있는 정보 다 출력
    comment_set = CommentSerializer(many=True, read_only=True) #이거 쓸때는 CommentSerializer가 이 class 위에서 정의 되어야함
    class Meta:
        model = Article
        fields = '__all__'
```

#### 5.3. 댓글 개수 구하기

```python
class ArticleSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
```

